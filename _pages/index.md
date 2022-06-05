---
title: "Arif Hamed"
layout: default
permalink: /
funky: true
---

<!-- <link rel="stylesheet" href="https://arifhamed.com/static/css/bootstrap.min.css">
<script src="https://arifhamed.com/static/js/jquery.min.js"></script>
<script src="https://arifhamed.com/static/js/bootstrap.min.js"></script>

<link rel="stylesheet" type="text/css" href="https://arifhamed.com/static/css/site.css"> -->


# arif hamed's guides, blogs & resources <br><span style="font-size:60%;">my casual digital abode</span>

wanna see my resume? go to my [`about` page](https://arifhamed.com/about).

here to look at some projects i did? go to my [`projects` page](https://arifhamed.com/projects).

looking for some tips or guidance in certain IT topics? check out all my guides from the nav.

got time to kill on your android phone? download some apks from my [`apk` resource page](https://arifhamed.com/resources/apk).

got an iphone instead? sponsor me a paid apple developer account cuz apple is an authoritarian company (still ethically better than nestle)

<s>maybe you wanna stick to the current trend? play my own copy of [`wordle`](https://arifhamed.com/games/wordle).</s> i think it's out of trend by now

think this homepage could be better? same. in fact, you can just leave comments almost anywhere in this website, you just need a github account.

<span id="time">i can't get the latest update to this website smh</span>

<script>
    getLatestCommitDate();
    async function getLatestCommitDate() {
        const response = await fetch("https://api.github.com/repos/arifhamed/arifhamed.github.io/commits");
        const all = await response.json();
        const latest_date = all[0]['commit']['author']['date']+" (GMT+8)";
        document.getElementById('time').innerHTML = "this website was last updated in "+latest_date;
    }
</script>


{% include comments.html url=page.url %}
<br><br>
<span style="font-size:70%;">[my to-do list](https://arifhamed.com/todo).</span>