
'use strict';

document.addEventListener('DOMContentLoaded', function() {
    let svg = d3.select('#canvas');
    let width = svg.attr('width');
    let height = svg.attr('height');
    let radius = 5;

    let color = d3.scaleOrdinal(d3.schemeCategory20);

    // Create the links group
    const links_group = svg.append('g')
        .attr('class', 'links');

    const nodes_group = svg.append('g')
        .attr('class', 'nodes');

    { // Create the slider
        const margin = 10;
        let slider_svg = d3.select('#slider');
        const slider = slider_svg.append('g')
            .attr('class', 'slider')
            .attr("transform", "translate(" + margin + "," + slider_svg.attr('height') / 2 + ")");

        const x = d3.scaleLinear()
            .domain([0, 1])
            .range([0, slider_svg.attr('width')-margin*2])
            .clamp(true);

        slider.append("line")
            .attr("class", "track")
            .attr("x1", x.range()[0])
            .attr("x2", x.range()[1])
            .select(function() { return this.parentNode.appendChild(this.cloneNode(true)); })
                .attr("class", "track-inset")
            .select(function() { return this.parentNode.appendChild(this.cloneNode(true)); })
                .attr("class", "track-overlay")
                .call(d3.drag()
                    .on("start.interrupt", function() { slider.interrupt(); })
                    .on("drag", function() { slider_move(d3.event.x, false); })
                    .on("end", function() { slider_move(d3.event.x, true); }));

        slider.insert("g", ".track-overlay")
            .attr("class", "ticks")
            .attr("transform", "translate(0," + 18 + ")")
            .selectAll("text")
                .data(x.ticks(10))
                .enter().append("text")
                    .attr("x", x)
                    .attr("text-anchor", "middle")
                    .text(function(d) { return d; });

        let handle = slider.insert("circle", ".track-overlay")
            .attr("class", "handle")
            .attr("r", 9);

        function slider_move(v, apply) {
            handle.attr('cx', x(x.invert(v)));
            if (apply) {
                update_graph(x.invert(v));
            }
        }

        slider_move(x(0.3), true);
    }

    function update_graph(threshold) {
        let [nodes, links] = generate_graph(threshold);
        let lines = links_group
            .selectAll('line')
            .data(links);

        lines.exit().remove();
        lines = lines.enter()
            .append('line')
            .merge(lines)
            .attr('stroke-width', function(d) { return radius * 2 * d.value; });

        let outer_g = nodes_group
            .selectAll('g')
            .data([]);

        outer_g.exit().remove();

        outer_g = nodes_group
            .selectAll('g')
            .data(nodes);

        outer_g.exit().remove();
        outer_g = outer_g.enter()
            .append('g')
            .merge(outer_g)
                .attr('class', 'node')
                .call(d3.drag()
                    .on('start', dragstarted)
                    .on('drag', dragged)
                    .on('end', dragended));

        let circles = outer_g
            .selectAll('circle')
            .data(function(d) { return [d]; });

        circles.exit().remove();
        circles.enter()
            .append('circle')
            .merge(circles)
                .attr('r', radius)
                    .attr('fill', function(d) { return color(d.group); });

        let labels = outer_g
            .selectAll('text')
            .data(function(d) { return [d]; });

        labels.exit().remove();
        labels.enter()
            .append('text')
            .merge(labels)
                .attr('dx', 12)
                .attr('dy', '.35em')
                .text(function(d) { return d.name; });

        let simulation = d3.forceSimulation()
            .force('link', d3.forceLink().id(function(d) { return d.id; }))
            .force('repel', d3.forceManyBody().strength(-20).distanceMax(120))
            .force('center', d3.forceCenter(width / 2, height / 2));

        simulation
            .nodes(nodes)
            .on('tick', ticked)
            .force('link')
                .links(links);

        function ticked() {
            lines
                .attr('x1', function(d) { return d.source.x; })
                .attr('y1', function(d) { return d.source.y; })
                .attr('x2', function(d) { return d.target.x; })
                .attr('y2', function(d) { return d.target.y; });

            outer_g
                .attr('transform', function(d) {
					d.x = Math.max(radius, Math.min(width - radius, d.x));
					d.y = Math.max(radius, Math.min(height - radius, d.y));
					return 'translate(' + d.x + ',' + d.y + ')'; 
				});
        }

        function dragstarted(d) {
            if (!d3.event.active) {
                simulation.alphaTarget(0.3).restart();
            }
            d.fx = d.x;
            d.fy = d.y;

            // Highlight the group
            let circles = nodes_group
                .selectAll('circle')
                .data(nodes);

            outer_g
                .classed('selected', function(dd) { return dd.group === d.group; })
                .classed('selected-node', function(dd) { return dd.id == d.id; });


            // Display this group
            update_group(d.id, d.group);
        }

        function dragged(d) {
            d.fx = d3.event.x;
            d.fy = d3.event.y;
        }

        function dragended(d) {
            if (!d3.event.active) {
                simulation.alphaTarget(0);
            }
            d.fx = null;
            d.fy = null;
        }

        function update_group(id, group) {
            let found = [];

            // Filter out the group
            for (let link of links) {
                if (link.source.group === group || link.target.group === group) {
                    found.push(link);
                }
            }

            const table = d3.select('#table-body');
            let rows = table.selectAll('tr')
                .data(found);

            rows.exit().remove();
            rows = rows.enter()
                .append('tr')
                .merge(rows);

            function make_name(x) {
                if (x.series !== '') {
                    return x.name + ' (' + x.series + ')';
                }

                return x.name;
            }

            let fields = rows.selectAll('td')
                .data(function(d) {
                    return [ d.source, d.target, d.value, d.matched_lines, d.link ]
                });

            fields.exit().remove();
            fields.enter()
                .append('td')
                .merge(fields)
                    .classed('selected-node', function(d, i) {
                        if (i == 0 || i == 1) {
                            if (d.id == id) {
                                return true;
                            }
                        }

                        return false;
                    })
                    .html(function(d, i) {
                        switch (i) {
                            case 0:
                                return make_name(d);
                            case 1:
                                return make_name(d);
                            case 2:
                                return Math.round(d * 100 * 100) / 100;
                            case 3:
                                return d;
                            case 4:
                                return '<a href="' + d + '">Link</a>';
                        }
                    });
        }
    }

    function generate_graph(threshold) {
        const links = [];
        const nodes = [];

        const nodeEdges = {};
        const nodeMap = {};

        for (let n of raw_nodes) {
            nodeMap[n.id] = {
                'id': n.id,
                'name': n.name,
                'series': n.series,
            };
        }

        for (let edge of raw_links) {
            if (edge.value > threshold) {
                if (nodeEdges[edge.source]) {
                    nodeEdges[edge.source].push(edge.target);
                } else {
                    nodeEdges[edge.source] = [edge.target];
                }

                if (nodeEdges[edge.target]) {
                    nodeEdges[edge.target].push(edge.source);
                } else {
                    nodeEdges[edge.target] = [edge.source];
                }

                // Reconstruct it to copy it.
                links.push({
                    'source': edge.source,
                    'target': edge.target,
                    'link': edge.link,
                    'matched_lines': edge.matched_lines,
                    'value': edge.value,
                });
            }
        }

        // Cluster by links
        const visited = {};
        function visit(id, group) {
            if (visited[id]) {
                return;
            }

            visited[id] = true;
            nodeMap[id].group = group;

            for (let child_id of (nodeEdges[id] || [])) {
                visit(child_id, group);
            }
        }

        for (let id of Object.keys(nodeEdges)) {
            visit(id, id);
        }

        for (let id of Object.keys(nodeEdges)) {
            nodes.push(nodeMap[id])
        }

        return [nodes, links, nodeEdges, nodeMap]
    }

}, false);
