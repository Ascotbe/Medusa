#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from OA.Tongda import TongdaOfficeAnywhereArbitraryFileUploadAndFileInclusionVulnerability

from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,UnixTimestamp):
    ThreadPool.Append(TongdaOfficeAnywhereArbitraryFileUploadAndFileInclusionVulnerability.medusa, Url, Values, UnixTimestamp)
    Prompt("Tongda")