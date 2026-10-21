"""Generates every SVG in ../assets. Run: python3 scripts/build_assets.py"""
from pathlib import Path
from html import escape

OUT = Path(__file__).resolve().parent.parent / "assets"

BG = "#0A0B0A"
PANEL = "#111311"
LINE = "#23271F"
TEXT = "#ECEEE6"
MUTED = "#8A8F84"
DIM = "#4A4F45"
LIME = "#CCFF4D"
AMBER = "#FFB547"

SANS = "ui-sans-serif, -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace"

BASE_STYLE = f"""<style>
  text {{ font-family: {SANS}; }}
  .m {{ font-family: {MONO}; }}
  @keyframes pulse {{ 0%,100% {{ opacity: 1 }} 50% {{ opacity: .25 }} }}
  .pulse {{ animation: pulse 1.6s ease-in-out infinite; }}
  @media (prefers-reduced-motion: reduce) {{ * {{ animation: none !important; }} }}
</style>"""


def svg(w, h, title, body, defs=""):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
        f'role="img" aria-label="{escape(title)}">\n<title>{escape(title)}</title>\n{BASE_STYLE}\n'
        f"<defs>{defs}</defs>\n{body}\n</svg>\n"
    )


def t(x, y, s, size=14, fill=TEXT, weight=400, mono=False, anchor="start", ls=0, extra=""):
    cls = ' class="m"' if mono else ""
    return (
        f'<text x="{x}" y="{y}"{cls} font-size="{size}" font-weight="{weight}" fill="{fill}" '
        f'text-anchor="{anchor}" letter-spacing="{ls}"{extra}>{escape(s)}</text>'
    )


def fade_in(inner, begin, dy=10, dur=0.6):
    # Static state is the final state, so renderers without SMIL still show everything.
    total = begin + dur
    kt = f"0;{begin / total:.3f};1"
    return (
        f'<g><animate attributeName="opacity" values="0;0;1" keyTimes="{kt}" dur="{total:.2f}s"/>'
        f'<animateTransform attributeName="transform" type="translate" values="0 {dy};0 {dy};0 0" keyTimes="{kt}" dur="{total:.2f}s"/>'
        f"{inner}</g>"
    )


def grow(attr, final, begin, dur):
    """Animate attr from 0 to its final value; the element itself already holds the final value."""
    total = begin + dur
    return (
        f'<animate attributeName="{attr}" values="0;0;{final}" keyTimes="0;{begin / total:.3f};1" dur="{total:.2f}s"/>'
    )


def dot_grid(w, h, gid="dots"):
    d = (
        f'<pattern id="{gid}" width="24" height="24" patternUnits="userSpaceOnUse">'
        f'<circle cx="1" cy="1" r="1" fill="{TEXT}" fill-opacity="0.07"/></pattern>'
    )
    return d, f'<rect width="{w}" height="{h}" fill="url(#{gid})"/>'


