需要用到mitmproxy以及redis还有celery

```
mitmdump  -p 54321 --proxyauth any --set block_global=false -s MedusaProxy.py
```

- `-p`表示你的端口
- `--proxyauth any`表示你需要用到账号密码
- `-s`代理脚本
- `--set block_global=false`全局可以访问，比如说不通的IP都可以代理

> 安装证书

站坑

