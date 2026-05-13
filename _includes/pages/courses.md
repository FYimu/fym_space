<div class="section-header">
    <div class="section-eyebrow">Academic Journey</div>
    <h1 class="section-title">Courses</h1>
  </div>

  <div id="courses-list">
    <h3 class="course-subhead">Graduate</h3>
    <div class="courses-grid">
      {% assign grad_courses = site.data.courses | where: "level", "graduate" %}
      {% for course in grad_courses %}
      <div class="course-card" data-course="{{ course.id }}">
        <div class="dot"></div>
        <div class="course-code">{{ course.code }}</div>
        <div class="course-name">{{ course.name }}</div>
        <div class="course-term">{{ course.term }}</div>
        <span class="course-arrow">→</span>
      </div>
      {% endfor %}
    </div>

    <h3 class="course-subhead">Undergraduate</h3>
    <div class="courses-grid">
      {% assign undergrad_courses = site.data.courses | where: "level", "undergraduate" %}
      {% for course in undergrad_courses %}
      <div class="course-card" data-course="{{ course.id }}">
        <div class="dot"></div>
        <div class="course-code">{{ course.code }}</div>
        <div class="course-name">{{ course.name }}</div>
        <div class="course-term">{{ course.term }}</div>
        <span class="course-arrow">→</span>
      </div>
      {% endfor %}
    </div>
  </div>

  <div id="course-review-panel" class="course-review-panel">
    <div class="back-btn" id="back-btn">← Back to Courses</div>
    <div class="review-header">
      <div class="course-code" id="rv-code"></div>
      <div class="review-title" id="rv-name"></div>
      <div class="review-meta" id="rv-meta"></div>
      <div class ="review-grade" id='rv-grade'></div>
    </div>
    <div class="review-rating">
      <div class="rating-item"><span class="rating-label">Difficulty</span><span class="rating-value" id="rv-diff"></span></div>
      <div class="rating-item"><span class="rating-label">Enjoyment</span><span class="rating-value" id="rv-enjoy"></span></div>
      <div class="rating-item"><span class="rating-label">Usefulness</span><span class="rating-value" id="rv-useful"></span></div>
    </div>
    <div class="review-section"><h3>Overview</h3><p id="rv-overview"></p></div>
    <div class="review-section"><h3>Assessment</h3><p id="rv-assessment"></p></div>
  </div>