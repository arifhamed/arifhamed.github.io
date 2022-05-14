---
title: Mediafire Direct Downloader
permalink: /tools/mediafire-direct-dl
layout: default
redirect_from:
 - /tools/mediafire-direct-dl/
 - /tools/mediafire-direct
 - /tools/mediafire-direct/
 - /tools/mediafire
 - /tools/mediafire/
 - /mediafire-direct-dl
 - /mediafire-direct-dl/
 - /mediafire-direct
 - /mediafire-direct/
 - /mediafire
 - /mediafire/
---


<!-- <link rel="stylesheet" href="/static/css/mediafire1.css"> -->
<script src="/static/js/mediafire.js"></script>
<!-- <link rel="stylesheet" href="/static/css/mediafire2.css"> -->


<input type="text" id="mediafire-url" autocomplete="off" spellcheck="false" placeholder="https://www.mediafire.com/file/abcde1234567890/file" aria-live="polite">
        
<p id="new-url" style="display:none;">You can use the link below on other websites for a direct download:<br>
<span id="mediafire-new-url"></span>
</p>

<p id="mediafire-dl-p"><a href="#" onclick="attemptDownloadRedirect();" id="mediafire-dl-btn" class="button green disable">Direct Download</a></p>

<div id="invalid-url" style="display:none;"><span style="color: red">Invalid URL or identifier, please make sure your Mediafire URL or identifier is in one of the following formats:</span><br>
    <ul style="color: lightslategray">
    <li>
        <span class="required">[download-identifier]</span>
    </li>
    <li>
        <span style="border-radius: 2px; border: 2px solid yellow; padding: 0.25em; margin: 0 0.125em;">http(s)://</span><span style="border-radius: 2px; border: 2px solid yellow; padding: 0.25em; margin: 0 0.125em;">www.</span><span class="required">mediafire.com/?[download-identifier]</span>
    </li>
    <li>
        <span style="border-radius: 2px; border: 2px solid yellow; padding: 0.25em; margin: 0 0.125em;">http(s)://</span><span style="border-radius: 2px; border: 2px solid yellow; padding: 0.25em; margin: 0 0.125em;">www.</span><span class="required">mediafire.com/view/[download-identifier]</span><span style="border-radius: 2px; border: 2px solid yellow; padding: 0.25em; margin: 0 0.125em;">/[file-name.extension]</span><span style="border-radius: 2px; border: 2px solid yellow; padding: 0.25em; margin: 0 0.125em;">/file</span>
    </li>
    <li>
        <span style="border-radius: 2px; border: 2px solid yellow; padding: 0.25em; margin: 0 0.125em;">http(s)://</span><span style="border-radius: 2px; border: 2px solid yellow; padding: 0.25em; margin: 0 0.125em;">www.</span><span class="required">mediafire.com/file/[download-identifier]</span><span style="border-radius: 2px; border: 2px solid yellow; padding: 0.25em; margin: 0 0.125em;">/[file-name.extension]</span><span style="border-radius: 2px; border: 2px solid yellow; padding: 0.25em; margin: 0 0.125em;">/file</span>
    </li>
    <li>
        <span style="border-radius: 2px; border: 2px solid yellow; padding: 0.25em; margin: 0 0.125em;">http(s)://</span><span style="border-radius: 2px; border: 2px solid yellow; padding: 0.25em; margin: 0 0.125em;">www.</span><span class="required">mediafire.com/download/[download-identifier]</span><span style="border-radius: 2px; border: 2px solid yellow; padding: 0.25em; margin: 0 0.125em;">/[file-name.extension]</span><span style="border-radius: 2px; border: 2px solid yellow; padding: 0.25em; margin: 0 0.125em;">/file</span>
    </li>
    </ul>
<span style="text-decoration: underline">Key:</span><br>
<span class="optional-key">&nbsp;&nbsp;</span> = Optional<br>
<span class="required-key">&nbsp;&nbsp;</span> = Required<br>
<br>
<span style="color: dimgray;">* Note: Folder downloads are not supported.</span>
</div>

<p id="invalid-page" style="display:none;"><span style="color: red">Invalid page, please make sure the Mediafire download is real and hasn't been taken down.</span></p>
</div>
</section>

