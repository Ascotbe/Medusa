import Vue from 'vue'
import api from '../api/rules'
let Base64 = require("js-base64").Base64;

//UNix时间转换正常时间并格式化YYYY-MM-DD hh-mm-ss格式时间
const QjUnixTimes = (e) => {
    let unixTimestamp = new Date(e * 1000);
    let Y = unixTimestamp.getFullYear() + "-";
    let M =
        (unixTimestamp.getMonth() + 1 < 10 ?
            "0" + (unixTimestamp.getMonth() + 1) :
            unixTimestamp.getMonth() + 1) + "-";
    let D =
        unixTimestamp.getDate() + 1 < 10 ?
            "0" + unixTimestamp.getDate() :
            unixTimestamp.getDate();
    let h = unixTimestamp.getHours() + ":";
    let m = unixTimestamp.getMinutes() + ":";
    let s = unixTimestamp.getSeconds();
    let Time = Y + M + D + '\xa0\xa0' + h + m + s;
    return Time;
}
//UNix时间转换正常时间并格式化hh-mm-ss格式时间2019-8-14 8:00:00
const QjUnixTimeHHMMSS = (e) => {
    let unixTimestamp = new Date(e * 1000);
    let Y = unixTimestamp.getFullYear() + "-";
    let M =
        (unixTimestamp.getMonth() + 1 < 10 ?
            "0" + (unixTimestamp.getMonth() + 1) :
            unixTimestamp.getMonth() + 1) + "-";
    let D =
        unixTimestamp.getDate() + 1 < 10 ?
            "0" + unixTimestamp.getDate() :
            unixTimestamp.getDate();
    let h = unixTimestamp.getHours() < 10 ?
        "0" + unixTimestamp.getHours() + ":" :
        unixTimestamp.getHours() + ":";

    let m = unixTimestamp.getMinutes() < 10 ?
        "0" + unixTimestamp.getMinutes() + ":" :
        unixTimestamp.getMinutes() + ":";

    let s = unixTimestamp.getSeconds() < 10 ?
        "0" + unixTimestamp.getSeconds() :
        unixTimestamp.getSeconds();
    let Time = Y + M + D + ' ' + h + m + s;
    return Time;
}
const QJBase64Encode = (e) => {//加密
    return Base64.encode(e);
}
const QJBase64Decode = (e) => {//解密
    return Base64.decode(e);
}
const QJMemorySize = (e) => {//内存处理
    let val = (e / 1024 / 1024 / 1024).toFixed(4)
    return val;
}

const QJGETCAPTCHA = () =>{//获取验证码
    let imgFilePath =  api.get_verification_code().then((res) => {
        return window.URL.createObjectURL(res);
    });
    return imgFilePath
}

export default function (Vue) {
    //添加全局API
    Vue.prototype.$qj = {
        QjUnixTimes,
        QJBase64Encode,
        QJBase64Decode,
        QJMemorySize,
        QjUnixTimeHHMMSS,
        QJGETCAPTCHA
    }
}