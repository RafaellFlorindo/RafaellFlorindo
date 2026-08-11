<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0F172A,50:1E3A8A,100:0EA5E9&height=200&section=header&text=Rafael%20Florindo&fontSize=52&fontColor=FFFFFF&fontAlignY=32&desc=GoHighLevel%20Specialist%20%C2%B7%20Automation%20Engineer&descAlignY=52&descSize=18" width="100%" />

<p align="center">
<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=20&duration=3500&pause=1000&color=0EA5E9&center=true&vCenter=true&multiline=false&repeat=true&width=600&height=45&lines=Processo+manual+%E2%86%92+sistema+que+roda+sozinho;IA+respondendo+lead+%C3%A0s+2h+da+manh%C3%A3;Pipeline+em+produ%C3%A7%C3%A3o%2C+n%C3%A3o+funil+bonito" alt="Rafael Florindo" />
</p>

<p align="center">
<img src="https://img.shields.io/badge/High%20Ticket%20Club-Automation%20Engineer-0EA5E9?style=for-the-badge&labelColor=0F172A" />
<img src="https://img.shields.io/badge/GoHighLevel-Specialist-1E3A8A?style=for-the-badge&labelColor=0F172A" />
<img src="https://img.shields.io/badge/Ci%C3%AAncia%20da%20Computa%C3%A7%C3%A3o-Univ%C3%A9rtix%20%C2%B7%207%C2%BA%20per%C3%ADodo-334155?style=for-the-badge&labelColor=0F172A" />
</p>

<p align="center">
<a href="https://www.linkedin.com/in/rafael-florindo/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white" /></a>
<a href="mailto:rafaelflorindodev@gmail.com"><img src="https://img.shields.io/badge/E--mail-EA4335?style=flat-square&logo=gmail&logoColor=white" /></a>
<a href="https://wa.me/5531997900284"><img src="https://img.shields.io/badge/WhatsApp-25D366?style=flat-square&logo=whatsapp&logoColor=white" /></a>
<img src="https://komarev.com/ghpvc/?username=RafaellFlorindo&style=flat-square&color=0EA5E9&label=perfil+visto" />
</p>

</div>

---

## 🧭 Quem sou

Meu trabalho é pegar processo comercial manual — atendimento, qualificação, follow-up — e transformar em **sistema que roda sozinho dentro de um CRM**.

Faço isso como técnico no **High Ticket Club**, uma das maiores agências afiliadas GoHighLevel do mercado. Curso **Ciência da Computação na Univértix (7º período)**, o que me dá base pra descer ao código quando o no-code trava.

> **Não entrego funil bonito. Entrego pipeline rodando em produção, com IA respondendo lead às 2h da manhã.**

---

## 🎯 O que eu resolvo

<table>
<tr>
<td width="33%" valign="top">

### 🧊 Lead que esfria na fila

Agentes de IA (**voz e texto**) que qualificam por conversa real, pontuam intenção e só devolvem pro humano o que vale fechar.

`VAPI` `ElevenLabs` `Conversation AI`

</td>
<td width="33%" valign="top">

### 📉 CRM que ninguém usa

Implantação de **GoHighLevel white-label ponta a ponta** — estrutura, snapshot, integração e onboarding. O sistema só serve se o time adotar.

`GHL` `Snapshots` `Onboarding`

</td>
<td width="33%" valign="top">

### ⏳ Trabalho repetitivo que come margem

Automações em **N8N** que substituem tarefa manual por fluxo: criação de subconta, distribuição de lead, scoring de call, dashboard executivo.

`N8N` `Webhooks` `REST API`

</td>
</tr>
</table>

---

## 🔁 Como o sistema funciona

```mermaid
flowchart LR
    A[Lead entra<br/>site · anúncio · WhatsApp] --> B[IA de triagem<br/>voz ou texto]
    B --> C{Qualificado?}
    C -->|Sim| D[Classificação por produto<br/>+ scoring de intenção]
    C -->|Não| E[Nutrição automática<br/>follow-up cadenciado]
    D --> F[Oportunidade no CRM<br/>SDR notificado · round-robin]
    F --> G[Humano fecha]
    E --> B
    F --> H[Dashboard executivo<br/>KPIs por departamento]

    style A fill:#0F172A,stroke:#0EA5E9,color:#fff
    style B fill:#1E3A8A,stroke:#0EA5E9,color:#fff
    style D fill:#1E3A8A,stroke:#0EA5E9,color:#fff
    style F fill:#0EA5E9,stroke:#0F172A,color:#0F172A
    style G fill:#16A34A,stroke:#0F172A,color:#fff
    style H fill:#334155,stroke:#0EA5E9,color:#fff
```

---

## 🚀 Sistemas em produção

