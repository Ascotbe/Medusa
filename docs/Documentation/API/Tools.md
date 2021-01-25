### 杀毒软件进程查询接口

`/api/antivirus_software_compared/`用来对比文本中是否存在杀软

```json
{
	"token": "",
	"process_name_list":[]
}
```

>参数解释

- `token`登录后返回的**token**
- `process_name_list`用户传入的进程列表，需要使用dict类型

> 返回状态码

- 169：呐呐呐！莎酱被玩坏啦(>^ω^<)
- 200：返回查询到的杀软
- 403：嘿~宝贝这是非法查询哦(๑•̀ㅂ•́)و✧
- 500：请使用Post请求
- 666：未查询到杀软

### PE文件解析接口

`/api/windows_portable_execute_analysis/`用来对比文本中是否存在杀软

```json
POST /api/windows_portable_execute_analysis/ HTTP/1.1
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryaFtQbWz7pBzNgCOv
token:UserToken

------WebKitFormBoundaryaFtQbWz7pBzNgCOv
Content-Disposition: form-data; name="file"; filename="test.exe"
Content-Type: text/exe

FileDate
------WebKitFormBoundaryaFtQbWz7pBzNgCOv--
```

>参数解释

- `token`登录后返回的**token**
- `FileDate`上传文件的内容

> 返回状态码

- 200：成功了
- 403：嘿~宝贝这是非法查询哦(๑•̀ㅂ•́)و✧
- 500：请使用Post请求
- 501：文件太大啦~(๑•̀ㅂ•́)و✧

### IOS应用收集

`/api/apple_app_collection/`用来对比文本中是否存在杀软

```json
{
	"token": "",
	"app_name":""
}
```

>参数解释

- `token`登录后返回的**token**
- `app_name`APP的名字

> 返回状态码

- 169：出现未知错误，详情看日志文件
- 200：任务下发成功(๑•̀ㅂ•́)و✧
- 403：小宝贝这是非法请求哦(๑•̀ㅂ•́)و✧
- 500：请使用Post请求
- 666：未查询到杀软

### 应用收集查询接口

`/api/application_collection_query/`获取全部的数据

```
{
	"token": ""
}
```

>参数解释

- `token`登录后返回的**token**

> 返回状态码

- 169：呐呐呐！莎酱被玩坏啦(>^ω^<)

