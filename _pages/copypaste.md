---
title: "my textual copy pastes"
permalink: /copypaste
layout: default
redirect_from:
 - /copypaste/
 - /copypasta
 - /copypasta/
---

for redacted text

``` html
<span class='disable-selection' ondblclick="this.innerHTML=''">&lt;<b>REDACTED</b>&gt;</span>
```

for getting latest release asset details from apk release

``` html
<span id="update"></span>
<script>
    getLatestUpdate();
    async function getLatestUpdate() {
        const response = await fetch("https://api.github.com/repos/arifhamed/arifhamed.github.io/releases/62234823/assets");
        const all_assets = await response.json();
        for (let i = 0; i < all_assets.length; i++){
        	console.log(all_assets[i]["name"]);
       		if (all_assets[i]["name"] == "{{ page.package }}"){
          		document.getElementById('update').innerHTML = "Downloads: "+all_assets[i]["download_count"]+"<br>Latest upload: "+all_assets[i]["updated_at"];
            }
        }
    }
</script>

```