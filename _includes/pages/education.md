<div class="section-header">
    <div class="section-eyebrow">Background</div>
    <h1 class="section-title">Education</h1>
  </div>

  <div class="pub-note"> * denotes expected graduation year </div>
  {% assign education_items = site.education | sort: "order" %}
  {% for edu in education_items %}
  <div class="edu-item">
    <div class="edu-year">{{ edu.year }}</div>
    <div>
      <div class="edu-degree">{% include utils/inline-markdown.html value=edu.degree %}</div>
      <div class="edu-institution">{{ edu.institution }}</div>
      <div class="edu-desc">
        {% if edu.content %}
          <div>{% include utils/inline-markdown.html value=edu.content %}</div>
        {% endif %}

        {% if edu.advisor %}
          <div>Advisors: {% include utils/inline-markdown.html value=edu.advisor %}</div>
        {% endif %}
        
        {% if edu.courses %}
          <div>Relevant coursework: {% include utils/inline-markdown.html value=edu.courses %}</div>
        {% endif %}
      </div>
    </div>
  </div>
  {% endfor %}
