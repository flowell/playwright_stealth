# -*- coding: utf-8 -*-
import json
from dataclasses import dataclass
from typing import Tuple, Optional, Dict

import pkg_resources
from playwright.async_api import Page as AsyncPage
from playwright.sync_api import Page as SyncPage


def from_file(name):
    """Read script from ./js directory"""
    return pkg_resources.resource_string('playwright_stealth', f'js/{name}').decode()


SCRIPTS: Dict[str, str] = {
    'chrome_csi': from_file('chrome.csi.js'),
    'chrome_app': from_file('chrome.app.js'),
    'chrome_runtime': from_file('chrome.runtime.js'),
    'chrome_load_times': from_file('chrome.load.times.js'),
    'chrome_hairline': from_file('chrome.hairline.js'),
    'generate_magic_arrays': from_file('generate.magic.arrays.js'),
    'iframe_content_window': from_file('iframe.contentWindow.js'),
    'media_codecs': from_file('media.codecs.js'),
    'navigator_plugins': from_file('navigator.plugins.js'),
    'navigator_permissions': from_file('navigator.permissions.js'),
    'navigator_languages': from_file('navigator.languages.js'),
    'navigator_platform': from_file('navigator.platform.js'),
    'navigator_user_agent': from_file('navigator.userAgent.js'),
    'navigator_hardware_concurrency': from_file('navigator.hardwareConcurrency.js'),
    'navigator_device_memory': from_file('navigator.deviceMemory.js'),
    'utils': from_file('utils.js'),
    'webdriver': from_file('navigator.webdriver.js'),
    'webgl_vendor': from_file('webgl.vendor.js'),
    'window_screen': from_file('window.screen.js'),
    'window_web_rtc': from_file('window.web_rtc.js'),
}


@dataclass
class StealthConfig:
    """
    Playwright stealth configuration that applies stealth strategies to playwright page objects.
    The stealth strategies are contained in ./js package and are basic javascript scripts that are executed
    on every page.goto() called.
    Note:
        All init scripts are combined by playwright into one script and then executed this means
        the scripts should not have conflicting constants/variables etc. !
        This also means scripts can be extended by overriding enabled_scripts generator:
        ```
        @property
        def enabled_scripts():
            yield 'console.log("first script")'
            yield from super().enabled_scripts()
            yield 'console.log("last script")'
        ```
    """
    # load script options
    webdriver: bool = True
    webgl_vendor: bool = True
    chrome_app: bool = True
    chrome_csi: bool = True
    chrome_load_times: bool = True
    chrome_runtime: bool = True
    iframe_content_window: bool = True
    media_codecs: bool = True
    navigator_hardware_concurrency: int = 12
    navigator_device_memory: int = 8
    navigator_languages: bool = True
    navigator_permissions: bool = True
    navigator_platform: bool = True
    navigator_plugins: bool = True
    navigator_user_agent: bool = True
    hairline: bool = True
    window_screen: bool = True
    window_web_rtc: bool = True

    # options
    wgl_vendor: str = 'Intel Inc.'
    renderer: str = 'Intel Iris OpenGL Engine'
    nav_vendor: str = 'Google Inc.'
    nav_app_name: str = 'Netscape'
    nav_app_code_name: str = 'Mozilla'
    nav_user_agent: str = None
    nav_platform: str = 'Win32'
    languages: Tuple[str] = ('zh-CN', 'zh')
    runOnInsecureOrigins: Optional[bool] = None

    window_inner_width: int = 1920
    window_outer_width: int = 1920
    window_inner_height: int = 937
    window_outer_height: int = 1040
    window_screen_width: int = 1920
    window_screen_height: int = 1080
    window_screen_avail_height: int = 1040
    window_screen_avail_width: int = 1920
    window_screen_avail_left: int = 0
    window_screen_avail_top: int = 0
    window_screen_color_depth: int = 24
    window_screen_pixel_depth: int = 24
    window_web_rtc_address: str = '127.0.0.1'
    
    @property
    def enabled_scripts(self):
        opts = json.dumps({
            'webgl_vendor': self.wgl_vendor,
            'webgl_renderer': self.renderer,
            'navigator_vendor': self.nav_vendor,
            'navigator_platform': self.nav_platform,
            'navigator_user_agent': self.nav_user_agent,
            'navigator_app_name': self.nav_app_name,
            'navigator_app_code_name': self.nav_app_code_name,
            'languages': list(self.languages),
            'runOnInsecureOrigins': self.runOnInsecureOrigins,
            'navigator_hardware_concurrency': self.navigator_hardware_concurrency,
            'navigator_device_memory': self.navigator_device_memory,
            'window_inner_width': self.window_inner_width,
            'window_outer_width': self.window_outer_width,
            'window_inner_height': self.window_inner_height,
            'window_outer_height': self.window_outer_height,
            'window_screen_width': self.window_screen_width,
            'window_screen_height': self.window_screen_height,
            'window_screen_avail_height': self.window_screen_avail_height,
            'window_screen_avail_width': self.window_screen_avail_width,
            'window_screen_avail_left': self.window_screen_avail_left,
            'window_screen_avail_top': self.window_screen_avail_top,
            'window_screen_color_depth': self.window_screen_color_depth,
            'window_screen_pixel_depth': self.window_screen_pixel_depth,
            'window_web_rtc_address': self.window_web_rtc_address,
        })
        # defined options constant
        yield f'const opts = {opts}'
        # init utils and generate_magic_arrays helper
        yield SCRIPTS['utils']
        yield SCRIPTS['generate_magic_arrays']

        if self.chrome_app:
            yield SCRIPTS['chrome_app']
        if self.chrome_csi:
            yield SCRIPTS['chrome_csi']
        if self.hairline:
            yield SCRIPTS['chrome_hairline']
        if self.chrome_load_times:
            yield SCRIPTS['chrome_load_times']
        if self.chrome_runtime:
            yield SCRIPTS['chrome_runtime']
        if self.iframe_content_window:
            yield SCRIPTS['iframe_content_window']
        if self.media_codecs:
            yield SCRIPTS['media_codecs']
        if self.navigator_hardware_concurrency:
            yield SCRIPTS['navigator_hardware_concurrency']
        if self.navigator_device_memory:
            yield SCRIPTS['navigator_device_memory']
        if self.navigator_languages:
            yield SCRIPTS['navigator_languages']
        if self.navigator_permissions:
            yield SCRIPTS['navigator_permissions']
        if self.navigator_platform:
            yield SCRIPTS['navigator_platform']
        if self.navigator_plugins:
            yield SCRIPTS['navigator_plugins']
        if self.navigator_user_agent:
            yield SCRIPTS['navigator_user_agent']
        if self.webdriver:
            yield SCRIPTS['webdriver']
        if self.webgl_vendor:
            yield SCRIPTS['webgl_vendor']
        if self.window_screen:
            yield SCRIPTS['window_screen']
        if self.window_web_rtc:
            yield SCRIPTS['window_web_rtc']

def stealth_sync(page: SyncPage, config: StealthConfig = None):
    """teaches synchronous playwright Page to be stealthy like a ninja!"""
    for script in (config or StealthConfig()).enabled_scripts:
        page.add_init_script(script)


async def stealth_async(page: AsyncPage, config: StealthConfig = None):
    """teaches asynchronous playwright Page to be stealthy like a ninja!"""
    for script in (config or StealthConfig()).enabled_scripts:
        await page.add_init_script(script)
