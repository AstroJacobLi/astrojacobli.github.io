---
layout: page
title: Blog
permalink: /blog/
---
<h3><cite>All science is either physics or stamp collecting. -- Ernest Rutherford </cite></h3>

<ul class="listing">
{% for post in site.posts %}
  {% capture y %}{{post.date | date:"%Y"}}{% endcapture %}
  {% if year != y %}
    {% assign year = y %}
    <li class="listing-seperator">{{ y }}</li>
  {% endif %}
  <li class="listing-item">
    <time datetime="{{ post.date | date:"%Y-%m-%d" }}">{{ post.date | date:"%Y-%m-%d" }}</time>
    <a href="{{ post.url }}" title="{{ post.title }}">{{ post.title }}</a>
  </li>
{% endfor %}
</ul>

### Some of interesing posts can be found in my previous [**Homepage**](https://astrojacobli.github.io/Homepage/).