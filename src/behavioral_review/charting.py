from __future__ import annotations


def render_svg_chart(points: list[tuple[str, int]]) -> str:
    width = 720
    height = 240
    left = 50
    right = 20
    top = 20
    bottom = 40
    plot_width = width - left - right
    plot_height = height - top - bottom

    if not points:
        return (
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}">'
            '<text x="24" y="40" font-family="sans-serif" font-size="16">No data yet</text>'
            '</svg>'
        )

    def y_for(score: int) -> float:
        return top + plot_height - (score / 100) * plot_height

    step = plot_width / max(1, len(points) - 1)
    coords = []
    for index, (_date, score) in enumerate(points):
        coords.append((left + index * step, y_for(score)))

    polyline = ' '.join(f'{x:.1f},{y:.1f}' for x, y in coords)

    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}">',
        f'<rect width="{width}" height="{height}" fill="#fcfaf3" />',
        f'<line x1="{left}" y1="{top}" x2="{left}" y2="{height-bottom}" stroke="#444" />',
        f'<line x1="{left}" y1="{height-bottom}" x2="{width-right}" y2="{height-bottom}" stroke="#444" />',
        f'<line x1="{left}" y1="{y_for(70):.1f}" x2="{width-right}" y2="{y_for(70):.1f}" stroke="#2f855a" stroke-dasharray="4 4" />',
        f'<line x1="{left}" y1="{y_for(45):.1f}" x2="{width-right}" y2="{y_for(45):.1f}" stroke="#dd6b20" stroke-dasharray="4 4" />',
        f'<polyline fill="none" stroke="#1f4f46" stroke-width="3" points="{polyline}" />',
    ]

    for (date_label, score), (x, y) in zip(points, coords):
        lines.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="#1f4f46" />')
        lines.append(f'<text x="{x:.1f}" y="{height-16}" text-anchor="middle" font-family="sans-serif" font-size="10">{date_label}</text>')
        lines.append(f'<text x="{x:.1f}" y="{y-10:.1f}" text-anchor="middle" font-family="sans-serif" font-size="10">{score}</text>')

    lines.extend([
        '<text x="54" y="18" font-family="sans-serif" font-size="14">Daily TA score</text>',
        f'<text x="{width-110}" y="{y_for(70)-6:.1f}" font-family="sans-serif" font-size="10" fill="#2f855a">good day</text>',
        f'<text x="{width-115}" y="{y_for(45)-6:.1f}" font-family="sans-serif" font-size="10" fill="#dd6b20">watch line</text>',
        '</svg>',
    ])
    return ''.join(lines)
