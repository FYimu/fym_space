---
layout: default
title: Life Notes
permalink: /hobbies/blog/
active_nav: hobbies
---

<div class="section-header">
  <div class="section-eyebrow">Side Mission</div>
  <h1 class="section-title">Life Notes</h1>
</div>

<a href="{{ '/hobbies/' | relative_url }}" class="back-btn">← Back to Side Missions</a>

{% assign life_posts = site.life_posts | sort: "date" | reverse %}
{% if life_posts.size > 0 %}
<div class="blog-list">
  {% for post in life_posts %}
  <a href="{{ post.url | relative_url }}" class="blog-card">
    {% if post.cover %}
      <img src="{{ post.cover | relative_url }}" alt="{{ post.title }}">
    {% endif %}
    <div class="blog-card-body">
      <div class="blog-date">{{ post.date | date: "%b %Y" }}</div>
      <div class="blog-title">{{ post.title }}</div>
      {% if post.summary %}
        <div class="blog-summary">{{ post.summary }}</div>
      {% endif %}
    </div>
  </a>
  {% endfor %}
</div>
{% else %}
<p class="gallery-intro">Notes coming soon.</p>
{% endif %}
