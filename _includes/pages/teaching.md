<div class="section-header">
  <div class="section-eyebrow">Pedagogy</div>
  <h1 class="section-title">Teaching</h1>
</div>

{% for item in site.data.teaching %}
<div class="teaching-item">
  <div class="teaching-code">{{ item.course_code }}</div>
  
  <div>
    <div class="teaching-title">{{ item.title }}</div>
    <div class="teaching-role">{{ item.role }}</div>
    <div class="teaching-desc">{{ item.description | markdownify }}</div>
    
    <ul class="teaching-semesters">
      {% for semester in item.semesters %}
        <li>{{ semester }}</li>
      {% endfor %}
    </ul>
  </div>
</div>
{% endfor %}