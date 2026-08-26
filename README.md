<div align="center">

# Rafael Florindo

### Automation & AI Engineer

**AI Agents · Business Automation · CRM Architecture · APIs · SaaS**

I design and ship production-ready systems that connect **AI, automation, CRM, and software engineering** — turning manual sales and operations into reliable, scalable workflows.

<br>

<a href="https://www.linkedin.com/in/rafael-florindo">
  <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect with Rafael Florindo on LinkedIn">
</a>
<a href="mailto:rafaelflorindodev@gmail.com">
  <img src="https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email Rafael Florindo">
</a>
<a href="https://wa.me/5531997900284">
  <img src="https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="Contact Rafael Florindo on WhatsApp">
</a>

</div>

---

## About me

I'm an **Automation & AI Engineer based in Brazil**, working on technical implementations at **High Ticket Club** and **Valente AI** while studying Computer Science at **Univértix**.

I work between the speed of low-code platforms and the depth of software engineering: **GoHighLevel and n8n** when they are the right tools; **Python, TypeScript, APIs, databases, background workers, tests, and infrastructure** when the problem requires custom logic.

My work covers lead qualification, customer service, follow-up, onboarding, CRM provisioning, opportunity routing, sales-call analysis, executive dashboards, AI voice agents, and multi-tenant SaaS products.

> **I don't automate clicks. I build operational systems designed to remain predictable when data is incomplete, APIs fail, or human intervention is required.**

---

## What I build

| Area | What I deliver |
| --- | --- |
| **AI Agents** | Voice and conversational agents for qualification, support, booking, follow-up, triage, and sales handoff |
| **Business Automation** | Event-driven workflows, API integrations, webhooks, onboarding, reporting, and data processing |
| **CRM Architecture** | Pipelines, lead scoring, routing, snapshots, workflows, custom fields, and reusable GoHighLevel environments |
| **Product Engineering** | Multi-tenant SaaS, internal tools, dashboards, backend services, and AI-assisted applications |

---

## Selected engineering work

### Escaluz — AI offer intelligence SaaS

`Private product` · `In active development`

A multi-tenant platform for researching, analyzing, and modeling digital offers. It combines Meta Ad Library mining, creative analysis, VSL transcription, AI classification, offer tracking, agent-assisted copy, page recreation, and media processing in one workflow.

- Built the application with **Next.js, TypeScript, Prisma, PostgreSQL, and dedicated background workers**.
- Integrated **Gemini, Groq Whisper, ElevenLabs, Playwright, and FFmpeg** for analysis and content pipelines.
- Implemented resource ownership checks, authenticated route coverage, encrypted provider secrets, and SSRF defenses.
- Latest local verification: **340 automated tests passing across 47 test files**.

`Next.js` · `TypeScript` · `PostgreSQL` · `Prisma` · `Vitest` · `AI APIs`

### AI voice agents connected to CRM operations

Reusable voice-agent architecture for inbound and outbound sales workflows. Agents can qualify leads, identify intent, update the CRM, book appointments, trigger follow-up sequences, and hand qualified opportunities to a human closer.

- Built with **VAPI, ElevenLabs, Twilio, n8n, and GoHighLevel**.
- Implemented webhook-driven outbound calls and multi-day call cadences.
- Designed guardrails, structured conversation goals, routing rules, and human handoff paths.

`VAPI` · `ElevenLabs` · `Twilio` · `n8n` · `GoHighLevel`

### Automated GoHighLevel provisioning and snapshot architecture

Systems that turn onboarding data into reusable CRM environments, reducing repetitive setup across clients and verticals.

- Automated subaccount creation, custom-value population, initial configuration, and onboarding distribution.
- Built reusable snapshot architectures for legal, dental, automotive, aesthetic, franchise, and US home-service operations.
- Implementations include a **17-workflow legal structure** and a **12-workflow dental structure**.

`GoHighLevel API` · `n8n` · `Webhooks` · `REST APIs`

### AI sales-call scoring

An automated pipeline that converts recorded sales calls into structured coaching data.

