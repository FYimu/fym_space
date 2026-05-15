---
layout: default
title: Statistics
permalink: /statistics/
active_nav: statistics
---

{% assign stats = site.data.statistics %}

<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/jsvectormap@1.7.0/dist/jsvectormap.min.css">

<div class="section-header">
  <div class="section-eyebrow">Footprints</div>
  <h1 class="section-title">Statistics</h1>
</div>

<div class="stats-wrap">
  <div id="stats-country-map" class="stats-map" aria-label="Website visits by country">
    <p class="stats-map-fallback">Loading map...</p>
  </div>

  <p class="stats-total">Thanks for lighting up your country on the map!</p>
</div>

<script>
  window.websiteStats = {
    total: {{ stats.total_visits | jsonify }},
    countries: {{ stats.countries | jsonify }}
  };
</script>
<script src="https://cdn.jsdelivr.net/npm/jsvectormap@1.7.0/dist/jsvectormap.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/jsvectormap@1.7.0/dist/maps/world.js"></script>
<script>
  document.addEventListener('DOMContentLoaded', () => {
    const target = document.querySelector('#stats-country-map');
    if (!target) return;
    const showMapFallback = () => {
      target.innerHTML = '<p class="stats-map-fallback">Map unavailable</p>';
      target.classList.add('is-unavailable');
    };

    if (!window.jsVectorMap) {
      showMapFallback();
      return;
    }

    const styles = getComputedStyle(document.documentElement);
    const rose = styles.getPropertyValue('--rose').trim();
    const roseLight = styles.getPropertyValue('--rose-light').trim();
    const linen = styles.getPropertyValue('--linen').trim();
    const ink = styles.getPropertyValue('--ink').trim();
    const countryVisits = window.websiteStats.countries || {};

    try {
      target.innerHTML = '';

      new jsVectorMap({
        selector: '#stats-country-map',
        map: 'world',
        backgroundColor: 'transparent',
        zoomButtons: false,
        zoomOnScroll: false,
        regionStyle: {
          initial: {
            fill: roseLight,
            fillOpacity: 0.35,
            stroke: linen,
            strokeWidth: 0.5
          },
          hover: {
            fill: rose,
            fillOpacity: 0.86,
            cursor: 'default'
          }
        },
        series: {
          regions: [{
            values: countryVisits,
            scale: [roseLight, rose],
            normalizeFunction: 'polynomial'
          }]
        },
        onRegionTooltipShow(event, tooltip, code) {
          const visits = countryVisits[code] || 0;
          tooltip.css({ color: ink, backgroundColor: linen, borderColor: rose });
          tooltip.text(`${tooltip.text()} · ${visits} visits`);
        }
      });
    } catch (error) {
      console.error('Could not load statistics map:', error);
      showMapFallback();
      return;
    }

    document.querySelectorAll('.jvm-region').forEach((region) => {
      region.style.transition = 'fill 0.2s, fill-opacity 0.2s';
    });
  });
</script>
