---
title: "apk tools"
permalink: /resources/apk/tools
redirect_from: /resources/apk/tools/
---

# Useful Tools for Android Package Kit

Here are some tools that I used in processing the APKs I have collected and saved into this website.

<hr>

### RAR & 7z

RAR & 7z, the cornerstones of data archival. I don't want to bore you (and me) with the description, so here it is, alongside what I used this is for and what you can use it for.
* Decompressing files that Windows does not recognize as archive files (anything besides ZIP, like XAPK & APKS), usually for analysis of smaller files inside
* Splitting of large files into split archives. The result of splitting a file (or a group of files, if you fancy) will lead to having multiple .part0.rar, .part01.rar, .part02.rar, and so on, it really depends on the configuration you set before splitting
    * ..and like-wise, you can use RAR to un-split it back. Just extract from one of the parts, RAR should be able to identify the others solely based off the name and the parts. Of course, errors will be thrown if the end-archive is corrupt (not all parts present and have the same name besides the suffix). 

<div class="text-center">
    <a class="btn btn-dark btn-block w-100" href="https://play.google.com/store/apps/details?id=com.rarlab.rar" target="_blank" style="text-decoration: none; background-color: #333;">RAR Google Play (recommended, latest update)</a><br>
    <a class="btn btn-dark btn-block w-100" onclick='apk("com.rarlab.rar_6.10.build104.apk")' target="_blank" style="text-decoration: none; background-color: #333;"> Download <b>com.rarlab.rar_6.10.build104.apk</b> (3.32 MB)</a><br>
    <a class="btn btn-dark btn-block w-100" href="https://play.google.com/store/apps/details?id=ru.zdevs.zarchiver" target="_blank" style="text-decoration: none; background-color: #333;">7z Google Play (recommended, latest update)</a><br>
    <a class="btn btn-dark btn-block w-100" onclick='apk("coming soon")' target="_blank" style="text-decoration: none; background-color: #333;"> Download <b>coming soon.apk</b> ( MB)</a><br>
</div>

<hr>

### HardwareInfo

I use this on multiple phones to check what kind of mobile GPU each phone has. For certain games, you may need to check the your device what kind of mobile GPU to get the recommended file(s) that are most compatible with it. Unfortunately, for whatever reason, it was removed from the Play Store.

<**for arif: include some screenshots here**>

<div class="text-center">
    <a class="btn btn-dark btn-block w-100" onclick='apk("com.dama.hardwareinfo_4.2.6.apk")' target="_blank" style="text-decoration: none; background-color: #333;"> Download <b>com.dama.hardwareinfo_4.2.6.apk</b> (5.98 MB)</a>
</div>

<hr>

### APK Installer

This is more than the usual package installer that every Android phone comes with. This can help you install .XAPK files, APKS files, the list probably ends there. There are many different versions of this app that you can find online, but the apkmody.io version is suffice imo. 

<div class="text-center">
    <a class="btn btn-dark btn-block w-100" href="https://play.google.com/store/apps/details?id=io.apkmody.sai" target="_blank" style="text-decoration: none; background-color: #333;"> Google Play (recommended, latest update)</a><br>
    <a class="btn btn-dark btn-block w-100" onclick='apk("io.apkmody.sai_2.1.6.apk")' target="_blank" style="text-decoration: none; background-color: #333;"> Download <b>io.apkmody.sai_2.1.6.apk</b> (7.94 MB)</a>
</div>

<hr>

### AntiSplit-X

This is, perhaps, super underrated. It combines every .apks file imagineable, into one .apk file. There is a lot of configs you can set in it too, like whether or not you want to sign your output.apk or not, and other stuff. I really praise it well for certain use cases that I have encountered with. Despite how well built the UI is, it lacks from the Play Store,

<div class="text-center">
    <a class="btn btn-dark btn-block w-100" onclick='apk("botX.arscmerge_1.4.apk")' target="_blank" style="text-decoration: none; background-color: #333;"> Download <b>botX.arscmerge_1.4.apk</b> ()</a>
</div>

<hr>