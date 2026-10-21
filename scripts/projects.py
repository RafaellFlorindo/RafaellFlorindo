"""Compact 'Selected work' grid. Imported by build_assets.py."""

PROJECTS = [
    ("Escaluz", "Ad-intelligence SaaS", "PRODUCTION"),
    ("SOF Jurídico", "Law-firm SaaS with an AI intake agent", "NEAR PRODUCTION"),
    ("ZapCRM", "A CRM inside WhatsApp Web", "SHIPPED"),
    ("HTC Ops", "AI-assisted customer-success cockpit", "IN USE"),
    ("Growth Dialer", "Parallel dialer with AI voice agents", "BETA"),
    ("Gravação Automática", "Camera-free AI video pipeline", "EXPERIMENT"),
]
LIVE = {"PRODUCTION", "SHIPPED", "IN USE"}


def build(g):
    t, svg, fade_in = g["t"], g["svg"], g["fade_in"]
    PANEL, LINE, TEXT, MUTED, LIME = (g[k] for k in ("PANEL", "LINE", "TEXT", "MUTED", "LIME"))
    W, cols, gap, th = 1200, 3, 16, 104
    tw = (W - gap * (cols - 1)) / cols
    rows = (len(PROJECTS) + cols - 1) // cols
    H = rows * th + (rows - 1) * gap
    body = ""
    for i, (name, line, status) in enumerate(PROJECTS):
        x, y = (i % cols) * (tw + gap), (i // cols) * (th + gap)
        live = status in LIVE
        inner = (
            f'<rect x="{x + .5}" y="{y + .5}" width="{tw - 1}" height="{th - 1}" rx="12" fill="{PANEL}" stroke="{LINE}"/>'
            + t(x + 22, y + 44, name, 20, TEXT, 800, ls=-0.5)
            + t(x + 22, y + 74, line, 14, MUTED, 400)
            + f'<circle cx="{x + tw - 32 - len(status) * 6.2}" cy="{y + 39}" r="3.5" fill="{LIME if live else MUTED}"/>'
            + t(x + tw - 20, y + 43, status, 10, LIME if live else MUTED, 600, mono=True, anchor="end")
        )
        body += fade_in(inner, 0.1 + i * 0.08)
    title = "Selected work: " + " · ".join(f"{n} ({l})" for n, l, _ in PROJECTS)
    return {"work.svg": svg(W, H, title, body)}
