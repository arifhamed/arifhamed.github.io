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

``` bash
~$ sudo tail -c+57 /sys/firmware/acpi/tables/MSDM
```

ez

Note that the output may look abit weird, like, there would be no newline after the license key text.<br>
Also note that this may not work for custom built machines (where Windows may not be pre-purchased with it)

<br><br><br>

---

### Get machine's serial number
I find this useful when you need to get the laptop's serial number and you're just to lazy to flip it around. Once again, go to terminal and enter in the following, followed by your user password:

``` bash
~$ sudo dmidecode -t system | grep Serial
```

<br><br><br>

---

### Temperature monitor from Terminal
This is a way to keep a tab on how hot your laptop would be. You would need to install the `lm-sensors` package through `apt` before running the `watch` command

``` bash
~$ sudo apt install lm-sensors

~$ watch -n 1 sensors
```

<br><br><br>

---

### Find display server protocol
In all honesty, idk why or how became a thing, and so far, i have not found a scenario where this tip would help, but just in case, here it is:

``` bash
~$ loginctl
SESSION  UID USER      SEAT  TTY
     c2 1000 arifhamed seat0    

1 sessions listed.
~$ loginctl show-session c2 -p Type
Type=x11
```

The `c2` in the first output is used as the 2nd paremeter for `loginctl` in the next user input, as shown above.

Note that there are <a href="https://en.wikipedia.org/wiki/Windowing_system#Display_server_communications_protocols" target="_blank">6 known protocols</a>:
1. X11
1. Wayland
1. Mir
1. SurfaceFlinger
1. Quarts Compositor
1. Desktop Window Manager

<br><br><br>

---

### ESO in Linux (or just large programs on Proton/Wine)
or just large Steam Games in general that are not built for Linux compatibility. For some reason, Proton or whatever will give you a very limited amount of storage for your Windows games to work with. This is an unfortunate case for _Elder Scrolls Online_, where it actually makes use of an external installer/launcher after downloading about 100GB of the game straight from Steam. After the initial download though, I don't think it actually downloads again, the installer/launcher is just there to apply updates when there is. To solve the limited storage space problem:

1. Go to your **Steam library**
1. **Right click** on the game that you want Wine to increase itself in size
1. Choose **Properties**
1. The second thing in the first page that you see should be "LAUNCH OPTIONS". In that text box, enter the following:
     * `PROTON_SET_GAME_DRIVE=1 %command%`

note that you actually need that total space in the start, minimum 128GB storage should be fine but i personally wouldn't recommend that. Also, it sure does work for me, though i may not guarantee that it'll work for everyone in different time periods (as would everything else here, really)

Answer found <a href="https://www.reddit.com/r/linuxquestions/comments/n4dbiy/eso_on_proton_disk_space_issue_with_linux_pop_os/gwv9qbj/?utm_source=share&utm_medium=web2x&context=3" target="_blank">on Reddit</a>.

<br><br><br>

---

### Locked folder in your own computer
I noticed that sometimes i get locked folders whenever i do some meta stuff that involves ubuntu. 

``` bash
~$ sudo chown -R $USER: $HOME
```

`$USER` refers to the current user, which is you. <br>`$HOME` refers to the current user's home directory. Just entering `$HOME` itself, bash will return "Is a directory".

Just to put it here, say for example, my _APKs_ folder in my removable storage is locked for whatever reason. I just replaced `$HOME` with the exact location of the folder.

``` bash
~$ sudo chown -R $USER: /media/arifhamed/080D1CF03C033DFF/APKs
```

<br><br><br>

---

### Timestamps in terminal/bash/console (whatever you call it)
I find that this is a rather cool feature for whatever you want to do on the console, like if i left a command to run, i may want to know when it finished when i was gone or in another window. Please `sudo apt install gedit` first if you don't have `gedit` already (it'll just make life a bit easier imo)

``` bash
~$ sudo gedit ~/.bashrc
```

A window should appear where you see a whole bunch of text and comments in it. Add the following to end of the file:

``` console
export PROMPT_COMMAND="echo -n \[\$(date +%H:%M:%S)\]\ "
```

it's good to leave your own comment in as well telling future you what it is. Next, _save_ and _exit_. Close and open console, and you should see something like this:

``` bash
[23:40:09] arifhamed@C640:~$
```

yup, i typed this tip on 11:40pm.

Source: <a href="https://askubuntu.com/questions/193416/adding-timestamps-to-terminal-prompts" target="_blank">AskUbuntu</a>

<br><br><br>

---

### Building Dolphin Emulator on Linux
no not the Dolphin File Explorer given by Kubuntu, this is the GameCube & Wii emulator. Start out at where your directory for your `Repos` are and enter this one line. You may require to enter in your admin password one or two times. I would more or less rather enter each line after each other. It is the last 3 lines that may take a while, and use 100% of your threads. So if you do enter all of the lines at once, just sit back, relax, and see all of the cmake wizardry scroll through the terminal.

```

sudo apt install --no-install-recommends ca-certificates qtbase5-dev qtbase5-private-dev git cmake make gcc g++ pkg-config libavcodec-dev libavformat-dev libavutil-dev libswscale-dev libxi-dev libxrandr-dev libudev-dev libevdev-dev libsfml-dev libminiupnpc-dev libmbedtls-dev libcurl4-openssl-dev libhidapi-dev libsystemd-dev libbluetooth-dev libasound2-dev libpulse-dev libpugixml-dev libbz2-dev libzstd-dev liblzo2-dev libpng-dev libusb-1.0-0-dev gettext; 

mkdir dolphin-emu; 

cd dolphin-emu; 

git clone https://github.com/dolphin-emu/dolphin; 

cd dolphin; 

git submodule update --init; 

mkdir Build && cd Build; 

cmake ..; 

make -j$(nproc); 

sudo make install

```

Source: <a href="https://wiki.dolphin-emu.org/index.php?title=Building_Dolphin_on_Linux" target="_blank">Dolphin Emulator Official Website</a>

<br><br><br>

---

### My own setup command.

the following are just **my** own commands that i run before taking a nap or have lunch after fresh installing a new ubuntu installation. If you can't tell by the fact that i have this entire page about Ubuntu, i obviously have lesser love for the other distros (like Arch and especially CentOS).

``` bash
sudo apt update; sudo apt upgrade -y; sudo apt install wine lm-sensors ffmpeg git gh asciinema adb apksigner qbittorrent hwinfo powertop powerstat fancontrol traceroute tint quadrapassel gnome-disk-utility gnome-screenshot gdebi gedit steam vlc obs-studio krita inkscape telegram-desktop kamoso kdenlive imagemagick baobab -y; sudo snap install discord mc-installer zoom-client; sudo snap install --classic sublime-text; sudo snap install --classic code; sudo snap install android-studio --classic; sudo apt install apt-transport-https dirmngr -y; sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF; echo "deb https://download.mono-project.com/repo/ubuntu vs-bionic main" | sudo tee /etc/apt/sources.list.d/mono-official-vs.list; sudo apt update; sudo apt-get install monodevelop mono-xsp4 -y; sudo apt update; sudo apt upgrade -y; sudo snap refresh; reboot
```

note for arif: the command above is configured for Kubuntu, where certain packages already exist as it's own version that belongs in KDE, such as _KDE Partition Manager_ that is the KDE version for _GParted_.
