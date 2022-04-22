---
title: "Undertale"
layout: post-apk
permalink: /resources/apk/:title
play-link: 
steam-link: https://store.steampowered.com/app/391540/Undertale/
tags: rpg great-soundtrack story-rich choices-matter
secret: javascript:document.getElementById('truth').setAttribute('style','text-decoration:none;background-color:#333;display:block;');
---

> _"Welcome to UNDERTALE. In this RPG, you control a human who falls underground into the world of monsters. Now you must find your way out... or stay trapped forever." - <a href="https://store.steampowered.com/app/391540/Undertale/" target="_blank">Steam</a>_

<span class="timestamp">21 April 2022:</span> Now imagine my surprise to find a mobile version of this game that exists.

While scavenging for APKs in a certain website, i came across Undertale. After finding out that perhaps people actually thought of porting the game from PC to Android (unofficially), i did a quick google search and found <a href="https://www.moddb.com/mods/undertale-mobile-mod" target="_blank">this</a>. All the details should be in the ModDB site, but just in case anyway, i've copied the guide here too.

---
---

## How to install the Undertale Mobile Mod for iOS and Android.

Posted by <a href="https://www.moddb.com/members/jockeholm" target="_blank">Jockeholm</a> on Nov 27th, 2019 - Intermediate Other

### <u>Preliminary setup:</u>

This mod requires you to own the v1.08 release on either Windows, Mac or Linux. Navigate to your install folder and copy your v1.08 data.win/ios/unx file and all of the .ogg files. These are required to create the ipa/apk.

A Windows PC is also required.

1. Download the <a href="https://arifhamed.github.io/static/archives/Undertale_Mobile_Mod_2.0.0.zip" target="_blank">mod zip</a> (last updated as of <span class="timestamp">09-Dec-2019</span>).
1. **SKIP THIS STEP IF YOU OWN THE STEAM v1.08 RELEASE**: Run DeltaPatcherLite.exe and drag and drop your data.win/.ios/.unx into the 'original file' box. (If you're using the Windows 10 Store, <span onclick="this.innerHTML='magnet:?xt=urn:btih:767CA0969B52378CF7FF12880AC3952EC280FD5E&tr=http%3A%2F%2Fbt2.t-ru.org%2Fann%3Fmagnet&dn=Undertale%20%5BL%5D%20%5BENG%5D%20(2015)%20(1.08)%20%5BGOG%5D'">GOG,</span> or Windows Collector's Edition version of the game drag and drop the "Windows Collector's Edition" .xdelta file into the 'XDelta Patch' box. Otherwise use the .xdelta patch which corresponds to your version of the game.) Click 'Apply patch' - this will give you the v1.08 Steam release version of the game.
1. Drag and drop the Steam data.win into the 'Original file' box, then drag and drop the Steam to Mobile Mod .xdelta patch into the 'XDelta Patch' box. Click 'Apply patch', this will give you the patched version of the game with the mobile mod installed.
1. Rename data.win to game.ios, or game.droid if you're installing on an Android device.

<u>Instructions (iOS no jailbreak): - _IMPACTOR CURRENTLY DOES NOT WORK, FOR NOW iOS IS JAILBREAK ONLY_</u>

1. Open the UNDERTALE.ipa file with a program such as WinRar or 7zip and place the patched data.win file into UNDERTALE.ipa\Payload\UNDERTALE.app\games\ alongside all of the .ogg files from your UNDERTALE install (If you don't include the ogg files, you won't have any music).
1. Download <a href="http://www.cydiaimpactor.com/" target="_blank">Cydia Impactor</a>
1. Create or login to your <a href="https://appleid.apple.com/account/manage" target="_blank">AppleID</a> and generate an app specific password. (You may need to enable 2FA to do this.)
1. Run Cydia Impactor and connect your iPhone to your PC. Drag and drop the UNDERTALE.ipa file into Cydia Impactor and sign into your AppleID, using the app specific password in the password field.
1. If all goes well UNDERTALE should now be installed on your phone. Check to see if the app icon has appeared. You may need to trust the app under Settings>General>Profiles & Device Management in order to run it. You may also need to renew the app every 7 days in order to keep using it. (This is a restriction put in place by Apple, I can't do anything about this unfortunately.)

<u>Instructions (iOS, Jailbreak required, permanent):</u>

1. Install ReProvision (<a href="https://repo.incendo.ws/" target="_blank">repo link</a>) & Filza File Manager via Cydia
1. Open Filza and press the cog/settings wheel at the bottom of the screen, then click 'Enable WebDAV server' (Make sure you turn this off after you're done!)
1. On your PC head to the http link listed underneath the WebDAV setting in Filza and navigate to /var/mobile/Documents
1. Upload your UNDERTALE.ipa via the upload button in the top-right of the screen. (Once this is done you can disable the WebDAV server and close Filza on your PC.)
1. Open Filza on your phone and you should see the ipa in your documents. Hold your finger on the ipa for a few seconds to select it, then click 'More' in the bottom right of the screen, then 'Open with'. Open the ipa with ReProvision.
1. Once ReProvision opens, sign in with your apple id if you haven't already, then click 'Install' on the UNDERTALE ipa pop-up. The app should now be on your homescreen and ready to run.

<u>Instructions (Android):</u>

1. Copy and paste your game.droid file and all of the .ogg files from your Undertale install into Android\assets
1. Back out into the Android folder and run create-apk.bat
1. Once the .apk is generated, plug your phone into your computer using the charging/usb cable, then right click the .apk file and go to Send to > 'Your phone name'
1. Navigate to 'My files' on your phone and locate the UNDERTALE.apk, then open it. A security pop-up should appear if this is your first time installing the app, go to settings and enable 'Allow from this source'. Back out of the menu and you should see a window prompting you to install the app. Press install.

---

Common issues (iOS):<br>
• Impactor displays "You already have a current iOS Development certificate or a pending certificate request." or other errors whilst attempting to install the ipa:<br>
Under the Xcode tab click 'Revoke Certificates'. If no certificates are revoked and the error is still occurring, you may need to use a new AppleID.<br>
• Impactor displays "Failed to verify code signature":<br>
You may have missed a step or incorrectly configured your ipa, check back and start over. Or I've messed up my instructions<br>
• Impactor displays "Please update to xcode 7.3":<br>
As of writing this Apple has pushed a server side change which stopped Impactor from working. Saurik will update this at somepoint in the future, but for now this method does not work.<br>
• ReProvision doesn't allow me to input my 2FA code:<br>
The current version of ReProvision does not support 2FA, please use an Apple ID without 2FA enabled. (You can use a burner account if you're worried about this)<br>

---
---

If you have followed this with no error than congrats, you now have mobile determination!

<div class="text-center">
    <a id="truth" class="btn btn-dark btn-block w-100" onclick='apk("com.jockeholm.undertale_2.0.0.apk")' target="_blank" style="text-decoration: none; background-color: #333; display: none;"> Download <b>om.jockeholm.undertale_2.0.0.apk</b> (142 MB)</a>
</div>
