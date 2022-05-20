---
title: "APK"
permalink: /resources/apk
redirect_from: 
- /apk/
- /apks
- /apks/
- /APK
- /APK/
- /APKs
- /APKs/
- /APKS
- /APKS/
- /resources/apk/
- /resources/apks
- /resources/apks/
- /resources/APK
- /resources/APK/
- /resources/APKs
- /resources/APKs/
- /resources/APKS
- /resources/APKS/
layout: default
# secret: "https://arifhamed.com/resources/apk?key=在他里面，我们借着耶稣的宝血得着救赎，我们的过犯得着赦免，是照着他丰富的恩典"
secret: javascript:togglePiracy();
---

<script>
    var paidlist=document.getElementsByClassName('paid');
    var freelist=document.getElementsByClassName('free');
    var paidflag=false;
    function togglePiracy(){
        for(let a of paidlist){
            //a.setAttribute('style','display:inline;')
            if (a.style.display == "none"){
                a.style.display = "inline";
                paidflag = true;
            } else {
                a.style.display = "none";
                paidflag = false;
            }
        };
    };
    function apkSearch(){
        const q = document.getElementById("apkSearchId");
        if (paidflag){
            console.log(q)
        }
    }
    async function getApkJson(n) {
        if (paidflag){
            const response = await fetch("https://arifhamed.com/_pages/resources/apk_search_full.json");
        } else {
            const response = await fetch("https://arifhamed.com/_pages/resources/apk_search.json");
        };
        const all_assets = await response.json();
        // document.getElementById('update').innerHTML = "bruh: "+all_assets[4]["title"];

    }
</script>

# APKs Downloads
Here are a few things to take note about the APKs here
1. _**SOURCES**_. Almost everything here are pulled from an Android phone using [ADB](https://arifhamed.com/resources/apk/tools), and all apps are originally installed from the **[Google Play Store](https://play.google.com)**. There will be quite a few exceptions.
1. _**UPDATES**_. Files here **might not be up-to-date** to the latest according to the Play Store, just comment in the page that it is outdated, or [report it](https://arifhamed.com/report)
1. _**FILE SIZE NOTICE**_. Files that exceed __2 GB__ are split into multiple archives. Use any archival software such as the one I used to pack them, <a href="https://www.win-rar.com/start.html?&L=0" target="_blank">WinRAR</a>, to unpack them. As of <span class="timestamp">03 May 2022</span>, I have yet to find a reliable place to store these huge files that are more than _2 GB_
1. _**VIRUSTOTAL**_. All files that are **less than 650 MB** <span class="timestamp">_[as of 03 May 2022]_</span> are scanned with <a href="https://www.virustotal.com/" target="_blank">_VirusTotal_</a> and _Windows Defender_.
    * Some files here have a few trivial detections picked up by VirusTotal, but they are usually false positives. Either way, anything detected by the softwares I would state clearly in their respective posts.
    * The maximum flags per file I would allow to be uploaded to my website would be _**1**_, or _**2** for a very few exceptions_.
    * Files that exceed 650 MB are usually XAPK or APKS, so I would just unpack those and then scan those files
        * ..however, some OBB files are still over 650 MB so for that I just scanned via Windows Defender (which really isn't much but whatevs)
1. _**TYPES**_. Not all files here are APKs:
    * Some are XAPK files. They are basically archive files that contains both APK and OBB. These require the <a onclick='window.open("https://github.com/arifhamed/arifhamed.github.io/releases/download/apk/io.apkmody.sai_2.1.6.apk", "_self")'>XAPK Installer</a> (contains ads) <span style="font-size: 70%;">(for backup's sake I have saved an APK for this, just in case something happens to the original uploader of XAPK Installer)</span>.
        * Play Store: <a href="https://play.google.com/store/apps/details?id=io.apkmody.sai" target="_blank"><i class='fab fa-google-play'></i></a>
        * Amazon Store: <a href="https://www.amazon.com/XAPKS-Installer-Install-APKs-XAPK/dp/B09769NSBY" target="_blank"><i class="fab fa-amazon"></i></a>
    * Some could be APKS files. It is basically an archive file that contains the base.apk with other split APKs that are required to be installed with the base.apk. These are rare, and thankfully so, getting an APKS file takes time to pull from a phone.
        * XAPK Installer works just as well too, actually.
1. _**FUNCTIONALITY**_. Not all apps here will be successfully installed into your phone
    * There are (at least) 2 architectures that every Android phone uses. If the APK and your phone is one of the other, then no install (no matching ABIs)
        * arm64-v8a
        * armeabi-v7a
1. _**TRAILERS**_. Almost all the trailers recorded for each game page here are pulled from Google Play. Those that don't come from Google Play may just be stills, short gameplay sourced from YouTube, and case-by-case may be from Steam as well.
1. _**METHODS & TOOLS**_. There are **a lot of tools** available that relate to installing or creating these APKs that I have, and you can find all of them **[here](https://arifhamed.com/resources/apk/tools)**
1. _**COMMENT**_. If any of the games do not work or does not seem to work as intended, **leave a comment** on that page, <span style="font-size:80%;">if the comment system still works</span>.

<!-- 1. _**GAMEPLAY**_. All gameplay here are **recorded by Genymobile's <a href="https://github.com/Genymobile/scrcpy" target="_blank">scrcpy</a> software, rom1v's <a href="https://github.com/rom1v/sndcpy" target="_blank">sndcpy</a> and Window’s Xbox Game Bar**.  -->
<!-- 1. _**REVIEW CREDIBILITY**_. Related to gameplay and compatibility, **not all games I have played through all the way**, so some of my thoughts may not be reflective of the whole game, and I would usually state about it too. -->
<!-- 1. **Personal disclaimer**: * I do not condone piracy, <span style="font-size:170%">but</span>, I also do not condone putting **paywalls** and **paid subscription** behind software that is or was free, or paid to begin with, and limiting **freedom** &amp; **opinion** of customers. <a href="https://upload.wikimedia.org/wikipedia/commons/d/d7/The.Pirate.Bay.Cartoon-small.png" target="_blank">stay woke</a> -->

<!-- <span ondblclick="document.getElementById('banned').style.display='block'" style="font-size:60%;">there's also some that I never want to install on any phone</span>

<pre id="banned" style="display:non;">

</pre> -->

<br>
<br>
<br>
<br>

<span style="font-size:150%">ALRIGHT</span>

So let's get straight to it. here it is. Search will definitely be implemented functionally soon.

<input id="apkSearchId" type="text" class="w-100" onkeyup="apkSearch()">


<div class="row" id="apk-gallery">
    {% for post in site.posts %}
    {% if post.url contains '/apk' %}
    <div class="col-sm-3 {% if post.paid or post.nsfw %} paid {% else %} free {% endif %}" title="{{ post.title }}" style="{% if post.paid or post.nsfw %} display:none; {% endif %}">
        <div class="card">
            <div class="card-body">
                <a href="{{site.baseurl}}{{post.url}}"><img class="card-img" src="/static/images{{ post.url }}-icon.webp" alt="{{ post.title }} icon"></a>
                <!-- <h5 class="card-title">{{ post.title }}</h5> -->
                <h5 class="card-title text-center">{{ post.title }}</h5>
            </div>
        </div>
    </div>
    {% endif %}
    {% endfor %}
</div>
