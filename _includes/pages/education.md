<div class="section-header">
    <div class="section-eyebrow">Background</div>
    <h1 class="section-title">Education</h1>
  </div>

  <div class="pub-note"> * denotes expected graduation year </div>
  {% for edu in site.data.education %}
  <div class="edu-item">
    <div class="edu-year">{{ edu.year }}</div>
    <div>
      <div class="edu-degree">{{ edu.degree }}</div>
      <div class="edu-institution">{{ edu.institution }}</div>
      <div class="edu-desc">
        {% if edu.description %}
          <div>{{ edu.description | markdownify | remove: '<p>' | remove: '</p>' }}</div>
        {% endif %}

        {% if edu.advisor %}
          <div>Advisors: {{ edu.advisor | markdownify | remove: '<p>' | remove: '</p>'}}</div>
        {% endif %}
        
        {% if edu.courses %}
          <div>Relevant coursework: {{ edu.courses | markdownify | remove: '<p>' | remove: '</p>'}}</div>
        {% endif %}
      </div>
    </div>
  </div>
  {% endfor %}