#!/usr/bin/env python3
"""Regenerate the animated README banners: python3 scripts/make_banner.py (run from repo root)."""
import sys
THEMES = {
  "light": dict(bg="#FAFAF7", border="#E6E4DD", text="#16181D", muted="#6A6F7A", faint="#C9CCD2", accent="#0E8F63", on_accent="#FFFFFF"),
  "dark":  dict(bg="#0D1117", border="#262C36", text="#E6EDF3", muted="#8B949E", faint="#3A414C", accent="#3FB950", on_accent="#0D1117"),
}
FONT = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"

def banner(t, animated=True, w=1280, h=360, social=False):
    c = THEMES[t]
    def anim(attr, frm, to, begin, dur="0.5s"):
        if not animated: return ""
        return f'<animate attributeName="{attr}" from="{frm}" to="{to}" begin="{begin}" dur="{dur}" fill="freeze"/>'
    opts = [("Option A", 118, False), ("Option B", 180, True), ("Don't buy", 242, False)]
    mx, my = 1030, 180
    parts = []
    for i,(label,y,win) in enumerate(opts):
        b = 0.3 + i*0.25
        stroke_final = c["accent"] if win else c["faint"]
        parts.append(f'''
  <rect x="760" y="{y-20}" width="170" height="40" rx="20" fill="none" stroke="{c['muted'] if animated else stroke_final}" stroke-width="1.5">
    {anim("stroke", c['muted'], stroke_final, "1.5s", "0.4s")}
  </rect>
  <text x="845" y="{y+6}" text-anchor="middle" font-size="17" fill="{c['text'] if (animated or win) else c['muted']}" font-weight="{600 if win else 500}">{label.replace("'", "&#8217;")}
    {anim("fill", c['text'], c['text'] if win else c['muted'], "1.5s", "0.4s")}
  </text>
  <path d="M930,{y} C980,{y} 980,{my} {mx},{my}" fill="none" stroke="{stroke_final if not animated else c['muted']}" stroke-width="{2.5 if win else 1.5}" pathLength="1" stroke-dasharray="1" stroke-dashoffset="{1 if animated else 0}" stroke-linecap="round">
    {anim("stroke-dashoffset", 1, 0, f"{b}s", "0.6s")}
    {anim("stroke", c['muted'], stroke_final, "1.5s", "0.4s")}
  </path>''')
    result = f'''
  <g opacity="{0 if animated else 1}">
    {anim("opacity", 0, 1, "1.7s", "0.5s")}
    <rect x="{mx}" y="{my-24}" width="190" height="48" rx="24" fill="{c['accent']}"/>
    <path d="M{mx+24},{my} l7,7 l13,-14" fill="none" stroke="{c['on_accent']}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
    <text x="{mx+58}" y="{my+6}" font-size="18" font-weight="700" fill="{c['on_accent']}">Go with B</text>
  </g>'''
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 1280 360" font-family="{FONT}">
  <title>everyday-decisions — Decide, don't dither.</title>
  <rect x="1" y="1" width="1278" height="358" rx="18" fill="{c['bg']}" stroke="{c['border']}" stroke-width="2"/>
  <text x="72" y="112" font-size="15" font-weight="600" letter-spacing="3" fill="{c['muted']}">AGENT SKILL</text>
  <text x="70" y="178" font-size="58" font-weight="800" letter-spacing="-1.5" fill="{c['text']}">everyday-decisions</text>
  <text x="72" y="228" font-size="30" font-weight="600" fill="{c['accent']}">Decide, don&#8217;t dither.</text>
  <text x="72" y="276" font-size="18" fill="{c['muted']}">One firm answer for everyday choices,</text>
  <text x="72" y="302" font-size="18" fill="{c['muted']}">with the trade-off named and a reason to revisit.</text>
  {''.join(parts)}
  {result}
</svg>
'''
for t in THEMES:
    open(f".github/assets/banner-{t}.svg","w").write(banner(t))
print("ok")
