---
title: "APK"
permalink: /resources/apk
redirect_from: 
- /apk/
- /apks
- /apks/
- /APK
- /APK/
- /APKs
- /APKs/
- /APKS
- /APKS/
- /resources/apk/
- /resources/apks
- /resources/apks/
- /resources/APK
- /resources/APK/
- /resources/APKs
- /resources/APKs/
- /resources/APKS
- /resources/APKS/
layout: default
# secret: "https://arifhamed.github.io/resources/apk?key=在他里面，我们借着耶稣的宝血得着救赎，我们的过犯得着赦免，是照着他丰富的恩典"
secret: javascript:var slist=document.getElementsByClassName('col-sm-3');for(let a of slist)a.setAttribute('style','display:inline;');
---

{% capture apk-md %}
{% include resources-apk-inc.md %}
{% endcapture %}
{{ apk-md | markdownify }}

<div class="row">
    {% for post in site.posts %}
    {% if post.url contains '/apk' %}
    <div class="col-sm-3" title="{{ post.title }}" style="{% if post.piracy or post.nsfw %} display:none; {% endif %}">
        <div class="card">
            <div class="card-body">
                <a href="{{site.baseurl}}{{post.url}}"><img class="card-img" src="/static/images{{ post.url }}-icon.png" alt="{{ post.title }} icon"></a>
                <!-- <h5 class="card-title">{{ post.title }}</h5> -->
                <h5 class="card-title text-center">{{ post.title }}</h5>
            </div>
        </div>
    </div>
    {% endif %}
    {% endfor %}
</div>
