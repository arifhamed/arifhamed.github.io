---
title: ubuntu tips
layout: default
permalink: /guides/ubuntu
redirect_from:
 - /guides/ubuntu/
 - /ubuntu
 - /ubuntu/
 - /guides/linux
 - /guides/linux/
 - /linux
 - /linux/
---

# ubuntu tips

This is more, like, for me to reference to. i learned some things **and i will forget them** after a while, so here it is.

I also have some [preference commands](#preference-commands) that i can input when installing ubuntu (and it's derivatives) fresh


<br><br><br>

---

### Get Windows License Key from machine 
Sometimes you need to get the license key for whatever reason, just go to terminal and enter in the following, followed by your user password:

``` console
sudo tail -c+57 /sys/firmware/acpi/tables/MSDM
```

ez

Note that the output may look abit weird, like, there would be no newline after the license key text.<br>
Also note that this may not work for custom built machines (where Windows may not be pre-purchased with it)

<br><br><br>

---

### Get machine's serial number
I find this useful when you need to get the laptop's serial number and you're just to lazy to flip it around. Once again, go to terminal and enter in the following, followed by your user password:

``` console
sudo dmidecode -t system | grep Serial
```

<br><br><br>

---

### Temperature monitor from Terminal
This is a way to keep a tab on how hot your laptop would be. You would need to install the `lm-sensors` package through `apt` before running the `watch` command

``` console
sudo apt install lm-sensors

watch -n 1 sensors
```

<br><br><br>

---

### Find display server protocol
In all honesty, idk why or how became a thing, and so far, i have not found a scenario where this tip would help, but just in case, here it is:

``` console
arifhamed@arifhamed-ThinkPad-X250:~/Downloads$ loginctl
SESSION  UID USER      SEAT  TTY
     c2 1000 arifhamed seat0    

1 sessions listed.
arifhamed@arifhamed-ThinkPad-X250:~/Downloads$ loginctl show-session c2 -p Type
Type=x11
```

Note that there are <a href="https://en.wikipedia.org/wiki/Windowing_system#Display_server_communications_protocols" target="_blank">6 known protocols</a>:
1. X11
1. Wayland
1. Mir
1. SurfaceFlinger
1. Quarts Compositor
1. Desktop Window Manager


<br><br><br>

---

### Preference commands

the following are just **my** own commands that i run before taking a nap after fresh installing a new ubuntu installation. If you can't tell by the fact that i have this entire page about Ubuntu, i obviously have lesser love for the other distros (like Arch or especially CentOS).

``` console
sudo apt update; sudo apt upgrade -y; sudo apt install wine lm-sensors ffmpeg git asciinema adb apksigner qbittorrent hwinfo powertop fancontrol traceroute gparted tint quadrapassel gdebi gedit steam vlc obs-studio krita inkscape telegram-desktop -y; sudo snap install --classic sublime-text; sudo snap install --classic code; reboot

sudo apt install apt-transport-https dirmngr -y; sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF; echo "deb https://download.mono-project.com/repo/ubuntu vs-bionic main" | sudo tee /etc/apt/sources.list.d/mono-official-vs.list; sudo apt update; sudo apt-get install monodevelop -y
```