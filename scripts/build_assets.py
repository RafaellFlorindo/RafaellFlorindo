"""Generates every SVG in ../assets/{dark,light}. Run: python3 scripts/build_assets.py

The whole profile is skinned from THEMES below. To change the accent colour,
edit ACCENT (and ACCENT_SOFT / ON_ACCENT) in both themes and re-run.
"""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "assets"

THEMES = {
    "dark": dict(
        BG="#0B0B0D", PANEL="#121215", RAISED="#18181C", LINE="#232329", STROKE="#30303A",
        TEXT="#F4F4F5", MUTED="#A1A1AA", DIM="#5C5C66",
        ACCENT="#FF6B35", ACCENT_SOFT="#FF9A70", ON_ACCENT="#160A04", ON_ACCENT_MUTED="#5C2610",
        GLOW=0.20, GRID=0.06,
    ),
    "light": dict(
        BG="#FFFFFF", PANEL="#FAFAFA", RAISED="#F4F4F5", LINE="#E4E4E7", STROKE="#D4D4D8",
        TEXT="#18181B", MUTED="#52525B", DIM="#A1A1AA",
        ACCENT="#EA580C", ACCENT_SOFT="#C2410C", ON_ACCENT="#FFFFFF", ON_ACCENT_MUTED="#FFE1D1",
        GLOW=0.10, GRID=0.09,
    ),
}
P = {}  # active palette, set per theme in main()

SANS = "ui-sans-serif, -apple-system, BlinkMacSystemFont, 'Segoe UI', Inter, Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, 'JetBrains Mono', Menlo, Consolas, 'Liberation Mono', monospace"

BASE_STYLE = f"""<style>
  text {{ font-family: {SANS}; }}
  .m {{ font-family: {MONO}; }}
  @keyframes pulse {{ 0%,100% {{ opacity: 1 }} 50% {{ opacity: .25 }} }}
  .pulse {{ animation: pulse 1.6s ease-in-out infinite; }}
  @media (prefers-reduced-motion: reduce) {{ * {{ animation: none !important; }} }}
</style>"""


# ---------------------------------------------------------------- primitives
def svg(w, h, title, body, defs=""):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
        f'role="img" aria-label="{escape(title)}">\n<title>{escape(title)}</title>\n{BASE_STYLE}\n'
        f"<defs>{defs}</defs>\n{body}\n</svg>\n"
    )


def t(x, y, s, size=14, fill=None, weight=400, mono=False, anchor="start", ls=0, extra=""):
    cls = ' class="m"' if mono else ""
    return (
        f'<text x="{x:.1f}" y="{y:.1f}"{cls} font-size="{size}" font-weight="{weight}" fill="{fill or P["TEXT"]}" '
        f'text-anchor="{anchor}" letter-spacing="{ls}"{extra}>{escape(s)}</text>'
    )


def card(x, y, w, h, rx=14, fill=None, stroke=None):
    return (
        f'<rect x="{x + .5:.1f}" y="{y + .5:.1f}" width="{w - 1:.1f}" height="{h - 1:.1f}" rx="{rx}" '
        f'fill="{fill or P["PANEL"]}" stroke="{stroke or P["LINE"]}"/>'
    )


def fade_in(inner, begin, dy=8, dur=0.6):
    # The static state is the final state, so renderers without SMIL still show everything.
    total = begin + dur
    kt = f"0;{begin / total:.3f};1"
    return (
        f'<g><animate attributeName="opacity" values="0;0;1" keyTimes="{kt}" dur="{total:.2f}s"/>'
        f'<animateTransform attributeName="transform" type="translate" values="0 {dy};0 {dy};0 0" keyTimes="{kt}" dur="{total:.2f}s"/>'
        f"{inner}</g>"
    )


def grow(attr, final, begin, dur):
    total = begin + dur
    return f'<animate attributeName="{attr}" values="0;0;{final}" keyTimes="0;{begin / total:.3f};1" dur="{total:.2f}s"/>'


def mono_w(s, size):
    """Approximate rendered width of monospace text."""
    return len(s) * size * 0.61


