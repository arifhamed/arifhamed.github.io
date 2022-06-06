---
title: HTML to Escape Code Sequence
layout: default
permalink: /resources/html-to-escape
---

# HTML to Escape Code Sequence

This was an idea that i had so that i don't have to keep on copying off from <a href="" target="_blank">other sources</a>, i'm just lazy so i got to work to make something to do it for me.

<div id="escape-table"></div>

## STILL WIP

<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/PapaParse/4.1.2/papaparse.js"></script>
<script>function arrayToTable(a){var r=$("<table></table>");return $(a).each(function(a,e){var t=$("<tr></tr>");$(e).each(function(a,e){t.append($("<td>"+e+"</td>"))}),r.append(t)}),r}$.ajax({type:"GET",url:"https://arifhamed.com/static/others/htmlescape.csv",success:function(a){$("#escape-table").append(arrayToTable(Papa.parse(a).data))}});</script>

globglogabgalab