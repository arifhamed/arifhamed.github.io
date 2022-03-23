---
title: Markdown Live Preview
layout: default
permalink: /resources/markdown-live-preview
redirect-from:
 - /resources/markdown-live-preview/
---

<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <style id="ace-github">.ace-github .ace_gutter {background: #e8e8e8;color: #AAA;}.ace-github  {background: #fff;color: #000;}.ace-github .ace_keyword {font-weight: bold;}.ace-github .ace_string {color: #D14;}.ace-github .ace_variable.ace_class {color: teal;}.ace-github .ace_constant.ace_numeric {color: #099;}.ace-github .ace_constant.ace_buildin {color: #0086B3;}.ace-github .ace_support.ace_function {color: #0086B3;}.ace-github .ace_comment {color: #998;font-style: italic;}.ace-github .ace_variable.ace_language  {color: #0086B3;}.ace-github .ace_paren {font-weight: bold;}.ace-github .ace_boolean {font-weight: bold;}.ace-github .ace_string.ace_regexp {color: #009926;font-weight: normal;}.ace-github .ace_variable.ace_instance {color: teal;}.ace-github .ace_constant.ace_language {font-weight: bold;}.ace-github .ace_cursor {color: black;}.ace-github.ace_focus .ace_marker-layer .ace_active-line {background: rgb(255, 255, 204);}.ace-github .ace_marker-layer .ace_active-line {background: rgb(245, 245, 245);}.ace-github .ace_marker-layer .ace_selection {background: rgb(181, 213, 255);}.ace-github.ace_multiselect .ace_selection.ace_start {box-shadow: 0 0 3px 0px white;}.ace-github.ace_nobold .ace_line > span {font-weight: normal !important;}.ace-github .ace_marker-layer .ace_step {background: rgb(252, 255, 0);}.ace-github .ace_marker-layer .ace_stack {background: rgb(164, 229, 101);}.ace-github .ace_marker-layer .ace_bracket {margin: -1px 0 0 -1px;border: 1px solid rgb(192, 192, 192);}.ace-github .ace_gutter-active-line {background-color : rgba(0, 0, 0, 0.07);}.ace-github .ace_marker-layer .ace_selected-word {background: rgb(250, 250, 255);border: 1px solid rgb(200, 200, 250);}.ace-github .ace_invisible {color: #BFBFBF}.ace-github .ace_print-margin {width: 1px;background: #e8e8e8;}.ace-github .ace_indent-guide {background: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAYAAACZgbYnAAAAE0lEQVQImWP4////f4bLly//BwAmVgd1/w11/gAAAABJRU5ErkJggg==") right repeat-y;}
            /*# sourceURL=ace/css/ace-github */
        </style>
        <style>    .error_widget_wrapper {        background: inherit;        color: inherit;        border:none    }    .error_widget {        border-top: solid 2px;        border-bottom: solid 2px;        margin: 5px 0;        padding: 10px 40px;        white-space: pre-wrap;    }    .error_widget.ace_error, .error_widget_arrow.ace_error{        border-color: #ff5a5a    }    .error_widget.ace_warning, .error_widget_arrow.ace_warning{        border-color: #F1D817    }    .error_widget.ace_info, .error_widget_arrow.ace_info{        border-color: #5a5a5a    }    .error_widget.ace_ok, .error_widget_arrow.ace_ok{        border-color: #5aaa5a    }    .error_widget_arrow {        position: absolute;        border: solid 5px;        border-top-color: transparent!important;        border-right-color: transparent!important;        border-left-color: transparent!important;        top: -5px;    }</style>
        <style id="ace-tm">.ace-tm .ace_gutter {background: #f0f0f0;color: #333;}.ace-tm .ace_print-margin {width: 1px;background: #e8e8e8;}.ace-tm .ace_fold {background-color: #6B72E6;}.ace-tm {background-color: #FFFFFF;color: black;}.ace-tm .ace_cursor {color: black;}.ace-tm .ace_invisible {color: rgb(191, 191, 191);}.ace-tm .ace_storage,.ace-tm .ace_keyword {color: blue;}.ace-tm .ace_constant {color: rgb(197, 6, 11);}.ace-tm .ace_constant.ace_buildin {color: rgb(88, 72, 246);}.ace-tm .ace_constant.ace_language {color: rgb(88, 92, 246);}.ace-tm .ace_constant.ace_library {color: rgb(6, 150, 14);}.ace-tm .ace_invalid {background-color: rgba(255, 0, 0, 0.1);color: red;}.ace-tm .ace_support.ace_function {color: rgb(60, 76, 114);}.ace-tm .ace_support.ace_constant {color: rgb(6, 150, 14);}.ace-tm .ace_support.ace_type,.ace-tm .ace_support.ace_class {color: rgb(109, 121, 222);}.ace-tm .ace_keyword.ace_operator {color: rgb(104, 118, 135);}.ace-tm .ace_string {color: rgb(3, 106, 7);}.ace-tm .ace_comment {color: rgb(76, 136, 107);}.ace-tm .ace_comment.ace_doc {color: rgb(0, 102, 255);}.ace-tm .ace_comment.ace_doc.ace_tag {color: rgb(128, 159, 191);}.ace-tm .ace_constant.ace_numeric {color: rgb(0, 0, 205);}.ace-tm .ace_variable {color: rgb(49, 132, 149);}.ace-tm .ace_xml-pe {color: rgb(104, 104, 91);}.ace-tm .ace_entity.ace_name.ace_function {color: #0000A2;}.ace-tm .ace_heading {color: rgb(12, 7, 255);}.ace-tm .ace_list {color:rgb(185, 6, 144);}.ace-tm .ace_meta.ace_tag {color:rgb(0, 22, 142);}.ace-tm .ace_string.ace_regex {color: rgb(255, 0, 0)}.ace-tm .ace_marker-layer .ace_selection {background: rgb(181, 213, 255);}.ace-tm.ace_multiselect .ace_selection.ace_start {box-shadow: 0 0 3px 0px white;}.ace-tm .ace_marker-layer .ace_step {background: rgb(252, 255, 0);}.ace-tm .ace_marker-layer .ace_stack {background: rgb(164, 229, 101);}.ace-tm .ace_marker-layer .ace_bracket {margin: -1px 0 0 -1px;border: 1px solid rgb(192, 192, 192);}.ace-tm .ace_marker-layer .ace_active-line {background: rgba(0, 0, 0, 0.07);}.ace-tm .ace_gutter-active-line {background-color : #dcdcdc;}.ace-tm .ace_marker-layer .ace_selected-word {background: rgb(250, 250, 255);border: 1px solid rgb(200, 200, 250);}.ace-tm .ace_indent-guide {background: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAYAAACZgbYnAAAAE0lEQVQImWP4////f4bLly//BwAmVgd1/w11/gAAAABJRU5ErkJggg==") right repeat-y;}
            /*# sourceURL=ace/css/ace-tm */
        </style>
        <style id="ace_editor.css">.ace_br1 {border-top-left-radius    : 3px;}.ace_br2 {border-top-right-radius   : 3px;}.ace_br3 {border-top-left-radius    : 3px; border-top-right-radius:    3px;}.ace_br4 {border-bottom-right-radius: 3px;}.ace_br5 {border-top-left-radius    : 3px; border-bottom-right-radius: 3px;}.ace_br6 {border-top-right-radius   : 3px; border-bottom-right-radius: 3px;}.ace_br7 {border-top-left-radius    : 3px; border-top-right-radius:    3px; border-bottom-right-radius: 3px;}.ace_br8 {border-bottom-left-radius : 3px;}.ace_br9 {border-top-left-radius    : 3px; border-bottom-left-radius:  3px;}.ace_br10{border-top-right-radius   : 3px; border-bottom-left-radius:  3px;}.ace_br11{border-top-left-radius    : 3px; border-top-right-radius:    3px; border-bottom-left-radius:  3px;}.ace_br12{border-bottom-right-radius: 3px; border-bottom-left-radius:  3px;}.ace_br13{border-top-left-radius    : 3px; border-bottom-right-radius: 3px; border-bottom-left-radius:  3px;}.ace_br14{border-top-right-radius   : 3px; border-bottom-right-radius: 3px; border-bottom-left-radius:  3px;}.ace_br15{border-top-left-radius    : 3px; border-top-right-radius:    3px; border-bottom-right-radius: 3px; border-bottom-left-radius: 3px;}.ace_editor {position: relative;overflow: hidden;padding: 0;font: 12px/normal 'Monaco', 'Menlo', 'Ubuntu Mono', 'Consolas', 'source-code-pro', monospace;direction: ltr;text-align: left;-webkit-tap-highlight-color: rgba(0, 0, 0, 0);}.ace_scroller {position: absolute;overflow: hidden;top: 0;bottom: 0;background-color: inherit;-ms-user-select: none;-moz-user-select: none;-webkit-user-select: none;user-select: none;cursor: text;}.ace_content {position: absolute;box-sizing: border-box;min-width: 100%;contain: style size layout;font-variant-ligatures: no-common-ligatures;}.ace_dragging .ace_scroller:before{position: absolute;top: 0;left: 0;right: 0;bottom: 0;content: '';background: rgba(250, 250, 250, 0.01);z-index: 1000;}.ace_dragging.ace_dark .ace_scroller:before{background: rgba(0, 0, 0, 0.01);}.ace_selecting, .ace_selecting * {cursor: text !important;}.ace_gutter {position: absolute;overflow : hidden;width: auto;top: 0;bottom: 0;left: 0;cursor: default;z-index: 4;-ms-user-select: none;-moz-user-select: none;-webkit-user-select: none;user-select: none;contain: style size layout;}.ace_gutter-active-line {position: absolute;left: 0;right: 0;}.ace_scroller.ace_scroll-left {box-shadow: 17px 0 16px -16px rgba(0, 0, 0, 0.4) inset;}.ace_gutter-cell {position: absolute;top: 0;left: 0;right: 0;padding-left: 19px;padding-right: 6px;background-repeat: no-repeat;}.ace_gutter-cell.ace_error {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAABOFBMVEX/////////QRswFAb/Ui4wFAYwFAYwFAaWGAfDRymzOSH/PxswFAb/SiUwFAYwFAbUPRvjQiDllog5HhHdRybsTi3/Tyv9Tir+Syj/UC3////XurebMBIwFAb/RSHbPx/gUzfdwL3kzMivKBAwFAbbvbnhPx66NhowFAYwFAaZJg8wFAaxKBDZurf/RB6mMxb/SCMwFAYwFAbxQB3+RB4wFAb/Qhy4Oh+4QifbNRcwFAYwFAYwFAb/QRzdNhgwFAYwFAbav7v/Uy7oaE68MBK5LxLewr/r2NXewLswFAaxJw4wFAbkPRy2PyYwFAaxKhLm1tMwFAazPiQwFAaUGAb/QBrfOx3bvrv/VC/maE4wFAbRPBq6MRO8Qynew8Dp2tjfwb0wFAbx6eju5+by6uns4uH9/f36+vr/GkHjAAAAYnRSTlMAGt+64rnWu/bo8eAA4InH3+DwoN7j4eLi4xP99Nfg4+b+/u9B/eDs1MD1mO7+4PHg2MXa347g7vDizMLN4eG+Pv7i5evs/v79yu7S3/DV7/498Yv24eH+4ufQ3Ozu/v7+y13sRqwAAADLSURBVHjaZc/XDsFgGIBhtDrshlitmk2IrbHFqL2pvXf/+78DPokj7+Fz9qpU/9UXJIlhmPaTaQ6QPaz0mm+5gwkgovcV6GZzd5JtCQwgsxoHOvJO15kleRLAnMgHFIESUEPmawB9ngmelTtipwwfASilxOLyiV5UVUyVAfbG0cCPHig+GBkzAENHS0AstVF6bacZIOzgLmxsHbt2OecNgJC83JERmePUYq8ARGkJx6XtFsdddBQgZE2nPR6CICZhawjA4Fb/chv+399kfR+MMMDGOQAAAABJRU5ErkJggg==");background-repeat: no-repeat;background-position: 2px center;}.ace_gutter-cell.ace_warning {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAAmVBMVEX///8AAAD///8AAAAAAABPSzb/5sAAAAB/blH/73z/ulkAAAAAAAD85pkAAAAAAAACAgP/vGz/rkDerGbGrV7/pkQICAf////e0IsAAAD/oED/qTvhrnUAAAD/yHD/njcAAADuv2r/nz//oTj/p064oGf/zHAAAAA9Nir/tFIAAAD/tlTiuWf/tkIAAACynXEAAAAAAAAtIRW7zBpBAAAAM3RSTlMAABR1m7RXO8Ln31Z36zT+neXe5OzooRDfn+TZ4p3h2hTf4t3k3ucyrN1K5+Xaks52Sfs9CXgrAAAAjklEQVR42o3PbQ+CIBQFYEwboPhSYgoYunIqqLn6/z8uYdH8Vmdnu9vz4WwXgN/xTPRD2+sgOcZjsge/whXZgUaYYvT8QnuJaUrjrHUQreGczuEafQCO/SJTufTbroWsPgsllVhq3wJEk2jUSzX3CUEDJC84707djRc5MTAQxoLgupWRwW6UB5fS++NV8AbOZgnsC7BpEAAAAABJRU5ErkJggg==");background-position: 2px center;}.ace_gutter-cell.ace_info {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAAAAAA6mKC9AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAAJ0Uk5TAAB2k804AAAAPklEQVQY02NgIB68QuO3tiLznjAwpKTgNyDbMegwisCHZUETUZV0ZqOquBpXj2rtnpSJT1AEnnRmL2OgGgAAIKkRQap2htgAAAAASUVORK5CYII=");background-position: 2px center;}.ace_dark .ace_gutter-cell.ace_info {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQBAMAAADt3eJSAAAAJFBMVEUAAAChoaGAgIAqKiq+vr6tra1ZWVmUlJSbm5s8PDxubm56enrdgzg3AAAAAXRSTlMAQObYZgAAAClJREFUeNpjYMAPdsMYHegyJZFQBlsUlMFVCWUYKkAZMxZAGdxlDMQBAG+TBP4B6RyJAAAAAElFTkSuQmCC");}.ace_scrollbar {contain: strict;position: absolute;right: 0;bottom: 0;z-index: 6;}.ace_scrollbar-inner {position: absolute;cursor: text;left: 0;top: 0;}.ace_scrollbar-v{overflow-x: hidden;overflow-y: scroll;top: 0;}.ace_scrollbar-h {overflow-x: scroll;overflow-y: hidden;left: 0;}.ace_print-margin {position: absolute;height: 100%;}.ace_text-input {position: absolute;z-index: 0;width: 0.5em;height: 1em;opacity: 0;background: transparent;-moz-appearance: none;appearance: none;border: none;resize: none;outline: none;overflow: hidden;font: inherit;padding: 0 1px;margin: 0 -1px;contain: strict;-ms-user-select: text;-moz-user-select: text;-webkit-user-select: text;user-select: text;white-space: pre!important;}.ace_text-input.ace_composition {background: transparent;color: inherit;z-index: 1000;opacity: 1;}.ace_composition_placeholder { color: transparent }.ace_composition_marker { border-bottom: 1px solid;position: absolute;border-radius: 0;margin-top: 1px;}[ace_nocontext=true] {transform: none!important;filter: none!important;clip-path: none!important;mask : none!important;contain: none!important;perspective: none!important;mix-blend-mode: initial!important;z-index: auto;}.ace_layer {z-index: 1;position: absolute;overflow: hidden;word-wrap: normal;white-space: pre;height: 100%;width: 100%;box-sizing: border-box;pointer-events: none;}.ace_gutter-layer {position: relative;width: auto;text-align: right;pointer-events: auto;height: 1000000px;contain: style size layout;}.ace_text-layer {font: inherit !important;position: absolute;height: 1000000px;width: 1000000px;contain: style size layout;}.ace_text-layer > .ace_line, .ace_text-layer > .ace_line_group {contain: style size layout;position: absolute;top: 0;left: 0;right: 0;}.ace_hidpi .ace_text-layer,.ace_hidpi .ace_gutter-layer,.ace_hidpi .ace_content,.ace_hidpi .ace_gutter {contain: strict;will-change: transform;}.ace_hidpi .ace_text-layer > .ace_line, .ace_hidpi .ace_text-layer > .ace_line_group {contain: strict;}.ace_cjk {display: inline-block;text-align: center;}.ace_cursor-layer {z-index: 4;}.ace_cursor {z-index: 4;position: absolute;box-sizing: border-box;border-left: 2px solid;transform: translatez(0);}.ace_multiselect .ace_cursor {border-left-width: 1px;}.ace_slim-cursors .ace_cursor {border-left-width: 1px;}.ace_overwrite-cursors .ace_cursor {border-left-width: 0;border-bottom: 1px solid;}.ace_hidden-cursors .ace_cursor {opacity: 0.2;}.ace_hasPlaceholder .ace_hidden-cursors .ace_cursor {opacity: 0;}.ace_smooth-blinking .ace_cursor {transition: opacity 0.18s;}.ace_animate-blinking .ace_cursor {animation-duration: 1000ms;animation-timing-function: step-end;animation-name: blink-ace-animate;animation-iteration-count: infinite;}.ace_animate-blinking.ace_smooth-blinking .ace_cursor {animation-duration: 1000ms;animation-timing-function: ease-in-out;animation-name: blink-ace-animate-smooth;}@keyframes blink-ace-animate {from, to { opacity: 1; }60% { opacity: 0; }}@keyframes blink-ace-animate-smooth {from, to { opacity: 1; }45% { opacity: 1; }60% { opacity: 0; }85% { opacity: 0; }}.ace_marker-layer .ace_step, .ace_marker-layer .ace_stack {position: absolute;z-index: 3;}.ace_marker-layer .ace_selection {position: absolute;z-index: 5;}.ace_marker-layer .ace_bracket {position: absolute;z-index: 6;}.ace_marker-layer .ace_error_bracket {position: absolute;border-bottom: 1px solid #DE5555;border-radius: 0;}.ace_marker-layer .ace_active-line {position: absolute;z-index: 2;}.ace_marker-layer .ace_selected-word {position: absolute;z-index: 4;box-sizing: border-box;}.ace_line .ace_fold {box-sizing: border-box;display: inline-block;height: 11px;margin-top: -2px;vertical-align: middle;background-image:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAAJCAYAAADU6McMAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAJpJREFUeNpi/P//PwOlgAXGYGRklAVSokD8GmjwY1wasKljQpYACtpCFeADcHVQfQyMQAwzwAZI3wJKvCLkfKBaMSClBlR7BOQikCFGQEErIH0VqkabiGCAqwUadAzZJRxQr/0gwiXIal8zQQPnNVTgJ1TdawL0T5gBIP1MUJNhBv2HKoQHHjqNrA4WO4zY0glyNKLT2KIfIMAAQsdgGiXvgnYAAAAASUVORK5CYII="),url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAA3CAYAAADNNiA5AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAACJJREFUeNpi+P//fxgTAwPDBxDxD078RSX+YeEyDFMCIMAAI3INmXiwf2YAAAAASUVORK5CYII=");background-repeat: no-repeat, repeat-x;background-position: center center, top left;color: transparent;border: 1px solid black;border-radius: 2px;cursor: pointer;pointer-events: auto;}.ace_dark .ace_fold {}.ace_fold:hover{background-image:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAAJCAYAAADU6McMAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAJpJREFUeNpi/P//PwOlgAXGYGRklAVSokD8GmjwY1wasKljQpYACtpCFeADcHVQfQyMQAwzwAZI3wJKvCLkfKBaMSClBlR7BOQikCFGQEErIH0VqkabiGCAqwUadAzZJRxQr/0gwiXIal8zQQPnNVTgJ1TdawL0T5gBIP1MUJNhBv2HKoQHHjqNrA4WO4zY0glyNKLT2KIfIMAAQsdgGiXvgnYAAAAASUVORK5CYII="),url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAA3CAYAAADNNiA5AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAACBJREFUeNpi+P//fz4TAwPDZxDxD5X4i5fLMEwJgAADAEPVDbjNw87ZAAAAAElFTkSuQmCC");}.ace_tooltip {background-color: #FFF;background-image: linear-gradient(to bottom, transparent, rgba(0, 0, 0, 0.1));border: 1px solid gray;border-radius: 1px;box-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);color: black;max-width: 100%;padding: 3px 4px;position: fixed;z-index: 999999;box-sizing: border-box;cursor: default;white-space: pre;word-wrap: break-word;line-height: normal;font-style: normal;font-weight: normal;letter-spacing: normal;pointer-events: none;}.ace_folding-enabled > .ace_gutter-cell {padding-right: 13px;}.ace_fold-widget {box-sizing: border-box;margin: 0 -12px 0 1px;display: none;width: 11px;vertical-align: top;background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAANElEQVR42mWKsQ0AMAzC8ixLlrzQjzmBiEjp0A6WwBCSPgKAXoLkqSot7nN3yMwR7pZ32NzpKkVoDBUxKAAAAABJRU5ErkJggg==");background-repeat: no-repeat;background-position: center;border-radius: 3px;border: 1px solid transparent;cursor: pointer;}.ace_folding-enabled .ace_fold-widget {display: inline-block;   }.ace_fold-widget.ace_end {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAANElEQVR42m3HwQkAMAhD0YzsRchFKI7sAikeWkrxwScEB0nh5e7KTPWimZki4tYfVbX+MNl4pyZXejUO1QAAAABJRU5ErkJggg==");}.ace_fold-widget.ace_closed {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAMAAAAGCAYAAAAG5SQMAAAAOUlEQVR42jXKwQkAMAgDwKwqKD4EwQ26sSOkVWjgIIHAzPiCgaqiqnJHZnKICBERHN194O5b9vbLuAVRL+l0YWnZAAAAAElFTkSuQmCCXA==");}.ace_fold-widget:hover {border: 1px solid rgba(0, 0, 0, 0.3);background-color: rgba(255, 255, 255, 0.2);box-shadow: 0 1px 1px rgba(255, 255, 255, 0.7);}.ace_fold-widget:active {border: 1px solid rgba(0, 0, 0, 0.4);background-color: rgba(0, 0, 0, 0.05);box-shadow: 0 1px 1px rgba(255, 255, 255, 0.8);}.ace_dark .ace_fold-widget {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHklEQVQIW2P4//8/AzoGEQ7oGCaLLAhWiSwB146BAQCSTPYocqT0AAAAAElFTkSuQmCC");}.ace_dark .ace_fold-widget.ace_end {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAH0lEQVQIW2P4//8/AxQ7wNjIAjDMgC4AxjCVKBirIAAF0kz2rlhxpAAAAABJRU5ErkJggg==");}.ace_dark .ace_fold-widget.ace_closed {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAMAAAAFCAYAAACAcVaiAAAAHElEQVQIW2P4//+/AxAzgDADlOOAznHAKgPWAwARji8UIDTfQQAAAABJRU5ErkJggg==");}.ace_dark .ace_fold-widget:hover {box-shadow: 0 1px 1px rgba(255, 255, 255, 0.2);background-color: rgba(255, 255, 255, 0.1);}.ace_dark .ace_fold-widget:active {box-shadow: 0 1px 1px rgba(255, 255, 255, 0.2);}.ace_inline_button {border: 1px solid lightgray;display: inline-block;margin: -1px 8px;padding: 0 5px;pointer-events: auto;cursor: pointer;}.ace_inline_button:hover {border-color: gray;background: rgba(200,200,200,0.2);display: inline-block;pointer-events: auto;}.ace_fold-widget.ace_invalid {background-color: #FFB4B4;border-color: #DE5555;}.ace_fade-fold-widgets .ace_fold-widget {transition: opacity 0.4s ease 0.05s;opacity: 0;}.ace_fade-fold-widgets:hover .ace_fold-widget {transition: opacity 0.05s ease 0.05s;opacity:1;}.ace_underline {text-decoration: underline;}.ace_bold {font-weight: bold;}.ace_nobold .ace_bold {font-weight: normal;}.ace_italic {font-style: italic;}.ace_error-marker {background-color: rgba(255, 0, 0,0.2);position: absolute;z-index: 9;}.ace_highlight-marker {background-color: rgba(255, 255, 0,0.2);position: absolute;z-index: 8;}.ace_mobile-menu {position: absolute;line-height: 1.5;border-radius: 4px;-ms-user-select: none;-moz-user-select: none;-webkit-user-select: none;user-select: none;background: white;box-shadow: 1px 3px 2px grey;border: 1px solid #dcdcdc;color: black;}.ace_dark > .ace_mobile-menu {background: #333;color: #ccc;box-shadow: 1px 3px 2px grey;border: 1px solid #444;}.ace_mobile-button {padding: 2px;cursor: pointer;overflow: hidden;}.ace_mobile-button:hover {background-color: #eee;opacity:1;}.ace_mobile-button:active {background-color: #ddd;}.ace_placeholder {font-family: arial;transform: scale(0.9);transform-origin: left;white-space: pre;opacity: 0.7;margin: 0 10px;}
            /*# sourceURL=ace/css/ace_editor.css */
        </style>
        <meta http-equiv="content-language" content="en">
        <meta http-equiv="content-script-type" content="text/javascript">
        <meta http-equiv="content-style-type" content="text/css">
        <meta name="description" content="This is the online markdown editor with live preview.">
        <link rel="stylesheet" type="text/css" href="/static/copy/markdown-live-preview/style.css">
        <link rel="stylesheet" type="text/css" href="/static/copy/markdown-live-preview/github-markdown.css">
        <link rel="icon" type="image/png" href="https://markdownlivepreview.com/favicon.png">
        <script type="text/javascript" async="" src="/static/copy/markdown-live-preview/ga.js"></script><script type="text/javascript" src="/static/copy/markdown-live-preview/jquery-1.6.1.min.js"></script>
        <script type="text/javascript" src="/static/copy/markdown-live-preview/jquery.autosize-min.js"></script>
        <script type="text/javascript" src="/static/copy/markdown-live-preview/marked.min.js"></script>
        <script type="text/javascript" src="/static/copy/markdown-live-preview/purify.min.js"></script>
        <script type="text/javascript" src="/static/copy/markdown-live-preview/ace.js"></script>
        <script type="text/javascript" src="/static/copy/markdown-live-preview/main.js"></script>
        <title>Markdown Live Preview</title>
        <script src="/static/copy/markdown-live-preview/theme-github.js"></script>
    </head>
    <body>
        <div id="header">
            <h1><a href="https://markdownlivepreview.com/">Markdown Live Preview</a></h1>
        </div>
        <div id="container" style="top: 47px;">
            <div id="edit" class="column" style="height: 519px;">
                <div id="editor-wrapper">
                    <div id="editor" class=" ace_editor ace-github" style="height: 1193px; font-size: 14px;">
                        <div style="position: absolute;"></div>
                        <textarea class="ace_text-input" wrap="off" autocorrect="off" autocapitalize="off" spellcheck="false" style="opacity: 0; font-size: 1px; height: 1px; width: 1px; top: 27px; left: 52px;"></textarea>
                        <div class="ace_gutter" aria-hidden="true" style="left: 0px; width: 49px;">
                            <div class="ace_layer ace_gutter-layer ace_folding-enabled" style="height: 1e+06px; top: 10px; left: 0px; width: 49px;">
                                <div class="ace_gutter-cell ace_gutter-active-line " style="height: 17px; top: 0px;">1<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 17px; top: 17px;">2<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 17px; top: 34px;">3<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 17px; top: 51px;">4<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 17px; top: 68px;">5<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 17px; top: 85px;">6<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 17px; top: 102px;">7<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 17px; top: 119px;">8<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 17px; top: 136px;">9<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 17px; top: 153px;">10<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 17px; top: 170px;">11<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 17px; top: 187px;">12<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 17px; top: 204px;">13<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 17px; top: 221px;">14<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 17px; top: 238px;">15<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 17px; top: 255px;">16<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 17px; top: 272px;">17<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 17px; top: 289px;">18<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 17px; top: 306px;">19<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 17px; top: 323px;">20<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 17px; top: 340px;">21<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 17px; top: 357px;">22<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 17px; top: 374px;">23<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 17px; top: 391px;">24<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 17px; top: 408px;">25<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 17px; top: 425px;">26<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 17px; top: 442px;">27<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 17px; top: 459px;">28<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 17px; top: 476px;">29<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 17px; top: 493px;">30<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 17px; top: 510px;">31<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 17px; top: 527px;">32<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 17px; top: 544px;">33<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 17px; top: 561px;">34<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 17px; top: 578px;">35<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 17px; top: 595px;">36<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 17px; top: 612px;">37<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 17px; top: 629px;">38<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 17px; top: 646px;">39<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 17px; top: 663px;">40<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 17px; top: 680px;">41<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 17px; top: 697px;">42<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 17px; top: 714px;">43<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 17px; top: 731px;">44<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 17px; top: 748px;">45<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 34px; top: 765px;">46<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 17px; top: 799px;">47<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 34px; top: 816px;">48<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 17px; top: 850px;">49<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 17px; top: 867px;">50<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 17px; top: 884px;">51<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 17px; top: 901px;">52<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 17px; top: 918px;">53<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 17px; top: 935px;">54<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 17px; top: 952px;">55<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 17px; top: 969px;">56<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 17px; top: 986px;">57<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 17px; top: 1003px;">58<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 17px; top: 1020px;">59<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 17px; top: 1037px;">60<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 17px; top: 1054px;">61<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 17px; top: 1071px;">62<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 17px; top: 1088px;">63<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 17px; top: 1105px;">64<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 17px; top: 1122px;">65<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 17px; top: 1139px;">66<span style="display: none;"></span></div>
                                <div class="ace_gutter-cell " style="height: 17px; top: 1156px;">67<span style="display: none;"></span></div>
                            </div>
                        </div>
                        <div class="ace_scroller" style="line-height: 17px; left: 49px; right: 0px; bottom: 0px;">
                            <div class="ace_content" style="top: 10px; left: 0px; width: 607px; height: 1227px;">
                                <div class="ace_layer ace_print-margin-layer">
                                    <div class="ace_print-margin" style="left: 620px; visibility: visible;"></div>
                                </div>
                                <div class="ace_layer ace_marker-layer">
                                    <div class="ace_active-line" style="height: 17px; top: 0px; left: 0px; right: 0px;"></div>
                                </div>
                                <div class="ace_layer ace_text-layer" style="height: 1e+06px; margin: 0px 4px; top: 0px; left: 0px;">
                                    <div class="ace_line_group" style="height: 17px; top: 0px;">
                                        <div class="ace_line" style="height: 17px;"># Markdown syntax guide</div>
                                    </div>
                                    <div class="ace_line_group" style="height: 17px; top: 17px;">
                                        <div class="ace_line" style="height: 17px;"></div>
                                    </div>
                                    <div class="ace_line_group" style="height: 17px; top: 34px;">
                                        <div class="ace_line" style="height: 17px;">## Headers</div>
                                    </div>
                                    <div class="ace_line_group" style="height: 17px; top: 51px;">
                                        <div class="ace_line" style="height: 17px;"></div>
                                    </div>
                                    <div class="ace_line_group" style="height: 17px; top: 68px;">
                                        <div class="ace_line" style="height: 17px;"># This is a Heading h1</div>
                                    </div>
                                    <div class="ace_line_group" style="height: 17px; top: 85px;">
                                        <div class="ace_line" style="height: 17px;">## This is a Heading h2 </div>
                                    </div>
                                    <div class="ace_line_group" style="height: 17px; top: 102px;">
                                        <div class="ace_line" style="height: 17px;">###### This is a Heading h6</div>
                                    </div>
                                    <div class="ace_line_group" style="height: 17px; top: 119px;">
                                        <div class="ace_line" style="height: 17px;"></div>
                                    </div>
                                    <div class="ace_line_group" style="height: 17px; top: 136px;">
                                        <div class="ace_line" style="height: 17px;">## Emphasis</div>
                                    </div>
                                    <div class="ace_line_group" style="height: 17px; top: 153px;">
                                        <div class="ace_line" style="height: 17px;"></div>
                                    </div>
                                    <div class="ace_line_group" style="height: 17px; top: 170px;">
                                        <div class="ace_line" style="height: 17px;">*This text will be italic*  </div>
                                    </div>
                                    <div class="ace_line_group" style="height: 17px; top: 187px;">
                                        <div class="ace_line" style="height: 17px;">_This will also be italic_</div>
                                    </div>
                                    <div class="ace_line_group" style="height: 17px; top: 204px;">
                                        <div class="ace_line" style="height: 17px;"></div>
                                    </div>
                                    <div class="ace_line_group" style="height: 17px; top: 221px;">
                                        <div class="ace_line" style="height: 17px;">**This text will be bold**  </div>
                                    </div>
                                    <div class="ace_line_group" style="height: 17px; top: 238px;">
                                        <div class="ace_line" style="height: 17px;">__This will also be bold__</div>
                                    </div>
                                    <div class="ace_line_group" style="height: 17px; top: 255px;">
                                        <div class="ace_line" style="height: 17px;"></div>
                                    </div>
                                    <div class="ace_line_group" style="height: 17px; top: 272px;">
                                        <div class="ace_line" style="height: 17px;">_You **can** combine them_</div>
                                    </div>
                                    <div class="ace_line_group" style="height: 17px; top: 289px;">
                                        <div class="ace_line" style="height: 17px;"></div>
                                    </div>
                                    <div class="ace_line_group" style="height: 17px; top: 306px;">
                                        <div class="ace_line" style="height: 17px;">## Lists</div>
                                    </div>
                                    <div class="ace_line_group" style="height: 17px; top: 323px;">
                                        <div class="ace_line" style="height: 17px;"></div>
                                    </div>
                                    <div class="ace_line_group" style="height: 17px; top: 340px;">
                                        <div class="ace_line" style="height: 17px;">### Unordered</div>
                                    </div>
                                    <div class="ace_line_group" style="height: 17px; top: 357px;">
                                        <div class="ace_line" style="height: 17px;"></div>
                                    </div>
                                    <div class="ace_line_group" style="height: 17px; top: 374px;">
                                        <div class="ace_line" style="height: 17px;">* Item 1</div>
                                    </div>
                                    <div class="ace_line_group" style="height: 17px; top: 391px;">
                                        <div class="ace_line" style="height: 17px;">* Item 2</div>
                                    </div>
                                    <div class="ace_line_group" style="height: 17px; top: 408px;">
                                        <div class="ace_line" style="height: 17px;">* Item 2a</div>
                                    </div>
                                    <div class="ace_line_group" style="height: 17px; top: 425px;">
                                        <div class="ace_line" style="height: 17px;">* Item 2b</div>
                                    </div>
                                    <div class="ace_line_group" style="height: 17px; top: 442px;">
                                        <div class="ace_line" style="height: 17px;"></div>
                                    </div>
                                    <div class="ace_line_group" style="height: 17px; top: 459px;">
                                        <div class="ace_line" style="height: 17px;">### Ordered</div>
                                    </div>
                                    <div class="ace_line_group" style="height: 17px; top: 476px;">
                                        <div class="ace_line" style="height: 17px;"></div>
                                    </div>
                                    <div class="ace_line_group" style="height: 17px; top: 493px;">
                                        <div class="ace_line" style="height: 17px;">1. Item 1</div>
                                    </div>
                                    <div class="ace_line_group" style="height: 17px; top: 510px;">
                                        <div class="ace_line" style="height: 17px;">1. Item 2</div>
                                    </div>
                                    <div class="ace_line_group" style="height: 17px; top: 527px;">
                                        <div class="ace_line" style="height: 17px;">1. Item 3</div>
                                    </div>
                                    <div class="ace_line_group" style="height: 17px; top: 544px;">
                                        <div class="ace_line" style="height: 17px;">  1. Item 3a</div>
                                    </div>
                                    <div class="ace_line_group" style="height: 17px; top: 561px;">
                                        <div class="ace_line" style="height: 17px;">  1. Item 3b</div>
                                    </div>
                                    <div class="ace_line_group" style="height: 17px; top: 578px;">
                                        <div class="ace_line" style="height: 17px;"></div>
                                    </div>
                                    <div class="ace_line_group" style="height: 17px; top: 595px;">
                                        <div class="ace_line" style="height: 17px;">## Images</div>
                                    </div>
                                    <div class="ace_line_group" style="height: 17px; top: 612px;">
                                        <div class="ace_line" style="height: 17px;"></div>
                                    </div>
                                    <div class="ace_line_group" style="height: 17px; top: 629px;">
                                        <div class="ace_line" style="height: 17px;">![This is a alt text.](/image/sample.png "This is a sample image.")</div>
                                    </div>
                                    <div class="ace_line_group" style="height: 17px; top: 646px;">
                                        <div class="ace_line" style="height: 17px;"></div>
                                    </div>
                                    <div class="ace_line_group" style="height: 17px; top: 663px;">
                                        <div class="ace_line" style="height: 17px;">## Links</div>
                                    </div>
                                    <div class="ace_line_group" style="height: 17px; top: 680px;">
                                        <div class="ace_line" style="height: 17px;"></div>
                                    </div>
                                    <div class="ace_line_group" style="height: 17px; top: 697px;">
                                        <div class="ace_line" style="height: 17px;">You may be using [Markdown Live Preview](https://markdownlivepreview.com/).</div>
                                    </div>
                                    <div class="ace_line_group" style="height: 17px; top: 714px;">
                                        <div class="ace_line" style="height: 17px;"></div>
                                    </div>
                                    <div class="ace_line_group" style="height: 17px; top: 731px;">
                                        <div class="ace_line" style="height: 17px;">## Blockquotes</div>
                                    </div>
                                    <div class="ace_line_group" style="height: 17px; top: 748px;">
                                        <div class="ace_line" style="height: 17px;"></div>
                                    </div>
                                    <div class="ace_line_group" style="height: 34px; top: 765px;">
                                        <div class="ace_line" style="height: 17px;">&gt; Markdown is a lightweight markup language with plain-text-formatting syntax</div>
                                        <div class="ace_line" style="height: 17px;">, created in 2004 by John Gruber with Aaron Swartz.</div>
                                    </div>
                                    <div class="ace_line_group" style="height: 17px; top: 799px;">
                                        <div class="ace_line" style="height: 17px;">&gt;</div>
                                    </div>
                                    <div class="ace_line_group" style="height: 34px; top: 816px;">
                                        <div class="ace_line" style="height: 17px;">&gt;&gt; Markdown is often used to format readme files, for writing messages in </div>
                                        <div class="ace_line" style="height: 17px;">online discussion forums, and to create rich text using a plain text editor.</div>
                                    </div>
                                    <div class="ace_line_group" style="height: 17px; top: 850px;">
                                        <div class="ace_line" style="height: 17px;"></div>
                                    </div>
                                    <div class="ace_line_group" style="height: 17px; top: 867px;">
                                        <div class="ace_line" style="height: 17px;">## Tables</div>
                                    </div>
                                    <div class="ace_line_group" style="height: 17px; top: 884px;">
                                        <div class="ace_line" style="height: 17px;"></div>
                                    </div>
                                    <div class="ace_line_group" style="height: 17px; top: 901px;">
                                        <div class="ace_line" style="height: 17px;">| Left columns  | Right columns |</div>
                                    </div>
                                    <div class="ace_line_group" style="height: 17px; top: 918px;">
                                        <div class="ace_line" style="height: 17px;">| ------------- |:-------------:|</div>
                                    </div>
                                    <div class="ace_line_group" style="height: 17px; top: 935px;">
                                        <div class="ace_line" style="height: 17px;">| left foo      | right foo     |</div>
                                    </div>
                                    <div class="ace_line_group" style="height: 17px; top: 952px;">
                                        <div class="ace_line" style="height: 17px;">| left bar      | right bar     |</div>
                                    </div>
                                    <div class="ace_line_group" style="height: 17px; top: 969px;">
                                        <div class="ace_line" style="height: 17px;">| left baz      | right baz     |</div>
                                    </div>
                                    <div class="ace_line_group" style="height: 17px; top: 986px;">
                                        <div class="ace_line" style="height: 17px;"></div>
                                    </div>
                                    <div class="ace_line_group" style="height: 17px; top: 1003px;">
                                        <div class="ace_line" style="height: 17px;">## Blocks of code</div>
                                    </div>
                                    <div class="ace_line_group" style="height: 17px; top: 1020px;">
                                        <div class="ace_line" style="height: 17px;"></div>
                                    </div>
                                    <div class="ace_line_group" style="height: 17px; top: 1037px;">
                                        <div class="ace_line" style="height: 17px;">```</div>
                                    </div>
                                    <div class="ace_line_group" style="height: 17px; top: 1054px;">
                                        <div class="ace_line" style="height: 17px;">let message = 'Hello world';</div>
                                    </div>
                                    <div class="ace_line_group" style="height: 17px; top: 1071px;">
                                        <div class="ace_line" style="height: 17px;">alert(message);</div>
                                    </div>
                                    <div class="ace_line_group" style="height: 17px; top: 1088px;">
                                        <div class="ace_line" style="height: 17px;">```</div>
                                    </div>
                                    <div class="ace_line_group" style="height: 17px; top: 1105px;">
                                        <div class="ace_line" style="height: 17px;"></div>
                                    </div>
                                    <div class="ace_line_group" style="height: 17px; top: 1122px;">
                                        <div class="ace_line" style="height: 17px;">## Inline code</div>
                                    </div>
                                    <div class="ace_line_group" style="height: 17px; top: 1139px;">
                                        <div class="ace_line" style="height: 17px;"></div>
                                    </div>
                                    <div class="ace_line_group" style="height: 17px; top: 1156px;">
                                        <div class="ace_line" style="height: 17px;">This web site is using `markedjs/marked`.</div>
                                    </div>
                                </div>
                                <div class="ace_layer ace_marker-layer"></div>
                                <div class="ace_layer ace_cursor-layer ace_hidden-cursors">
                                    <div class="ace_cursor" style="display: block; top: 0px; left: 4px; width: 8px; height: 17px;"></div>
                                </div>
                            </div>
                        </div>
                        <div class="ace_scrollbar ace_scrollbar-v" style="display: none; width: 22px; bottom: 0px;">
                            <div class="ace_scrollbar-inner" style="width: 22px; height: 1193px;">&nbsp;</div>
                        </div>
                        <div class="ace_scrollbar ace_scrollbar-h" style="display: none; height: 22px; left: 49px; right: 0px;">
                            <div class="ace_scrollbar-inner" style="height: 22px; width: 627px;">&nbsp;</div>
                        </div>
                        <div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: hidden;">
                            <div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: visible;">הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה</div>
                            <div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font-style: inherit; font-variant: inherit; font-stretch: inherit; font-size: inherit; line-height: inherit; font-family: inherit; overflow: visible;">XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX</div>
                        </div>
                    </div>
                </div>
            </div>
            <!-- Do not insert new line here -->
            <div id="preview" class="column" style="height: 519px;">
                <div id="preview-wrapper">
                    <div id="output" class="content markdown-body">
                        <h1 id="markdown-syntax-guide">Markdown syntax guide</h1>
                        <h2 id="headers">Headers</h2>
                        <h1 id="this-is-a-heading-h1">This is a Heading h1</h1>
                        <h2 id="this-is-a-heading-h2">This is a Heading h2</h2>
                        <h6 id="this-is-a-heading-h6">This is a Heading h6</h6>
                        <h2 id="emphasis">Emphasis</h2>
                        <p><em>This text will be italic</em><br><em>This will also be italic</em></p>
                        <p><strong>This text will be bold</strong><br><strong>This will also be bold</strong></p>
                        <p><em>You <strong>can</strong> combine them</em></p>
                        <h2 id="lists">Lists</h2>
                        <h3 id="unordered">Unordered</h3>
                        <ul>
                            <li>Item 1</li>
                            <li>Item 2</li>
                            <li>Item 2a</li>
                            <li>Item 2b</li>
                        </ul>
                        <h3 id="ordered">Ordered</h3>
                        <ol>
                            <li>Item 1</li>
                            <li>Item 2</li>
                            <li>
                                Item 3
                                <ol>
                                    <li>Item 3a</li>
                                    <li>Item 3b</li>
                                </ol>
                            </li>
                        </ol>
                        <h2>Images</h2>
                        <p><img title="This is a sample image." alt="This is a alt text." src="/static/copy/markdown-live-preview/sample.png"></p>
                        <h2>Links</h2>
                        <p>You may be using <a href="https://markdownlivepreview.com/">Markdown Live Preview</a>.</p>
                        <h2 id="blockquotes">Blockquotes</h2>
                        <blockquote>
                            <p>Markdown is a lightweight markup language with plain-text-formatting syntax, created in 2004 by John Gruber with Aaron Swartz.</p>
                            <blockquote>
                                <p>Markdown is often used to format readme files, for writing messages in online discussion forums, and to create rich text using a plain text editor.</p>
                            </blockquote>
                        </blockquote>
                        <h2 id="tables">Tables</h2>
                        <table>
                            <thead>
                                <tr>
                                    <th>Left columns</th>
                                    <th align="center">Right columns</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>left foo</td>
                                    <td align="center">right foo</td>
                                </tr>
                                <tr>
                                    <td>left bar</td>
                                    <td align="center">right bar</td>
                                </tr>
                                <tr>
                                    <td>left baz</td>
                                    <td align="center">right baz</td>
                                </tr>
                            </tbody>
                        </table>
                        <h2 id="blocks-of-code">Blocks of code</h2>
                        <pre><code>let message = 'Hello world';
alert(message);</code></pre>
                        <h2 id="inline-code">Inline code</h2>
                        <p>This web site is using <code>markedjs/marked</code>.</p>
                    </div>
                </div>
            </div>
        </div>
        <div id="footer">
            <div id="copyright"><a href="https://github.com/tanabe/markdown-live-preview"><img src="/static/copy/markdown-live-preview/GitHub-Mark-Light-32px.png"></a></div>
        </div>
        <script type="text/javascript">
            var _gaq = _gaq || [];
            _gaq.push(['_setAccount', 'UA-73660-14']);
            _gaq.push(['_trackPageview']);
            
            (function() {
              var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
              ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
              var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
            })();
        </script>
    </body>
</html>