def chip(x, y, label, size=11, h=26, strong=False):
    w = mono_w(label, size) + 24
    fill = P["RAISED"]
    stroke = P["ACCENT"] if strong else P["STROKE"]
    color = P["TEXT"] if strong else P["MUTED"]
    return (
        f'<rect x="{x:.1f}" y="{y}" width="{w:.1f}" height="{h}" rx="{h / 2}" fill="{fill}" stroke="{stroke}"/>'
        + t(x + w / 2, y + h / 2 + size * 0.36, label, size, color, 500, mono=True, anchor="middle")
    ), w


def glow_def(gid, cx, cy, r):
    return (
        f'<radialGradient id="{gid}" cx="{cx}" cy="{cy}" r="{r}" gradientUnits="userSpaceOnUse">'
        f'<stop offset="0" stop-color="{P["ACCENT"]}" stop-opacity="{P["GLOW"]}"/>'
        f'<stop offset="1" stop-color="{P["ACCENT"]}" stop-opacity="0"/></radialGradient>'
    )


# ---------------------------------------------------------------- hero
def hero():
    W, H = 1200, 480
    defs = (
        f'<pattern id="dots" width="24" height="24" patternUnits="userSpaceOnUse">'
        f'<circle cx="1" cy="1" r="1" fill="{P["TEXT"]}" fill-opacity="{P["GRID"]}"/></pattern>'
        f'<clipPath id="frame"><rect width="{W}" height="{H}" rx="18"/></clipPath>'
        + glow_def("glow", 910, 260, 380)
        + glow_def("glow2", 120, 120, 300)
    )

    bw, bh = 230, 72
    nodes = {
        "in": (660, 112, "INBOUND", "whatsapp · forms · calls"),
        "ai": (930, 112, "AI AGENT", "qualify · answer · route"),
        "crm": (930, 236, "CRM", "gohighlevel · pipelines"),
        "cal": (660, 236, "CALENDAR", "~30 calendars routed"),
        "won": (795, 360, "BOOKED", "revenue, not busywork"),
    }

    def port(k, side):
        x, y = nodes[k][0], nodes[k][1]
        return {"r": (x + bw, y + bh / 2), "l": (x, y + bh / 2), "b": (x + bw / 2, y + bh), "t": (x + bw / 2, y)}[side]

    p1, p2 = port("in", "r"), port("ai", "l")
    p3, p4 = port("ai", "b"), port("crm", "t")
    p5, p6 = port("crm", "l"), port("cal", "r")
    p7, p8 = port("cal", "b"), port("won", "t")
    mid_y = (p7[1] + p8[1]) / 2
    path = (
        f"M{p1[0]},{p1[1]} H{p2[0]} M{p3[0]},{p3[1]} V{p4[1]} M{p5[0]},{p5[1]} H{p6[0]} "
        f"M{p7[0]},{p7[1]} V{mid_y} H{p8[0]} V{p8[1]}"
    )
    motion = (
        f"M{p1[0]},{p1[1]} H{p2[0]} H{p3[0]} V{p4[1]} V{p5[1]} H{p6[0]} H{p7[0]} "
        f"V{mid_y} H{p8[0]} V{p8[1]}"
    )
    wires = (
        f'<path d="{path}" fill="none" stroke="{P["STROKE"]}" stroke-width="1.5"/>'
        f'<path d="{path}" fill="none" stroke="{P["ACCENT"]}" stroke-width="1.5" stroke-dasharray="3 9" opacity=".6">'
        f'<animate attributeName="stroke-dashoffset" from="24" to="0" dur="1.2s" repeatCount="indefinite"/></path>'
    )
    packets = "".join(
        f'<circle r="4" fill="{P["ACCENT"]}"><animateMotion path="{motion}" dur="5.2s" begin="{i * 1.3}s" repeatCount="indefinite"/></circle>'
        for i in range(4)
    )

    boxes = ""
    for i, (k, (x, y, title, sub)) in enumerate(nodes.items()):
        won = k == "won"
        tc = P["ON_ACCENT"] if won else P["TEXT"]
        sc = P["ON_ACCENT_MUTED"] if won else P["MUTED"]
        inner = (
            card(x, y, bw, bh, 12, P["ACCENT"] if won else P["PANEL"], P["ACCENT"] if won else P["STROKE"])
            + t(x + 18, y + 31, title, 13, tc, 700, mono=True, ls=1.5)
            + t(x + 18, y + 53, sub, 12, sc, 400, mono=True)
            + t(x + bw - 16, y + 31, f"0{i + 1}", 11, sc, 400, mono=True, anchor="end")
        )
        if not won:
            inner += (
                f'<circle cx="{x + bw - 19}" cy="{y + 50}" r="3" fill="{P["ACCENT"]}" opacity=".2">'
                f'<animate attributeName="opacity" values=".2;1;.2" dur="5.2s" begin="{i * 1.05}s" repeatCount="indefinite"/></circle>'
            )
        boxes += fade_in(inner, 0.5 + i * 0.15)

    name = (
        fade_in(t(70, 194, "Rafael", 88, P["TEXT"], 800, ls=-3.5), 0.1)
        + fade_in(
            f'<text x="70" y="282" font-size="88" font-weight="800" fill="{P["TEXT"]}" letter-spacing="-3.5">Florindo'
            f'<tspan fill="{P["ACCENT"]}">.</tspan></text>',
            0.25,
        )
        + fade_in(t(73, 330, "I engineer the system behind the operation.", 22, P["TEXT"], 600, ls=-0.3), 0.45)
        + fade_in(t(73, 360, "AI agents that sell, CRMs that scale, integrations that don't break.", 15, P["MUTED"]), 0.6)
    )
    chips, x = "", 73
    for i, tag in enumerate(["AI AGENTS", "GOHIGHLEVEL", "N8N", "TYPESCRIPT", "PYTHON", "POSTGRES"]):
        c, w = chip(x, 390, tag, 11, 26, strong=i == 0)
        chips += c
        x += w + 8
    name += fade_in(chips, 0.75)

    top = (
        f'<line x1="0" y1="52" x2="{W}" y2="52" stroke="{P["LINE"]}"/>'
        f'<circle cx="40" cy="27" r="4" fill="{P["ACCENT"]}" class="pulse"/>'
        + t(54, 31, "SYSTEM ONLINE", 11, P["ACCENT"], 600, mono=True, ls=1.5)
        + t(170, 31, "/  AUTOMATION & AI ENGINEER", 11, P["MUTED"], 400, mono=True, ls=1.5)
        + t(W - 40, 31, "MINAS GERAIS, BR  →  WORKING WORLDWIDE", 11, P["MUTED"], 400, mono=True, anchor="end", ls=1.5)
        + t(660, 92, "// the pipeline I build, live", 12, P["DIM"], 400, mono=True)
    )
    bottom = (
        f'<line x1="0" y1="{H - 30}" x2="{W}" y2="{H - 30}" stroke="{P["LINE"]}"/>'
        + t(40, H - 11, "LEAD IN → QUALIFIED → ROUTED → BOOKED", 10, P["DIM"], 400, mono=True, ls=2)
        + t(W - 40, H - 11, "GITHUB.COM/RAFAELLFLORINDO", 10, P["DIM"], 400, mono=True, anchor="end", ls=2)
    )
    body = (
        f'<g clip-path="url(#frame)"><rect width="{W}" height="{H}" fill="{P["BG"]}"/>'
        f'<rect width="{W}" height="{H}" fill="url(#dots)"/>'
        f'<rect width="{W}" height="{H}" fill="url(#glow)"/><rect width="{W}" height="{H}" fill="url(#glow2)"/>'
        f"{top}{name}{wires}{boxes}{packets}{bottom}</g>"
        f'<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="18" fill="none" stroke="{P["LINE"]}"/>'
    )
    return svg(W, H, "Rafael Florindo — Automation & AI Engineer. I engineer the system behind the operation.", body, defs)