# ---------------------------------------------------------------- hero
def hero():
    W, H = 1200, 480
    grid_def, grid = dot_grid(W, H)
    defs = grid_def + f'<clipPath id="frame"><rect width="{W}" height="{H}" rx="16"/></clipPath>'

    # pipeline nodes: (key, x, y, title, sub)
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
        return {
            "r": (x + bw, y + bh / 2), "l": (x, y + bh / 2),
            "b": (x + bw / 2, y + bh), "t": (x + bw / 2, y),
        }[side]

    p1, p2 = port("in", "r"), port("ai", "l")
    p3, p4 = port("ai", "b"), port("crm", "t")
    p5, p6 = port("crm", "l"), port("cal", "r")
    p7 = port("cal", "b")
    p8 = port("won", "t")
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
        f'<path d="{path}" fill="none" stroke="{DIM}" stroke-width="1.5"/>'
        f'<path d="{path}" fill="none" stroke="{LIME}" stroke-width="1.5" stroke-dasharray="4 10" opacity=".55">'
        f'<animate attributeName="stroke-dashoffset" from="28" to="0" dur="1.2s" repeatCount="indefinite"/></path>'
    )
    packets = ""
    for i in range(4):
        packets += (
            f'<rect x="-4" y="-4" width="8" height="8" fill="{LIME}">'
            f'<animateMotion path="{motion}" dur="5.2s" begin="{i * 1.3}s" repeatCount="indefinite" keyPoints="0;1" keyTimes="0;1" calcMode="linear"/></rect>'
        )

    boxes = ""
    for i, (k, (x, y, title, sub)) in enumerate(nodes.items()):
        won = k == "won"
        fill = LIME if won else PANEL
        stroke = LIME if won else "#2E3329"
        tc = BG if won else TEXT
        sc = "#2B3310" if won else MUTED
        inner = (
            f'<rect x="{x}" y="{y}" width="{bw}" height="{bh}" rx="10" fill="{fill}" stroke="{stroke}"/>'
            + t(x + 18, y + 31, title, 14, tc, 700, mono=True, ls=1.5)
            + t(x + 18, y + 53, sub, 12, sc, 400, mono=True)
            + t(x + bw - 16, y + 31, f"0{i + 1}", 11, sc, 400, mono=True, anchor="end")
        )
        if not won:
            # live led on each node, staggered
            inner += (
                f'<circle cx="{x + bw - 18}" cy="{y + 52}" r="3" fill="{LIME}" opacity=".2">'
                f'<animate attributeName="opacity" values=".2;1;.2" dur="5.2s" begin="{i * 1.05}s" repeatCount="indefinite"/></circle>'
            )
        boxes += fade_in(inner, 0.5 + i * 0.15)

    left = (
        fade_in(t(72, 196, "Rafael", 84, TEXT, 800, ls=-3), 0.1)
        + fade_in(
            t(72, 282, "Florindo", 84, TEXT, 800, ls=-3)
            + f'<rect x="404" y="262" width="20" height="20" fill="{LIME}"/>',
            0.25,
        )
        + fade_in(t(74, 330, "I engineer the system behind the operation.", 22, TEXT, 500), 0.45)
        + fade_in(
            t(74, 362, "AI agents that sell, CRMs that scale, integrations that don't break.", 15, MUTED, 400),
            0.6,
        )
    )
    tags = ["AI AGENTS", "GOHIGHLEVEL", "N8N", "TYPESCRIPT", "PYTHON", "POSTGRES"]
    tx = 74
    chips = ""
    for tag in tags:
        w = len(tag) * 7.9 + 22
        chips += (
            f'<rect x="{tx}" y="390" width="{w}" height="26" rx="4" fill="none" stroke="#2E3329"/>'
            + t(tx + w / 2, 407, tag, 11, MUTED, 500, mono=True, anchor="middle", ls=0.5)
        )
        tx += w + 8
    left += fade_in(chips, 0.75)

    top = (
        f'<line x1="0" y1="52" x2="{W}" y2="52" stroke="{LINE}"/>'
        f'<circle cx="40" cy="27" r="4" fill="{LIME}" class="pulse"/>'
        + t(54, 31, "SYSTEM ONLINE", 11, LIME, 600, mono=True, ls=1.5)
        + t(176, 31, "/  AUTOMATION & AI ENGINEER", 11, MUTED, 400, mono=True, ls=1.5)
        + t(W - 40, 31, "MINAS GERAIS, BR  →  WORKING WORLDWIDE", 11, MUTED, 400, mono=True, anchor="end", ls=1.5)
        + t(660, 92, "// the pipeline I build, live", 12, DIM, 400, mono=True)
    )
    bottom = (
        f'<line x1="0" y1="{H - 30}" x2="{W}" y2="{H - 30}" stroke="{LINE}"/>'
        + t(40, H - 11, "LEAD IN → QUALIFIED → ROUTED → BOOKED", 10, DIM, 400, mono=True, ls=2)
        + t(W - 40, H - 11, "GITHUB.COM/RAFAELLFLORINDO", 10, DIM, 400, mono=True, anchor="end", ls=2)
    )

    body = (
        f'<g clip-path="url(#frame)"><rect width="{W}" height="{H}" fill="{BG}"/>{grid}'
        f"{top}{left}{wires}{boxes}{packets}{bottom}</g>"
        f'<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="16" fill="none" stroke="{LINE}"/>'
    )
    title = "Rafael Florindo — Automation & AI Engineer. I engineer the system behind the operation."
    return svg(W, H, title, body, defs)


# ---------------------------------------------------------------- metrics
METRICS = [
    ("694", "", "AUTOMATED TESTS", "across my products"),
    ("17", "", "PRODUCTION WORKFLOWS", "live in production"),
    ("~30", "", "CALENDARS ROUTED BY AI", "routed by AI agents"),
    ("55.8", "%", "FASTER WITH AI", "thesis · p = 0.0017"),
]


