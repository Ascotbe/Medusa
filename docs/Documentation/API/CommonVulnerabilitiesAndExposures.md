### GitHub监控详细

`/api/github_monitor/`GitHubCVE数查询接口

```json
{
	"token": "xxx"
}
```

> 参数解释

- `token`登录后返回的**token**

> 返回状态码

- 200：返回查询到的数据

  ```json
  {
  	"message": [{
  		"github_id": "226311004",
  		"name": "cve_feeds",
  		"html_url": "https://github.com/AppThreat/cve_feeds",
  		"created_at": "2019-12-06T11:07:01Z",
  		"updated_at": "2021-01-04T08:21:49Z",
  		"pushed_at": "2021-01-04T08:21:46Z",
  		"forks_count": "6",
  		"watchers_count": "7"
  	}, {
  		"github_id": "300791308",
  		"name": "cvebase.com",
  		"html_url": "https://github.com/cvebase/cvebase.com",
  		"created_at": "2020-10-03T03:58:04Z",
  		"updated_at": "2020-12-30T22:21:09Z",
  		"pushed_at": "2020-12-30T22:21:10Z",
  		"forks_count": "22",
  		"watchers_count": "61"
  	}, {
  		"github_id": "306793101",
  		"name": "CVE_REQUEST-apache",
  		"html_url": "https://github.com/plr47/CVE_REQUEST-apache",
  		"created_at": "2020-10-24T02:55:10Z",
  		"updated_at": "2020-10-24T05:48:22Z",
  		"pushed_at": "2020-10-24T05:48:20Z",
  		"forks_count": "0",
  		"watchers_count": "3"
  	}, {
  		"github_id": "223232536",
  		"name": "php-version-audit",
  		"html_url": "https://github.com/lightswitch05/php-version-audit",
  		"created_at": "2019-11-21T17:54:51Z",
  		"updated_at": "2021-01-04T05:18:57Z",
  		"pushed_at": "2021-01-04T05:18:59Z",
  		"forks_count": "14",
  		"watchers_count": "79"
  	}, {
  		"github_id": "195458483",
  		"name": "cvelist",
  		"html_url": "https://github.com/vmcommunity/cvelist",
  		"created_at": "2019-07-05T19:30:48Z",
  		"updated_at": "2021-01-04T03:31:16Z",
  		"pushed_at": "2021-01-04T03:31:13Z",
  		"forks_count": "6",
  		"watchers_count": "8"
  	}],
  	"code": 200
  }
  ```

  > 返回参数解释

  **会有多个数组的集合**

  - `github_id`任务ID
  - `name`目标连接
  - `html_url`项目连接
  - `created_at`项目创建时间
  - `updated_at`项目更新时间
  - `pushed_at`项目推送时间
  - `forks_count`项目fork数量
  - `watchers_count`项目star数量

- 403：小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧

- 404：非法查询哦宝贝！

- 500：请使用Post请求

### 