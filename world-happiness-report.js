document.addEventListener("DOMContentLoaded", function () {
    var viz1, viz2;

    // Visualization 1: Overall Happiness Scores
    var containerDiv1 = document.getElementById("tableauViz1"),
        url1 = "https://public.tableau.com/app/profile/colin.geraghty1705/viz/EUHasitis/Dashboard2?publish=yes";
    var options1 = {
        hideTabs: true,
        width: "100%",
        height: "600px",
        onFirstInteractive: function () {
            console.log("Viz 1 loaded successfully.");
        }
    };

    viz1 = new tableau.Viz(containerDiv1, url1, options1); // Creates the Tableau Viz in the specified container

    // Visualization 2: GDP vs Happiness
    var containerDiv2 = document.getElementById("tableauViz2"),
        url2 = "https://public.tableau.com/app/profile/colin.geraghty1705/viz/EUS_17272910513640/Dashboard3?publish=yes";
    var options2 = {
        hideTabs: true,
        width: "100%",
        height: "600px",
        onFirstInteractive: function () {
            console.log("Viz 2 loaded successfully.");
        }
    };

    viz2 = new tableau.Viz(containerDiv2, url2, options2); // Creates the Tableau Viz in the specified container
});
