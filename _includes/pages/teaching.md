<div class="section-header">
  <div class="section-eyebrow">Pedagogy</div>
  <h1 class="section-title">Teaching</h1>
</div>

{% assign teaching_items = site.teaching | sort: "order" %}
{% for item in teaching_items %}
<div class="teaching-item">
  <div class="teaching-code">{{ item.course_code }}</div>
  
  <div>
    <div class="teaching-title">{{ item.title }}</div>
    <div class="teaching-role">{{ item.role }}</div>
    <div class="teaching-desc">{{ item.content | markdownify }}</div>
    
    <ul class="teaching-semesters">
      {% for semester in item.semesters %}
        <li>{{ semester }}</li>
      {% endfor %}
    </ul>
  </div>
</div>
{% endfor %}
