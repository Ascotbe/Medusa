### GitHub监控数据联合查询

`/api/github_monitor_search/`GitHub监控数据联合查询和全量查询

```json
{
	"token": "xxx",
	"name":"xx",
	"github_id":"",
	"html_url":"",
	"number_of_pages": "xxx"
}
```

> 参数解释

- `token`登录后返回的**token**
- `name`要搜索的项目名称
- `github_id`GitHub中的id数
- `html_url`项目连接
- `number_of_pages`页码数

> 特别解释

当传入的参数为`name`、`github_id` 、 `html_url`都为空的时候，该接口会进行所有数据查询，当这三个参数其中一个或者多个组合的时候可以进行联合查询

> 返回状态码

- 200：返回查询到的数据

  ```json
  {
  	"message":  [{
  			"github_id": "349467219",
  			"name": "CVEs",
  			"html_url": "https://github.com/s1vona/CVEs",
  			"created_at": "2021-03-19T15:20:24Z",
  			"updated_at": "2021-05-10T13:53:20Z",
  			"pushed_at": "2021-05-10T13:53:17Z",
  			"forks_count": "0",
  			"watchers_count": "0"
  		}, {
  			"github_id": "366957392",
  			"name": "cves",
  			"html_url": "https://github.com/sebaslavigne/cves",
  			"created_at": "2021-05-13T06:36:10Z",
  			"updated_at": "2021-07-27T23:15:47Z",
  			"pushed_at": "2021-07-27T23:15:44Z",
  			"forks_count": "0",
  			"watchers_count": "0"
  		}],
    "number": 2,
  	"code": 200
  }
  ```

> 返回参数解释

- 200：返回多个内容
  - `message`详细数据
    - `github_id`任务ID
    - `name`目标连接
    - `html_url`项目连接
    - `created_at`项目创建时间
    - `updated_at`项目更新时间
    - `pushed_at`项目推送时间
    - `forks_count`项目fork数量
    - `watchers_count`项目star数量

  - `number`个数

- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧
- 404：非法查询哦宝贝！
- 500：请使用Post请求

-----

### Nist全量数据查询

`/api/nist_data_bulk_query/`CVE监控首页精简数据查询

```json
{
	"token": "xxx",
	"number_of_pages":"20"
}
```

> 参数解释

- `token`登录后返回的**token**
- `number_of_pages`页数，传入的值必须大于0

> 返回状态码

- 200：返回查询到的数据（为了文档可观，只列出部分数据，正常数据为100条）

  ```json
  {
  	"message": [{
  		"vulnerability_number": "CVE-2003-0267",
  		"v3_base_score": "",
  		"v3_base_severity": "",
  		"v2_base_score": "5.0",
  		"v2_base_severity": "MEDIUM",
  		"last_up_date": "1539881160",
      "published_date" : "1151532300",
  		"vulnerability_description": "ShowGodLog.dll in SLWebMail 3 on Windows systems allows remote attackers to read arbitrary files by directly calling ShowGodLog.dll with an argument specifying the full path of the target file.",
  		"vendors": ["Bvrp Software"],
  		"products": ["Slwebmail"]
  	}, {
  		"vulnerability_number": "CVE-2003-0268",
  		"v3_base_score": "",
  		"v3_base_severity": "",
  		"v2_base_score": "5.0",
  		"v2_base_severity": "MEDIUM",
  		"last_up_date": "1500514320",
      "published_date" : "1151532300",
  		"vulnerability_description": "SLWebMail 3 on Windows systems allows remote attackers to identify the full path of the server via invalid requests to DLLs such as WebMailReq.dll, which reveals the path in an error message.",
  		"vendors": ["Bvrp Software"],
  		"products": ["Slwebmail"]
  	}, {
  		"vulnerability_number": "CVE-2003-0269",
  		"v3_base_score": "",
  		"v3_base_severity": "",
  		"v2_base_score": "7.2",
  		"v2_base_severity": "HIGH",
  		"last_up_date": "1539881220",
      "published_date" : "1151532300",
  		"vulnerability_description": "Buffer overflow in youbin allows local users to gain privileges via a long HOME environment variable.",
  		"vendors": ["Youbin"],
  		"products": ["Youbin"]
  	}, {
  		"vulnerability_number": "CVE-2003-0367",
  		"v3_base_score": "",
  		"v3_base_severity": "",
  		"v2_base_score": "2.1",
  		"v2_base_severity": "LOW",
  		"last_up_date": "1220648940",
      "published_date" : "1151532300",
  		"vulnerability_description": "znew in the gzip package allows local users to overwrite arbitrary files via a symlink attack on temporary files.",
  		"vendors": ["Gnu", "Debian"],
  		"products": ["Gzip", "Debian Linux"]
  	}],
    "number":4,
  	"code": 200
  }
  ```

  > 返回参数解释

  - `number` 个数

  - `message`**会有多个数组的集合**

    - `vulnerability_number`漏洞编号

    - `v3_base_score`CVSS v3 分数

    - `v3_base_severity`CVSS v3 分级

    - `v2_base_score`CVSS v2 分数

    - `v2_base_severity`CVSS v2 分级

    - `last_up_date`最后更新时间
    - `published_date`发现时间 

    - `vulnerability_description`漏洞说明

    - `vendors`开发商名称

    - `products`产品名称

- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧

- 500：请使用Post请求

- 503：你家有小于0的页码？

### Nist数据中单个CVE详情查询

`/api/nist_data_detailed_query/`获取单个详细的CVE编号

```json
{
	"token": "xxx",
	"common_vulnerabilities_and_exposures":"CVE-2021-3177"
}
```

> 参数解释

- `token`登录后返回的**token**
- `common_vulnerabilities_and_exposures`CVE编号

> 返回状态码

- 200：返回查询到的数据，message中为需要用到的原始数据

  ```json
  {
  	"message": {
  		"cve": {
  			"data_type": "CVE",
  			"data_format": "MITRE",
  			"data_version": "4.0",
  			"CVE_data_meta": {
  				"ID": "CVE-2021-3177",
  				"ASSIGNER": "cve@mitre.org"
  			},
  			"problemtype": {
  				"problemtype_data": [{
  					"description": [{
  						"lang": "en",
  						"value": "CWE-120"
  					}]
  				}]
  			},
  			"references": {
  				"reference_data": [{
  					"url": "https://bugs.python.org/issue42938",
  					"name": "https://bugs.python.org/issue42938",
  					"refsource": "MISC",
  					"tags": ["Exploit", "Issue Tracking", "Patch", "Vendor Advisory"]
  				}, {
  					"url": "https://github.com/python/cpython/pull/24239",
  					"name": "https://github.com/python/cpython/pull/24239",
  					"refsource": "MISC",
  					"tags": ["Patch", "Third Party Advisory"]
  				}, {
  					"url": "https://python-security.readthedocs.io/vuln/ctypes-buffer-overflow-pycarg_repr.html",
  					"name": "https://python-security.readthedocs.io/vuln/ctypes-buffer-overflow-pycarg_repr.html",
  					"refsource": "MISC",
  					"tags": ["Patch", "Third Party Advisory"]
  				}, {
  					"url": "https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/NQPARTLNSFQVMMQHPNBFOCOZOO3TMQNA/",
  					"name": "FEDORA-2021-cc3ff94cfc",
  					"refsource": "FEDORA",
  					"tags": ["Third Party Advisory"]
  				}, {
  					"url": "https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/MGSV6BJQLRQ6RKVUXK7JGU7TP4QFGQXC/",
  					"name": "FEDORA-2021-faf88b9499",
  					"refsource": "FEDORA",
  					"tags": ["Third Party Advisory"]
  				}, {
  					"url": "https://security.gentoo.org/glsa/202101-18",
  					"name": "GLSA-202101-18",
  					"refsource": "GENTOO",
  					"tags": ["Third Party Advisory"]
  				}, {
  					"url": "https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/Z7GZV74KM72O2PEJN2C4XP3V5Q5MZUOO/",
  					"name": "FEDORA-2021-e3a5a74610",
  					"refsource": "FEDORA",
  					"tags": ["Third Party Advisory"]
  				}, {
  					"url": "https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/CCFZMVRQUKCBQIG5F2CBVADK63NFSE4A/",
  					"name": "FEDORA-2021-ced31f3f0c",
  					"refsource": "FEDORA",
  					"tags": ["Third Party Advisory"]
  				}, {
  					"url": "https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/BRHOCQYX3QLDGDQGTWQAUUT2GGIZCZUO/",
  					"name": "FEDORA-2021-42ba9feb47",
  					"refsource": "FEDORA",
  					"tags": ["Third Party Advisory"]
  				}, {
  					"url": "https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/V6XJAULOS5JVB2L67NCKKMJ5NTKZJBSD/",
  					"name": "FEDORA-2021-851c6e4e2d",
  					"refsource": "FEDORA",
  					"tags": ["Third Party Advisory"]
  				}, {
  					"url": "https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/NXSMBHES3ANXXS2RSO5G6Q24BR4B2PWK/",
  					"name": "FEDORA-2021-076a2dccba",
  					"refsource": "FEDORA",
  					"tags": ["Third Party Advisory"]
  				}, {
  					"url": "https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/YDTZVGSXQ7HR7OCGSUHTRNTMBG43OMKU/",
  					"name": "FEDORA-2021-66547ff92d",
  					"refsource": "FEDORA",
  					"tags": ["Third Party Advisory"]
  				}, {
  					"url": "https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/Y4KSYYWMGAKOA2JVCQA422OINT6CKQ7O/",
  					"name": "FEDORA-2021-17668e344a",
  					"refsource": "FEDORA",
  					"tags": ["Third Party Advisory"]
  				}, {
  					"url": "https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/FPE7SMXYUIWPOIZV4DQYXODRXMFX3C5E/",
  					"name": "FEDORA-2021-d5cde50865",
  					"refsource": "FEDORA",
  					"tags": ["Third Party Advisory"]
  				}, {
  					"url": "https://news.ycombinator.com/item?id=26185005",
  					"name": "https://news.ycombinator.com/item?id=26185005",
  					"refsource": "MISC",
  					"tags": ["Third Party Advisory"]
  				}, {
  					"url": "https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/HCQTCSP6SCVIYNIRUJC5X7YBVUHPLSC4/",
  					"name": "FEDORA-2021-7547ad987f",
  					"refsource": "FEDORA",
  					"tags": ["Third Party Advisory"]
  				}, {
  					"url": "https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/NODWHDIFBQE5RU5PUWUVE47JOT5VCMJ2/",
  					"name": "FEDORA-2021-f4fd9372c7",
  					"refsource": "FEDORA",
  					"tags": ["Third Party Advisory"]
  				}, {
  					"url": "https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/MP572OLHMS7MZO4KUPSCIMSZIA5IZZ62/",
  					"name": "FEDORA-2021-3352c1c802",
  					"refsource": "FEDORA",
  					"tags": ["Third Party Advisory"]
  				}, {
  					"url": "https://lists.apache.org/thread.html/rf9fa47ab66495c78bb4120b0754dd9531ca2ff0430f6685ac9b07772@%3Cdev.mina.apache.org%3E",
  					"name": "[mina-dev] 20210225 [jira] [Created] (FTPSERVER-500) Security vulnerability in common/lib/log4j-1.2.17.jar",
  					"refsource": "MLIST",
  					"tags": ["Mailing List", "Third Party Advisory"]
  				}, {
  					"url": "https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/FONHJIOZOFD7CD35KZL6SVBUTMBPGZGA/",
  					"name": "FEDORA-2021-907f3bacae",
  					"refsource": "FEDORA",
  					"tags": ["Third Party Advisory"]
  				}, {
  					"url": "https://security.netapp.com/advisory/ntap-20210226-0003/",
  					"name": "https://security.netapp.com/advisory/ntap-20210226-0003/",
  					"refsource": "CONFIRM",
  					"tags": ["Third Party Advisory"]
  				}, {
  					"url": "https://lists.debian.org/debian-lts-announce/2021/04/msg00005.html",
  					"name": "[debian-lts-announce] 20210405 [SECURITY] [DLA 2619-1] python3.5 security update",
  					"refsource": "MLIST",
  					"tags": []
  				}]
  			},
  			"description": {
  				"description_data": [{
  					"lang": "en",
  					"value": "Python 3.x through 3.9.1 has a buffer overflow in PyCArg_repr in _ctypes/callproc.c, which may lead to remote code execution in certain Python applications that accept floating-point numbers as untrusted input, as demonstrated by a 1e300 argument to c_double.from_param. This occurs because sprintf is used unsafely."
  				}]
  			}
  		},
  		"configurations": {
  			"CVE_data_version": "4.0",
  			"nodes": [{
  				"operator": "OR",
  				"children": [],
  				"cpe_match": [{
  					"vulnerable": true,
  					"cpe23Uri": "cpe:2.3:a:python:python:*:*:*:*:*:*:*:*",
  					"versionStartIncluding": "3.6.0",
  					"versionEndIncluding": "3.6.12",
  					"cpe_name": []
  				}, {
  					"vulnerable": true,
  					"cpe23Uri": "cpe:2.3:a:python:python:*:*:*:*:*:*:*:*",
  					"versionStartIncluding": "3.7.0",
  					"versionEndIncluding": "3.7.9",
  					"cpe_name": []
  				}, {
  					"vulnerable": true,
  					"cpe23Uri": "cpe:2.3:a:python:python:*:*:*:*:*:*:*:*",
  					"versionStartIncluding": "3.8.0",
  					"versionEndIncluding": "3.8.7",
  					"cpe_name": []
  				}, {
  					"vulnerable": true,
  					"cpe23Uri": "cpe:2.3:a:python:python:*:*:*:*:*:*:*:*",
  					"versionStartIncluding": "3.9.0",
  					"versionEndIncluding": "3.9.1",
  					"cpe_name": []
  				}]
  			}, {
  				"operator": "OR",
  				"children": [],
  				"cpe_match": [{
  					"vulnerable": true,
  					"cpe23Uri": "cpe:2.3:o:fedoraproject:fedora:32:*:*:*:*:*:*:*",
  					"cpe_name": []
  				}, {
  					"vulnerable": true,
  					"cpe23Uri": "cpe:2.3:o:fedoraproject:fedora:33:*:*:*:*:*:*:*",
  					"cpe_name": []
  				}]
  			}, {
  				"operator": "OR",
  				"children": [],
  				"cpe_match": [{
  					"vulnerable": true,
  					"cpe23Uri": "cpe:2.3:a:netapp:ontap_select_deploy_administration_utility:-:*:*:*:*:*:*:*",
  					"cpe_name": []
  				}]
  			}]
  		},
  		"impact": {
  			"baseMetricV3": {
  				"cvssV3": {
  					"version": "3.1",
  					"vectorString": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H",
  					"attackVector": "NETWORK",
  					"attackComplexity": "LOW",
  					"privilegesRequired": "NONE",
  					"userInteraction": "NONE",
  					"scope": "UNCHANGED",
  					"confidentialityImpact": "HIGH",
  					"integrityImpact": "HIGH",
  					"availabilityImpact": "HIGH",
  					"baseScore": 9.8,
  					"baseSeverity": "CRITICAL"
  				},
  				"exploitabilityScore": 3.9,
  				"impactScore": 5.9
  			},
  			"baseMetricV2": {
  				"cvssV2": {
  					"version": "2.0",
  					"vectorString": "AV:N/AC:L/Au:N/C:P/I:P/A:P",
  					"accessVector": "NETWORK",
  					"accessComplexity": "LOW",
  					"authentication": "NONE",
  					"confidentialityImpact": "PARTIAL",
  					"integrityImpact": "PARTIAL",
  					"availabilityImpact": "PARTIAL",
  					"baseScore": 7.5
  				},
  				"severity": "HIGH",
  				"exploitabilityScore": 10.0,
  				"impactScore": 6.4,
  				"acInsufInfo": false,
  				"obtainAllPrivilege": false,
  				"obtainUserPrivilege": false,
  				"obtainOtherPrivilege": false,
  				"userInteractionRequired": false
  			}
  		},
  		"publishedDate": "2021-01-19T06:15Z",
  		"lastModifiedDate": "2021-07-20T23:15Z"
  	},
  	"code": 200
  }
  ```

- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧

- 500：请使用Post请求

### Nist模糊搜索接口

`/api/nist_search/`对于严重性等级筛选

```json
{
	"token": "xxx",
	"number_of_pages":"0",
	"severity":"xxxx",
	"key":"xxxx"
}
```

> 参数解释

- `token`登录后返回的**token**
- `number_of_pages`页数，传入的值必须大于0
- `severity`严重性等级，可传入参数：NONE、LOW、MEDIUM、HIGH、CRITICAL
- `key`传入你查询的关键字

> 返回状态码

- 200：返回查询到的数据（为了文档可观，只列出部分数据，正常数据为100条）

  ```json
  {
  	"message": [{
  		"vulnerability_number": "CVE-2003-0267",
  		"v3_base_score": "",
  		"v3_base_severity": "",
  		"v2_base_score": "5.0",
  		"v2_base_severity": "MEDIUM",
  		"last_up_date": "1539881160",
      "published_date" : "1151532300",
  		"vulnerability_description": "ShowGodLog.dll in SLWebMail 3 on Windows systems allows remote attackers to read arbitrary files by directly calling ShowGodLog.dll with an argument specifying the full path of the target file.",
  		"vendors": ["Bvrp Software"],
  		"products": ["Slwebmail"]
  	}, {
  		"vulnerability_number": "CVE-2003-0268",
  		"v3_base_score": "",
  		"v3_base_severity": "",
  		"v2_base_score": "5.0",
  		"v2_base_severity": "MEDIUM",
  		"last_up_date": "1500514320",
      "published_date" : "1151532300",
  		"vulnerability_description": "SLWebMail 3 on Windows systems allows remote attackers to identify the full path of the server via invalid requests to DLLs such as WebMailReq.dll, which reveals the path in an error message.",
  		"vendors": ["Bvrp Software"],
  		"products": ["Slwebmail"]
  	}, {
  		"vulnerability_number": "CVE-2003-0269",
  		"v3_base_score": "",
  		"v3_base_severity": "",
  		"v2_base_score": "7.2",
  		"v2_base_severity": "HIGH",
  		"last_up_date": "1539881220",
      "published_date" : "1151532300",
  		"vulnerability_description": "Buffer overflow in youbin allows local users to gain privileges via a long HOME environment variable.",
  		"vendors": ["Youbin"],
  		"products": ["Youbin"]
  	}, {
  		"vulnerability_number": "CVE-2003-0367",
  		"v3_base_score": "",
  		"v3_base_severity": "",
  		"v2_base_score": "2.1",
  		"v2_base_severity": "LOW",
  		"last_up_date": "1220648940",
      "published_date" : "1151532300",
  		"vulnerability_description": "znew in the gzip package allows local users to overwrite arbitrary files via a symlink attack on temporary files.",
  		"vendors": ["Gnu", "Debian"],
  		"products": ["Gzip", "Debian Linux"]
  	}],
    "number":4,
  	"code": 200
  }
  ```
  
  > 返回参数解释
  
  - `number`该等级的漏洞个数
  - `message`里面存在当前页面100个数据，数据参数解释如下
    - `vulnerability_number`漏洞编号
    - `v3_base_score`CVSS v3 分数
    - `v3_base_severity`CVSS v3 分级
    - `v2_base_score`CVSS v2 分数
    - `v2_base_severity`CVSS v2 分级
    - `last_up_date`最后更新时间
    - `published_date`发现时间
    - `vulnerability_description`漏洞说明
    - `vendors`开发商名称
    - `products`产品名称
  
- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧

- 500：请使用Post请求

- 503：你家有小于1的页码？

- 505：咋了？查询不知道传数据吗？
