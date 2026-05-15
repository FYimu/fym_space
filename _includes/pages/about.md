<div class="section-header">
    <div class="section-eyebrow">Introduction</div>
    <h1 class="section-title">About Me</h1>
  </div>

  <div class="about-grid">
    <div class="about-text">
      <p>
        Hi, Fan Jue (范珏) here! I am a CS PhD student in School of Computing at National University of Singapore (NUS). I am very fortunate to be advised by Prof. {{ site.data.profile.people.bryan }} and Dr. {{ site.data.profile.people.nancy }}. My research primarily focuses on data-efficient AI and answering the question: <em>how much is the data worth?</em>
      </p>

      <p>
        Before my doctoral studies, I completed my undergraduate studies at NUS (too), where I obtained a Bachelor of Science (Highest Distinction) degree in Applied Mathematics and a Bachelor of Computing (Highest Distinction) degree in Computer Science. I started my journey in research during Undergraduate Research Opportunities Programme (UROP) and continued in my Final Year Project (FYP). My FYP thesis was supervised by Prof. {{ site.data.profile.people.bryan }} and Prof. {{ site.data.profile.people.jonathan }} and in collaboration with Dr. {{ site.data.profile.people.rachael }} and {{ site.data.profile.people.tx }}.
      </p>

      <p>
        Research keeps my head in the clouds; traveling and dancing keep my feet on the ground (and occasionally off it), see <a href="{{ '/hobbies/' | relative_url }}" class="about-nav"><strong>SIDE MISSIONS</strong></a>.
      </p>
    </div>

    <div class="about-photo">
        <img src="{{ '/assets/gallery/me.jpg' | relative_url }}" alt="PHOTO">
    </div>
  </div>

  <div class="about-info">
        <span class="label">Position</span>
        <span class="value">PhD Student, 2025 Spring</span>
        <span class="label">Institution</span>
        <span class="value">National University of Singapore</span>
        <span class="label">Location</span>
        <span class="value">Singapore</span>
        <span class="label">Interests</span>
        <span class="value">Data-Efficient AI, Trustworthy AI</span>
      </div>


<div class="updates-container">
  <div class="updates-header">Latest Updates</div>
  <ul class="updates-list" id="updates-list">
    {% assign updates = site.updates | sort: "order" %}
    {% for update in updates %}
    <li class="update-item {% if forloop.index > 10 %}is-collapsed{% endif %}">
      <span class="update-date">{{ update.date_label }}</span>
      <span class="update-text">
        {% include utils/inline-markdown.html value=update.content %}
        {% if update.link %}
          <a href="{{ update.link | relative_url }}{% if update.paper_id %}#{{ update.paper_id }}{% endif %}" class="update-arrow-link js-update-link">→</a>
        {% endif %}
      </span>
    </li>
    {% endfor %}
  </ul>

  {% if updates.size > 10 %}
    <button id="toggle-updates-btn" class="updates-toggle">
      Show More
    </button>
  {% endif %}
</div>

<footer class="about-footer">
  <div>© {{ 'now' | date: "%Y" }} {{ 'FAN JUE' }}</div>
  <a href="{{ '/statistics/' | relative_url }}">Statistics</a>
</footer>
