Highcharts.chart('pie-chart', {
    chart: {
        type: 'pie',
        options3d: {
            enabled: true,
            alpha: 45,
            beta: 0
        }
    },
    credits: {
        enabled: false
    },
    title: {
        text: '% of Money Blocked and Unlocked'
    },
    accessibility: {
        point: {
            valueSuffix: '%'
        }
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}% : ${point.y:1f}</b>'
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            depth: 35,
            dataLabels: {
                enabled: true,
                format: '{point.name}'
            }
        }
    },
    series: [{
        type: 'pie',
        name: 'Amount',
        data: [
            ['Virtual Money', 123220],
          ['Real Money', 463730]
        ]
    }]
});

Highcharts.chart('expense-chart', {
    chart: {
        type: 'column'
    },
    title: {
        text: "Parent's Monthly Expense"
    },
    credits: {
        enabled: false
    },
    xAxis: {
        categories: [
            'Jan',
            'Feb',
            'Mar',
            'Apr',
            'May',
            'Jun',
            'Jul',
            'Aug',
            'Sep',
            'Oct',
            'Nov',
            'Dec'
        ],
        crosshair: true
    },
    yAxis: {
        min: 0,
        title: {
            text: 'Amount ($)'
        }
    },
    tooltip: {
        headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
        pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
            '<td style="padding:0"><b>${point.y:.1f}</b></td></tr>',
        footerFormat: '</table>',
        shared: true,
        useHTML: true
    },
    plotOptions: {
        column: {
            pointPadding: 0.2,
            borderWidth: 0
        }
    },
    series: [{
        name: 'Child1',
        data: [49.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4]

    }, {
        name: 'Child2',
        data: [83.6, 78.8, 98.5, 93.4, 106.0, 84.5, 105.0, 104.3, 91.2, 83.5, 106.6, 92.3]

    }]
});
// Create the chart
Highcharts.chart('bar-courses', {
    chart: {
        type: 'bar'
    },
    credits: {
        enabled: false
    },
    title: {
        text: 'Course Progress'
    },
    subtitle: {
        text: 'Click the columns to view module progress.'
    },
    accessibility: {
        announceNewData: {
            enabled: true
        }
    },
    xAxis: {
        type: 'category'
    },
    yAxis: {
        title: {
            text: 'Percent progress'
        }

    },
    legend: {
        enabled: false
    },
    plotOptions: {
        series: {
            borderWidth: 0,
            dataLabels: {
                enabled: true,
                format: '{point.y:.1f}%'
            }
        }
    },

    tooltip: {
        headerFormat: '<span style="font-size:11px">{series.name}</span><br>',
        pointFormat: '<span style="color:{point.color}">{point.name}</span>: <b>{point.y:.2f}%</b> of total<br/>'
    },

    series: [
        {
            name: "Children",
            colorByPoint: true,
            data: [
                {
                    name: "Child1",
                    y: 62.74,
                    drilldown: "Child1"
                },
                {
                    name: "Child2",
                    y: 10.57,
                    drilldown: "Child2"
                }
            ]
        }
    ],
    drilldown: {
        breadcrumbs: {
            position: {
                align: 'right'
            }
        },
        series: [
            {
                name: "Child1",
                id: "Child1",
                data: [
                    [
                        "Course1",
                        0.1
                    ],
                    [
                        "Course2",
                        1.3
                    ],
                    [
                        "Course3",
                        53.02
                    ]
                ]
            },
            {
                name: "Child2",
                id: "Child2",
                data: [
                    [
                        "Course1",
                        1.02
                    ],
                    [
                        "Course2",
                        7.36
                    ]
                ]
            }
        ]
    }
});

Highcharts.chart('line-chart', {

    title: {
        text: "Children Expenditure"
    },

    credits: {
        enabled: false
    },

    yAxis: {
        title: {
            text: 'Amount ($)'
        }
    },

    xAxis: {
        categories: [
            'Jan',
            'Feb',
            'Mar',
            'Apr',
            'May',
            'Jun',
            'Jul',
            'Aug',
            'Sep',
            'Oct',
            'Nov',
            'Dec'
        ],
        crosshair: true
    },

    legend: {
        layout: 'vertical',
        align: 'right',
        verticalAlign: 'middle'
    },

    plotOptions: {
        series: {
            label: {
                connectorAllowed: false
            }
        }
    },

    series: [{
        name: 'Child1',
        data: [439, 523, 177, 658, 831, 931, 733, 175, 567, 837, 264, 946]
    }, {
        name: 'Child2',
        data: [916, 564, 742, 251, 390, 382, 381, 434, 635, 256, 984, 645]
    }],

    responsive: {
        rules: [{
            condition: {
                maxWidth: 500
            },
            chartOptions: {
                legend: {
                    layout: 'horizontal',
                    align: 'center',
                    verticalAlign: 'bottom'
                }
            }
        }]
    }

});