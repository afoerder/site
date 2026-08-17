const cv = document.querySelector('.site-field');
if (cv) {
  const ctx = cv.getContext('2d');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const dpr = Math.min(devicePixelRatio || 1, 2);
  let W = 0, H = 0, pts = [], vel = [], V = null;

  try {
    const m = await import('https://cdn.jsdelivr.net/npm/d3-delaunay@6/+esm');
    V = m.Delaunay;
  } catch (e) { V = null; }

  function seed() {
    W = innerWidth; H = innerHeight;
    cv.width = W * dpr; cv.height = H * dpr;
    cv.style.width = W + 'px'; cv.style.height = H + 'px';
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    const n = Math.max(60, Math.round(W * H / 13000));
    pts = []; vel = [];
    for (let i = 0; i < n; i++) {
      pts.push([Math.random() * W, Math.random() * H]);
      vel.push([(Math.random() - 0.5) * 0.12, (Math.random() - 0.5) * 0.12]);
    }
  }

  function drawVoronoi() {
    const d = V.from(pts), v = d.voronoi([0, 0, W, H]);
    ctx.lineWidth = 1;
    ctx.strokeStyle = 'rgba(63,208,124,0.16)';
    ctx.beginPath(); v.render(ctx); ctx.stroke();
    const cc = v.circumcenters;
    for (let i = 0; i < cc.length; i += 2) {
      const x = cc[i], y = cc[i + 1];
      if (x < 0 || y < 0 || x > W || y > H) continue;
      const hot = (i / 2) % 13 === 0;
      ctx.fillStyle = hot ? 'rgba(224,138,50,0.75)' : 'rgba(63,208,124,0.30)';
      ctx.beginPath(); ctx.arc(x, y, hot ? 2 : 1.1, 0, 6.2832); ctx.fill();
    }
  }

  function drawFallback() {
    ctx.lineWidth = 1;
    ctx.strokeStyle = 'rgba(63,208,124,0.13)';
    ctx.beginPath();
    for (let i = 0; i < pts.length; i++) {
      const d = [];
      for (let j = 0; j < pts.length; j++) {
        if (i === j) continue;
        const dx = pts[i][0] - pts[j][0], dy = pts[i][1] - pts[j][1];
        d.push([dx * dx + dy * dy, j]);
      }
      d.sort((a, b) => a[0] - b[0]);
      for (let k = 0; k < 3; k++) {
        ctx.moveTo(pts[i][0], pts[i][1]);
        ctx.lineTo(pts[d[k][1]][0], pts[d[k][1]][1]);
      }
    }
    ctx.stroke();
    for (let i = 0; i < pts.length; i++) {
      const hot = i % 13 === 0;
      ctx.fillStyle = hot ? 'rgba(224,138,50,0.75)' : 'rgba(63,208,124,0.30)';
      ctx.beginPath(); ctx.arc(pts[i][0], pts[i][1], hot ? 2 : 1.1, 0, 6.2832); ctx.fill();
    }
  }

  function draw() { ctx.clearRect(0, 0, W, H); V ? drawVoronoi() : drawFallback(); }

  function step() {
    for (let i = 0; i < pts.length; i++) {
      pts[i][0] += vel[i][0]; pts[i][1] += vel[i][1];
      if (pts[i][0] < 0 || pts[i][0] > W) vel[i][0] *= -1;
      if (pts[i][1] < 0 || pts[i][1] > H) vel[i][1] *= -1;
    }
    draw();
    requestAnimationFrame(step);
  }

  seed(); draw();
  if (!reduce) requestAnimationFrame(step);
  let t;
  addEventListener('resize', () => { clearTimeout(t); t = setTimeout(() => { seed(); draw(); }, 200); });
}
