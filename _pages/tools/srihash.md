---
title: SRIHash
permalink: /tools/srihash
layout: default
redirect_from:
 - /tools/srihash/
 - /srihash
 - /srihash/
---
<script src="/static/js/clipboard.js" defer=""></script>
<script src="/static/js/srihash.js" defer=""></script>
<pre id="for-copy" style="display:none;"></pre>
<div id="app" class="container">
    <div class="container" id="sriAppContainer">
        <div id="sri-app">
            <h1>SRI Hash Generator</h1>
            <label for="url">Enter the URL of the resource you wish to use:</label>
            <form id="sri-form" action="#">
                <input id="url" name="url" type="url" value="" placeholder="Resource URL" required="" autofocus="" spellcheck="false">
                <select id="sriHash" type="select">
                <option value="sha256">SHA-256</option>
                <option value="sha384" selected="">SHA-384</option>
                <option value="sha512">SHA-512</option>
                </select>
                <input id="sriSubmit" type="submit" value="Hash!">
            </form>
            <pre id="sri-snippet" name="sriSnippet"></pre>
            <div id="sri-error"></div>
        </div>
    </div>
</div>