- 200：返回查询到的项目信息

  ```
  {
  	"message": [{
  		"program_type": "Apple",
  		"creation_time": "1611390585",
  		"status": "1",
  		"application_data": "",
  		"request_failed_application_name": "[]",
  		"total_number_of_applications": "99",
  		"number_of_failures": "0"
  	}],
  	"code": 200
  }
  ```

  > 返回参数解释

  **会有多个数组的集合**

  - `program_type`收集类型，安卓或者iOS

  - `creation_time`创建时间

  - `status`状态值，0表示正在执行，1表示执行成功

  - `application_data`获取到的数据内容

    ```
    {\"Icon\": \"https://is2-ssl.mzstatic.com/image/thumb/Purple124/v4/38/ad/e7/38ade7d4-d6bf-a226-d77b-9557f589faf0/source/100x100bb.jpg\", \"AppName\": \"\\u817e\\u8baf\\u5730\\u56fe-\\u8def\\u7ebf\\u89c4\\u5212,\\u5bfc\\u822a\\u6253\\u8f66\\u51fa\\u884c\\u5fc5\\u5907\", \"Description\": \"\\u817e\\u8baf\\u5730\\u56fe-\\u817e\\u8baf\\u56e2\\u961f\\u503e\\u529b\\u6253\\u9020\\uff0c\\u4ebf\\u4e07\\u7528\\u6237\\u4fe1\\u8d56\\u7684\\u51fa\\u884c\\u5bfc\\u822a\\u5fc5\\u5907\\u5e94\\u7528\\uff01\\n\\u3010\\u6d77\\u91cf\\u6570\\u636e\\u3011\\n-200+\\u57ce\\u5e02\\u8def\\u51b5\\u5b9e\\u65f6\\u5237\\u65b0\\uff0c\\u62e5\\u5835\\u65e9\\u77e5\\u9053\\u3002\\n-2000+\\u5957\\u5ba4\\u5185\\u5730\\u56fe\\uff0c\\u8986\\u76d6\\u5404\\u5927\\u673a\\u573a\\u3001\\u706b\\u8f66\\u7ad9\\u3001\\u4e3b\\u6d41\\u5546\\u573a\\u3002\\n\\u3010\\u7cbe\\u51c6\\u5bfc\\u822a\\u3011\\n-\\u63d0\\u4f9b\\u5305\\u542b\\u9a7e\\u8f66\\u3001\\u6253\\u8f66\\u3001\\u516c\\u4ea4\\u3001\\u6b65\\u884c\\u3001\\u9a91\\u884c\\u7b49\\u51fa\\u884c\\u65b9\\u5f0f\\u7684\\u667a\\u80fd\\u89c4\\u5212\\u65b9\\u6848\\u548c\\u7cbe\\u51c6\\u667a\\u80fd\\u5bfc\\u822a\\u3002\\u7efc\\u5408\\u8fd0\\u7528\\u5927\\u6570\\u636e\\u3001\\u7b97\\u529b\\u548c\\u7b97\\u6cd5\\u80fd\\u529b\\uff0c\\u63d0\\u5347\\u7528\\u6237\\u7684\\u51fa\\u884c\\u6548\\u7387\\u3002\\n-\\u5b9e\\u65f6\\u5b9a\\u4f4d\\u7cbe\\u51c6\\uff0c\\u76ee\\u7684\\u5730\\u8be6\\u7ec6\\u4f4d\\u7f6e\\u5f15\\u5bfc\\uff0c\\u63d0\\u4f9b\\u591a\\u79cd\\u51fa\\u884c\\u65b9\\u5f0f\\u7ec4\\u5408\\u7684\\u65b9\\u6848\\uff0c\\u884c\\u4e1a\\u9886\\u5148\\u7684AR\\u5b9e\\u666f\\u6b65\\u884c\\u5bfc\\u822a\\uff0c\\u66f4\\u4f18\\u7cbe\\u51c6\\u670d\\u52a1\\u8986\\u76d6\\u5168\\u7a0b\\u3002\\n\\u3010\\u8def\\u7ebf\\u89c4\\u5212\\u3011\\n-\\u8def\\u7ebf\\u7cbe\\u51c6\\u89c4\\u5212\\uff0c\\u9884\\u6d4b\\u51fa\\u884c\\u8def\\u51b5\\u4e0e\\u8017\\u65f6\\uff0c\\u51c6\\u786e\\u9884\\u4f30\\u5230\\u8fbe\\u65f6\\u95f4\\u3002\\u63d0\\u4f9b\\u8def\\u51b5\\u5b9e\\u65f6\\u5237\\u65b0\\uff0c\\u63a8\\u8350\\u66f4\\u4f18\\u901a\\u884c\\u8def\\u7ebf\\uff0c\\u5b9e\\u65f6\\u8eb2\\u907f\\u62e5\\u5835\\u3002\\n-AI\\u8bed\\u97f3\\u52a9\\u624b\\u300e\\u53ee\\u5f53\\u53ee\\u5f53\\u300f\\u667a\\u80fd\\u63a8\\u8350\\u7ebf\\u8def\\uff0c\\u8bed\\u97f3\\u5168\\u65b9\\u4f4d\\u4ea4\\u4e92\\uff0c\\u5bfc\\u822a\\u4e2d\\u540c\\u6b65\\u652f\\u6301\\u66f4\\u6539\\u76ee\\u7684\\u5730\\u3001\\u5237\\u65b0\\u8def\\u7ebf\\u3001\\u8def\\u51b5\\u67e5\\u8be2\\u3002\\n- \\u5b9e\\u65f6\\u516c\\u4ea4\\u4fe1\\u606f\\uff0c\\u5b9a\\u4f4d\\u516c\\u4ea4\\u8f66\\u7684\\u5b9e\\u65f6\\u4f4d\\u7f6e\\uff0c\\u7cbe\\u51c6\\u8ba1\\u7b97\\u5230\\u7ad9\\u65f6\\u95f4\\uff0c\\u516c\\u4ea4\\u62e5\\u6324\\u7a0b\\u5ea6\\u5b9e\\u65f6\\u663e\\u793a\\u3002\\n\\u3010\\u51fa\\u884c\\u670d\\u52a1\\u3011\\n-\\u6253\\u8f66\\u5168\\u7f51\\u4e00\\u952e\\u53eb\\u8f66\\uff0c\\u591a\\u79cd\\u8f66\\u578b\\u540c\\u65f6\\u547c\\u53eb\\uff0c\\u66f4\\u5feb\\u51fa\\u53d1\\uff0c\\u805a\\u5408\\u591a\\u4e2a\\u6253\\u8f66\\u5e73\\u53f0\\uff0c\\u4ef7\\u683c\\u900f\\u660e\\u3002\\n-\\u63a5\\u5165\\u591a\\u79cd\\u51fa\\u884c\\u670d\\u52a1\\u5c0f\\u7a0b\\u5e8f\\uff0c\\u53ef\\u4ee5\\u5728\\u7aef\\u5185\\u9884\\u5b9a\\u706b\\u8f66\\u7968\\u3001\\u98de\\u673a\\u7968\\u3001\\u6c7d\\u8f66\\u7968\\u3001\\u65e0\\u9700\\u518d\\u6253\\u5f00\\u591a\\u4e2aApp\\uff0c\\u514d\\u53bb\\u7e41\\u7410\\u64cd\\u4f5c\\uff0c\\u4e3a\\u51fa\\u6e38\\u63d0\\u4f9b\\u66f4\\u591a\\u4fbf\\u5229\\u9009\\u62e9\\u3002\\n\\u3010\\u7279\\u8272\\u670d\\u52a1\\u3011\\n-\\u7279\\u8272\\u8bed\\u97f3\\uff1a\\u65b9\\u8a00\\u3001\\u738b\\u8005\\u8363\\u8000\\u82f1\\u96c4\\u8bed\\u97f3\\u3001\\u548c\\u5e73\\u7cbe\\u82f1\\u8bed\\u97f3\\u3001DNF\\u8d5b\\u5229\\u4e9a\\u8bed\\u97f3\\n-\\u7279\\u8272\\u4e3b\\u9898\\u8f66\\u6807\\uff1a\\u738b\\u8005\\u8363\\u8000\\u3001\\u548c\\u5e73\\u7cbe\\u82f1\\u3001\\u8dd1\\u8dd1\\u5361\\u4e01\\u8f66\\n-\\u7279\\u8272\\u5730\\u56fe\\uff1a3D\\u5730\\u56fe\\u3001\\u536b\\u661f\\u5730\\u56fe\\u3001\\u8857\\u666f\\u5730\\u56fe\\u3001\\u666f\\u533a\\u624b\\u7ed8\\u5730\\u56fe\\n-\\u641c\\u7d22\\u5468\\u8fb9\\u670d\\u52a1\\uff1a\\u5403\\u559d\\u73a9\\u4e50\\u3001\\u4f4f\\u5bbf\\u65c5\\u884c\\u4e00\\u5e94\\u4ff1\\u5168\\n-\\u738b\\u5361\\u514d\\u6d41\\u91cf\\u670d\\u52a1\\uff0c\\u96f6\\u6d41\\u91cf\\u4e5f\\u53ef\\u5bfc\\u822a\\n\\u3010\\u6027\\u80fd\\u4f18\\u826f\\u3011\\n-\\u7701\\u6d41\\u91cf\\u3001\\u4f4e\\u8017\\u7535\\u3001\\u5360\\u7528\\u7a7a\\u95f4\\u5c0f\\uff0c\\u64cd\\u4f5c\\u7b80\\u5355\\u3001\\u754c\\u9762\\u7f8e\\u89c2\\n\\u3010\\u8054\\u7cfb\\u6211\\u4eec\\u3011\\n-\\u5b98\\u65b9\\u7528\\u6237QQ\\u7fa4\\uff1a293687610\\n-\\u60a8\\u8fd8\\u53ef\\u4ee5\\u5728app\\u5e94\\u7528\\u5185\\u201c\\u8bbe\\u7f6e-\\u610f\\u89c1\\u53cd\\u9988\\u201d\\u5165\\u53e3\\u8fdb\\u884c\\u53cd\\u9988\\uff0c\\u6211\\u4eec\\u4f1a\\u53ca\\u65f6\\u5904\\u7406\\u60a8\\u7684\\u95ee\\u9898\\n-\\u5728\\u540e\\u53f0\\u6301\\u7eed\\u4f7f\\u7528GPS\\u4f1a\\u51cf\\u5c11\\u7535\\u6c60\\u7eed\\u822a\\u65f6\\u957f\", \"FileSizeBytes\": \"261801984\", \"SellerName\": \"Shenzhen Tencent Computer Systems Company Limited\", \"Advisories\": [], \"ReleaseDate\": \"2011-11-29T10:58:32Z\", \"Screenshot\": [\"https://is4-ssl.mzstatic.com/image/thumb/Purple114/v4/a6/fc/aa/a6fcaa65-8531-43e7-c830-4c1e04935cb4/5f6bb3dd-d57b-48d5-a314-a58f7d80f1e9_1242x2208bb__U00281_U0029.png/392x696bb.png\", \"https://is2-ssl.mzstatic.com/image/thumb/Purple114/v4/46/ea/97/46ea97d0-273f-0b08-60dd-0b75757d99de/61df55c6-21ba-40f6-b9de-cd06aca908e9__U6253_U8f66_U5907_U4efd.png/392x696bb.png\", \"https://is5-ssl.mzstatic.com/image/thumb/Purple114/v4/9c/77/6b/9c776b37-5e89-36ca-9d8a-e1d442509b7a/b4faf0a9-f1a1-41c7-89cb-69f0f882ae7b_1242x2208bb__U00282_U0029.png/392x696bb.png\", \"https://is3-ssl.mzstatic.com/image/thumb/Purple124/v4/5d/58/09/5d58091d-b95b-2873-48f8-849d12e03133/f942d90c-f8e7-455c-bc5f-7a9716abef38_1242x2208bb.png/392x696bb.png\", \"https://is5-ssl.mzstatic.com/image/thumb/Purple114/v4/ba/16/85/ba1685da-4440-eeb3-5c3b-30394040488c/2b1607a4-2ca7-45fe-9cd0-5ce43d8260f4_1242x2208bb__U00284_U0029.png/392x696bb.png\", \"https://is3-ssl.mzstatic.com/image/thumb/Purple124/v4/23/18/24/231824b4-265c-9b4d-512c-4fd86f686edd/428f4542-6826-4bac-b8f2-659fe373a8fa_1242x2208bb__U00285_U0029.png/392x696bb.png\", \"https://is1-ssl.mzstatic.com/image/thumb/Purple114/v4/a8/98/2c/a8982cb1-e665-4af8-0e84-304506fcb27d/8f2e1693-b987-4fd6-8133-718796ee73f4_1242x2208bb__U00286_U0029.png/392x696bb.png\", \"https://is4-ssl.mzstatic.com/image/thumb/PurpleSource124/v4/36/e2/d6/36e2d6db-11b7-65e5-11da-4d64c9ac5869/bb4a837f-3c7d-4f50-ad83-5896400550b3_8.CarPlay.png/392x696bb.png\", \"https://is2-ssl.mzstatic.com/image/thumb/Purple124/v4/39/79/a6/3979a654-4f0d-7d4f-c7f4-9339c49991c9/fdd0a8f8-02f5-4f9b-8c59-9a6899695ebd_1242x2208bb__U00288_U0029.png/392x696bb.png\"], \"ArtistName\": \"Tencent Mobile Games\", \"ArtistViewUrl\": \"https://apps.apple.com/cn/developer/tencent-mobile-games/id446324237?uo=4\", \"DownloadLink\": \"https://apps.apple.com/cn/app/%E8%85%BE%E8%AE%AF%E5%9C%B0%E5%9B%BE-%E8%B7%AF%E7%BA%BF%E8%A7%84%E5%88%92-%E5%AF%BC%E8%88%AA%E6%89%93%E8%BD%A6%E5%87%BA%E8%A1%8C%E5%BF%85%E5%A4%87/id481623196?uo=4\"}
    ```

    - `Icon`图标地址
    - `AppName`应用名称
    - `Description`
    - `FileSizeBytes`
    - `SellerName`
    - `Advisories`
    - `ReleaseDate`
    - `Screenshot`
    - `ArtistName`
    - `ArtistViewUrl`
    - `DownloadLink`

  - `request_failed_application_name`获取失败的应用名

  - `total_number_of_applications`总共获取的应用数量

  - `number_of_failures`失败的应用数量

- 403：嘿~宝贝这是非法查询哦(๑•̀ㅂ•́)و✧

- 500：请使用Post请求

