#include <io.h>
#include <iostream>
#include <fstream>
#include<Windows.h>
#include<winhttp.h>
#include<vector>
using namespace std;
const char* suffix_list[]  = {"docx","txt"};



void GetDrive(vector<string> &drive_vector)//获取系统有哪些可用盘符
{

    DWORD len = GetLogicalDriveStrings(0, NULL);//获取系统盘符字符串长度
    char* drive = new char[len];//构建字符数组
    GetLogicalDriveStrings(len, drive);//获取系统盘符字符串
    int type = 0;

    while (*drive != '\0')
   
    {
        type = GetDriveType(drive);
        if (type == DRIVE_FIXED || type == DRIVE_REMOVABLE)//只要可移动磁盘和硬盘
        {
            drive_vector.push_back(drive);
        }
        drive += strlen(drive) + 1;			//定位到下一个字符串.加一是为了跳过'\0'字符串.
        
    }


}


void GetFilePath(string folder_path, vector<string>& file_path)
{
    //文件句柄
    //注意：我发现有些文章代码此处是long类型，实测运行中会报错访问异常
    intptr_t file_handle = 0;
    //文件信息
    struct _finddata_t file_info;
    string p;
    if ((file_handle = _findfirst(p.assign(folder_path).append("\\*").c_str(), &file_info)) != -1)
    {
        do
        {
            //如果是目录,递归查找
            //如果不是,把文件绝对路径存入vector中
            if (strcmp(file_info.name, "Windows") == 0 && folder_path.length() <= 4)//排除系统文件
            {
                continue;
            }
            else if ((file_info.attrib & _A_SUBDIR))
            {

                if(strcmp(file_info.name, ".") != 0 && strcmp(file_info.name, "..") != 0) 
                {
                    GetFilePath(p.assign(folder_path).append("\\").append(file_info.name), file_path);

                }
            }
            else
            {
                //file_path.push_back(p.assign(folder_path).append("\\").append(file_info.name));

                string tmp = file_info.name;
                string::size_type str_size = tmp.find_last_of('\\') + 1;
                string file_name = tmp.substr(str_size, tmp.length() - str_size);//获取文件名


                //获取不带后缀的文件名
                //string name = filename.substr(0, filename.rfind("."));

                string suffix_str = file_name.substr(file_name.find_last_of('.') + 1);//获取后缀名
                //cout << folder_path.c_str() << "\\" << file_info.name << endl;
      
                for (int i = 0; i < (sizeof(suffix_list) / sizeof(char*)); i++)
                {
                    if (strcmp(suffix_list[i], suffix_str.c_str()) == 0)
                    {
                        file_path.push_back(folder_path + '\\' + tmp);
                  
                    }

                }

            }
            
        } while (_findnext(file_handle, &file_info) == 0);
        _findclose(file_handle);
    }
}

int main() 
{
    vector<string> drive_vector;
    vector<string>file_path;
    GetDrive(drive_vector);
    for (unsigned int i = 0; i < drive_vector.size(); i++)
    {
        GetFilePath(drive_vector[i].c_str(), file_path);
        //GetFilePath("C:\\v2rayN", file_path);

    }
    for (unsigned int i = 0; i < file_path.size(); i++)
    {
       cout<<file_path[i].c_str()<<endl;

    }
    
    return 0;
}