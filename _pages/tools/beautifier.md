---
title: beautifier
permalink: /tools/beautifier
layout: default
redirect_from:
 - /tools/beautifier/
 - /beautifier
 - /beautifier/
published: false
---

<div>
    <div style="text-align: center;">
    <button class="submit"><strong>Beautify Code</strong> <em>(ctrl-enter)</em></button>
    <input type="file" onchange="changeToFileContent(this)">
    <button class="control" type="button" onclick="copyText()"><strong>Copy to Clipboard</strong></button>
    <button class="control" type="button" onclick="selectAll()"><strong>Select All</strong></button>
    <button class="control" type="button" onclick="clearAll()"><strong>Clear</strong></button>
    </div>
    <textarea id="source" rows="30" cols="160" style="display: none;"></textarea><div class="CodeMirror cm-s-default"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 5px; left: 35px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;" tabindex="0"></textarea></div><div class="CodeMirror-vscrollbar" tabindex="-1" cm-not-content="true"><div style="min-width: 1px; height: 0px;"></div></div><div class="CodeMirror-hscrollbar" tabindex="-1" cm-not-content="true"><div style="height: 100%; min-height: 1px; width: 0px;"></div></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 30px; margin-bottom: -17px; border-right-width: 13px; min-height: 50px; min-width: 521.625px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div role="presentation" style="position: relative; outline: none;"><div class="CodeMirror-measure"><pre class="CodeMirror-line-like"><span>xxxxxxxxxx</span></pre></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-cursors" style=""><div class="CodeMirror-cursor" style="left: 4px; top: 0px; height: 14px;">&nbsp;</div></div><div class="CodeMirror-code" role="presentation"><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">1</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-comment">// This is just a sample script. Paste your real code (javascript or HTML) here.</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">2</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -30px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 21px;">3</div></div><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-keyword">if</span> (<span class="cm-string">'this_is'</span><span class="cm-operator">==</span><span class="cm-string-2">/an_example/</span>){<span class="cm-variable">of_beautifier</span>();}<span class="cm-keyword">else</span>{<span class="cm-keyword">var</span> <span class="cm-def">a</span><span class="cm-operator">=</span><span class="cm-variable">b</span><span class="cm-operator">?</span>(<span class="cm-variable">c</span><span class="cm-operator">%</span><span class="cm-variable">d</span>):<span class="cm-variable">e</span>[<span class="cm-variable">f</span>];}</span></pre></div></div></div></div></div></div><div style="position: absolute; height: 13px; width: 1px; border-bottom: 0px solid transparent; top: 50px;"></div><div class="CodeMirror-gutters" style="height: 63px;"><div class="CodeMirror-gutter CodeMirror-linenumbers" style="width: 29px;"></div></div></div></div>
    <div style="text-align: center;">
    <button class="submit"><strong>Beautify Code</strong> <em>(ctrl-enter)</em></button>
    <input type="file" onchange="changeToFileContent(this)">
    <button class="control" type="button" onclick="copyText()"><strong>Copy to Clipboard</strong></button>
    <button class="control" type="button" onclick="selectAll()"><strong>Select All</strong></button>
    <button class="control" type="button" onclick="clearAll()"><strong>Clear</strong></button>
    </div>
</div>
<p style="margin:6px 0 0 0">Your Selected Options (JSON):</p>
<div>
    <textarea readonly="" id="options-selected" rows="10" cols="40"></textarea>
</div>
<p id="open-issue" hidden="">Not pretty enough for you?
    <button type="button" onclick="submitIssue()" name="issue-button">Report a problem with this input</button>
</p>
<div id="testresults"></div>
