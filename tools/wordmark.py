import uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.misc.transform import Transform

FONT = "apple_garamond/AppleGaramond-Light.ttf"
LINES = ["Something", "Wonderful", "Studios"]
LEADING = 1.08  # in em

blob = hb.Blob.from_file_path(FONT)
face = hb.Face(blob)
hbfont = hb.Font(face)
upem = face.upem

tt = TTFont(FONT)
glyph_set = tt.getGlyphSet()
glyph_order = tt.getGlyphOrder()

line_paths = []
line_widths = []
for text in LINES:
    buf = hb.Buffer()
    buf.add_str(text)
    buf.guess_segment_properties()
    hb.shape(hbfont, buf)
    x = 0
    d_parts = []
    for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
        gname = glyph_order[info.codepoint]
        pen = SVGPathPen(glyph_set)
        # y-flip: SVG y grows downward
        tpen = TransformPen(pen, Transform(1, 0, 0, -1, x + pos.x_offset, -pos.y_offset))
        glyph_set[gname].draw(tpen)
        d = pen.getCommands()
        if d:
            d_parts.append(d)
        x += pos.x_advance
    line_paths.append(" ".join(d_parts))
    line_widths.append(x)

max_w = max(line_widths)
asc = tt["hhea"].ascent
line_h = upem * LEADING
total_h = asc + line_h * (len(LINES) - 1) + upem * 0.25

parts = []
for i, (d, w) in enumerate(zip(line_paths, line_widths)):
    tx = (max_w - w) / 2
    ty = asc + i * line_h
    parts.append(f'<path transform="translate({tx:.0f} {ty:.0f})" d="{d}"/>')

svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {max_w:.0f} {total_h:.0f}" '
       f'fill="currentColor">{"".join(parts)}</svg>')

with open("wordmark.svg", "w") as f:
    f.write(svg)
print(f"wordmark.svg written, {len(svg)} bytes, viewBox 0 0 {max_w:.0f} {total_h:.0f}")
