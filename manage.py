#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from apscheduler.schedulers.background import BackgroundScheduler
from Web.CommonVulnerabilitiesAndExposuresMonitor.VulnerabilityUtilizationMonitoring.Github import GithubMonitor
from Web.SystemInfo.HardwareInfo import Monitor
from config import github_cve_monitor_job_time,hardware_info_monitor_job_time,nist_update_job_time
import portalocker#为了兼容Windows
from Web.CommonVulnerabilitiesAndExposuresMonitor.VulnerabilityNumberMonitoring.NistInitialization import NistInitialization
import atexit
from ClassCongregation import ErrorLog
from Web.CommonVulnerabilitiesAndExposuresMonitor.VulnerabilityNumberMonitoring.NistUpdate import NistUpdateDownload

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Web.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

def Job():#定时任务，加锁防止重复运行
    f = open("scheduler.lock", "wb")
    try:
        portalocker.lock(f, portalocker.LOCK_EX | portalocker.LOCK_NB)
        scheduler = BackgroundScheduler()
        scheduler.add_job(GithubMonitor, 'interval', id='github_cve_monitor_job', seconds=github_cve_monitor_job_time)
        scheduler.add_job(Monitor, 'interval', id='hardware_info_monitor_job', seconds=hardware_info_monitor_job_time)
        scheduler.add_job(NistUpdateDownload, 'interval', id='nist_update_job', seconds=nist_update_job_time)
        scheduler.start()
    except Exception as e:
        ErrorLog().Write("manage_Job(def)",e)

    def unlock():
        portalocker.unlock(f)
        f.close()
    atexit.register(unlock)

if __name__ == '__main__':

    Job()
    NistInitialization()  # 进行CVE数据初始化爬取
    main()




