##  Environment configuration

### System environment configuration

> Ubuntu

The `JAVA` environment needs to be installed and the `java` command can be executed in the global variables

> CentOS

1.The `JAVA` environment needs to be installed and the `java` command can be executed in the global variables

2.You need to execute the `yum install sqlite*` command to install the **sqlite3.so** library

> Mac OS

The `JAVA` environment needs to be installed and the `java` command can be executed in the global variables

### Install Python env

The current plug-in is developed under the `Python3.7.x` environment. Below` 3.7`, some functions cannot be used. If you need to use a scanner or write a plug-in, you must first install the `Python` development environment. It is recommended to use` PyCharm` + `Anaconda` as development environment.

### Install dependencies

The packages needed to run Medusa are executed in the root directory

```python
pip install -r Medusa.txt
```


## Configuration file

The configuration file referred to in this section is the same file

#### 0x01 DNSLOG

Since the `DNSLOG` I built does not support certain protocols, there are currently two methods for detecting third-party platforms

> The first method (by default)

The first is the default method, no need to modify, convenient and fast

> The second method

Use `DNSLOG` in http://ceye.io/, this method needs to modify the configuration file

```
#Open this file in the root directory (Medusa directory)
vim config.py
```

Change `ceye_dnslog_url` and`ceye_dnslog_key` to the values of your `Identifier` and` API Token` at http://ceye.io/ , Then change `dnslog_name` to `ceye`

**Note: **When using the script, ensure that the network is unblocked. If the vulnerability is not scanned, you may wish to see if the `DNSLOG` data exists

#### 0x02 Debug mode 

This mode is closed by default. If you need to open it, please modify the parameters in the `config.py` file

```
#Default
debug_mode = False
#Turn on Debug mode
debug_mode = True
```

The output content of this mode is not the progress bar and module loading content, but has become the error message of each plugin

