Object.defineProperty(Object.getPrototypeOf(navigator), 'languages', {
    get: () => opts.languages || ['zh-CN', 'zh']
})
Object.defineProperty(Object.getPrototypeOf(navigator), 'language', {
    get: () => opts.languages[0]
})
