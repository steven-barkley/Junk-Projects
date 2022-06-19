// Accordion code

var acc = document.getElementsByClassName("accordion");
var i;

for (i=0; i<acc.length; i++)
{
    acc[i].addEventListener("click", function() {
        /* Toggle between adding and removing the "active" class,
        to highlight the button that controls the panel */
        this.classList.toggle("active");

        /* Toggle between hiding and showing the active panel */
        var panel = this.nextElementSibling;
        if (panel.style.display === "block")
        {
            panel.style.display = "none";
        }
        else 
        {
            panel.style.display = "block";
        }
    });
}

/// End of Accordion code

// Load google charts 
google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawPieChart);

google.charts.load('current', {'packages':['bar']});
google.charts.setOnLoadCallback(drawBarChart);


// Draw the chart and set the chart values
function drawPieChart() {
    var data = google.visualization.arrayToDataTable([
        ['Activity', 'Hours per Day'],
        ['Eating', 2],
        ['Working', 8],
        ['Commuting',2],
        ['Reading', 0.5],
        ['Preening', 0.2],
        ['Sleeping', 4.5],
        ['Studying', 3],
        ['Entertaining',3.8]
    ]);

// Optional; add a title and set the width and height of the chart
var options = 
            {
                'title': 'My Daily Activity Data', 
                //is3D: true,
            };


// Display the chart inside the <div> element with id="piechart"
var chart = new google.visualization.PieChart(document.getElementById('piechart'));
chart.draw(data, options);
}

// Draw the chart and set the chart values
function drawBarChart() {
    var data = google.visualization.arrayToDataTable([
        ['Personality Trait', 'Percentile', 'Aspect-1','Aspect-2'],
        ['Openness to Experience', 57,67,44],
        ['Conscientiousness', 8, 8, 16],
        ['Extraversion', 34, 8, 73],
        ['Agreeableness', 43, 42, 45 ],
        ['Neuroticism', 53, 83, 21]
    ]);


// Optional; add a title and set the width and height of the chart
var options = 
            { 
                chart: 
                {
                'title': 'My Personality Data',
                'subtitle': 'The Big Five Aspects Scale', 
                },
            bars: 'horizontal' // Required for Material Bar Charts.    
            };

// Display the chart inside the <div> element with id="barchart"
var chart = new google.charts.Bar(document.getElementById('barchart'));

chart.draw(data, google.charts.Bar.convertOptions(options));
}


