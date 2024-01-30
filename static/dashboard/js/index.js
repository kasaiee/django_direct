$((function () {
  var o = document.getElementById("chartBar1")
  new Chart(o, {
    type: "bar",
    data: {
      labels: ["اسفند", "بهمن", "دی", "آذر", "آبان", "مهر", "تیر"],
      datasets: [{
        label: "داده 1",
        data: [65, 59, 80, 81, 56, 55, 40],
        borderColor: "#6259ca",
        borderWidth: "0",
        backgroundColor: "#6259ca"
      }, {
        label: "داده ها2",
        data: [28, 48, 40, 19, 86, 27, 90],
        borderColor: "#53caed",
        borderWidth: "0",
        backgroundColor: "#53caed"
      }]
    },
    options: {
      responsive: !0,
      maintainAspectRatio: !1,
      scales: {
        xAxes: [{
          ticks: { fontColor: "#77778e" },
          gridLines: { color: "rgba(119, 119, 142, 0.2)" }
        }],
        yAxes: [{
          ticks: { beginAtZero: !0, fontColor: "#77778e" },
          gridLines: { color: "rgba(119, 119, 142, 0.2)" }
        }]
      },
      legend: { labels: { fontColor: "#77778e" } }
    }
  });
}));
