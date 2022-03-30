---
title: "Projects"
layout: default
permalink: /resources/projects
redirect_from:
 - /resources/projects/
 - /projects 
 - /projects/
---

<!-- {% capture projects-md %}
{% include projects-inc.md %}
{% endcapture %}
{{ projects-md | markdownify }} -->

# Projects <span style="font-size:70%">by Arif Hamed</span>

I have a list of projects below that I have started and participated in. The first few are projects that originate from school.

**THIS PAGE IS STILL WIP**

{% for post in site.posts %}
  {% if post.url contains 'projects' %}
    <div class="project">
      {{ post.excerpt }}
      <div class="text-center"><a class="w-100" href="{{ site.baseurl }}{{ post.url }}">Read more...</a></div>
    </div>
  {% endif %}
{% endfor %}

{% include comments.html %}