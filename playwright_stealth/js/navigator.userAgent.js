// replace Headless references in default useragent
var __navigator_user_agent = navigator.userAgent
Object.defineProperty(Object.getPrototypeOf(navigator), 'userAgent', {
    get: () =>  opts.navigator_user_agent || __navigator_user_agent.replace('Headless', '')
})

Object.defineProperty(Object.getPrototypeOf(navigator), 'appCodeName', {
    get: () => opts.navigator_app_code_name || 'Mozilla'
})

Object.defineProperty(Object.getPrototypeOf(navigator), 'appVersion', {
    get: () => navigator.userAgent.replace(navigator.appCodeName+'/', '')
})

Object.defineProperty(Object.getPrototypeOf(navigator), 'appname', {
    get: () => opts.navigator_app_name || 'Netscape'
})

Object.defineProperty(Object.getPrototypeOf(navigator), 'vendor', {
    get: () => opts.navigator_vendor || 'Google Inc.'
})