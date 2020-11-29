<img src="https://github.com/Ascotbe/Medusa/blob/master/Medusa.png?raw=true" width="1500" alt="Medusa" /> 

 <p align="center">
    <a href="https://github.com/Ascotbe/Medusa"><img alt="Release" src="https://img.shields.io/badge/Ascotbe-Medusa-green"></a>
    <a href="https://github.com/Ascotbe/Medusa"><img alt="Release" src="https://img.shields.io/badge/python-3.7+-blueviolet"></a>
    <a href="https://github.com/Ascotbe/Medusa"><img alt="Release" src="https://img.shields.io/badge/Version-0.92-red"></a>
    <a href="https://github.com/Ascotbe/Medusa"><img alt="Release" src="https://img.shields.io/badge/LICENSE-GPL-ff69b4"></a>
	<a href="https://github.com/ascotbe/Medusa/stargazers"><img alt="Release" src="https://img.shields.io/github/stars/ascotbe/Medusa.svg"></a>
	<a href="https://github.com/Ascotbe/Medusa"><img alt="Release" src="https://img.shields.io/badge/Plugin-200+-success"></a>
 </p>

<h1 align="center" >Welcome to Medusa</h1>

### :point_right:About `Medusa`

> The project is licensed under `GPL`.Free for non-commercial use.
>
> The project development manpower is insufficient. If you find a problem or have comments, please contact us.
>
> `bash` Ver. Online
>
> `Web` Ver. Under development

#### **[中文文档](https://github.com/Ascotbe/Medusa/blob/master/README.CN.md) | EnglishDocumentation**

### :bulb:Document

```
http://medusa.ascotbe.com
```

### :mag_right:Bug coverage list

```
http://medusa.ascotbe.com/Documentation/#/PluginDirectory
```

### :space_invader:Demo

![demo](https://github.com/Ascotbe/Random-img/blob/master/Medusa/demo.gif?raw=true)


### :book:`Bash` Ver. instructions for use

```bash
# clone project files(example for ubuntu
git clone https://github.com/Ascotbe/Medusa.git
cd Medusa
# Install python packages
python3 -m pip3 install -r Medusa.txt
# Use the scanner
python3 MedusaScan.py -u www.ascotbe.com
```

### :rocket:Git proxy

```bash
# If download speed too slow when cloning, then you can use proxy. 
# Global proxy setting
git config --global http.proxy http://127.0.0.1:1080
git config --global https.proxy https://127.0.0.1:1080
```

### :clipboard:Parameters

| Command | Number of parameters | Effect                                                         | Annotation                                                         |
| ---- | -------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| -u   | 1        | Input single url（Use `http://` or `https://` first better than none, do not use any paremeters follow the url | example : `-u https://www.ascotbe.com` or `-u https://192.168.0.1`           |
| -a   | 1        | Specify header files or use random headers                                       | When using this feature, please refer to the documentation for this content |
| -f   | 1        | The filename includes urls that want to scan.                              | `-u` or `-f` must exists one and only one                         |
| -p | 1 | You need to fill in the IP of your proxy, if you have a port you need to bring the port | to use BURP as a proxy then you should pass in 127.0.0.1:8080 |
| -m   | 1        | Scan for single module,such as: Struts2 or Apache, etc.                  | The specific content can be entered by the corresponding name in the project Modules folder. |
| -t   | 1        | Processes usage setting, default(-t 5)                                    |                                                           None   |
|-s    |1       | Enable subdomain detection| |
|-PL |1 |Ports in list form| As long as they are separated by non-numbers, ports exceeding 65535 will be eliminated. If -p or -P is not output, the default port will be scanned. eg: 22,139,445,3389|
|-PR |1 |Ports in the form of ranges| As long as they are separated by non-digits, ports exceeding 65535 will be eliminated. If -p or -P is not output, the default port will be scanned. eg:1-65535 |

### :four_leaf_clover:Updating logs

```
http://medusa.ascotbe.com/Documentation/#/UpDataLog
```

### :open_file_folder:Bug replicate document

```
https://www.ascotbe.com/Loophole
```


### :green_heart:Discussion

- If you find that the corresponding vulnerability cannot be scanned by the plug-in, please submit the [Bug] issue
- If you have any problems that cannot be solved by the documentation, please submit an issue of [help]
- If you have any good comments or ideas, please submit [idea] issue
- QQ group：**690021184**

### :warning:Disclaimer

Add the following content to the original [protocol](https://github.com/Ascotbe/Medusa/blob/master/LICENSE):

- If there is any ambiguity, the Chinese version of the description shall be the only explanation

- Unauthorized commercial use is prohibited for this project
- This project is only for the safe construction activities of enterprises that are **legally authorized**. When using this project for testing, you should ensure that the behavior complies with local laws and regulations and has obtained sufficient authorization.
- If you have any illegal behavior in the process of using this project, you need to bear the corresponding consequences yourself, and we will not bear any legal and joint liabilities.
- Before using this project, please **read carefully and fully understand the content of each clause**. Restrictions, exemption clauses or other clauses involving your major rights and interests may be bolded, underlined, etc. to remind you to pay attention. Unless you have fully read, fully understood and accepted all the terms of this agreement, please do not use this item. Your use behavior or your acceptance of this agreement in any other express or implied manner shall be deemed to have been read and agreed to be bound by this agreement.

### :palm_tree:Contributors

![commit](https://opencollective.com/Medusa/contributors.svg?width=890&button=false)


### :checkered_flag:Timeline

![star](https://starchart.cc/Ascotbe/Medusa.svg)

