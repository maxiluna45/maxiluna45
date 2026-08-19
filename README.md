# SANITIZATION PROBE

## TEST 1: <style> block with keyframes
<style>
@keyframes blinktest { 0%,100%{opacity:1} 50%{opacity:0} }
.blinker { animation: blinktest 1s steps(1) infinite; color: red; }
</style>
<span class="blinker">[IF YOU SEE THIS BLINKING, STYLE BLOCKS SURVIVE]</span>

## TEST 2: inline style attribute (display:grid)
<div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;border:1px solid #333;padding:8px;font-family:monospace;">
  <div style="border:1px solid #555;padding:6px;">cell A</div>
  <div style="border:1px solid #555;padding:6px;">cell B</div>
</div>

## TEST 3: SMIL animation in inline SVG (rotating rect)
<svg width="60" height="60" viewBox="0 0 60 60" xmlns="http://www.w3.org/2000/svg">
  <rect x="25" y="5" width="10" height="25" fill="#000">
    <animateTransform attributeName="transform" type="rotate" from="0 30 30" to="360 30 30" dur="2s" repeatCount="indefinite"/>
  </rect>
  <circle cx="30" cy="30" r="3" fill="#000"/>
</svg>

## TEST 4: pixel-art SVG (crispEdges)
<svg width="40" height="40" viewBox="0 0 8 8" shape-rendering="crispEdges" xmlns="http://www.w3.org/2000/svg">
  <rect x="1" y="1" width="6" height="6" fill="#000"/>
  <rect x="2" y="2" width="2" height="2" fill="#fff"/>
  <rect x="4" y="2" width="2" height="2" fill="#fff"/>
</svg>

## TEST 5: img referencing local SVG
<img src="./probe.svg" width="60" height="60" alt="probe">

## TEST 6: script (should be stripped)
<script>document.body.style.background='red'</script>

## TEST 7: table
<table>
  <tr><td style="border:1px solid #333;padding:4px;">t1</td><td style="border:1px solid #333;padding:4px;">t2</td></tr>
</table>
