// Sample data
const data = [
    { group: "White", iq: 100, moral: 95, crime: 30, income: 75, reproduction: 48 },
    { group: "Black", iq: 108, moral: 85, crime: 35, income: 45, reproduction: 55 },
    { group: "Asian", iq: 105, moral: 90, crime: 25, income: 70, reproduction: 47 },
    { group: "Hispanic", iq: 102, moral: 80, crime: 40, income: 50, reproduction: 60 },
    { group: "Other", iq: 98, moral: 85, crime: 45, income: 55, reproduction: 52 },
];

// Chart dimensions
const width = 800, height = 500, margin = { top: 20, right: 20, bottom: 50, left: 70 };

// Scales
const xScale = d3.scaleBand()
    .domain(data.map(d => d.group))
    .range([margin.left, width - margin.right])
    .padding(0.1);

const yScale = d3.scaleLinear()
    .domain([0, 400])
    .range([height - margin.bottom, margin.top]);

// SVG Container
const svg = d3.select("#chart").append("svg")
    .attr("width", width)
    .attr("height", height);

// Axes
svg.append("g")
    .attr("transform", `translate(0,${height - margin.bottom})`)
    .call(d3.axisBottom(xScale));

svg.append("g")
    .attr("transform", `translate(${margin.left},0)`)
    .call(d3.axisLeft(yScale));

// Bars
const bars = svg.selectAll(".bar")
    .data(data)
    .enter()
    .append("rect")
    .attr("class", "bar")
    .attr("x", d => xScale(d.group))
    .attr("y", d => yScale(0))
    .attr("width", xScale.bandwidth())
    .attr("height", 0)
    .attr("fill", "steelblue");

// Initial chart update
function updateChart(weights) {
    const updatedData = data.map(d => ({
        group: d.group,
        value: d.iq * weights.iq + d.moral * weights.moral - d.crime * weights.crime + d.income * weights.income - d.reproduction * weights.reproduction
    }));

    yScale.domain([0, d3.max(updatedData, d => d.value)]);

    bars.data(updatedData)
        .transition()
        .duration(500)
        .attr("y", d => yScale(d.value))
        .attr("height", d => height - margin.bottom - yScale(d.value));
}

// Initial weights
const weights = { iq: 1, moral: 1, crime: 1, income: 1, reproduction: 1 };
updateChart(weights);

// Slider event listeners
["iq", "moral", "crime", "income", "reproduction"].forEach(variable => {
    d3.select(`#slider-${variable}`).on("input", function () {
        weights[variable] = +this.value;
        d3.select(`#weight-${variable}`).text(this.value.toFixed(1));
        updateChart(weights);
    });
});