# ---------------------------------------------------------------- metrics
METRICS = [
    ("694", "", "AUTOMATED TESTS", "across my products"),
    ("17", "", "PRODUCTION WORKFLOWS", "running for real clients"),
    ("~30", "", "CALENDARS", "routed by AI agents"),
    ("55.8", "%", "FASTER WITH AI", "thesis · p = 0.0017"),
]


def metrics():
    W, H, gap = 1200, 150, 16
    n = len(METRICS)
    cw = (W - gap * (n - 1)) / n
    body = ""
    for i, (num, unit, label, sub) in enumerate(METRICS):
        x = i * (cw + gap)
        inner = (
            card(x, 0, cw, H, 14)
            + f'<rect x="{x + 22}" y="23" width="6" height="6" rx="1" fill="{P["ACCENT"]}"/>'
            + t(x + 36, 30, label, 11, P["MUTED"], 500, mono=True, ls=1.2)
            + f'<text x="{x + 20}" y="96" font-size="54" font-weight="800" fill="{P["TEXT"]}" letter-spacing="-2.5">{escape(num)}'
            + (f'<tspan fill="{P["ACCENT"]}" font-size="34" dx="3">{unit}</tspan>' if unit else "")
            + "</text>"
            + t(x + 22, 124, sub, 12, P["DIM"], 400, mono=True)
            + f'<rect x="{x + 22}" y="{H - 9}" height="2" rx="1" width="{cw - 44:.1f}" fill="{P["ACCENT"]}">'
            + grow("width", f"{cw - 44:.1f}", 0.3 + i * 0.15, 1.2) + "</rect>"
        )
        body += fade_in(inner, 0.1 + i * 0.15)
    return svg(W, H, " · ".join(f"{a}{b} {c.lower()} {d}" for a, b, c, d in METRICS), body)


