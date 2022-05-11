---
title: "Media Tips & Tricks"
permalink: /guides/media-tips
redirect_from:
 = /guides/media-tips/
 - /guides/mediatips
 - /guides/mediatips/
 - /guides/media
 - /guides/media/
 - /media
 - /media/
 - /mediatips
 - /mediatips/
 - /media-tips
 - /media-tips/
---

# Media Tips<br><span style="font-size:70%;">handling images, videos, audio & more
I have worked with quite a lot of images, videos & audio, and I have learnt quite a lot (from the Internet) that I will share, not only for everyone but also for me if those pages that were accessible online were taken down for some reason. Tips are still incoming, slowly though.

---

### Batch convert image types using ImageMagick

ImageMagick is a , and I use it whenever I want to convert images offline. You can download it <a href="https://imagemagick.org/script/download.php" target="_blank">here</a>.

Say for example, I want to convert a lot of .WEBP that I downloaded from the internet, but as it seems, its actually gifs. Through the command prompt, I can use ImageMagick to create new .gif from reading the .webp, basically making a duplicate to your liking. The code is as showed below: 

``` console
magick mogrify -format gif *.webp
```

---

### Downloading an blob video using FFMPEG
