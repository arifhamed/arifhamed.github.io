---
title: Respondus Lockdown Browser 
layout: default
permalink: /guides/ldb-in-ubuntu
redirect_from:
 - /guides/ldb-in-ubuntu/
 - /guides/ldb-ubuntu
 - /guides/ldb-ubuntu/
 - /ldb-in-ubuntu
 - /ldb-in-ubuntu/
 - /ldb-ubuntu
 - /ldb-ubuntu/
---

# Respondus Lockdown Browser 

This is a piece of software that has some questionable legality, yet schools all around the world uses it, from Houston Uni to NYP. Despite it being free, I say it's questionable because it forces us to use Windows & Mac OS, both of which is are paid software.

But either way, whatever.

Lockdown Browser is a problem for Linux users like me. There are many solutions that people use in the past, but so far none work for me.

So, well, all i did was a dual-boot. I foresee that I may use Windows once in a while, so i may as well have it permanently. 

btw, Lockdown Browser knows it when you use any virtualization software, such as VMWare or Gnome Boxes. I attempted to use the latter but the browser knew that I was running on a virtual environment. 

So, here's what I did.

### Step 1: Prepare removable media

You can create 2 different USBs, one matching your Linux distro, and another for Windows. I have found something that could make this part better, and it's called <a href="https://ventoy.net/en/index.html" target="_blank">Ventoy</a>. Check it out, as it has been the only USB Toolkit that I have used ever since I found it.

### Step 2: Boot into the removable Linux

_NOTE: Disable "Secure Boot" in BIOS when you can, thought you should know that because Linux isn't native to any computer._

I did this because when you just run your Linux computer, it locks your internal storage, so we couldn't do the necessary operations on the main Linux OS. For me, Ubuntu gives the option to run from the "CD", or rather, the ISO from my Ventoy drive. Boot in by using your BIOS, which is dependant on your laptop hardware manufacturer, then boot into the Linux media (which you should have connected it by now via USB-A).

### Step 3: Install GParted

GParted is a very useful tool for doing storage manipulations. Run the following command to your terminal:

``` console
sudo apt install gparted
```

This is for Debian & Ubuntu, other distros, just figure out yourself. Just accept the rest and then it should appear in your Applications. 

### Step 4: Make some space for Windows

Using GParted, resize your current local Linux, minusing off about 20GB or more for Windows. **Be sure to backup your data as there can be an error that will cause DATA LOSS or something like that**. After that, select the unallocated section and add new partition. Set it as NTFS, you can rename the label and partition whatever you want. 

### Step 5: Restart and boot into the Windows media

The same as step 2, just replace the Linux media with the Windows media

### Step 6: Install Windows

CHOOSE CUSTOM INSTALLATION. From there it shows which partition to install on. Choose the one of the size that you set a new parti- its pretty obvious. Besides that you can just install it normally.

### Step 7: Boot Priority

Set boot priority to your distro first, because Windows will take precedance when you install it. BE SURE TO disable "Secure Boot" if you haven't done so. Oh, what is the "Windows Boot Manager"? Beats me, i think that's what takes over if Secure Boot in the UEFI is enabled.

### Step 8: Necessary steps from there

Choosing between Linux & Windows should be easy if you know how to easily access your boot options. Switch back to Windows to install Respondus Lockdown Browser from there (may require you to log into your school account mail to access the links to download the school specific LDB)

### Epilogue

You know, there was a time where gestures on precision touchpads were not detected, until some narc bragged about to our applications security teacher one day. now i can't cheat anymore :(

No one likes Lockdown Browser.
