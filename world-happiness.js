<script type="text/javascript">
var viz1, viz2;

// Visualization 1: Overall Happiness Scores
var containerDiv1 = document.getElementById("tableauViz1"),
    url1 = "https://public.tableau.com/app/profile/colin.geraghty1705/viz/EUHasitis/Dashboard2?publish=yes"; // Replace with your actual URL for Viz 1

var options1 = {
    width: "100%",
    height: "600px",
    hideTabs: true,
    onFirstInteractive: function () {
        console.log("Viz 1 loaded successfully.");
    }
};

// Initialize viz1
if (containerDiv1) {
    viz1 = new tableau.Viz(containerDiv1, url1, options1);
}

// Visualization 2: GDP vs Happiness
var containerDiv2 = document.getElementById("tableauViz2"),
    url2 = "https://public.tableau.com/app/profile/colin.geraghty1705/viz/EUS_17272910513640/Dashboard3?publish=yes"; // Replace with your actual URL for Viz 2

var options2 = {
    width: "100%",
    height: "600px",
    hideTabs: true,
    onFirstInteractive: function () {
        console.log("Viz 2 loaded successfully.");
    }
};

// Initialize viz2
if (containerDiv2) {
    viz2 = new tableau.Viz(containerDiv2, url2, options2);
}
</script>
