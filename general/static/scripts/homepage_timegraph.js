$(document).ready(loadChart);

async function loadChart() {
    await getJobsDatabaseStatistics()
        .then(r => {
            if (r == undefined ||
                r.data == undefined ||
                r.data.length == 0) {
                return;
            }
            labels = [];
            totalJobs = [];
            activeJobs = [];
            expiredJobs = [];
            for (item of r.data){
                labels.push(new Date(item.time).toISOString().split('T')[0].slice(5));
                totalJobs.push(item.total);
                activeJobs.push(item.active);
                expiredJobs.push(item.expired);
            }

            // Get the context of the canvas element
            const ctx = document.getElementById('jobDatabaseStatistics').getContext('2d');

            // Chart configuration
            const config = {
                type: 'line',
                data: {
                    labels: labels, // Dates (MM-DD)
                    datasets: [
                        {
                            label: 'Total Jobs',
                            data: totalJobs, // Generated total jobs data
                            fill: true,
                            backgroundColor: 'rgba(100, 100, 255, 0.2)', // Light blue with 20% opacity
                            borderColor: 'rgba(100, 100, 255, 1)', // Solid blue for the line
                            borderWidth: 1,
                            tension: 0.1,
                            order: 1, // Total jobs in the background
                        },
                        {
                            label: 'Active Jobs',
                            data: activeJobs, // Generated active jobs data
                            fill: true,
                            backgroundColor: 'rgba(255, 165, 0, 0.5)', // Bright orange with 50% opacity
                            borderColor: 'rgba(255, 165, 0, 1)', // Bright orange for the line
                            borderWidth: 1,
                            tension: 0.1,
                            order: 2, // Active jobs in the middle
                        },
                        {
                            label: 'Expired Jobs',
                            data: expiredJobs, // Generated expired jobs data
                            fill: true,
                            backgroundColor: 'rgba(255, 99, 132, 0.5)', // Bright red with 50% opacity
                            borderColor: 'rgba(255, 99, 132, 1)', // Bright red for the line
                            borderWidth: 1,
                            tension: 0.1,
                            order: 3, // Expired jobs in the front
                        }
                    ]
                },
                options: {
                    scales: {
                        x: {
                            type: 'category', // Category scale for the x-axis
                            title: {
                                display: true,
                                text: 'Date',
                                color: '#ffcc00', // Bright yellow for x-axis title
                                font: {
                                    size: 14,
                                    weight: 'bold'
                                }
                            },
                            ticks: {
                                color: '#33cc33', // Bright green for x-axis labels
                                font: {
                                    size: 12,
                                    weight: 'bold'
                                }
                            }
                        },
                        y: {
                            beginAtZero: true,
                            title: {
                                display: true,
                                text: 'Number of Jobs',
                                color: '#ffcc00', // Bright yellow for y-axis title
                                font: {
                                    size: 14,
                                    weight: 'bold'
                                }
                            },
                            ticks: {
                                color: '#33cc33', // Bright green for y-axis labels
                                font: {
                                    size: 12,
                                    weight: 'bold'
                                }
                            }
                        }
                    },
                    plugins: {
                        title: {
                            display: true,
                            text: 'Job Database',
                            color: '#ff6600', // Bright orange for the title
                            font: {
                                size: 24, // Larger font size for the title
                                weight: 'bold',
                                family: 'Trebuchet MS', // Custom font family
                            }
                        }
                    },
                },
            };

            // Create the chart
            const mainStatisticsJobDatabase = new Chart(ctx, config);
            $(mainStatisticsJobDatabase).on('slid.bs.carousel', () => {
                mainStatisticsJobDatabase.resize();
            });
        });
}