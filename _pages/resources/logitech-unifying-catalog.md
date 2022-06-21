---
title: Logitech Unifying Catalog
permalink: /resources/logitech-unifying-catalog
layout: default
redirect_from:
 - /resources/logitech-unifying-catalog/
 - /resources/logitech-catalog
 - /resources/logitech-catalog/
 - /resources/unifying-catalog
 - /resources/unifying-catalog/
 - /logitech-unifying-catalog
 - /logitech-unifying-catalog/
 - /logitech-catalog
 - /logitech-catalog/
 - /unifying-catalog
 - /unifying-catalog/
 - /resources/logitech-unifying
 - /resources/logitech-unifying/
 - /resources/logitech
 - /resources/logitech/
 - /resources/unifying
 - /resources/unifying/
 - /logitech-unifying
 - /logitech-unifying/
 - /logitech
 - /logitech/
 - /unifying
 - /unifying/
---

# Logitech Unifying Catalog

So, the only place where I could find a list of Logitech devices, that are compatible with the Unifying Dongle that Logitech created, is in <a href="https://www.quora.com/What-devices-can-I-pair-with-my-Logitech-unifying-receiver-other-than-a-mouse-and-keyboard" target="_blank">this Quora page</a>, last updated 2014 (yikes).

The Unifying Technology that Logitech created is actually amazing. The average number of USB type A ports in any typical laptop is usually 2. Both of my X250 and my C640 have 2 USB type A ports. What if you need to connect to 2 devices using both ports, then basically you will have both ports used up like that! 

The Unifying Technology allows **multiple devices** that are compatible with Unifying to **_connect to the same Unifying Dongle_**, and even the dongle that came with those devices doesn't even need to be used! Up to **6** devices can be connected at a time, which, in my perspective, is already more than what an average consumer uses. 

Unfortunately, Logitech nowadays is trying to market other products that are not Unifying, and I don't know of a solid reason why so. If you kinda know why, please leave a comment below!

<span style="font-size:60%;">Footnote: Unifying Software is not available for Linux & Unix systems</span>

---

still wip. i'm thinking to just note that each of device will just show the image, click on it, then it brings you to the most viable spec sheet.

<div class="container" id="luc-devices">
    <div class="row row-cols-3">
        {% for post in site.categories.luc %}
            <a class="col btn btn-outline-dark" href="{{ site.baseurl }}{{ post.url }}">
                {{ post.title }} &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; {{ post.url }} 
                <br><br>
                {{ post.date | date: "%-d %B %Y" }}
                <br><br>
                <img src="{{ post.thumbnail }}">
            </a>
        {% endfor %}
    </div>
</div>

---

{% include comments.html url=page.url %}