```text
Call recording → Whisper transcription → LLM evaluation → Script comparison → Score and recommendations
```

The workflow evaluates script adherence, discovery quality, objection handling, missed opportunities, and sales-process execution, then stores structured results for reporting.

`OpenAI Whisper` · `Structured LLM Output` · `n8n` · `Google Sheets`

### MatchGoal — football analytics SaaS

A football data and analytics product built for the **2026 FIFA World Cup**. I co-develop the platform and own the **n8n integrations and payment infrastructure**, connecting the product layer to its operational workflows.

`Next.js` · `Supabase` · `Vercel` · `n8n` · `AbacatePay`

> Some implementations are private or belong to clients. The architecture and outcomes are described here without exposing proprietary code, credentials, or confidential business data.

---

## Public projects

| Project | What it demonstrates | Stack |
| --- | --- | --- |
| [**NotaZen**](https://github.com/RafaellFlorindo/NotaZen) | Privacy-first, offline-capable financial PWA for Brazilian solo entrepreneurs. Uses integer-cent calculations, validated local persistence, CSV export, and JSON backup. | React 19, Vite, Tailwind, Vitest |
| [**NEW Energy Executive Dashboard**](https://github.com/RafaellFlorindo/Dashboard-New-Energia) · [Live](https://dashboard-new-energia.vercel.app) | Executive KPI application that consolidates CRM and weekly operational data into commercial, marketing, engineering, and operations views. | Next.js, TypeScript, Supabase, Recharts |
| [**Skills for Claude Code**](https://github.com/RafaellFlorindo/Skills-Claude) | A curated skill library for AI-assisted copywriting, product design, SEO, frontend engineering, and code review workflows. | Markdown, JavaScript, AI tooling |

---

## Research — Generative AI × Software Engineering

My Computer Science thesis analyzes controlled experimental data comparing conventional development with AI-assisted development.

Across **70 completed observations**, the AI-assisted group finished the programming task **55.8% faster** on average. The functional-quality difference was not statistically significant — an important distinction between producing code faster and producing better engineering outcomes.

The research evaluates:

- development time and functional correctness;
- automated test approval;
- code quality and maintainability;
- the real productivity impact of generative AI.

---

## Core stack

| Domain | Technologies |
| --- | --- |
| **AI & Automation** | OpenAI, Gemini, n8n, VAPI, ElevenLabs, Twilio, LLM workflows, AI agents |
| **CRM & Integrations** | GoHighLevel, REST APIs, webhooks, lead routing, Conversation AI, Voice AI |
| **Backend** | Python, FastAPI, Flask, Node.js, background workers, event-driven workflows |
| **Frontend & Products** | TypeScript, JavaScript, Next.js, React, Vite, Tailwind CSS |
| **Data & Infrastructure** | PostgreSQL, Supabase, Prisma, SQLite, Docker, Vercel, Linux |
| **Quality & Delivery** | Git, GitHub Actions, Vitest, Playwright, automated testing, security review |

---

## Engineering principles

```text
Trigger
  ↓
Validation
  ↓
Business logic
  ↓
External services
  ↓
Error handling + observability
  ↓
Fallback or human handoff
  ↓
Predictable result
```

- Design for failure, retries, and partial data — not only the happy path.
- Keep integrations observable and business rules explicit.
- Test critical behavior, authentication, and tenant isolation.
- Productize repeated work into reusable workflows, snapshots, and services.
- Balance automation depth with infrastructure cost and operational margin.

---

<div align="center">

## Let's build something reliable

If you're working on **AI agents, business automation, CRM systems, API integrations, internal tools, or SaaS**, let's connect.

<a href="https://www.linkedin.com/in/rafael-florindo">
  <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect with Rafael Florindo on LinkedIn">
</a>
<a href="mailto:rafaelflorindodev@gmail.com">
  <img src="https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email Rafael Florindo">
</a>
<a href="https://wa.me/5531997900284">
  <img src="https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="Contact Rafael Florindo on WhatsApp">
</a>

<br><br>

**Rafael Florindo**  
`Automation & AI Engineer`

</div>
