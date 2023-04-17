<template>
    <div>

        <div class="chart2" v-show="chart != null">
            <h3 style="color: black; font-size: 21px;
                                                                        font-weight: 800;
                                                                        text-transform: capitalize;
                                                                        margin: 0;
                                                                        color: rgb(47 48 49);"> Hourly Forecast </h3>
            <canvas id="myChart"></canvas>
            <h1> {{ hourly.list.city.country }}</h1>
        </div>
        <div>
            <h1>Hello</h1>
        </div>
    </div>
</template>

<script>
import Chart from 'chart.js'
//import planetChartData from '../planet-data.js'


export default {

    props: ['hourly'],
    data() {
        return {
            chart: null,
            city: "tunis",
            dates: [],
            temps: [],
        }
    },
    mounted() {
        //  this.getData();
        console.log(this.hourly.list)
    },
    methods: {
        getData() {
            if (this.chart != null) {
                this.chart.destroy();
            }
            // console.log(response.data.list);
            this.dates = this.hourly.list.map(list => {
                return list.dt_txt;
            });

            this.temps = this.hourly.list.map(list => {
                return list.main.temp;
            });

            var ctx = document.getElementById("myChart");
            this.chart = new Chart(ctx, {
                type: "line",
                data: {
                    labels: this.dates,
                    datasets: [
                        {
                            label: "Avg. Temp",
                            backgroundColor: "#a3d8fc",
                            borderColor: "#5aa5f3",
                            borderWidth: 3,
                            data: this.temps
                        }
                    ]
                },
                options: {
                    title: {
                        display: true,
                        text: "Temperature per 3 hour"
                    },
                    tooltips: {
                        callbacks: {
                            label: function (tooltipItem, data) {
                                var label =
                                    data.datasets[tooltipItem.datasetIndex].label || "";

                                if (label) {
                                    label += ": ";
                                }

                                label += Math.floor(tooltipItem.yLabel);
                                return label + "°C";
                            }
                        }
                    },
                    scales: {
                        xAxes: [
                            {
                                type: "time",
                                time: {
                                    unit: "hour",
                                    displayFormats: {
                                        hour: "ddd hA"
                                    },
                                    tooltipFormat: "ddd hA"
                                },
                                scaleLabel: {
                                    display: true,
                                    labelString: "Time"
                                }
                            }
                        ],
                        yAxes: [
                            {
                                scaleLabel: {
                                    display: true,
                                    labelString: "Temperature (°C)"
                                },
                                ticks: {
                                    callback: function (value) {
                                        return value + "°C";
                                    }
                                }
                            }
                        ]
                    }
                }
            });

        }
    },
}
</script>
<style>
.chart2 {
    margin-top: 50px;
    padding: 10px;
    background-color: white;
    border-radius: 10px;
    margin-left: 3%;
    height: 460px;
    width: 90%;

}
</style>