// Utility function to check current page
function getCurrentPage() {
    const path = window.location.pathname;
    const page = path.split("/").pop(); // Get the last part of the path (e.g., 'eugenic-beginnings.html')
    return page;
}

/**
 * Eugenic Beginnings Page Logic
 */
if (getCurrentPage() === 'eugenic-beginnings.html') {
    // Function to create the genealogical tree visualization
    function createGenealogicalTree() {
        const data = {
            name: "Francis Galton",
            children: [
                { 
                    name: "Karl Pearson", 
                    children: [
                        { name: "Correlation Coefficient", description: "A measure of linear relationship between two variables." },
                        { name: "Regression", description: "A method to model and analyze relationships between variables." }
                    ]
                },
                { 
                    name: "Ronald Fisher", 
                    children: [
                        { name: "ANOVA", description: "Analysis of variance, used to compare means across groups." },
                        { name: "Maximum Likelihood", description: "A method for estimating parameters of a statistical model." }
                    ]
                }
            ]
        };

        const svg = d3.select("svg"),
            width = +svg.attr("width"),
            height = +svg.attr("height");

        const root = d3.hierarchy(data);
        const treeLayout = d3.tree().size([width - 100, height - 100]);

        treeLayout(root);

        const g = svg.append("g").attr("transform", "translate(50,50)");

        // Add links between nodes
        g.selectAll(".link")
            .data(root.links())
            .enter()
            .append("line")
            .attr("class", "link")
            .attr("x1", d => d.source.x)
            .attr("y1", d => d.source.y)
            .attr("x2", d => d.target.x)
            .attr("y2", d => d.target.y)
            .attr("stroke", "#001f3f");

        // Add nodes (circles)
        g.selectAll(".node")
            .data(root.descendants())
            .enter()
            .append("circle")
            .attr("class", "node")
            .attr("cx", d => d.x)
            .attr("cy", d => d.y)
            .attr("r", 10)
            .attr("fill", "#28a745")
            .on("mouseover", handleMouseOver)  // Add event listener for hover
            .on("mouseout", handleMouseOut);   // Remove tooltip on mouseout

        // Add labels to the nodes
        g.selectAll(".label")
            .data(root.descendants())
            .enter()
            .append("text")
            .attr("class", "label")
            .attr("x", d => d.x)
            .attr("y", d => d.y - 15)
            .attr("text-anchor", "middle")
            .text(d => d.data.name);

        // Tooltip container
        const tooltip = d3.select("body").append("div")
            .attr("class", "tooltip")
            .style("position", "absolute")
            .style("visibility", "hidden")
            .style("background", "#f4f4f4")
            .style("border", "1px solid #333")
            .style("padding", "8px")
            .style("border-radius", "5px");

        // Function to handle mouseover event
        function handleMouseOver(event, d) {
            tooltip.html(d.data.description || "No additional information")
                .style("top", `${event.pageY - 10}px`)
                .style("left", `${event.pageX + 10}px`)
                .style("visibility", "visible");
        }

        // Function to handle mouseout event
        function handleMouseOut() {
            tooltip.style("visibility", "hidden");
        }
    }

    createGenealogicalTree();
}

/**
 * Slider Code for a Different Page (e.g., subjective.html)
 */
if (getCurrentPage() === 'subjective.html') {
    // Select the sliders
    const raceSlider = document.getElementById('race-bias');
    const classSlider = document.getElementById('class-bias');
    const genderSlider = document.getElementById('gender-bias');

    // Ensure sliders exist before adding event listeners
    if (raceSlider && classSlider && genderSlider) {
        // Update slider values in real-time
        raceSlider.oninput = function() {
            document.getElementById('race-bias-value').innerText = raceSlider.value;
            updateHistogram();
        };

        classSlider.oninput = function() {
            document.getElementById('class-bias-value').innerText = classSlider.value;
            updateHistogram();
        };

        genderSlider.oninput = function() {
            document.getElementById('gender-bias-value').innerText = genderSlider.value;
            updateHistogram();
        };

        // Function to update the histogram based on biases
        function updateHistogram() {
            const raceBias = parseInt(raceSlider.value);
            const classBias = parseInt(classSlider.value);
            const genderBias = parseInt(genderSlider.value);

            const modifiedData = data.map(d => {
                let bias = 0;
                if (d.group === 'Group A') bias = raceBias;
                if (d.group === 'Group B') bias = classBias;
                if (d.group === 'Group C') bias = genderBias;
                return { group: d.group, value: d.value + bias };
            });

            const bars = svg.selectAll("rect")
                .data(modifiedData);

            // Add new bars
            bars.enter().append("rect")
                .merge(bars)
                .attr("x", d => xScale(d.group))
                .attr("y", d => yScale(d.value))
                .attr("width", xScale.bandwidth())
                .attr("height", d => 400 - yScale(d.value))
                .attr("fill", "#001f3f");

            // Remove old bars
            bars.exit().remove();
        }
    }
}

