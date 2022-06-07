---
title: HTML to Escape Code Sequence
layout: default
permalink: /resources/html-to-escape
---

# HTML to Escape Code Sequence

This was an idea that i had so that i don't have to keep on copying off from <a href="" target="_blank">other sources</a>, i'm just lazy so i got to work to make something to do it for me.

<input id="input_raw" type="text" class="w-100" onkeyup="refreshOutput()">

<div id="escape-table"></div>

## STILL WIP

<script src="https://cdnjs.cloudflare.com/ajax/libs/PapaParse/4.1.2/papaparse.js"></script>
<script>function arrayToTable(a){var n=$("<table></table>");return $(a).each(function(a,e){var t=$("<tr></tr>");$(e).each(function(a,e){t.append($("<td><pre>"+e+"</pre></td>"))}),n.append(t)}),n}function refreshOutput(){var a=document.getElementById("input_raw").value;console.log(a)}$.ajax({type:"GET",url:"https://arifhamed.com/static/others/htmlescape.csv",success:function(a){$("#escape-table").append(arrayToTable(Papa.parse(a).data))}});</script>
