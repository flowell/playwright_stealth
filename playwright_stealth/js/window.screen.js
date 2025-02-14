"use strict";

if (window) {
    window.innerWidth = opts.window_inner_width || 1920;
    window.outerWidth = opts.window_outer_width || 1920;
    window.innerHeight = opts.window_inner_height || 937;
    window.outerHeight = opts.window_outer_height || 1040;

    if (window.screen) {
        Object.defineProperty(window.screen, "width", {
          value: opts.window_screen_width || 1920,
          configurable: true,
        });
        Object.defineProperty(window.screen, "height", {
          value: opts.window_screen_height || 1080,
          configurable: true,
        });
        Object.defineProperty(window.screen, "availHeight", {
          value: opts.window_screen_avail_height || 1040,
          configurable: true,
        });
        Object.defineProperty(window.screen, "availWidth", {
          value: opts.window_screen_avail_width || 1920,
          configurable: true,
        });
        Object.defineProperty(window.screen, "availLeft", {
          value: opts.window_screen_avail_left || 0,
          configurable: true,
        });
        Object.defineProperty(window.screen, "availTop", {
          value: opts.window_screen_avail_top || 0,
          configurable: true,
        });
        Object.defineProperty(window.screen, "colorDepth", {
          value: opts.window_screen_color_depth || 24,
          configurable: true,
        });
        Object.defineProperty(window.screen, "pixelDepth", {
          value: opts.window_screen_pixel_depth || 24,
          configurable: true,
        });
    }
}

