"""Project cards for the 'Selected work' section. Imported by build_assets.py."""
import textwrap

PROJECTS = [
    {
        "slug": "escaluz",
        "name": "Escaluz",
        "status": "PRODUCTION-GRADE",
        "kind": "SAAS",
        "pitch": "Offer-intelligence SaaS: reads the Meta Ad Library, breaks down creatives and generates new ads with AI copy, image and voice agents.",
        "proof": [
            "154 test files · CI runs typecheck, lint, test, build",
            "Multi-tenant ADR · billing with usage reservations",
            "Worker queue · 24 migrations · Sentry · Semgrep",
        ],
        "stack": ["NEXT.JS", "TYPESCRIPT", "POSTGRES", "OPENAI"],
    },
    {
        "slug": "sof-juridico",
        "name": "SOF Jurídico",
        "status": "NEAR PRODUCTION",
        "kind": "SAAS",
        "pitch": "Practice-management SaaS for Brazilian law firms: scheduling, cases, client CRM and an AI intake agent on web chat and WhatsApp.",
        "proof": [
            "50 migrations · 26 edge functions · iOS + Android",
            "Row-level security per role, tested on throwaway Postgres",
            "Claude agent with fallback model + monthly budget per firm",
        ],
        "stack": ["REACT", "SUPABASE", "CLAUDE", "CAPACITOR"],
    },
    {
        "slug": "zapcrm",
        "name": "ZapCRM",
        "status": "SHIPPED · v1.16",
        "kind": "CHROME EXTENSION",
        "pitch": "A CRM that lives inside WhatsApp Web: kanban funnel, labels, quick replies, message flows and scheduled follow-ups. No server.",
        "proof": [
            "Shadow DOM panel that survives WhatsApp's own DOM",
            "Cross-tab send lock · business-hours throttling",
            "Playwright tests · versioned changelog",
        ],
        "stack": ["REACT", "TYPESCRIPT", "MANIFEST V3", "PLAYWRIGHT"],
    },
    {
        "slug": "htc-ops",
        "name": "HTC Ops",
        "status": "IN DAILY USE",
        "kind": "INTERNAL TOOL",
        "pitch": "Customer-success cockpit for High Ticket Club: every 15 minutes Claude drafts member messages and call scripts into today's queue.",
        "proof": [
            "Autonomy levels: manual → approve → auto with daily caps",
            "Meet transcripts summarized into GoHighLevel notes",
            "GHL OAuth through an n8n broker · Slack tickets",
        ],
        "stack": ["NEXT.JS", "GOHIGHLEVEL", "N8N", "CLAUDE"],
    },
    {
        "slug": "growth-dialer",
        "name": "Growth Dialer",
        "status": "BETA",
        "kind": "SAAS",
        "pitch": "Prospecting SaaS: dials 1–10 lines in parallel, hands answered calls to AI voice agents and builds lead lists from public company data.",
        "proof": [
            "Twilio Voice · answering-machine detection",
            "ElevenLabs agents · conference bridge to the browser",
            "Workspaces with plans, limits and signed webhooks",
        ],
        "stack": ["NEXT.JS", "PRISMA", "TWILIO", "ELEVENLABS"],
    },
    {
        "slug": "gravacao-automatica",
        "name": "Gravação Automática",
        "status": "EXPERIMENT",
        "kind": "AI VIDEO PIPELINE",
        "pitch": "Camera-free videos driven by Claude Code: an AI avatar presents, the product is captured in 4K and the edit assembles itself.",
        "proof": [
            "HeyGen avatar reads the script",
            "Scenes are functions of time, rendered in Chrome",
            "Remotion edit orchestrated by Claude skills",
        ],
        "stack": ["CLAUDE CODE", "HEYGEN", "REMOTION"],
    },
]


def build(g):
    t, svg, fade_in, escape = g["t"], g["svg"], g["fade_in"], g["escape"]
    PANEL, LINE, TEXT, MUTED, DIM, LIME = (g[k] for k in ("PANEL", "LINE", "TEXT", "MUTED", "DIM", "LIME"))
    W, H = 592, 300
    out = {}
    for i, p in enumerate(PROJECTS):
        live = p["status"] in ("PRODUCTION-GRADE", "SHIPPED · v1.16", "IN DAILY USE")
        sw = len(p["status"]) * 7.2 + 34
        head = (
            t(24, 38, f"P/0{i + 1}", 11, LIME, 700, mono=True, ls=1)
            + t(72, 38, f"{p['kind']}  ·  PRIVATE REPO", 11, DIM, 500, mono=True, ls=1)
            + f'<rect x="{W - 24 - sw}" y="22" width="{sw}" height="24" rx="12" fill="none" stroke="{LIME if live else "#3A3F34"}"/>'
            + f'<circle cx="{W - 24 - sw + 14}" cy="34" r="3.5" fill="{LIME if live else MUTED}"'
            + (' class="pulse"' if live else "")
            + "/>"
            + t(W - 24 - sw + 24, 38, p["status"], 11, LIME if live else MUTED, 600, mono=True)
        )
        name = t(24, 90, p["name"], 32, TEXT, 800, ls=-1)
        lines = textwrap.wrap(p["pitch"], 72)
        assert len(lines) <= 2, f"{p['name']}: pitch must fit in two lines"
        pitch = "".join(
            t(24, 124 + j * 22, line, 15, MUTED, 400)
            for j, line in enumerate(lines)
        )
        proof = "".join(
            f'<rect x="24" y="{177 + j * 22}" width="6" height="6" fill="{LIME}"/>'
            + t(40, 186 + j * 22, line, 13, TEXT, 400, mono=True)
            for j, line in enumerate(p["proof"])
        )
        cx, chips = 24, ""
        for s in p["stack"]:
            w = len(s) * 7 + 20
            chips += (
                f'<rect x="{cx}" y="{H - 44}" width="{w}" height="22" rx="4" fill="#161915" stroke="{LINE}"/>'
                + t(cx + w / 2, H - 29, s, 10, MUTED, 500, mono=True, anchor="middle", ls=0.5)
            )
            cx += w + 6
        body = (
            f'<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="14" fill="{PANEL}" stroke="{LINE}"/>'
            f'<rect x="24" y=".5" width="64" height="2" fill="{LIME}"/>'
            + fade_in(head + name + pitch, 0.1)
            + fade_in(proof + chips, 0.35)
        )
        title = f"{p['name']} — {p['pitch']}"
        out[f"project-{p['slug']}.svg"] = svg(W, H, title, body)
    return out
