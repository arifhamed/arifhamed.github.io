---
title: "Android Debug Bridge"
permalink: /guides/android-debug-bridge
redirect_from:
 - /guides/adb
 - /guides/adb/
 - /adb
 - /adb/
layout: default
---

# Android Debug Bridge <br><span style="font-size:70%;">and it's capabilities</span>

I used adb when messing around with android applicatioin packages (.apk files) and opaque binary blobs (.obb files), but it has quite a lot of capabilities beyond installing APKs to a phone.

This guide is really just for me to refer to if i'm in and out of debugging android devices.

## adb commands
* <a href="#devices">devices</a>
* <a href="#tcpip">tcpip</a>
* <a href="#connect">connect</a>
* <a href="#install">install</a>
* <a href="#shell">shell pm path</a>
* <a href="#pull">pull</a>
* <a href="#push">push</a>
* <a href="#"></a>

## adb options
* <a href="#-s">-s</a>
* <a href="#"></a>

<hr>

## devices
The command `adb devices` is used to check what devices are connected to the computer.
``` bash
~$ adb devices
List of devices attached
4200440cd42745ad        device
```
Over here, there are 1 device is connected via USB. 

**Important**: Android devices are required to have **developer options** to be unlocked <span style="font-size:70%;">(unlocked usually just by tapping on the build number in the "About" section of Settings)</span> in order for adb to have access to your device.

<hr>

## tcpip
The command `adb tcpip` is used set the target device to listen for a TCP/IP connection on a port, usually 5555.
``` bash
~$ adb tcpip 5555
restarting in TCP mode port: 5555
```
This is used to prepare for the next command

<hr>

## connect
The command `adb connect` is used to connect to a device that has not been connected yet. This is usually used to connect a device wirelessly that is connected to the same WiFi network.
``` bash
~$ adb connect 192.168.50.154:5555
connected to 192.168.50.154:5555
```
Now you can use `adb devices` to check if the device is connected
``` bash
~$ adb devices
List of devices attached
4200440cd42745ad        device
192.168.50.154:5555     device
```
Now adb is connected to multiple devices. Most commands here will return this error: `adb: error: failed to get feature set: more than one device/emulator`. In order to solve this error, look at <a href="#-s">-s</a>

<hr>

## install

The command `adb install` is used to install an APK file to a connected device.

``` bash
~$ adb install com.rarlab.rar_6.10.build104.apk
```

If your APK does not support the device's ABIs, it will not install, and adb will instead, return an error

If you copied your APK from a debug installation, usually done by running an app from Android Studio, you can specify as shown below
``` bash
~$ adb install -r -t base.apk
```

<hr>

## shell
There are many uses to `adb shell`, but i've used `adb shell` to primarily identify locations of files by using `adb shell pm path`.
``` bash My own app
~$ adb shell pm path com.arifhamed.albus
package:/data/app/~~Csp-EsZddaHFDHOLpuzSiw==/com.arifhamed.albus-nwluTCiu_4zV2HznTGtlFQ==/base.apk
```
``` bash RAR app
~$ adb shell pm path "com.rarlab.rar"
package:/data/app/~~Q_2vPHIW_fget0QXGx4WLA==/com.rarlab.rar-vyLBQeS4znyP8jiS0AvGmQ==/base.apk
package:/data/app/~~Q_2vPHIW_fget0QXGx4WLA==/com.rarlab.rar-vyLBQeS4znyP8jiS0AvGmQ==/split_config.arm64_v8a.apk
package:/data/app/~~Q_2vPHIW_fget0QXGx4WLA==/com.rarlab.rar-vyLBQeS4znyP8jiS0AvGmQ==/split_config.xhdpi.apk
```
Here, I have used the name of an application package to find the exact location of the base APK. Note that installed APKs are never easily found in most file managers, hence explains the very mutated naming conventions.

Besides the base.apk, there are other APKs or files that could be present. This is usually Google Play's actions, or manually by XAPK Installer's customization. They are usually labeled as "split", as shown above.

<hr>

## pull

This command is used to simply copy from your android device to your computer.
``` bash
~$ adb pull /data/app/~~Csp-EsZddaHFDHOLpuzSiw==/com.arifhamed.albus-nwluTCiu_4zV2HznTGtlFQ==/base.apk
/data/app/~~Csp-EsZddaHFDHOLpuzSiw==/com.arifhamed.albus-nwlu... 1 file pulled, 0 skipped. 3.3 MB/s (5269281 bytes in 1.501s)
```
As show above, adb will actually show progress if the APK or OBB is large, and it willl save the file to the current working directory. For getting files that are accessible via the built-in file manager, just mention `sdcard` instead.
``` bash
~$ adb pull /sdcard/Download/my-eyes.gif
/sdcard/Download/my-eyes.gif: 1 file pulled, 0 skipped. 8.3 MB/s (870969 bytes in 0.100s)
```
`sdcard` actually refers to Internal Storage

<hr>

## push

The command `adb push` is basically the opposite of `adb pull`, copying a file from the computer to the device. 
``` bash
~$ adb push maxresdefault.jpg /sdcard/Download/
maxresdefault.jpg: 1 file pushed, 0 skipped. 10.2 MB/s (124332 bytes in 0.012s)
```
In `adb push`, it is essential to state the end location for the file that will be pushed to.

<hr>

## -s
This option is essential when there are multiple devices connected to the computer. A simple example is as follows:

``` bash
~$ adb -s 4200440cd42745ad install com.rarlab.rar_6.10.build104.apk
Performing Streamed Install
Success
```
Right after `adb` and before `<any command>`, you must state which device to do the action. For example, doing `shell` like shown above in this page will be like this: `adb -s 192.168.50.154:5555 shell pm path com.rarlab.rar`. Note that it is no different for wirelessly connected devices as well.

{% include comments.html url=page.url %}
