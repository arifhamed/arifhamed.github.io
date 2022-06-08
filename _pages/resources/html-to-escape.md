---
title: HTML to Escape Code Sequence
layout: default
permalink: /resources/html-to-escape
---

# HTML to Escape Code Sequence

This was an idea that i had so that i don't have to keep on copying off from <a href="" target="_blank">other sources</a>, i'm just lazy so i got to work to make something to do it for me.

<input id="input_raw" type="text" class="w-100" onkeyup="refreshOutput()">

<pre id="output_baked" class="w-100">Your output will appear here</pre>

<div id="escape-table"></div>

## STILL WIP

<script src="https://cdnjs.cloudflare.com/ajax/libs/PapaParse/4.1.2/papaparse.js"></script>
<!-- <script>function arrayToTable(a){var n=$("<table></table>");return $(a).each(function(a,e){var t=$("<tr></tr>");$(e).each(function(a,e){t.append($("<td><pre>"+e+"</pre></td>"))}),n.append(t)}),n}function refreshOutput(){var a=document.getElementById("input_raw").value;console.log(a)}$.ajax({type:"GET",url:"https://arifhamed.com/static/others/htmlescape.csv",success:function(a){$("#escape-table").append(arrayToTable(Papa.parse(a).data))}});</script> -->
<script></script>

---
---
---

<p>Select Application Family: <select id="app_family"></select>
<p>Select Application: <select id="app"></select>

<script>var data;$.ajax({type:"GET",url:"https://arifhamed.com/static/others/htmlescape.csv",success:data=Papa.parse(a).data}),(data=data.split("\n")).shift();for(var fields,families={},$family=$("#app_family"),$app=$("#app"),i=0;i<data.length;i++)data[i]&&(fields=data[i].split(","),families.hasOwnProperty(fields[0])||(families[fields[0]]=[],$family.append('<option value="'+fields[0]+'">'+fields[0]+"</option>")),families[fields[0]].push(fields[1]));function updateApp(){for(var a=families[$family.val()],i="",p=0;p<a.length;p++)i+='<option value="'+a[p]+'">'+a[p]+"</option>";$app.html(i)}updateApp(),$family.change(updateApp);</script>