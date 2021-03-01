### 获取当前机器CPU和内存使用率

`/api/system_hardware_usage_query/`用来当前机器的CPU和内存使用率，区间为当前时间之前1小时

```json
{
	"token": ""
}
```

>参数解释

- `token`登录后返回的**token**

> 返回状态码

- 169：呐呐呐！莎酱被玩坏啦(>^ω^<)

- 200：返回查询到的详细信息

  ```json
  {
  	"message": [{
  		"memory_used": "16130277376",
  		"memory_free": "31186944",
  		"memory_percent": "68.3",
  		"creation_time": "1609745554",
  		"central_processing_unit_usage_rate": "10.6",
  		"per_core_central_processing_unit_usage_rate": [37.4, 1.2, 33.9, 1.0, 28.2, 0.8, 26.7, 0.6, 19.2, 0.5, 15.1, 0.5, 11.1, 0.4, 4.2, 0.2]
  	}, {
  		"memory_used": "16105447424",
  		"memory_free": "83730432",
  		"memory_percent": "68.3",
  		"creation_time": "1609745564",
  		"central_processing_unit_usage_rate": "10.2",
  		"per_core_central_processing_unit_usage_rate": [37.3, 1.1, 33.4, 1.1, 28.1, 1.0, 25.8, 0.8, 18.0, 0.7, 15.3, 0.6, 12.3, 0.4, 7.2, 0.4]
  	}],
  	"code": 200
  }
  ```

  > 返回参数解释

  **会有多个数组的集合**

  - `memory_used`使用的内存
  - `memory_free`空闲的内存
  - `memory_percent`内存使用率
  - `creation_time`记录时间
  - `central_processing_unit_usage_rate`CPU总使用率
  - `per_core_central_processing_unit_usage_rate`每个CPU核心数的使用率

- 403：嘿~宝贝这是非法查询哦(๑•̀ㅂ•́)و✧

- 500：请使用Post请求

### 获取当前机器基础信息

`/api/system_hardware_initialization/`用来当前机器的基础信息

```json
{
	"token": ""
}
```

>参数解释

- `token`登录后返回的**token**

> 返回状态码

- 169：呐呐呐！莎酱被玩坏啦(>^ω^<)

- 200：返回计算机信息

  ```json
  {
  	"message": {
  		"central_processing_unit_architecture": "i386",
  		"system_info": "Darwin-20.2.0-x86_64-i386-64bit",
  		"server_start_time": "1609048960",
  		"system_name": "Darwin",
  		"system_type": "x86_64",
  		"user_name": "orange.local",
  		"memory_total": 34359738368,
  		"central_processing_unit_count": 16
  	},
  	"code": 200
  }
  ```

  > 返回参数解释

  - `central_processing_unit_architecture`中央处理单元架构
  - `system_info`系统信息
  - `server_start_time`系统启动时间
  - `system_name`系统名称
  - `system_type`系统架构
  - `user_name`用户名称
  - `memory_total`内存大小
  - `central_processing_unit_count`中央处理单元数

- 403：嘿~宝贝这是非法查询哦(๑•̀ㅂ•́)و✧

- 500：请使用Post请求
