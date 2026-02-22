
'use strict';

document.addEventListener('DOMContentLoaded', function() {
    var leftCM = CodeMirror.fromTextArea(document.getElementsByClassName('left-content')[0], {
        lineNumbers: true,
    });
	leftCM.setValue(d1);

    var rightCM = CodeMirror.fromTextArea(document.getElementsByClassName('right-content')[0], {
        lineNumbers: true,
    });
	rightCM.setValue(d2);

    var d1Regions = [];
    var d2Regions = [];

    var d1Lines = leftCM.getDoc().lineCount();
    var d2Lines = rightCM.getDoc().lineCount();

    for (var i = 0; i < regions.length; i++) {
        var region = regions[i];

        var d1Start = leftCM.posFromIndex(region.doc1.start);
        var d1End = leftCM.posFromIndex(region.doc1.end);

        var d2Start = rightCM.posFromIndex(region.doc2.start);
        var d2End = rightCM.posFromIndex(region.doc2.end);

        leftCM.getDoc().markText(d1Start, d1End, { className: 'CodeMirror-marker-' + (i % 9) });
        rightCM.getDoc().markText(d2Start, d2End, { className: 'CodeMirror-marker-' + (i % 9) });

        d1Regions.push({ from: d1Start, to: d1End, idx: i, start: region.doc1.start, total: d1Lines });
        d2Regions.push({ from: d2Start, to: d2End, idx: i, start: region.doc2.start, total: d2Lines });
    }

	var insert_names = function(d_index, d_files, cm) {
		var doc = cm.getDoc();
		for (var i = 0; i < d_index.length-1; i++) {
			var start_line = doc.posFromIndex(d_index[i]).line;

			var msg = document.createElement('div');
			msg.appendChild(document.createTextNode(d_files[i]));
			msg.className = i === 0 ? "file-name-first" : "file-name";

			doc.addLineWidget(start_line, msg, {above: true, coverGutter: true, noHScroll: true});

			if (i !== 0) {
				var bar = document.createElement('div');
				bar.className = "bar";
				doc.addLineWidget(start_line, bar, {above: true, coverGutter: true, noHScroll: true});
			}
		}
	}

	insert_names(d1_index, d1_files, leftCM);
	insert_names(d2_index, d2_files, rightCM);

    // Scroll function
    var jump = function(leftPos, rightPos) {
        var leftTop = leftCM.charCoords(leftPos, "local").top;
        var leftBottom = leftCM.charCoords(leftCM.posFromIndex(d1.length), "local").top;

        var rightTop = rightCM.charCoords(rightPos, "local").top;
        var rightBottom = rightCM.charCoords(rightCM.posFromIndex(d2.length), "local").top;

        var leftView = leftCM.getScrollInfo();
        var rightView = rightCM.getScrollInfo();

        var leftMissing = leftView.clientHeight - (leftBottom - leftTop);
        var rightMissing = rightView.clientHeight - (rightBottom - rightTop);

        var missing = Math.max(Math.max(leftMissing, rightMissing), 0);

        leftCM.scrollTo(null, leftTop - missing);
        rightCM.scrollTo(null, rightTop - missing);
    };

    // Create the bar
    var make = function(clazz, regs) {
        var sections = d3.select(clazz)
            .selectAll('div')
            .data(regs);

        sections.exit().remove();

        sections.enter()
			.append('div')
		  .merge(sections)
            .attr('class', function(d, i) {
                var clazz = 'section section-' + i;
                if (d.idx !== -1) {
                    clazz += ' CodeMirror-marker-' + (d.idx % 9);
                }

                return clazz;
            })
            .style('width', function(d) {
                return ((d.to.line - d.from.line) / d.total) * 100 + '%';
            })
            .on('click', function(d) {
                jump(d1Regions[d.idx].from, d2Regions[d.idx].from);
            });
    };

    var render = function() {

        // Sort the regions by their start
        var one = d1Regions.slice(0).sort(function(x, y) { return x.start - y.start; });
        var two = d2Regions.slice(0).sort(function(x, y) { return x.start - y.start; });

        make('.left-legend', one);
        make('.right-legend', two);
    };

    render();

}, false);

