document.addEventListener('DOMContentLoaded', () => {
  const enter = document.getElementById("enter");
  const distros = document.getElementById("distros");
  const trialsEl = document.getElementById("trials");
  const probEl = document.getElementById("success_rate");

  const mean = document.getElementById("mean");
  const variance = document.getElementById("variance");
  const stddev = document.getElementById("standard_deviation");
  const mgf = document.getElementById("moment_generating_function");
  const pmfCanvas = document.getElementById("pmf");
  const cdfCanvas = document.getElementById("cmf");

  let pmfChart = null;
  let cdfChart = null;

  enter.addEventListener("click", async (e) => {
    e.preventDefault();

    const distro = distros.value.toLowerCase();
    p = parseFloat(probEl.value);
    const trials = parseInt(trialsEl.value);
    if (p == 1){
        //will be fixed on backend
        p = 1.000001
    }

    const response = await fetch(`/${distro}/${p}/${trials}`);
    const data = await response.json();

    mean.textContent = `Mean: ${data.mean}`;
    variance.textContent = `Variance: ${data.variance}`;
    stddev.textContent = `Standard Deviation: ${data.stddev}`;
    mgf.textContent = `Moment Generating Function: ${data.mgf}`;

    drawCharts(data.pmf, data.cdf);
  });

  function drawCharts(pmf, cdf) {
    const pmfCtx = pmfCanvas.getContext('2d');
    const cdfCtx = cdfCanvas.getContext('2d');

    const normalize = obj => {
      const keys = Object.keys(obj).sort((a,b)=>a-b);
      return { labels: keys, values: keys.map(k => obj[k]) };
    };

    const pmfData = normalize(pmf);
    const cdfData = normalize(cdf);

    if (pmfChart) pmfChart.destroy();
    if (cdfChart) cdfChart.destroy();

    pmfChart = new Chart(pmfCtx, {
      type: 'bar',
      data: {
        labels: pmfData.labels,
        datasets: [{ label: 'PMF', data: pmfData.values, borderColor: 'blue', borderWidth: 2 }]
      },
      options: { scales: { y: { beginAtZero: true } } }
    });

    cdfChart = new Chart(cdfCtx, {
      type: 'bar',
      data: {
        labels: cdfData.labels,
        datasets: [{ label: 'CDF', data: cdfData.values, borderColor: 'green', borderWidth: 2 }]
      },
      options: { scales: { y: { beginAtZero: true } } }
    });
  }
});