| Projeto | O que faz | Stack |
|---|---|---|
| **Agentes de voz com IA** | Atendimento e qualificação por voz, integrado ao CRM, com cadência de rechamada | `VAPI` `ElevenLabs` `Twilio` `GHL` |
| **Snapshots white-label** | Templates reutilizáveis de GoHighLevel por vertical (advocacia, odonto, concessionária, clínica estética, franquia) | `GHL` `Automações` `Custom Values` |
| **Automação de subconta** | Criação de subconta e preenchimento de custom values a partir do formulário de onboarding | `N8N` `Webhooks` `GHL API` |
| **Scoring de call por IA** | Transcrição e nota automática de ligação de vendas contra o script comercial | `N8N` `Whisper` `OpenAI` `Sheets` |
| **Funil + triagem por IA** | CRM do zero, triagem automática de lead, roteamento por produto e dashboard executivo | `GHL` `N8N` `Next.js` `Supabase` |
| **MatchGoal** | SaaS de analytics de futebol para a Copa do Mundo 2026 | `Next.js` `Vercel` `Supabase` `N8N` |

<details>
<summary><b>📂 Por que a maior parte dos repositórios não está pública</b></summary>

<br/>

São sistemas em operação, com dados e credenciais de clientes ativos. O que eu consigo mostrar em conversa:

- Arquitetura do fluxo (diagrama e decisões de engenharia)
- Demo em ambiente controlado
- Trechos de workflow N8N e estrutura de prompt sanitizados

</details>

---

## 🛠️ Ferramentas

<div align="center">

**Automação & IA**

<p align="center">
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/n8n-EA4B71?style=for-the-badge&logo=n8n&logoColor=white" />
<img src="https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white" />
<img src="https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white" />
<img src="https://img.shields.io/badge/VAPI-0EA5E9?style=for-the-badge&logoColor=white" />
<img src="https://img.shields.io/badge/ElevenLabs-000000?style=for-the-badge&logoColor=white" />
</p>

**CRM & Vendas**

<p align="center">
<img src="https://img.shields.io/badge/GoHighLevel-155EEF?style=for-the-badge&logoColor=white" />
<img src="https://img.shields.io/badge/REST%20API-005571?style=for-the-badge&logo=fastapi&logoColor=white" />
<img src="https://img.shields.io/badge/Webhooks-6D28D9?style=for-the-badge&logo=webhook&logoColor=white" />
<img src="https://img.shields.io/badge/Twilio-F22F46?style=for-the-badge&logo=twilio&logoColor=white" />
</p>

**Backend & Infra**

<p align="center">
<img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" />
<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
<img src="https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white" />
<img src="https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white" />
<img src="https://img.shields.io/badge/Supabase-3FCF8E?style=for-the-badge&logo=supabase&logoColor=white" />
<img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" />
<img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black" />
</p>

**Base**

<p align="center">
<img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" />
<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white" />
<img src="https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white" />
</p>

</div>

---

## 📊 Painel

<div align="center">

<p align="center">
<img height="170" src="https://github-readme-stats-git-masterrstaa-rickstaa.vercel.app/api?username=RafaellFlorindo&show_icons=true&hide_border=true&title_color=0EA5E9&icon_color=0EA5E9&text_color=94A3B8&bg_color=0F172A&include_all_commits=true&count_private=true&cache_seconds=86400" alt="Estatísticas do GitHub" />
<img height="170" src="https://github-readme-stats-git-masterrstaa-rickstaa.vercel.app/api/top-langs/?username=RafaellFlorindo&layout=compact&hide_border=true&title_color=0EA5E9&text_color=94A3B8&bg_color=0F172A&langs_count=8&cache_seconds=86400" alt="Linguagens mais usadas" />
</p>

<p align="center">
<img height="170" src="https://streak-stats.demolab.com?user=RafaellFlorindo&hide_border=true&background=0F172A&stroke=0EA5E9&ring=0EA5E9&fire=0EA5E9&currStreakLabel=0EA5E9&sideLabels=94A3B8&currStreakNum=FFFFFF&sideNums=FFFFFF&dates=64748B" alt="Sequência de contribuições" />
</p>

</div>

---

## 🔬 Pesquisa — TCC

> ### *Análise Comparativa entre Reuso Tradicional de Código e Desenvolvimento Assistido por IA Generativa*
> **Um Experimento Controlado sobre Produtividade** — Univértix

**📌 Questão central:** IA generativa torna devs mais produtivos — ou apenas mais rápidos em criar problemas novos?

**📊 Variáveis medidas:**

| Variável | O que mede |
|---|---|
| ⏱️ Tempo de conclusão | Velocidade real de entrega da tarefa |
| 🧩 Qualidade do código | Aderência a boas práticas e legibilidade |
| ✅ Aprovação em testes | Corretude funcional verificada |
| 🔧 Manutenibilidade | Custo de evoluir o código depois |

---

<div align="center">

### 💬 Quer ver rodando?

Arquitetura, decisões técnicas e demo eu mostro em conversa.

<p align="center">
<a href="https://www.linkedin.com/in/rafael-florindo/"><img src="https://img.shields.io/badge/Falar%20comigo%20no%20LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" /></a>
<a href="mailto:rafaelflorindodev@gmail.com"><img src="https://img.shields.io/badge/Me%20mandar%20um%20e--mail-EA4335?style=for-the-badge&logo=gmail&logoColor=white" /></a>
</p>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0EA5E9,50:1E3A8A,100:0F172A&height=120&section=footer" width="100%" />

</div>
