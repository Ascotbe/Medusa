#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.SecCms import SecCmsRemoteCodeExecutionV6_45
from Modules.Cms.SecCms import SecCmsRemoteCodeExecutionV6_54
from Modules.Cms.SecCms import SecCmsRemoteCodeExecutionV6_55
from ClassCongregation import Prompt
def Main(Pool,**kwargs):
    Pool.Append(SecCmsRemoteCodeExecutionV6_45.medusa, **kwargs)
    Pool.Append(SecCmsRemoteCodeExecutionV6_54.medusa, **kwargs)
    Pool.Append(SecCmsRemoteCodeExecutionV6_55.medusa, **kwargs)
    Prompt("SecCms")
