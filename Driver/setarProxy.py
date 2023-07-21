import zipfile


def configurarProxt(proxyUser):
    proxyUser = proxyUser.split(":")
    PROXY_HOST = proxyUser[0]  # rotating proxy or host
    PROXY_PORT = proxyUser[1]  # port
    PROXY_USER = proxyUser[2]  # username
    PROXY_PASS = proxyUser[3]  # password
    manifest_json = """
        {
        "version": "1.0.0",
        "manifest_version": 2,
        "name": "Chrome Proxy",
        "permissions": [
            "proxy",
            "tabs",
            "unlimitedStorage",
            "storage",
            "<all_urls>",
            "webRequest",
            "webRequestBlocking"
        ],
        "background": {
            "scripts": ["background.js"]
        },
        "minimum_chrome_version":"22.0.0"
        }
        """
    background_js = """
        var config = {
            mode: "fixed_servers",
            rules: {
            singleProxy: {
                scheme: "http",
                host: "%s",
                port: parseInt(%s)
            },
            bypassList: ["localhost"]
            }
        };

    chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

    function callbackFn(details) {
        return {
            authCredentials: {
                username: "%s",
                password: "%s"
            }
        };
    }

    chrome.webRequest.onAuthRequired.addListener(
                callbackFn,
                {urls: ["<all_urls>"]},
                ['blocking']
    );
    """ % (
        PROXY_HOST,
        PROXY_PORT,
        PROXY_USER,
        PROXY_PASS,
    )
    pluginfile = "proxy_auth_plugin.zip"
    with zipfile.ZipFile(pluginfile, "w") as zp:
        zp.writestr("manifest.json", manifest_json)
        zp.writestr("background.js", background_js)
