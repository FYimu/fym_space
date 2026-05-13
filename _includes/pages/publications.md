
<div class="section-header">
    <div class="section-eyebrow">Research</div>
    <h1 class="section-title">Publications</h1>
  </div>

<div class="pub-note"> † denotes equal contribution</div>
{% for pub in site.data.publications %}
  <div class="pub-item" id="{{ pub.id }}">
  <div class="pub-title">{{ pub.title | markdownify | remove: '<p>' | remove: '</p>'}}</div>
  <div class="pub-authors">{{ pub.authors | markdownify | remove: '<p>' | remove: '</p>'}}</div>
  <div class="pub-venue">{{ pub.venue | markdownify | remove: '<p>' | remove: '</p>'}}</div>
  <div class="pub-links">
    <a class="pub-tag" href="{{ pub.pdf }}" target="_blank" rel="noopener noreferrer">PDF</a>
  </div>
</div>
{% endfor %}