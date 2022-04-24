---
title: "Web Dev Tips"
layout: default
permalink: /guides/webdevtips
redirect_from:
 - /guides/webdevtips/
 - /guides/webdev
 - /guides/webdev/
 - /webdev
 - /webdev/
---
# Web Development Tips
I have worked with quite a lot of websites, undoubtedly this one too (obviously), and I have learnt quite a lot that I will share, not only for everyone but also for me if i ever take a long break from I.T. and forget everything (just like every guide here). Tips are still incoming, slowly though.

<br>
<br>


### Forcing the footer to the foot (without it pasted to the screen)
This is quite a universal and long-lasting problem that everyone that starts out in web development. The following are codes that make your footer stay at the bottom without putting in a lot of breaklines or making your footer absolute (as if you pasted a piece of paper onto your monitor, you don't need that). This solution actually fixed this website's pages shorter than the view height, hence I will show as if you made a Jekyll website (can apply to any website, really)
``` css
body {
    display: flex;
    min-height: 100vh;
    flex-direction: column;
}
```
The above is CSS you can put into your site.css that can apply to all pages (as I also have done <a href="https://arifhamed.com/static/css/site.css" target="_blank">here</a>), and the below is an example of what to do in your layouts html files. The effect will, of course, be visible in _vertically smaller pages_. In the example below though, all i did to change to the layout is add in the style attribute to the _main_content_wrap_ division. 
``` html
<div id="header_wrap" class="outer">
    <!-- HEADER CONTENT -->
</div>

<div id="main_content_wrap" class="outer" style="flex: 1;">
    <section id="main_content" class="inner">
        <!-- MAIN CONTENT -->
    </section>
</div>

<div id="footer_wrap" class="outer">
    <!-- FOOTER CONTENT -->
</div>
```
<hr>

### Place PDFs in website (with and without Bootstrap)
&lt;will be updated soon(ish)&gt;
still currently finding the best way as of <span class="timestamp">25 March 2022</span>

### General script and css tips
In every website, javascript and css will always be present, whether you like it or not. When a website loads a javascript file or a css file, it will take longer if either files are large. So here's just a small list of online tools that would help you:
- [JS Compress](https://jscompress.com/)
- [JS Beautifier](https://beautifier.io/)
- [Bytesize](https://www.javainuse.com/bytesize)

of course, I may update this part soon with more script importing tips or whatnot.

{% include comments.html %}