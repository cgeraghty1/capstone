// Function to create the genealogical tree visualization
function createGenealogicalTree() {
    const data = {
        name: "Gregor Mendel",
        description: "Father of genetics. Known for his work on pea plants and inheritance.",
        children: [
            { 
                name: "Francis Galton", 
                description: "Eugenicist who pioneered correlation and regression, applying statistics to human traits.",
                children: [
                    { 
                        name: "Karl Pearson", 
                        description: "Developed the correlation coefficient, expanded Galton's ideas into biometrics.",
                        children: [
                            { name: "Correlation Coefficient", description: "A measure of the strength and direction of association between two variables." },
                            { name: "Regression", description: "Statistical method to model relationships between variables." }
                        ]
                    },
                    { 
                        name: "Ronald Fisher", 
                        description: "Developed ANOVA and maximum likelihood estimation, critical in modern genetics.",
                        children: [
                            { name: "ANOVA", description: "Analysis of variance, used to compare means across multiple groups." },
                            { name: "Maximum Likelihood", description: "A method to estimate the parameters of a statistical model." }
                        ]
                    }
                ]
            }
        ]
    };

    const svg = d3.select("svg"),
        width = +svg.attr("width"),
        height = +svg.attr("height");

    const root = d3.hierarchy(data);
    
    // Make the tree layout horizontal
    const treeLayout = d3.tree().size([height - 100, width - 100]);
    treeLayout(root);

    const g = svg.append("g").attr("transform", "translate(50,50)");

    // Add links between nodes (horizontal orientation)
    g.selectAll(".link")
        .data(root.links())
        .enter()
        .append("line")
        .attr("class", "link")
        .attr("x1", d => d.source.y)
        .attr("y1", d => d.source.x)
        .attr("x2", d => d.target.y)
        .attr("y2", d => d.target.x)
        .attr("stroke", "#001f3f")  // Navy blue color
        .attr("stroke-width", "1.5px");  // Thin crisp lines

    // Add nodes (interactive circles)
    g.selectAll(".node")
        .data(root.descendants())
        .enter()
        .append("circle")
        .attr("class", "node")
        .attr("cx", d => d.y)
        .attr("cy", d => d.x)
        .attr("r", 12)  // Adjust the size of the circles
        .attr("fill", "#28a745")  // Fill color
        .attr("stroke", "#001f3f")  // Navy blue outline
        .attr("stroke-width", "2px")
        .on("mouseover", handleMouseOver)  // Add event listener for hover
        .on("mouseout", handleMouseOut);   // Remove tooltip on mouseout

    // Add labels to the nodes (horizontally aligned)
    g.selectAll(".label")
        .data(root.descendants())
        .enter()
        .append("text")
        .attr("class", "label")
        .attr("x", d => d.y + 15)  // Position the text slightly right of the circles
        .attr("y", d => d.x)
        .attr("dy", "0.35em")
        .attr("text-anchor", "start")
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

// Run the function to create the tree
createGenealogicalTree();
