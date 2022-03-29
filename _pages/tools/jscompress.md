---
title: jscompress
permalink: /tools/jscompress
layout: default
redirect_from:
 - /tools/jscompress/
 - /jscompress
 - /jscompress/
---

<main>
    <label class="use-ecmascript-next-label">
            <input type="checkbox" class="use-ecmascript-next"> ECMAScript <script type="text/javascript">document.write(new Date().getFullYear());</script>2022 (via babel-minify)
        </label>
    <ul class="tab-nav">
        <li data-tab="copyPaste" class="tab-nav-item active">Copy &amp; Paste JavaScript Code</li>
        <li data-tab="upload" class="tab-nav-item">Upload Javascript Files</li>
        <li data-tab="output" class="tab-nav-item">Output</li>
    </ul>
    <div class="tabs">
        <div class="tab-pane" id="copyPaste">
            <output class="error"></output>
            <form name="copyPasteForm">
                <textarea name="code" placeholder="Code to compress..."></textarea>
                <button class="button" type="submit">Compress JavaScript</button>
            </form>
        </div>
        <div class="tab-pane hide" id="upload">
            <output class="error"></output>
            <div class="file-wrapper">
                <input type="file" multiple="" id="file-input" class="file-input">
                <div class="file-list">
                    <label for="file-input" class="file-label">Choose files</label> or drag them here.
                    <div class="buttons">
                        <button class="button compress" disabled="">Compress</button>
                        <button class="button clear" disabled="">Remove all</button>
                    </div>
                    <div class="no-files"></div>
                </div>
            </div>
        </div>
        <div class="tab-pane hide" id="output">
            <textarea class="output-code" readonly=""></textarea>
            <a class="button download" href="blob:https://jscompress.com/5cd78d48-cdac-4300-a0e2-bc64dcf59760" download="compressed.js">Download</a> Stats: <output class="compression">0</output>% compression, saving <output class="saving">0</output> kb
        </div>
    </div>
</main>
<script src="/static/js/jscompress.js"></script>