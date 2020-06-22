#### 安装docker

不同的系统选择不通的安装方式，当前只用Ubuntu演示

```bash
#Ubuntu
sudo apt install docker.io
```

#### 拉取容器仓库

```bash
docker pull ascotbe/medusa:latest
```

#### 启动容器

```bash
 docker run -d -i -t --name  medusa -p 9999:9999 ascotbe/medusa:latest
```

启动容器后会返回一串字符串

```bash
root@iZbp19pfnyuhlghdkeobejZ:~#docker run -d -i -t --name  medusa -p 9999:9999 ascotbe/medusa:latest
2638732ee693ee9d4813cc2d2e39eae636de23ecfcbaf619a276e445435425bf
```

`2638732ee693ee9d4813cc2d2e39eae636de23ecfcbaf619a276e445435425bf`这串字符串就是容器的唯一**ID**值，不同容器**ID**不一样请自行查看

#### 进入容器

```bash
docker exec -it 2638732ee693ee9d4813cc2d2e39eae636de23ecfcbaf619a276e445435425bf /bin/bash
```

#### 启动Medusa

在启动容器之前注意修改DNSlog，具体改法参考bash版本

```bash
#进入目录
cd /Medusa/
#启动
./start.sh
#退出容器
exit
```

最后访问`http://127.0.0.1:9999`就可以看到登录页面了