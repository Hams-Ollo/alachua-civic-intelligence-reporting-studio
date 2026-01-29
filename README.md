# 🏛️ Alachua Civic Intelligence System

**An AI-powered local government accountability monitoring platform**

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![LangGraph](https://img.shields.io/badge/orchestration-LangGraph-orange.svg)](https://langchain-ai.github.io/langgraph/)
[![Supabase](https://img.shields.io/badge/database-Supabase-green.svg)](https://supabase.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Location:** 📍 City of Alachua, Alachua County, Florida, USA  
**Version:** 2.0 (Automated Architecture)  
**Status:** 🚧 Active Development

> *"Understanding systems is the path to freedom."*

---

## 🎯 The Problem

Local government decisions happen fast. Agendas are posted days before meetings. Permit applications are buried in obscure portals. Public notices appear in newspapers most people don't read. By the time citizens learn about a development project threatening their water supply, it's often too late to respond.

**The Tara Development Case Study:**  
The "Tara" development portfolio (~580 acres, 1,000+ homes) sits directly above **Mill Creek Sink**—a karst feature with a proven 12-day hydrologic connection to Hornsby Spring via the Floridan Aquifer. Despite documented environmental concerns, the project has advanced through fragmented municipal processes across City, County, and State agencies.

This system exists to ensure **no civic action goes unnoticed**.

---

## 💡 The Solution

An automated **AI agent system** that continuously monitors 15+ government data sources, detects new documents within hours of publication, extracts actionable intelligence, and generates weekly reports for community distribution.

```mermaid
flowchart TB
    subgraph Sources["🌐 Government Data Sources"]
        S1[City of Alachua<br/>CivicClerk Portal]
        S2[Alachua County<br/>eScribe Meetings]
        S3[SRWMD<br/>Water Permits]
        S4[Florida Public Notices<br/>Legal Notices]
        S5[County GIS<br/>Map Genius]
    end

    subgraph Monitor["👁️ Change Detection"]
        CD[Playwright + Firecrawl<br/>SPA Scraping]
        PDF[PDF Processor<br/>pdfplumber + Gemini]
    end

    subgraph Agents["🤖 LangGraph Agent Orchestration"]
        subgraph L1["Layer 1: Scouts (Daily)"]
            A1[A1: Meeting Scout]
            A2[A2: Permit Scout]
            A3[A3: Legislative Monitor]
        end
        
        subgraph L2["Layer 2: Analysts (Weekly)"]
            B1[B1: Impact Analyst]
            B2[B2: Procedural Analyst]
        end
        
        subgraph L3["Layer 3: Synthesizers (Monthly)"]
            C1[C1: Newsletter Generator]
            C2[C2: Social Media Planner]
        end
    end

    subgraph Storage["💾 Knowledge Base"]
        DB[(Supabase PostgreSQL<br/>Structured Reports)]
        VEC[(pgvector<br/>Semantic Search)]
        DOCS[(Document Archive<br/>Original PDFs)]
    end

    subgraph Output["📤 Community Distribution"]
        NEWS[Weekly Newsletter]
        DASH[Alert Dashboard]
        API[REST API]
    end

    Sources --> Monitor
    Monitor --> L1
    L1 --> DB
    DB --> L2
    L2 -->|Human Approval| L3
    L3 --> NEWS & DASH
    DB --> VEC
    DOCS --> VEC
```

---

## 🏗️ System Architecture

### Three-Layer Agent Framework

| Layer | Agents | Frequency | Purpose |
|:------|:-------|:----------|:--------|
| **Layer 1: Scouts** | A1-A4 | Daily | Data collection from government portals. Deterministic, fact-based extraction. |
| **Layer 2: Analysts** | B1-B2 | Weekly | Pattern recognition across Scout data. Deep research via Tavily. |
| **Layer 3: Synthesizers** | C1-C4 | Monthly | Public-facing content generation. Requires human approval before publishing. |

### Technology Stack

```mermaid
graph LR
    subgraph Frontend["🖥️ API Layer"]
        FAST[FastAPI + Uvicorn]
        SSE[Server-Sent Events]
    end

    subgraph Orchestration["🔀 Orchestration"]
        LG[LangGraph<br/>Multi-Agent Workflows]
        APS[APScheduler<br/>Cron Jobs]
    end

    subgraph AI["🧠 AI/ML"]
        GEM[Gemini 2.5 Pro/Flash]
        TAV[Tavily Search]
        EMB[Embeddings + RAG]
    end

    subgraph Data["💾 Data Layer"]
        SUP[(Supabase<br/>PostgreSQL + pgvector)]
        STORE[(Supabase Storage<br/>PDF Archive)]
    end

    subgraph Scraping["🕷️ Scraping"]
        PW[Playwright<br/>SPA Rendering]
        FC[Firecrawl<br/>LLM-ready Markdown]
        PP[pdfplumber<br/>PDF Extraction]
    end

    FAST --> LG
    LG --> GEM & TAV
    LG --> SUP
    APS --> LG
    Scraping --> LG
    GEM --> EMB --> SUP
```

| Component | Technology | Purpose |
|:----------|:-----------|:--------|
| **Web Server** | FastAPI + Uvicorn | REST API, SSE streaming, approval endpoints |
| **Orchestration** | LangGraph | Multi-agent workflows with human-in-the-loop |
| **Scheduling** | APScheduler | Daily/weekly/monthly cron triggers |
| **LLM** | Gemini 2.5 Pro & Flash | Pro for reasoning, Flash for extraction |
| **Search** | Tavily | AI-optimized web research |
| **Database** | Supabase (PostgreSQL) | Structured data, JSONB, pgvector |
| **Document Storage** | Supabase Storage | PDF archive with full traceability |
| **Validation** | Pydantic v2 | Strict schemas for all data |
| **Scraping** | Playwright + Firecrawl | JavaScript rendering, PDF processing |

---

## 📊 Data Flow: From Source to Newsletter

```mermaid
sequenceDiagram
    participant CRON as ⏰ Scheduler
    participant SCOUT as 🔍 Scout Agent
    participant SRC as 🌐 CivicClerk
    participant PDF as 📄 PDF Processor
    participant DB as 💾 Supabase
    participant ANALYST as 🧠 Analyst Agent
    participant HUMAN as 👤 Human Reviewer
    participant SYNTH as 📝 Synthesizer
    participant EMAIL as 📧 Newsletter

    CRON->>SCOUT: Daily trigger (6 AM)
    SCOUT->>SRC: Fetch meeting list (Playwright)
    SRC-->>SCOUT: JSON + PDF links
    SCOUT->>PDF: Download agenda packets
    PDF-->>SCOUT: Extracted text + tables
    SCOUT->>DB: Store ScoutReport + embeddings
    
    Note over DB: Deduplicate via content hash
    
    CRON->>ANALYST: Weekly trigger (Monday 9 AM)
    ANALYST->>DB: Query RED/YELLOW alerts
    ANALYST->>ANALYST: Tavily deep research
    ANALYST->>DB: Store AnalystReport
    ANALYST->>HUMAN: interrupt() - Approval required
    
    HUMAN-->>ANALYST: Approved ✓
    
    ANALYST->>SYNTH: Resume workflow
    SYNTH->>SYNTH: Generate newsletter content
    SYNTH->>EMAIL: Send via Resend API
```

---

## 📁 Project Structure

```
alachua-civic-intelligence-reporting-studio/
├── src/
│   ├── main.py                     # FastAPI application entry point
│   ├── config.py                   # Environment configuration
│   ├── database.py                 # Supabase client
│   ├── schemas.py                  # Pydantic models
│   ├── registry.py                 # Source URL registry
│   │
│   ├── agents/
│   │   ├── base.py                 # Base agent class
│   │   ├── scout.py                # A1-A4 Scout implementations
│   │   └── analyst.py              # B1-B2 Analyst implementations
│   │
│   ├── workflows/
│   │   ├── graphs.py               # LangGraph workflow definitions
│   │   ├── checkpointer.py         # Supabase state persistence
│   │   └── nodes.py                # Reusable node functions
│   │
│   ├── api/
│   │   └── routes/
│   │       ├── workflows.py        # POST /run, GET /status
│   │       ├── approvals.py        # Human-in-the-loop endpoints
│   │       └── streaming.py        # SSE for real-time updates
│   │
│   ├── tools/
│   │   ├── civicclerk_scraper.py   # CivicClerk SPA scraper
│   │   ├── pdf_processor.py        # pdfplumber + Gemini hybrid
│   │   └── document_storage.py     # Supabase file management
│   │
│   └── scheduler/
│       ├── manager.py              # APScheduler setup
│       └── jobs.py                 # Scheduled task definitions
│
├── prompt_library/                 # Agent prompt templates
│   ├── config/                     # Source registry, geographic scope
│   ├── layer-1-scouts/             # A1-A4 prompts
│   ├── layer-2-analysts/           # B1-B2 prompts
│   └── layer-3-synthesizers/       # C1-C4 prompts
│
├── docs/
│   ├── PLAN.md                     # Technical architecture plan
│   └── DEVELOPER_GUIDE.md          # Setup and contribution guide
│
├── data/                           # Generated reports by frequency
│   ├── daily/
│   ├── weekly/
│   └── monthly/
│
├── requirements.txt
├── .env.example
└── README.md
```

---

## 🌐 Monitored Data Sources

| Tier | Source | Platform | Priority | Scraping Method |
|:-----|:-------|:---------|:---------|:----------------|
| **1** | City of Alachua Meetings | CivicClerk (SPA) | 🔴 Critical | Playwright + XHR interception |
| **1** | Development Projects Map | Granicus CMS | 🔴 Critical | BeautifulSoup |
| **2** | Alachua County Meetings | eScribe | 🔴 Critical | Playwright + PDF download |
| **2** | Map Genius (Projects) | County GIS | 🔴 Critical | JSON API |
| **3** | SRWMD Water Permits | E-Permitting Portal | 🔴 Critical | Form submission + scrape |
| **4** | Florida Public Notices | Statewide Repository | 🔴 Critical | Filter by county + parse |
| **5** | WUFT Environment News | WordPress | 🟡 High | RSS feed |

Full registry: [`prompt_library/config/source-registry.md`](prompt_library/config/source-registry.md)

---

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- Docker (optional, for local Supabase)
- API keys: Google AI (Gemini), Tavily, Firecrawl, Supabase

### Installation

```bash
# Clone the repository
git clone https://github.com/Hams-Ollo/alachua-civic-intelligence-reporting-studio.git
cd alachua-civic-intelligence-reporting-studio

# Create virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your API keys
```

### Environment Variables

```bash
# .env
GOOGLE_API_KEY=your_gemini_api_key
TAVILY_API_KEY=your_tavily_key
FIRECRAWL_API_KEY=your_firecrawl_key
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your_supabase_anon_key
SUPABASE_DB_URL=postgresql://postgres:password@db.your-project.supabase.co:5432/postgres
```

### Running the Server

```bash
# Start the FastAPI server
uvicorn src.main:app --reload --port 8000

# The API will be available at http://localhost:8000
# Docs at http://localhost:8000/docs
```

### Running Agents Manually

```bash
# Run a specific Scout agent
curl -X POST "http://localhost:8000/run" \
  -H "Content-Type: application/json" \
  -d '{"agent": "A1", "url": "https://alachuafl.portal.civicclerk.com/"}'

# Check pending approvals
curl "http://localhost:8000/approvals/pending"

# Approve an analyst report
curl -X POST "http://localhost:8000/approvals/{thread_id}/decide" \
  -H "Content-Type: application/json" \
  -d '{"decision": "approved", "comments": "Looks good!"}'
```

---

## 📅 Roadmap

### Phase 1: Foundation ✅
- [x] Project structure and configuration
- [x] Pydantic schemas for all data models
- [x] Supabase database connection
- [x] Source registry documentation

### Phase 2: Scout Layer (Current) 🚧
- [ ] CivicClerk scraper with Playwright
- [ ] PDF processing pipeline (pdfplumber + Gemini)
- [ ] Document storage with Supabase
- [ ] Change detection and deduplication

### Phase 3: Analyst Layer
- [ ] LangGraph workflow implementation
- [ ] Tavily integration for deep research
- [ ] Human approval checkpoint (interrupt/resume)
- [ ] FastAPI approval endpoints

### Phase 4: Synthesizer Layer
- [ ] Newsletter generation with MJML
- [ ] Resend email integration
- [ ] Social media content templates
- [ ] Quarterly health scorecard

### Phase 5: Production Hardening
- [ ] APScheduler cron integration
- [ ] Error handling and retry logic
- [ ] Monitoring and alerting
- [ ] Docker deployment

---

## 🤝 Contributing

We welcome contributions! Please see [`docs/DEVELOPER_GUIDE.md`](docs/DEVELOPER_GUIDE.md) for setup instructions and coding standards.

**Priority Areas:**
- Government portal scrapers (new sources)
- PDF extraction improvements
- Newsletter template design
- Documentation and testing

---

## 📧 Contact

**Project Lead:** Hans  
**Coalition:** Our Alachua Water  
**Repository:** [github.com/Hams-Ollo/alachua-civic-intelligence-reporting-studio](https://github.com/Hams-Ollo/alachua-civic-intelligence-reporting-studio)

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Let's protect our water, our community, and our democracy. 💧🌍✊**