def metrics():
    W, H = 1200, 150
    gap, n = 16, len(METRICS)
    cw = (W - gap * (n - 1)) / n
    body = ""
    for i, (num, unit, label, sub) in enumerate(METRICS):
        x = i * (cw + gap)
        inner = (
            f'<rect x="{x + .5}" y=".5" width="{cw - 1}" height="{H - 1}" rx="12" fill="{PANEL}" stroke="{LINE}"/>'
            f'<rect x="{x + 20}" y="22" width="6" height="6" fill="{LIME}"/>'
            + t(x + 34, 29, label, 11, MUTED, 500, mono=True, ls=1.2)
            + f'<text x="{x + 20}" y="94" font-size="52" font-weight="800" fill="{TEXT}" letter-spacing="-2">{escape(num)}'
            + (f'<tspan fill="{LIME}" font-size="32" dx="4">{unit}</tspan>' if unit else "")
            + "</text>"
            + t(x + 20, 124, sub, 13, DIM, 400, mono=True)
            + f'<rect x="{x + 20}" y="{H - 8}" height="2" width="{cw - 40}" fill="{LIME}">'
            + grow("width", cw - 40, 0.3 + i * 0.15, 1.2) + "</rect>"
        )
        body += fade_in(inner, 0.1 + i * 0.15)
    return svg(W, H, " · ".join(f"{n}{u} {l.lower()}" for n, u, l, _ in METRICS), body)


# ---------------------------------------------------------------- research
def research():
    W, H = 1200, 300
    max_w = 480
    conv, cop = 160.89, 71.17
    x0 = 220
    bars = ""
    for i, (label, val, color, tc) in enumerate(
        [("CONVENTIONAL", conv, DIM, TEXT), ("WITH COPILOT", cop, LIME, LIME)]
    ):
        y = 112 + i * 64
        w = max_w * val / conv
        bars += (
            t(40, y + 22, label, 12, MUTED, 500, mono=True, ls=1.2)
            + f'<rect x="{x0}" y="{y}" width="{max_w}" height="32" rx="4" fill="#161915"/>'
            + f'<rect x="{x0}" y="{y}" width="{w:.1f}" height="32" rx="4" fill="{color}">'
            + grow("width", f"{w:.1f}", 0.4 + i * 0.3, 1.4) + "</rect>"
            + fade_in(t(x0 + w + 14, y + 22, f"{val:.2f} min", 15, tc, 700, mono=True), 1.6 + i * 0.3, dy=0)
        )
    right = 860
    side = (
        f'<line x1="{right - 30}" y1="96" x2="{right - 30}" y2="{H - 40}" stroke="{LINE}"/>'
        + t(right, 112, "MEAN COMPLETION TIME", 11, MUTED, 500, mono=True, ls=1.2)
        + f'<text x="{right - 4}" y="176" font-size="64" font-weight="800" fill="{LIME}" letter-spacing="-3">−55.8<tspan font-size="36">%</tspan></text>'
        + t(right, 206, "p = 0.0017 · n = 35 + 35", 13, TEXT, 500, mono=True)
        + t(right, 240, "Functional tests: +7 p.p.", 13, MUTED, 400, mono=True)
        + t(right, 260, "not statistically significant", 13, AMBER, 400, mono=True)
    )
    head = (
        t(40, 48, "THESIS · UNIVÉRTIX · POSTER AT FAVE 2026", 11, LIME, 600, mono=True, ls=1.5)
        + t(40, 78, "Does generative AI make developers faster? Yes. Better? Not proven yet.", 20, TEXT, 600)
    )
    body = (
        f'<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="14" fill="{PANEL}" stroke="{LINE}"/>'
        + head + bars + fade_in(side, 1.2)
    )
    return svg(W, H, "Thesis: Copilot-assisted developers finished 55.8% faster (160.89 → 71.17 min, p = 0.0017); quality gain not significant.", body)


# ---------------------------------------------------------------- section headers
def header(num, title, note):
    W, H = 1200, 64
    tw = len(title) * 13.2
    body = (
        t(0, 40, num, 13, LIME, 700, mono=True, ls=1)
        + t(36, 41, title, 22, TEXT, 800, ls=1)
        + f'<line x1="{36 + tw + 24}" y1="34" x2="{W}" y2="34" stroke="{LINE}"/>'
        + f'<rect x="{36 + tw + 24}" y="33" width="80" height="2" fill="{LIME}">'
        f'<animate attributeName="x" from="{36 + tw + 24}" to="{W - 80}" dur="4s" repeatCount="indefinite"/>'
        f'<animate attributeName="opacity" values="0;1;1;0" keyTimes="0;.1;.85;1" dur="4s" repeatCount="indefinite"/></rect>'
        + t(W, 58, note, 11, DIM, 400, mono=True, anchor="end", ls=1)
    )
    return svg(W, H, title, body)


HEADERS = [
    ("01", "WHAT I BUILD", "// the layers behind revenue operations"),
    ("02", "SELECTED WORK", "// a few things I have shipped"),
    ("03", "RESEARCH", "// generative AI × software engineering"),
    ("04", "TOOLKIT", "// what I reach for, and why"),
    ("05", "HOW I WORK", "// AI as an execution and review layer"),
]


