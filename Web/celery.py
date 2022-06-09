#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
import os
from config import github_cve_monitor_job_time,hardware_info_monitor_job_time,nist_update_job_time
from celery import Celery
from celery.schedules import crontab,timedelta
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Web.settings')

app = Celery('Medusa')  # 这边要加上redis不然默认是mq的

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks({"Web.ApplicationCollection.CollectionWork.AppleCollectionWork",
                        "Web.CVE.GithubMonitoring.Github.Monitor",
                        "Web.CVE.NistMonitoring.Update.Download",
                        "Web.Email.Send.SendMail",
                        "Web.FileAcquisition.Receive.Pack",
                        "Web.SystemInfo.HardwareInfo.Monitor",
                        "Web.TrojanOrVirus.TrojanInterface.CompileCode",
                        "Web.TrojanOrVirus.TrojanInterface.CompilePortableExecutableFile",
                        "Web.Email.Graph.Manufacture"})# 自动搜索并加载任务，任务列表防止找不到任务而报错
app.conf.beat_schedule = {
        'HardwareInfoMonitor': {
            'task': 'Web.SystemInfo.HardwareInfo.Monitor',
            'schedule': timedelta(seconds=hardware_info_monitor_job_time),
        },
        'GithubCveMonitor': {
            'task': 'Web.CVE.GithubMonitoring.Github.Monitor',
            'schedule': timedelta(seconds=github_cve_monitor_job_time),
        },
        'NistMonitor': {
            'task': 'Web.CVE.NistMonitoring.Update.Download',
            'schedule': timedelta(seconds=nist_update_job_time),
        }

}
app.autodiscover_tasks(lambda:settings.INSTALLED_APPS)



