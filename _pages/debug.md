---
title: "Debug"
layout: default
permalink: /debug
---
# you're not supposed be here
this is where i do random stuff before publishing

<!-- <iframe width="1066" height="483" src="https://www.youtube.com/embed/O8ClOsE8ihA?rel=0&modestbranding=1&autohide=1&showinfo=0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> -->

Current test: testing apk_search.json, found [here](https://arifhamed.com/_pages/resources/apk_search.json)

Hypothesis: The span element, identified as "update", will get updated with the text "Crying Suns".

Good result tasks: Proceed to implement search in /resources/apk

Bas result tasks: analyse apk_search.json and/or javascript function

<span id="update"></span>
<script>
    getLatestUpdate();
    async function getLatestUpdate() {
        const response = await fetch("https://arifhamed.com/_pages/resources/apk_search.json");
        const all_assets = await response.json();
        // for (let i = 0; i < all_assets.length; i++){
        // 	console.log(all_assets[i]["name"]);
       	// 	if (all_assets[i]["name"] == ""){
        //   		document.getElementById('update').innerHTML = "Downloads: "+all_assets[i]["download_count"]+"<br>Latest upload: "+all_assets[i]["updated_at"];
        //     }
        // }
        document.getElementById('update').innerHTML = "bruh: "+all_assets[2]["title"];
    }
</script>