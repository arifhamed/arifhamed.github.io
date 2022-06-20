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


<br><br><br>

---

### Get Windows License Key from machine 
Sometimes you need to get the license key for whatever reason, just go to terminal and enter in the following, followed by your user password:

``` console
sudo tail -c+57 /sys/firmware/acpi/tables/MSDM
```

ez

Note that the output may look abit weird, like, there would be no newline after the license key text.<br>
Also note that this may not work for custom built machines.

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