---
title: "Debug"
layout: default
permalink: /debug
---
# you're not supposed be here
this is where i do random stuff before publishing

<!-- <iframe width="1066" height="483" src="https://www.youtube.com/embed/O8ClOsE8ihA?rel=0&modestbranding=1&autohide=1&showinfo=0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> -->
<br><br><br><br><br>
Current test: testing apk_search.json, found [here](https://arifhamed.com/_pages/resources/apk_search.json)

Hypothesis: The span element, identified as "update", will get updated with.. certain text.

Good result tasks: Proceed to implement search in /resources/apk

Bad result tasks: analyse apk_search.json and/or javascript function

<br><br><br><br><br><br>


<span id="update"></span>
<script>
    getLatestUpdate();
    async function getLatestUpdate() {
        const response = await fetch("https://arifhamed.com/_pages/resources/apk_search.json");
        const all_assets = await response.json();
        document.getElementById('update').innerHTML = "bruh: "+all_assets[4]["title"];
    }
</script>

<hr>

This text is to test if the thinkpad git credentials are functioning correctly