![debug](https://github.com/Ascotbe/Random-img/blob/master/Medusa/0.76Debug.gif?raw=true)

#### 0x03 Multithreading

Because the refactoring replaces the previous multi-threads with multi-processes, the for loop in a single plugin is replaced with multi-threads, so the default number of threads is **15**. If you need to modify, change the value of `thread_number` in the configuration file to The number of threads you need

```
thread_number=15 #Default number of threads
```



## Quick start

The tool is still in the testing stage. If you have any questions, please submit `issues`. Remember, this scanner is only use for authorized testing

#### 0x01 Use the scanner to scan a single website

Note: It is recommended to put the complete path, some plugins need to use the full path name, for example: `Struts2`

```bash
python3 MedusaScan.py -u https://www.ascotbe.com
```

#### 0x02 Use the scanner to scan a batch of websites

`Ascotbe.txt` is the file you store. It is best to put it in the same directory as the` MedusaScan.py` file. The file format you store `URL` is one` url` per line

Documents need to pay attention to several specifications

- Need to fill in `url` and one` url` per line

- `url` needs to bring` http:// `or` https:// `, if both protocols need to be scanned it can be written in two lines

- If different ports in a single `url` correspond to different services, you need to write them. For example, **8080** and **1024** correspond to different services, and if you want to scan all, you need to press the following Written in the form

  ```
  http://ascotbe.com:1024/test
  http://ascotbe.com:8080/test
  ```

- Different subdirectories, such as `test` and` medusa`, also need to be written on separate branches

  ```
  http://ascotbe.com:1024/test
  http://ascotbe.com:1024/medusa
  ```

Next run the following command to start scanning

```bash
python3 MedusaScan.py -f Ascotbe.txt #Your files are best placed in the same level as MedusaScan
```

#### ~~0x03 Link crawling in JavaScript on the target website~~

This function is commented because not very useful now

```bash
python3 MedusaScan.py -u https://www.ascotbe.com -j
```

#### 0x04 Collect subdomains for the target website

The scan result is in the `ScanResult` directory, only the domain name is supported and the **IP** form is not supported

```bash
python3 MedusaScan.py -u https://www.ascotbe.com -s
```

#### 0x05 Proxy function

```bash
python3 MedusaScan.py -u https://www.ascotbe.com -p 127.0.0.1:8080
```

#### 0x06 Using target Header

Supported parameters：`firefox`，`ie`，`msie`，`opera`，`chrome`，`AppleWebKit`，`Gecko`，`safari `

Currently supports common browsers, 3 of which are listed below (case sensitive)

```bash
python3 MedusaScan.py -u https://www.ascotbe.com -a firefox
python3 MedusaScan.py -u https://www.ascotbe.com -a ie
python3 MedusaScan.py -u https://www.ascotbe.com -a Gecko
```

You can also customize the `header` parameter, remember to add double quotes to the custom` header` containing `" "`, if your `header` is not compliant, it will not prompt an error

```bash
python3 MedusaScan.py -u https://www.ascotbe.com -a "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2117.157 Safari/537.36"
```

#### 0x07 Scanning for single modules

Please use the name supported by the module for the root folder. A folder name corresponds to a module, and please pay attention to capitalization. It is really incomprehensible. Please refer to [in this file](https://www.ascotbe.com/Medusa/Documentation/#/PluginDirectory) name

```bash
python3 MedusaScan.py -u https://www.ascotbe.com -m Struts2
```

#### 0x08 Processes setting

Turn on the multi-process function, the default is 15 processes, the more processes, the faster, when a plugin uses the for loop, it will start multi-threading in the process!

```bash
python3 MedusaScan.py -u https://www.ascotbe.com -t 100 #100 processes
```

#### 0x09 sensitive information leakage

Integrated into the module, the full scan is automatically started, if you need to scan separately, you only need to enter the module name

#### 0x10 Interactive command execution

Call the plug-in that can perform command execution interaction, you can use the `-l` (not yet written) parameter view

```bash
python3 MedusaScan.py -u http://127.0.0.1:7001 -e CVE-2019-2729
```

After the call is successful, you need to enter the target operating system first, and then enter the executed command. If the execution is changed without echo, it will output `Return packet: The vulnerability is command execution without echo`, if not, it will be returned. Explicit execution.

If you need to log out, please enter `QuitMedusa` to exit the command execution.

```bash
ascotbe@orange$ python3 MedusaScan.py -u http://127.0.0.1:7001 -e CVE-2019-2729



  ___ __ __   ______   ______   __  __   ______   ________      
 /__//_//_/\ /_____/\ /_____/\ /_/\/_/\ /_____/\ /_______/\     
 \::\| \| \ \\::::_\/_\:::_ \ \\:\ \:\ \\::::_\/_\::: _  \ \    
  \:.      \ \\:\/___/\\:\ \ \ \\:\ \:\ \\:\/___/\\::(_)  \ \   
   \:.\-/\  \ \\::___\/_\:\ \ \ \\:\ \:\ \\_::._\:\\:: __  \ \  
    \. \  \  \ \\:\____/\\:\/.:| |\:\_\:\ \ /____\:\\:.\ \  \ \ 
     \__\/ \__\/ \_____\/ \____/_/ \_____\/ \_____\/ \__\/\__\/ 
                                                                
 
                                                                                   
          Blog  https://www.ascotbe.com  |  v0.86    

[ + ] Please enter the target operating system [windows / linux]: Windows
[ + ] Please enter the command to be executed: echo Ayanami Rei
[ + ] Command sent successfully, please refer to the returned data packet
[ + ] Return packet：Ayanami Rei
[ + ] Please enter the command to be executed: QuitMedusa
[ ! ] Command execution call has ended~ 
```

## Result

1. The output `The number of vulnerabilities scanned was: 0` means that the vulnerability was not scanned

2. There are no other files in the `ScanResult` directory except `Medusa.txt`

3. There is no new content in the `Medusa.db` file, or the file is not created

4. If none of the above three points exist, it means that no loopholes really have been found

