---
layout: default
title: Home
---

<section id="about" class="section active">
  {% include pages/about.md %}
</section>


<section id="education" class="section">
  {{ include.content | capture: "edu_content" }}
  {% capture edu_md %}{% include pages/education.md %}{% endcapture %}
  {{ edu_md | markdownify }}
</section>

<section id="publications" class="section">
  {% capture pub_md %}{% include pages/publications.md %}{% endcapture %}
  {{ pub_md | markdownify }}
</section>

<section id="hobbies" class="section">
  {% capture hob_md %}{% include pages/hobbies.md %}{% endcapture %}
  {{ hob_md | markdownify }}
</section>

<section id="courses" class="section">
  {% capture course_md %}{% include pages/courses.md %}{% endcapture %}
  {{ course_md | markdownify }}
</section>

<section id="teaching" class="section">
  {% capture teach_md %}{% include pages/teaching.md %}{% endcapture %}
  {{ teach_md | markdownify }}
</section>