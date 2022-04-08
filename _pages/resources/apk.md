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
# secret: "https://arifhamed.github.io/resources/apk?key=在他里面，我们借着耶稣的宝血得着救赎，我们的过犯得着赦免，是照着他丰富的恩典"
secret: javascript:var slist=document.getElementsByClassName('col-sm-3');for(let a of slist)a.setAttribute('style','display:inline;');
---

# APKs Downloads
Here are a few things to take note about the APKs here
1. Everything here are **sourced from other websites** that I will not disclose (i know for a fact that those websites plagiarize from each other so i think i'm safe)
    * Most of these apps would create text when booting up (in Android dev terms, a "_Toast_" would appear). That text would contain the source website link text. There could be a few cases where text from other languages would appear, such as _Arabic_ or _Japanese_. **just ignore those, if <a href="https://www.virustotal.com/" target="_blank">_VirusTotal_</a> says its fine, its fineeee**
1. Due to these files are **not updated according to Play Store**, **most games here are usually outdated as of time of uploading that game**.
    * Besides, the older the version is, higher chance of having it without _viruses_.
1. Files that exceed __2 GB__ are split into multiple archives. Use any archival software such as the one I used to pack them, <a href="https://www.win-rar.com/start.html?&L=0" target="_blank">WinRAR</a>, to unpack them.
1. All files that are **less than 650 MB** _[as of 2022-Feb-2022]_ are scanned with <a href="https://www.virustotal.com/" target="_blank">_VirusTotal_</a> and _Windows Defender_.
    * Some files here have a few trivial detections picked up by VirusTotal, but they are usually false positives. Either way, anything detected by the softwares I would state clearly in their respective posts.
    * The maximum flags per file I would allow to be uploaded to my website would be _**1**_, or _**2** for a very few exceptions_.
    * Files that exceed 650 MB are usually XAPK or APKS, so I would just unpack those and then scan those files
        * ..however, some OBB files are still over 650 MB so for that I just scanned via Windows Defender (which really isn't much but whatevs)
1. **Not all files here are APKs**:
    * Some are XAPK files. They are basically archive files that contains both APK and OBB. These require the <a href="https://github.com/arifhamed/arifhamed.github.io/releases/download/apk/io.apkmody.sai_2.1.6.apk" target="_blank">XAPK Installer</a> (contains ads) <span style="font-size: 70%;">(for backup's sake I have saved an APK for this, just in case something happens to the original uploader of XAPK Installer)</span>.
        * Play Store: <a href="https://play.google.com/store/apps/details?id=io.apkmody.sai" target="_blank"><i class='fab fa-google-play'></i></a>
        * Amazon Store: <a href="https://www.amazon.com/XAPKS-Installer-Install-APKs-XAPK/dp/B09769NSBY" target="_blank"><i class="fab fa-amazon"></i></a>
    * Some could be APKS files. It is basically an archive file that contains the base.apk with other split APKs that are required to be installed with the base.apk. These are rare, and thankfully so, getting an APKS file takes time to pull from a phone.
        * XAPK Installer works just as well too, actually.
1. **Not all apps here will be successfully installed into your phone**
    * I have gotten this error quite a few times on different phones when installing through adb: "```INSTALL_FAILED_NO_MATCHING_ABIS: Failed to extract native libraries, res=-113```".
    * <span style="font-size:80%;">(My explanation is an over-simplification, but)</span> This is due to many phones having different architecture (or rather, ABIs) than whatever software the developer have intended for that, kinda like how a x86 OS cannot run modern x64 programs, but x64 OS can run both x64 *and* x86 programs. 
        * As an example, my A16 supports these ABIs
            * arm64-v8a
            * armeabi-v7a
            * armeabi
    * <span style="font-size:130%;">Basically, you can't combine an Samsung phone with an iPhone case</span> (somehow that was the best example I could think of)
    * Same thing for phones, like for example with one of these games I have uploaded here, some can run on my newer phone but not my older one.
    * [**Android**] A simple way to check if you phone is compatible with a game here is by just opening the Play Store and seeing if that app is there. If you have multiple phones that use the same Google account, you can use the Play Store web (on browser) and look at where the "INSTALL" and "Add to wishlist" buttons are.
        * <video muted autoplay loop onclick="this.paused ? this.play() : this.pause();"> <source src="/static/webm/resources/apk/android-limited-distro.webm" type="video/webm"></source></video>
        * The video above is an example of how _Portal Knights_ is only compatible with my _Oppo_ phone, not the _SMJ4_ (the other 2 are from qemulator of Android Studio)
        * I never knew certain games existed unless I manually Google them, such as _[Just Cause Mobile]()_
1. All gameplay here are recorded by Genymobile's <a href="https://github.com/Genymobile/scrcpy" target="_blank">scrcpy</a> software, rom1v's <a href="https://github.com/rom1v/sndcpy" target="_blank">sndcpy</a> and Window’s Xbox Game Bar. 
1. **Related to gameplay and compatibility, not all games I have played through all the way**, so some of my thoughts may not be reflective of the whole game, and I would usually state about it too.
1. If any of the games do not work or does not seem to work as intended, **leave a comment** on that page, <span style="font-size:80%;">if the comment system still works</span>.

<!-- 1. **Personal disclaimer**: * I do not condone piracy, <span style="font-size:170%">but</span>, I also do not condone putting **paywalls** and **paid subscription** behind software that is or was free, or paid to begin with, and limiting **freedom** &amp; **opinion** of customers. <a href="https://upload.wikimedia.org/wikipedia/commons/d/d7/The.Pirate.Bay.Cartoon-small.png" target="_blank">stay woke</a> -->

<span ondblclick="document.getElementById('unobtainium').style.display='block'">I have a list of APKs that I just can't seem to possess at all, anywhere online.</span>

<pre id="unobtainium" style="display:none;">
- Megatroid
    - Every APK found online besides Play Store either does not work or it is littered with viruses
- Bladed Fury
    - Every APK of bladed fury isn't functional for some reason
- Portalize
    - Nah. Almost all apks i have encountered are polluted as heck, just like Megatroid
- Morphite
    - All either non-premium or just adware that you do not want
</pre>

<!-- <span ondblclick="document.getElementById('banned').style.display='block'" style="font-size:60%;">there's also some that I never want to install on any phone</span>

<pre id="banned" style="display:non;">

</pre> -->

<br>
<br>
<br>
<br>

<span style="font-size:150%">ALRIGHT</span>

So let's get straight to it. here it is.


<div class="row">
    {% for post in site.posts %}
    {% if post.url contains '/apk' %}
    <div class="col-sm-3" title="{{ post.title }}" style="{% if post.piracy or post.nsfw %} display:none; {% endif %}">
        <div class="card">
            <div class="card-body">
                <a href="{{site.baseurl}}{{post.url}}"><img class="card-img" src="/static/images{{ post.url }}-icon.png" alt="{{ post.title }} icon"></a>
                <!-- <h5 class="card-title">{{ post.title }}</h5> -->
                <h5 class="card-title text-center">{{ post.title }}</h5>
            </div>
        </div>
    </div>
    {% endif %}
    {% endfor %}
</div>
