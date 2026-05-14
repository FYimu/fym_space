---
layout: default
title: Travel Gallery
permalink: /travel/
active_nav: hobbies
---

<div class="section-header">
  <div class="section-eyebrow">Side Mission</div>
  <h1 class="section-title">Travelling</h1>
</div>

<a href="/#hobbies" class="back-btn">← Back to Side Missions </a>

<p class="gallery-intro">A visual journal of structural and natural design, capturing the geometry of the places I’ve wandered.</p>

<div class="gallery-grid">
  {% for item in site.data.travel_gallery %}
  <figure class="gallery-item">

    <img src="{{ '/assets/gallery/' | append: item.image | relative_url }}" alt="{{ item.caption }}">
    
    {% if item.caption %}
      <figcaption class="gallery-caption">{{ item.caption }}</figcaption>
    {% endif %}
    {% if item.date %}
      <figcaption class="update-date">{{ item.date }}</figcaption>
    {% endif %}
  </figure>
  {% endfor %}
</div>