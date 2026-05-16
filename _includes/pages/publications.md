
<div class="section-header">
    <div class="section-eyebrow">Research</div>
    <h1 class="section-title">Publications</h1>
  </div>

<div class="pub-note"> † denotes equal contribution</div>
{% assign publication_topics = "Data Valuation|Data Selection|Incentives|Differential Privacy|Mechanism Design|Machine Unlearning" | split: "|" %}
<div class="pub-topic-filter" aria-label="Filter publications by topic">
  <button class="pub-topic-pill js-pub-topic active" type="button" data-topic="all">All</button>
  {% for topic in publication_topics %}
    <button class="pub-topic-pill js-pub-topic" type="button" data-topic="{{ topic | escape }}">{{ topic }}</button>
  {% endfor %}
</div>

{% assign publications = site.publications | sort: "order" %}
{% for pub in publications %}
  <div class="pub-item" id="{{ pub.slug }}" data-topics="{{ pub.topics | join: '|' | escape }}">
  <div class="pub-title">{% include utils/inline-markdown.html value=pub.title %}</div>
  <div class="pub-authors">{% include utils/inline-markdown.html value=pub.authors %}</div>
  <div class="pub-venue">{% include utils/inline-markdown.html value=pub.venue %}</div>
  {% if pub.topics %}
    <div class="pub-topics">
      {% for topic in pub.topics %}
        <button class="pub-topic-pill js-pub-topic" type="button" data-topic="{{ topic | escape }}">{{ topic }}</button>
      {% endfor %}
    </div>
  {% endif %}
  <div class="pub-links">
    <a class="pub-tag" href="{{ pub.pdf }}" target="_blank" rel="noopener noreferrer">PDF</a>
  </div>
</div>
{% endfor %}
