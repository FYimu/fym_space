
<div class="section-header">
    <div class="section-eyebrow">Research</div>
    <h1 class="section-title">Publications</h1>
  </div>

<div class="pub-note"> † denotes equal contribution</div>
{% assign publications = site.publications | sort: "order" %}
{% for pub in publications %}
  <div class="pub-item" id="{{ pub.slug }}">
  <div class="pub-title">{% include utils/inline-markdown.html value=pub.title %}</div>
  <div class="pub-authors">{% include utils/inline-markdown.html value=pub.authors %}</div>
  <div class="pub-venue">{% include utils/inline-markdown.html value=pub.venue %}</div>
  <div class="pub-links">
    <a class="pub-tag" href="{{ pub.pdf }}" target="_blank" rel="noopener noreferrer">PDF</a>
  </div>
</div>
{% endfor %}