# ---------------------------------------------------------------- section headers
HEADERS = [
    ("01", "WHAT I BUILD", "// the layers behind revenue operations"),
    ("02", "SELECTED WORK", "// things I have shipped"),
    ("03", "RESEARCH", "// generative AI × software engineering"),
    ("04", "TOOLKIT", "// what I reach for"),
    ("05", "HOW I WORK", "// AI as an execution and review layer"),
]


def header(num, title, note):
    W, H = 1200, 64
    tw = len(title) * 14.6
    lx = 46 + tw + 22
    body = (
        f'<rect x="0" y="22" width="34" height="24" rx="6" fill="none" stroke="{P["ACCENT"]}"/>'
        + t(17, 38.5, num, 12, P["ACCENT"], 700, mono=True, anchor="middle")
        + t(46, 42, title, 22, P["TEXT"], 800, ls=1.2)
        + f'<line x1="{lx:.1f}" y1="34" x2="{W}" y2="34" stroke="{P["LINE"]}"/>'
        + f'<rect x="{lx:.1f}" y="33" width="80" height="2" fill="{P["ACCENT"]}">'
        f'<animate attributeName="x" from="{lx:.1f}" to="{W - 80}" dur="4s" repeatCount="indefinite"/>'
        f'<animate attributeName="opacity" values="0;1;1;0" keyTimes="0;.1;.85;1" dur="4s" repeatCount="indefinite"/></rect>'
        + t(W, 60, note, 11, P["DIM"], 400, mono=True, anchor="end", ls=0.5)
    )
    return svg(W, H, f"{num} — {title.title()}", body)


# ---------------------------------------------------------------- capability cards
CAPS = [
    ("AI AGENTS", ["Qualify, answer, route and book —", "with guardrails and human handoff."]),
    ("CRM ARCHITECTURE", ["GoHighLevel snapshots, pipelines", "and white-label setups at scale."]),
    ("INTEGRATIONS", ["APIs, webhooks and n8n flows with", "retries and idempotency built in."]),
    ("PRODUCT ENGINEERING", ["TypeScript, Python, Postgres,", "workers and tests — tools and SaaS."]),
]


def capabilities():
    W, H, gap = 1200, 200, 16
    cw = (W - gap * 3) / 4
    a = P["ACCENT"]
    icons = [
        lambda x, y: f'<circle cx="{x + 14}" cy="{y + 14}" r="12" fill="none" stroke="{a}" stroke-width="2"/><circle cx="{x + 14}" cy="{y + 14}" r="4.5" fill="{a}"/>',
        lambda x, y: f'<rect x="{x + 1}" y="{y + 1}" width="26" height="26" rx="5" fill="none" stroke="{a}" stroke-width="2"/><path d="M{x + 1} {y + 10}H{x + 27}M{x + 10} {y + 10}V{y + 27}" stroke="{a}" stroke-width="2"/>',
        lambda x, y: f'<path d="M{x} {y + 14}H{x + 9}M{x + 19} {y + 14}H{x + 28}" stroke="{a}" stroke-width="2"/><circle cx="{x + 14}" cy="{y + 14}" r="5" fill="none" stroke="{a}" stroke-width="2"/><circle cx="{x + 2}" cy="{y + 14}" r="2.5" fill="{a}"/><circle cx="{x + 26}" cy="{y + 14}" r="2.5" fill="{a}"/>',
        lambda x, y: f'<path d="M{x + 8} {y + 4}L{x + 1} {y + 14}L{x + 8} {y + 24}M{x + 20} {y + 4}L{x + 27} {y + 14}L{x + 20} {y + 24}" fill="none" stroke="{a}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>',
    ]
    body = ""
    for i, (title, lines) in enumerate(CAPS):
        x = i * (cw + gap)
        inner = (
            card(x, 0, cw, H, 14)
            + f'<rect x="{x + 20}" y="20" width="48" height="48" rx="12" fill="{P["RAISED"]}" stroke="{P["STROKE"]}"/>'
            + icons[i](x + 30, 30)
            + t(x + cw - 20, 40, f"0{i + 1}", 11, P["DIM"], 400, mono=True, anchor="end")
            + t(x + 22, 104, title, 14, P["TEXT"], 700, mono=True, ls=1)
            + "".join(t(x + 22, 136 + j * 21, ln, 13.5, P["MUTED"]) for j, ln in enumerate(lines))
        )
        body += fade_in(inner, 0.1 + i * 0.12)
    return svg(W, H, "What I build: AI agents, CRM architecture, integrations, product engineering", body)


