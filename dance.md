---
layout: default
title: Dance Gallery
permalink: /hobbies/dance/
active_nav: hobbies
---

<div class="section-header">
  <div class="section-eyebrow">Side Mission</div>
  <h1 class="section-title">Dancing</h1>
</div>

<a href="{{ '/hobbies/' | relative_url }}" class="back-btn">← Back to Side Missions</a>

<p class="gallery-intro">A celebration of frames, feel, and footwork: documenting the expressive power of Latin and Ballroom dance.</p>

<div class="gallery-grid">
  {% for item in site.data.galleries.dance_gallery %}
  <figure class="gallery-item">

    <img src="{{ '/assets/gallery/' | append: item.image | relative_url }}" alt="{{ item.caption }}"{% if item.position %} style="object-position: {{ item.position }};"{% endif %}>
    
    {% if item.caption %}
      <figcaption class="gallery-caption">{{ item.caption }}</figcaption>
    {% endif %}
  </figure>
  {% endfor %}
</div>
