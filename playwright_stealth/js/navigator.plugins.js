data = {
    "mimeTypes": [
        {
            "type": "application/pdf",
            "suffixes": "pdf",
            "description": "Portable Document Format",
            "__pluginName": "PDF Viewer"
        },
        {
            "type": "text/pdf",
            "suffixes": "pdf",
            "description": "Portable Document Format",
            "__pluginName": "PDF Viewer"
        }
    ],
    "plugins": [
        {
            "name": "PDF Viewer",
            "filename": "internal-pdf-viewer",
            "description": "Portable Document Format",
            "__mimeTypes": ["application/pdf", "text/pdf"]
        },
        {
            "name": "Chrome PDF Viewer",
            "filename": "internal-pdf-viewer",
            "description": "Portable Document Format",
            "__mimeTypes": ["application/pdf", "text/pdf"]
        },
        {
            "name": "Chromium PDF Viewer",
            "filename": "internal-pdf-viewer",
            "description": "Portable Document Format",
            "__mimeTypes": ["application/pdf", "text/pdf"]
        },
        {
            "name": "Microsoft Edge PDF Viewer",
            "filename": "internal-pdf-viewer",
            "description": "Portable Document Format",
            "__mimeTypes": ["application/pdf", "text/pdf"]
        },
        {
            "name": "WebKit built-in PDF",
            "filename": "internal-pdf-viewer",
            "description": "Portable Document Format",
            "__mimeTypes": ["application/pdf", "text/pdf"]
        }
    ]
}

// That means we're running headful
const hasPlugins = 'plugins' in navigator && navigator.plugins.length
if (!(hasPlugins)) {

    const mimeTypes = generateMagicArray(
        data.mimeTypes,
        MimeTypeArray.prototype,
        MimeType.prototype,
        'type'
    )
    const plugins = generateMagicArray(
        data.plugins,
        PluginArray.prototype,
        Plugin.prototype,
        'name'
    )

    // Plugin and MimeType cross-reference each other, let's do that now
    // Note: We're looping through `data.plugins` here, not the generated `plugins`
    for (const pluginData of data.plugins) {
        pluginData.__mimeTypes.forEach((type, index) => {
            plugins[pluginData.name][index] = mimeTypes[type]
            plugins[type] = mimeTypes[type]
            if (!Object.getOwnPropertyDescriptor(mimeTypes[type], 'enabledPlugin')) {
                Object.defineProperty(mimeTypes[type], 'enabledPlugin', {
                    value: JSON.parse(JSON.stringify(plugins[pluginData.name])),
                    writable: false,
                    enumerable: false, // Important: `JSON.stringify(navigator.plugins)`
                    configurable: false
                })
            }
        })
    }

    const patchNavigator = (name, value) =>
        utils.replaceProperty(Object.getPrototypeOf(navigator), name, {
            get() {
                return value
            }
        })

    patchNavigator('mimeTypes', mimeTypes)
    patchNavigator('plugins', plugins)
}