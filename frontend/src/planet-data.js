export const planetChartData = {
    type: "line",
    data: {
        labels: ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"],
        datasets: [
            {
                label: "Number of Moons",
                data: [0, 0, 1, 2, 79, 82, 27, 14],
                backgroundColor: "rgba(54,73,93,.5)",
                borderColor: "#36495d",
                borderWidth: 3
            },
            {
                label: "Planetary Mass (relative to the Sun x 10^-6)",
                data: [0.166, 2.081, 3.003, 0.323, 954.792, 285.886, 43.662, 51.514],
                backgroundColor: "#5aa5f3",
                borderColor: "#5aa5f3",
                borderWidth: 3
            }
        ]
    },
    options: {
        responsive: true,
        lineTension: 1,
        scales: {
            yAxes: [
                {
                    ticks: {
                        beginAtZero: true,
                        padding: 25
                    }
                }
            ]
        }
    }
};

export default planetChartData;