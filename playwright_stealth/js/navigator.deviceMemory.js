Object.defineProperty(Object.getPrototypeOf(navigator), 'deviceMemory', {
    get: () => opts.device_memory || 8
})
