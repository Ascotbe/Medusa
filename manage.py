#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Django's command-line utility for administrative tasks."""
import os
import sys
from Web.CommonVulnerabilitiesAndExposuresMonitor.VulnerabilityNumberMonitoring.NistInitialization import NistInitialization
from Web.ActiveScan import InitializationPlugin
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


if __name__ == '__main__':
    InitializationPlugin.Run()#初始化插件数据库
    NistInitialization()  # 进行CVE数据初始化爬取
    main()




