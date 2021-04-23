import axios from 'axios'
import qs from 'qs'
import { message } from 'ant-design-vue';
import store from '../Vuex'

// import Cookies from 'js-cookie'

// const xsrfToken = Cookies.get('XSRF-TOKEN')

const config = require('../../faceConfig')
export const baseURL = config.basePath


// create an axios instance
const service = axios.create({
  baseURL,
  timeout: 20000, // request timeout
})
console.log(service)
// // request interceptor
service.interceptors.request.use(
  config => {

    // console.log(store.state.storeToken)
    // if(store.state.storeToken){
    //   config.headers.common['Token'] = store.state.storeToken
    // }
    // console.log(config)
    // console.log(store.state.storeToken)

    // do something before request is sent
    // if (xsrfToken) {
    //   config.headers['X-XSRF-TOKEN'] = xsrfToken
    //   // console.log(xsrfToken)
    // }
    // if (store.getters.token) {
    //   // let each request carry token
    //   // ['X-Token'] is a custom headers key
    //   // please modify it according to the actual situation
    //   config.headers['X-Token'] = getToken()
    // }
    return config
  },
  error => {
    // do something with request error
    console.log(error) // for debug
    return Promise.reject(error)
  }
)

// response interceptor
service.interceptors.response.use(
  /**
   * If you want to get http information such as headers or status
   * Please return  response => response
   */

  /**
   * Determine the request status by custom code
   * Here is just an example
   * You can also judge the status by HTTP Status Code
   */
  response => {
    if(response.headers.verificationcodekey){
      store.commit("verificationcodekey", response.headers.verificationcodekey)
    }
    const res = response.data
    // console.log(message)
    // if the custom code is not 0, it is judged as an error.
    // if (res.code !== 0) {
    // Message.error(res.message || 'Error')
    // 50008: Illegal token; 50012: Other clients logged in; 50014: Token expired;
    // if (res.code === 50008 || res.code === 50012 || res.code === 50014) {
    //   // to re-login
    //   MessageBox.confirm(
    //     'You have been logged out, you can cancel to stay on this page, or log in again',
    //     'Confirm logout',
    //     {
    //       confirmButtonText: 'Re-Login',
    //       cancelButtonText: 'Cancel',
    //       type: 'warning'
    //     }
    //   ).then(() => {
    //     store.dispatch('user/resetToken').then(() => {
    //       location.reload()
    //     })
    //   })
    // }
    //   return Promise.reject(new Error(res.message || 'Error'))
    // } else {
    return res
    // }
  },
  error => {
    console.log('err' + error) // for debug
    message.error(error.message)

    return Promise.reject(error)
  }
)

export function get(url, params, config) {
  return new Promise((resolve, reject) => {
    service
      .get(url, {
        params: params,
        ...config
      })
      .then(response => {
        resolve(response)
      })
      .catch(err => {
        reject(err)
      })
  })
}
export function getParams(url, params, config) {
  return new Promise((resolve, reject) => {
    service
      .get(url, {
        params: qs.stringify(params),
        ...config
      })
      .then(response => {
        resolve(response)
      })
      .catch(err => {
        reject(err)
      })
  })
}

export function post(url, params, config) {
  return new Promise((resolve, reject) => {
    service
      .post(url, params, {
        ...config
      })
      .then(response => {
        resolve(response)
      })
      .catch(err => {
        reject(err)
      })
  })
}

export function postAcction(url, params, config) {
  return new Promise((resolve, reject) => {
    service
      .post(url, qs.stringify(params), {
        ...config
      })
      .then(response => {
        resolve(response)
      })
      .catch(err => {
        reject(err)
      })
  })
}

export function postDownload(url, params, config) {
  return new Promise((resolve, reject) => {
    service
      .post(url, params, {
        ...config,
        responseType: 'blob'
      })
      .then(response => {
        resolve(response)
      })
      .catch(err => {
        reject(err)
      })
  })
}
export function postParams(url, params, config) {
  return new Promise((resolve, reject) => {
    service
      .post(url, qs.stringify(params), {
        ...config
      })
      .then(response => {
        resolve(response)
      })
      .catch(err => {
        reject(err)
      })
  })
}

export default service