# ---------------------------------------------------------------- capability cards
CAPS = [
    ("AI AGENTS", "Qualify, answer, route and book —", "with guardrails and human handoff."),
    ("CRM ARCHITECTURE", "GoHighLevel snapshots, pipelines and", "white-label setups that hold at scale."),
    ("INTEGRATIONS", "APIs, webhooks and n8n flows with", "retries and idempotency built in."),
    ("PRODUCT ENGINEERING", "TypeScript, Python, Postgres, workers", "and tests — internal tools and SaaS."),
]


def capabilities():
    W, H = 1200, 196
    gap = 16
    cw = (W - gap * 3) / 4
    body = ""
    icons = [
        # simple geometric glyphs, drawn at (x,y)
        lambda x, y: f'<circle cx="{x + 12}" cy="{y + 12}" r="11" fill="none" stroke="{LIME}" stroke-width="2"/><circle cx="{x + 12}" cy="{y + 12}" r="4" fill="{LIME}"/>',
        lambda x, y: f'<rect x="{x}" y="{y}" width="24" height="24" rx="3" fill="none" stroke="{LIME}" stroke-width="2"/><path d="M{x} {y + 9}H{x + 24}M{x + 9} {y + 9}V{y + 24}" stroke="{LIME}" stroke-width="2"/>',
        lambda x, y: f'<path d="M{x} {y + 12}H{x + 8}M{x + 16} {y + 12}H{x + 24}" stroke="{LIME}" stroke-width="2"/><circle cx="{x + 12}" cy="{y + 12}" r="4" fill="none" stroke="{LIME}" stroke-width="2"/><circle cx="{x + 2}" cy="{y + 12}" r="2" fill="{LIME}"/><circle cx="{x + 22}" cy="{y + 12}" r="2" fill="{LIME}"/>',
        lambda x, y: f'<path d="M{x + 7} {y + 4}L{x} {y + 12}L{x + 7} {y + 20}M{x + 17} {y + 4}L{x + 24} {y + 12}L{x + 17} {y + 20}" fill="none" stroke="{LIME}" stroke-width="2"/>',
    ]
    for i, (title, l1, l2) in enumerate(CAPS):
        x = i * (cw + gap)
        inner = (
            f'<rect x="{x + .5}" y=".5" width="{cw - 1}" height="{H - 1}" rx="12" fill="{PANEL}" stroke="{LINE}"/>'
            + icons[i](x + 22, 24)
            + t(x + cw - 20, 40, f"0{i + 1}", 11, DIM, 400, mono=True, anchor="end")
            + t(x + 22, 92, title, 15, TEXT, 700, mono=True, ls=1)
            + t(x + 22, 124, l1, 13, MUTED, 400)
            + t(x + 22, 144, l2, 13, MUTED, 400)
        )
        body += fade_in(inner, 0.1 + i * 0.12)
    return svg(W, H, "What I build: AI agents, CRM architecture, integrations, product engineering", body)


# ---------------------------------------------------------------- footer
def footer():
    W, H = 1200, 120
    body = (
        f'<line x1="0" y1="40" x2="{W}" y2="40" stroke="{LINE}"/>'
        f'<rect x="0" y="39" width="140" height="2" fill="{LIME}">'
        f'<animate attributeName="x" from="-140" to="{W}" dur="5s" repeatCount="indefinite"/></rect>'
        + t(W / 2, 82, "END OF TRANSMISSION", 12, MUTED, 500, mono=True, anchor="middle", ls=4)
        + f'<rect x="{W / 2 + 104}" y="71" width="8" height="13" fill="{LIME}" class="pulse"/>'
        + t(W / 2, 106, "thanks for stopping by", 12, DIM, 400, mono=True, anchor="middle", ls=1)
    )
    return svg(W, H, "End of transmission — thanks for stopping by", body)


def main():
    files = {
        "banner.svg": hero(),
        "metrics.svg": metrics(),
        "research.svg": research(),
        "capabilities.svg": capabilities(),
        "outro.svg": footer(),
    }
    for num, title, note in HEADERS:
        files[f"h-{num}.svg"] = header(num, title, note)
    try:
        import sys; sys.path.insert(0, str(Path(__file__).parent)); import projects
        files.update(projects.build(globals()))
    except ImportError:
        pass
    for name, content in files.items():
        (OUT / name).write_text(content, encoding="utf-8")
    print(f"wrote {len(files)} files to {OUT}")


if __name__ == "__main__":
    main()
