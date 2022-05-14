---
title: Mediafire Direct Downloader
permalink: /tools/mediafire-direct-dl
layout: default
redirect_from:
 - /tools/mediafire-direct-dl/
 - /tools/mediafire
 - /tools/mediafire/
 - /mediafire
 - /mediafire/
---


<script src="/static/js/mediafire.js"></script>
<link rel="stylesheet" href="/static/css/mediafire.css">


<input type="text" id="mediafire-url" autocomplete="off" spellcheck="false" placeholder="https://www.mediafire.com/file/abcde1234567890/file" aria-live="polite">
        
<p id="new-url" class="hide">You can use the link below on other websites for a direct download:<br>
    <span id="mediafire-new-url"></span>
</p>

<p id="mediafire-dl-p"><a href="#" onclick="attemptDownloadRedirect();" id="mediafire-dl-btn" class="button green disable">Direct Download</a></p>

<div id="invalid-url" class="hide"><span style="color: red">Invalid URL or identifier, please make sure your Mediafire URL or identifier is in one of the following formats:</span><br>
    <ul style="color: lightslategray">
    <li>
        <span class="required">[download-identifier]</span>
    </li>
    <li>
        <span class="optional">http(s)://</span><span class="optional">www.</span><span class="required">mediafire.com/?[download-identifier]</span>
    </li>
    <li>
        <span class="optional">http(s)://</span><span class="optional">www.</span><span class="required">mediafire.com/view/[download-identifier]</span><span class="optional">/[file-name.extension]</span><span class="optional">/file</span>
    </li>
    <li>
        <span class="optional">http(s)://</span><span class="optional">www.</span><span class="required">mediafire.com/file/[download-identifier]</span><span class="optional">/[file-name.extension]</span><span class="optional">/file</span>
    </li>
    <li>
        <span class="optional">http(s)://</span><span class="optional">www.</span><span class="required">mediafire.com/download/[download-identifier]</span><span class="optional">/[file-name.extension]</span><span class="optional">/file</span>
    </li>
    </ul>
<span style="text-decoration: underline">Key:</span><br>
<span class="optional-key">&nbsp;&nbsp;</span> = Optional<br>
<span class="required-key">&nbsp;&nbsp;</span> = Required<br>
<br>
<span class="subtle">* Note: Folder downloads are not supported.</span>
</div>

<p id="invalid-page" class="hide"><span style="color: red">Invalid page, please make sure the Mediafire download is real and hasn't been taken down.</span></p>
</div>
</section>