# ---------------------------------------------------------------- selected work
PROJECTS = [
    ("Escaluz", "Ad-intelligence SaaS", "PRODUCTION"),
    ("SOF Jurídico", "Law-firm SaaS with an AI intake agent", "NEAR PRODUCTION"),
    ("ZapCRM", "A CRM inside WhatsApp Web", "SHIPPED"),
    ("HTC Ops", "AI-assisted customer-success cockpit", "IN USE"),
    ("Growth Dialer", "Parallel dialer with AI voice agents", "BETA"),
    ("Gravação Automática", "Camera-free AI video pipeline", "EXPERIMENT"),
]
LIVE = {"PRODUCTION", "SHIPPED", "IN USE"}


def work():
    W, cols, gap, th = 1200, 3, 16, 112
    tw = (W - gap * (cols - 1)) / cols
    rows = (len(PROJECTS) + cols - 1) // cols
    H = rows * th + (rows - 1) * gap
    body = ""
    for i, (name, line, status) in enumerate(PROJECTS):
        x, y = (i % cols) * (tw + gap), (i // cols) * (th + gap)
        live = status in LIVE
        pw = mono_w(status, 10) + 30
        px = x + tw - 20 - pw
        color = P["ACCENT"] if live else P["MUTED"]
        inner = (
            card(x, y, tw, th, 14)
            + t(x + 22, y + 46, name, 20, P["TEXT"], 800, ls=-0.4)
            + t(x + 22, y + 78, line, 14, P["MUTED"])
            + f'<rect x="{px:.1f}" y="{y + 26}" width="{pw:.1f}" height="22" rx="11" fill="{P["RAISED"]}" stroke="{P["ACCENT"] if live else P["STROKE"]}"/>'
            + f'<circle cx="{px + 12:.1f}" cy="{y + 37}" r="3" fill="{color}"'
            + (' class="pulse"' if live else "") + "/>"
            + t(px + 21, y + 40.5, status, 10, color, 600, mono=True)
        )
        body += fade_in(inner, 0.1 + i * 0.08)
    return svg(W, H, "Selected work: " + " · ".join(f"{n} ({l}, {s.lower()})" for n, l, s in PROJECTS), body)


# ---------------------------------------------------------------- research
def research():
    W, H = 1200, 300
    max_w, x0 = 470, 220
    conv, cop = 160.89, 71.17
    bars = ""
    for i, (label, val, color, tc) in enumerate(
        [("CONVENTIONAL", conv, P["DIM"], P["TEXT"]), ("WITH COPILOT", cop, P["ACCENT"], P["ACCENT"])]
    ):
        y = 116 + i * 62
        w = max_w * val / conv
        bars += (
            t(40, y + 21, label, 12, P["MUTED"], 500, mono=True, ls=1.2)
            + f'<rect x="{x0}" y="{y}" width="{max_w}" height="30" rx="6" fill="{P["RAISED"]}"/>'
            + f'<rect x="{x0}" y="{y}" width="{w:.1f}" height="30" rx="6" fill="{color}">'
            + grow("width", f"{w:.1f}", 0.4 + i * 0.3, 1.4) + "</rect>"
            + fade_in(t(x0 + w + 14, y + 21, f"{val:.2f} min", 15, tc, 700, mono=True), 1.6 + i * 0.3, dy=0)
        )
    r = 860
    side = (
        f'<line x1="{r - 32}" y1="100" x2="{r - 32}" y2="{H - 40}" stroke="{P["LINE"]}"/>'
        + t(r, 116, "MEAN COMPLETION TIME", 11, P["MUTED"], 500, mono=True, ls=1.2)
        + f'<text x="{r - 4}" y="180" font-size="66" font-weight="800" fill="{P["ACCENT"]}" letter-spacing="-3">−55.8<tspan font-size="36">%</tspan></text>'
        + t(r, 210, "p = 0.0017 · n = 35 + 35", 13, P["TEXT"], 500, mono=True)
        + t(r, 242, "Functional tests: +7 p.p.", 13, P["MUTED"], 400, mono=True)
        + t(r, 262, "not statistically significant", 13, P["DIM"], 400, mono=True)
    )
    head = (
        t(40, 50, "THESIS · UNIVÉRTIX · POSTER AT FAVE 2026", 11, P["ACCENT"], 600, mono=True, ls=1.5)
        + t(40, 82, "Does generative AI make developers faster? Yes. Better? Not proven yet.", 21, P["TEXT"], 700, ls=-0.3)
    )
    body = card(0, 0, W, H, 16) + head + bars + fade_in(side, 1.2)
    return svg(W, H, "Thesis: Copilot-assisted developers finished 55.8% faster (160.89 → 71.17 min, p = 0.0017, n = 35 + 35). Functional tests +7 p.p., not statistically significant.", body)


# ---------------------------------------------------------------- toolkit
TOOLKIT = [
    ("AUTOMATION", ["GoHighLevel", "n8n", "Webhooks", "Twilio", "WhatsApp"]),
    ("AI", ["Claude Code", "Codex CLI", "OpenAI"]),
    ("PRODUCT", ["TypeScript", "JavaScript", "Python", "React", "Next.js", "Node.js", "Tailwind", "Vite"]),
    ("DATA & INFRA", ["Postgres", "Supabase", "Prisma", "Docker", "Linux", "Vercel", "Cloudflare", "GitHub Actions"]),
    ("QUALITY", ["Vitest", "Playwright"]),
]


def toolkit():
    W, row = 1200, 54
    H = 28 + len(TOOLKIT) * row + 10
    body = card(0, 0, W, H, 16)
    for i, (label, items) in enumerate(TOOLKIT):
        y = 26 + i * row
        if i:
            body += f'<line x1="28" y1="{y - 9}" x2="{W - 28}" y2="{y - 9}" stroke="{P["LINE"]}"/>'
        inner = (
            f'<rect x="32" y="{y + 11}" width="6" height="6" rx="1" fill="{P["ACCENT"]}"/>'
            + t(48, y + 18, label, 11, P["MUTED"], 600, mono=True, ls=1.4)
        )
        x = 220
        for it in items:
            c, w = chip(x, y + 1, it, 12, 28, strong=i == 0 and it in ("GoHighLevel", "n8n"))
            inner += c
            x += w + 8
        body += fade_in(inner, 0.1 + i * 0.1)
    return svg(W, H, "Toolkit — " + " · ".join(f"{l.title()}: {', '.join(it)}" for l, it in TOOLKIT), body)


# ---------------------------------------------------------------- how I work
STAGES = [
    ("CONTEXT", ["Obsidian second brain", "that agents read and", "keep up to date."]),
    ("ORCHESTRATE", ["A lead agent splits the", "work; specialists take", "front, back and tests."]),
    ("IMPLEMENT", ["Claude Code + Codex CLI", "on real repos, with", "atomic, reviewable commits."]),
    ("VERIFY", ["Cross-model audits,", "Playwright E2E, security", "sweeps, DB rehearsals."]),
    ("GUARDRAILS", ["Manual → approve → auto,", "always with caps. Never", "unsupervised by default."]),
]


def workflow():
    W, H, gap = 1200, 196, 14
    n = len(STAGES)
    cw = (W - gap * (n - 1)) / n
    body = (
        f'<line x1="{cw / 2:.1f}" y1="32" x2="{W - cw / 2:.1f}" y2="32" stroke="{P["STROKE"]}" stroke-width="1.5"/>'
        f'<line x1="{cw / 2:.1f}" y1="32" x2="{W - cw / 2:.1f}" y2="32" stroke="{P["ACCENT"]}" stroke-width="1.5" stroke-dasharray="3 9">'
        f'<animate attributeName="stroke-dashoffset" from="24" to="0" dur="1.2s" repeatCount="indefinite"/></line>'
    )
    for i, (title, lines) in enumerate(STAGES):
        x = i * (cw + gap)
        last = i == n - 1
        inner = (
            card(x, 56, cw, H - 56, 14, stroke=P["ACCENT"] if last else P["LINE"])
            + f'<circle cx="{x + cw / 2:.1f}" cy="32" r="15" fill="{P["ACCENT"] if last else P["BG"]}" stroke="{P["ACCENT"]}" stroke-width="1.5"/>'
            + t(x + cw / 2, 36, f"0{i + 1}", 11, P["ON_ACCENT"] if last else P["ACCENT"], 700, mono=True, anchor="middle")
            + t(x + 20, 92, title, 13, P["TEXT"], 700, mono=True, ls=1.2)
            + "".join(t(x + 20, 120 + j * 20, ln, 13, P["MUTED"]) for j, ln in enumerate(lines))
        )
        body += fade_in(inner, 0.1 + i * 0.12)
    return svg(W, H, "How I work: " + " → ".join(f"{t_.title()} ({' '.join(l)})" for t_, l in STAGES), body)


# ---------------------------------------------------------------- buttons & footer
BUTTONS = {
    "btn-linkedin": ("LINKEDIN", False),
    "btn-email": ("EMAIL", False),
    "btn-repos": ("REPOSITORIES", False),
    "cta-linkedin": ("CONNECT ON LINKEDIN", True),
    "cta-email": ("SEND AN EMAIL", False),
}


def button(label, primary):
    size = 12
    h = 44 if primary or label.startswith(("CONNECT", "SEND")) else 38
    w = round(len(label) * size * 0.72 + 70)
    fill = P["ACCENT"] if primary else P["PANEL"]
    stroke = P["ACCENT"] if primary else P["STROKE"]
    tc = P["ON_ACCENT"] if primary else P["TEXT"]
    ac = P["ON_ACCENT"] if primary else P["ACCENT"]
    body = (
        f'<rect x=".5" y=".5" width="{w - 1}" height="{h - 1}" rx="{h / 2}" fill="{fill}" stroke="{stroke}"/>'
        + t(24, h / 2 + 4.3, label, size, tc, 700, mono=True, ls=1)
        + t(w - 22, h / 2 + 4.8, "↗", 14, ac, 700, mono=True, anchor="end")
    )
    return svg(w, h, label.title(), body)


def footer():
    W, H = 1200, 120
    body = (
        f'<line x1="0" y1="40" x2="{W}" y2="40" stroke="{P["LINE"]}"/>'
        f'<rect x="0" y="39" width="140" height="2" fill="{P["ACCENT"]}">'
        f'<animate attributeName="x" from="-140" to="{W}" dur="5s" repeatCount="indefinite"/></rect>'
        + t(W / 2, 82, "END OF TRANSMISSION", 12, P["MUTED"], 500, mono=True, anchor="middle", ls=4)
        + f'<rect x="{W / 2 + 106}" y="71" width="8" height="13" fill="{P["ACCENT"]}" class="pulse"/>'
        + t(W / 2, 106, "thanks for stopping by", 12, P["DIM"], 400, mono=True, anchor="middle", ls=1)
    )
    return svg(W, H, "End of transmission — thanks for stopping by", body)


def main():
    count = 0
    for theme, palette in THEMES.items():
        P.clear()
        P.update(palette)
        files = {
            "banner.svg": hero(),
            "metrics.svg": metrics(),
            "capabilities.svg": capabilities(),
            "work.svg": work(),
            "research.svg": research(),
            "toolkit.svg": toolkit(),
            "workflow.svg": workflow(),
            "outro.svg": footer(),
        }
        for num, title, note in HEADERS:
            files[f"h-{num}.svg"] = header(num, title, note)
        for name, (label, primary) in BUTTONS.items():
            files[f"{name}.svg"] = button(label, primary)
        out = ROOT / theme
        out.mkdir(parents=True, exist_ok=True)
        for name, content in files.items():
            (out / name).write_text(content, encoding="utf-8")
        count += len(files)
    print(f"wrote {count} files to {ROOT}")


if __name__ == "__main__":
    main()
