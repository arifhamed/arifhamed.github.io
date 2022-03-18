---
title: "Automation with Python"
permalink: /guides/automation-with-python
redirect_from:
 - /guides/automation-with-python/
 - /guides/automation
 - /guides/automation/
layout: default
---
# Automation Scripts with Python 

Disclaimer: All scripts here are tested and functional in Windows 10, and most scripts (unless otherwise stated) are tested and functional in Python 3.9

Python was the first language I have ever learnt when I started my journey into IT. Learnt it back in 2017, when it was part of the new Computing subject for GCE "O" Levels. Ever since then though, I barely use it in any actual homework in my NYP course, with likely 3 modules that are an exception.

However, Python has some pretty useful uses in handling files, and as a data hoarder, using Python for automating data handling is just what I need

This page is just simply some scripts that I use to automate some stuff. Each script should have plenty of comments inside to explain what it does. Like the other guides, this page is more for my own reference.
<hr>

## GitHub Release Assets Batch **Uploader**
``` py
{% include_relative files/github-release-assets-batch-uploader.py %}
```
<hr>

## GitHub Release Assets Batch **Downloader**
i made this before finding out about `gh release download <tag>`
``` py
{% include_relative files/github-release-assets-batch-downloader.py %}
```
<hr>

## VirusTotal Batch Scanner <span style="font-size:130%">STILL WIP</span>
``` py
{% include_relative files/virustotal-cli-batch-scanner.py %}
```
<hr>

## FFMPEG Batch Converter <span style="font-size:130%">STILL WIP</span>
``` py
{% include_relative files/ffmpeg-batch-converter.py %}
```

{% include comments.html %}