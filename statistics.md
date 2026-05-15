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

  <p class="stats-note">
    This page keeps a tiny, aggregate headcount of where visitors come from, mostly so I can admire the map slowly waking up. No names, no IP addresses, no personal detective work; just country-level dots and a visit total.
  </p>

  
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
    const tinyCountries = {
      SG: { name: 'Singapore', coords: [1.3521, 103.8198] },
      HK: { name: 'Hong Kong', coords: [22.3193, 114.1694] },
      MO: { name: 'Macau', coords: [22.1987, 113.5439] },
      BH: { name: 'Bahrain', coords: [26.0667, 50.5577] },
      MT: { name: 'Malta', coords: [35.9375, 14.3754] },
      LU: { name: 'Luxembourg', coords: [49.8153, 6.1296] },
      AD: { name: 'Andorra', coords: [42.5063, 1.5218] },
      LI: { name: 'Liechtenstein', coords: [47.166, 9.5554] },
      MC: { name: 'Monaco', coords: [43.7384, 7.4246] },
      SM: { name: 'San Marino', coords: [43.9424, 12.4578] },
      VA: { name: 'Vatican City', coords: [41.9029, 12.4534] },
      MV: { name: 'Maldives', coords: [3.2028, 73.2207] },
      BN: { name: 'Brunei', coords: [4.5353, 114.7277] },
      QA: { name: 'Qatar', coords: [25.3548, 51.1839] }
    };
    const tinyCountryMarkers = Object.entries(tinyCountries)
      .filter(([code]) => Number(countryVisits[code] || 0) > 0)
      .map(([code, country]) => ({
        ...country,
        code,
        visits: Number(countryVisits[code] || 0)
      }));

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
        markers: tinyCountryMarkers,
        markerStyle: {
          initial: {
            r: 7,
            fill: rose,
            fillOpacity: 0.92,
            stroke: linen,
            strokeWidth: 2.4
          },
          hover: {
            fill: rose,
            stroke: ink,
            cursor: 'default'
          }
        },
        onRegionTooltipShow(event, tooltip, code) {
          const visits = countryVisits[code] || 0;
          tooltip.css({ color: ink, backgroundColor: linen, borderColor: rose });
          tooltip.text(`${tooltip.text()} · ${visits} visits`);
        },
        onMarkerTooltipShow(event, tooltip, index) {
          const marker = tinyCountryMarkers[index];
          if (!marker) return;
          tooltip.css({ color: ink, backgroundColor: linen, borderColor: rose });
          tooltip.text(`${marker.name} · ${marker.visits} visits`);
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
