# [identity-01] Anshumaan Singh — Comprehensive Master Resume

This is the sole factual source for tailored resumes. Identifiers in brackets
are stable evidence references; preserve them when expanding this document.

AI Systems

- [identity-02] Phone: +1 (934)-219-4495
- [identity-03] Email: anshumaanvsingh@gmail.com
- [identity-04] LinkedIn: https://www.linkedin.com/in/anshumaanvsingh
- [identity-05] GitHub: https://github.com/KrossKinetic
- [identity-06] Portfolio: https://krosskinetic.github.io

## Education

### [edu-01] Stony Brook University — Stony Brook, NY

B.S. in Computer Science Honors, GPA: 3.9/4.0  
Aug 2023 – May 2027

- [edu-02] Honors / Awards: SUNY SOAR Fellow, URECA Fellow, University Scholars, Dean’s List (2023 – 2025).
- [edu-03] Completed CSE coursework (through Spring 2026): Computer Science Principles; Introduction to Object-Oriented Programming; Data Structures; Foundations of Computer Science; Programming Abstractions; Systems Fundamentals I; Technical Communications; Software Development; Systems Fundamentals II; Theory of Computation: Honors; Research in Computer Science; Internship in Computer Science.
- [edu-04] Completed AMS coursework (through Spring 2026): Applied Calculus II; Applied Linear Algebra; Applied Calculus III; Finite Mathematical Structures; Survey of Probability and Statistics.
- [edu-05] Registered for Fall 2026 (not yet completed on the July 31, 2026 transcript): Compiler Design; Computer Networks; Legal Issues in Computing; Natural Language Processing.

## Technical Skills

- [skill-01] Agentic AI & ML Systems: Model Context Protocol (MCP), agent/tool calling, RAG, LLM fine-tuning, LoRA/QLoRA, model distillation, vLLM, provider-agnostic LLM gateways, PyTorch, TensorFlow, Transformers, Reinforcement Learning, MPC, CMA-ES.
- [skill-02] Backend, APIs & Protocols: Python, C#, FastAPI, ASGI/Uvicorn, Flask, Node.js, REST APIs, JSON-RPC, HTTP, Server-Sent Events (SSE), WebSockets, SQLAlchemy.
- [skill-03] Data & Platform Engineering: PostgreSQL, SQLite, MongoDB, DuckDB, Apache Parquet, enterprise SQL, ETL/data pipelines, cron scheduling, caching, AWS (EC2/S3), Docker, Slurm HPC, Linux.
- [skill-04] Concurrent & Reliable Systems: async programming, multithreaded job scheduling, queue back-pressure, race-condition avoidance, atomic writes, retry/backoff, parallel execution, sandboxing, IPC, CI/CD.
- [skill-05] Security & Automation: role-based access control (RBAC), JWT/API-key authentication, OAuth/OIDC, bcrypt/SHA-256 hashing, audit logging, Playwright browser automation, enterprise document APIs.
- [skill-06] Full-Stack & Developer Tooling: React.js, JSX, Firebase, Google Cloud, Google Developer Console, Atlassian Suite.
- [skill-07] Languages: Python, C, C#, Java, JavaScript, Kotlin, MATLAB, MIPS Assembly, HTML/CSS.

## Work Experience

### [bmo-01] AI & ML Engineering Intern — Bank of Montreal (BMO)

Berkeley Heights, NJ | Jun 2026 – Aug 2026

- [bmo-02] Built a C# adapter layer and automated ingestion pipelines to normalize heterogeneous upstream data for an analytics-platform modernization; added black-box regression tests with verified input/output fixtures to validate mappings against the legacy implementation.
- [bmo-03] As sole engineer, built a 39-tool Python/FastAPI Model Context Protocol (MCP) server for an integrated AML case-investigation pipeline from a blank scaffold in approximately 6 weeks, implementing HTTP, SSE, and WebSocket transports.
- [bmo-04] Designed the end-to-end AML pipeline so cron-scheduled backend jobs refresh the cache and agents call MCP tools for on-demand case preparation and investigation; reduced a 3–4-hour manual workflow to 1–2 minutes (approximately 99% faster) and delivered a six-step cached data-assembly DAG in approximately 2 seconds, with management projecting approximately $2M in savings over two years.
- [bmo-05] Engineered a three-pool concurrent job router with bounded queues, HTTP 429 back-pressure, and serialized cache writes; built the cron-scheduled cache-refresh service with atomic Parquet writes and retry/backoff for resilient daily refreshes.
- [bmo-06] Designed a reusable tool-composition framework that lets non-engineers chain existing MCP tools into multi-step workflows without writing new integration code, alongside deterministic-first LLM analysis for grounded investigative narratives.
- [bmo-07] Implemented security controls for a regulated internal platform, including four authentication paths, role-based authorization, API-key/password hashing, audit logging, and confirmation gates for destructive operations.

### [rel-01] Undergraduate Research Assistant — Reliable Systems Lab, Stony Brook University

Stony Brook, NY | Jan 2026 – Present

- [rel-05] Advisors: Prof. Scott Stoller and Prof. Scott Smolka. Researching multi-agent cyber-physical systems, including neural controllers and MPC algorithms for autonomous UAV-swarm coordination under adversarial conditions.
- [rel-06] Conducted large-scale SeaWulf HPC simulations evaluating neural-flocking behavior against supervised-learning and reinforcement-learning benchmarks.
- [rel-02] Engineering a lightweight encoder-only attention architecture for multi-agent systems, leveraging permutation equivariance to process jagged input arrays and eliminate data sorting overhead.
- [rel-03] Improving UAV Agent target seeking efficiency by 34.6% by architecting a Curriculum Weight Tuning API using CMA-ES through a grouped parameter strategy.
- [rel-04] Enabling 100% collision-free horizontal scaling on the SeaWulf HPC cluster by building a distributed isolation framework using dynamic sandboxing to eliminate MATLAB/MEX race conditions.

### [lunr-01] Undergraduate Research Assistant — LUNR Lab, Stony Brook University

Stony Brook, NY | Feb 2025 – Mar 2026

- [lunr-02] Improved Coding RAG accuracy by 5.4% and accelerated code rag bench runtimes by 73.5% by fine-tuning CodeLlama-7B via LoRA and designing a parallelized vLLM routing system.
- [lunr-03] Reducing LLM inference costs by up to 100% by architecting and integrating an SQLite3 caching layer directly into the model distillation pipeline.
- [lunr-04] Refactored the research implementation of REPLUG to enable LM-Supervised Retrieval (LSR) fine-tuning for code generation tasks by architecting a training pipeline driven by a local vLLM server.
- [lunr-05] Fine-tuned CodeLlama-7B on a custom dataset of more than 460K samples; the resulting Coding RAG work improved MBPP evaluation accuracy by 5.4% and ODEX evaluation accuracy by 1.6%.
- [lunr-06] Designed the parallelized RAG benchmark system using vLLM and multiple commercial APIs; measured benchmark runtimes 73.5% faster than existing baselines.

### [mailgator-01] Software Developer Intern — Mailgator

Palo Alto, CA (Hybrid) | Sep 2025 – Jan 2026

- [mailgator-02] Reduced validation latency by 99.9% (60m to <2s) by architecting a scalable CI/CD pipeline on AWS EC2 with automated asynchronous integrity checks for a FastAPI backend.
- [mailgator-03] Optimized system reliability by refactoring LLM-driven parsing logic for deterministic data extraction, ensuring 100% accuracy across complex sender-recipient edge cases.
- [mailgator-04] Developed Generative AI email-analysis systems with a five-person agile team, including prompt-QA and UX-test infrastructure for an ML backend built with FastAPI, Node.js, React, and PostgreSQL.
- [mailgator-05] Resolved critical parsing bugs and refined OpenAI prompts for data extraction, including sender-recipient edge cases.

### [igem-01] Software Engineer — iGEM at Stony Brook University

Stony Brook, NY | Feb 2024 – Oct 2024

- [igem-04] Performed computational biology to improve a miRNA-detector bacteria system for human Non-Hodgkin’s B-cell lymphoma, using molecular-dynamics simulations to assess AGO2 and miRNA-326 binding.
- [igem-02] Achieved 90% retrieval accuracy on embedded research documents by building a RAG Q&A chatbot with Transformers and LangChain, improving the research-wiki experience.
- [igem-03] Led a three-person team to develop a Flask research wiki that attracted more than 15 stakeholders, helping secure more than $50K in funding and expand outreach.
- [igem-05] Awarded a Gold Medal for the team’s research efforts at the iGEM Paris 2024 Jamboree.

## Projects

### [fuzzer-01] Automated Systems Fuzzer (C & Unix Systems)

Spring 2026

- [fuzzer-02] Engineered a high-performance C fuzzer utilizing Unix signals and syscalls (`fork`, `waitpid`) to stress-test executables via mutated input streams, achieving 100% process isolation and automated memory leak detection.

### [cmdflow-01] CMDFlow at HackPrinceton (Semantic Search & Local-First Systems)

November 2025

- [cmdflow-02] Engineered a local-first command-tracking system (FastAPI, MongoDB) that streams shell activity with <1s latency, performs automated PII scrubbing, and semantically indexes CLI commands for natural language search.
- [cmdflow-03] Built CMDFlow with React.js and automatic project-based command organization.

### [notisentry-01] NotiSentry: A Smart DND with LLMs (Generative AI and Android)

Jun 2025 – Sep 2025

- [notisentry-02] Built an intelligent Android notification-filtering and summarization tool using the Firebase Gemini API and Jetpack Compose; optimized it to less than 1% battery drain over five hours and 1.3-second worst-case latency.

### [replug-01] REPLUG LSR with vLLM (AI Research & Infrastructure)

Jun 2025

- [replug-02] Refactored REPLUG to enable LM-Supervised Retrieval (LSR) fine-tuning for code-generation tasks through a high-performance training pipeline using a local vLLM server.

### [mtplx-01] pi-mtplx (Local LLM Runtime Integration)

Aug 2026

- [mtplx-02] Published `pi-mtplx`, a Pi extension for local MTPLX inference; reached 1,173 monthly downloads as of Aug 2026.
- [mtplx-03] Built zero-configuration discovery and registration of locally installed models, deriving context-window, vision, reasoning, and token-limit capabilities from each installed artifact rather than hard-coding a model catalog.
- [mtplx-04] Engineered a local model-server lifecycle with health checks and ownership-aware cleanup, plus persistent SSD session-cache and thermal fan-mode controls; added live token-per-second monitoring in Pi’s footer.
- [mtplx-05] Ensured a Pi session stops only the MTPLX server it started, leaving manually launched servers untouched and switching models only after health-checking the expected local endpoint.

### [orbit-01] pi-orbit (Developer Environment Orchestration)

Aug 2026

- [orbit-02] Published `pi-orbit`, a Pi project manager that packages a working directory, model, reasoning level, tool allowlist, environment variables, and optional skills into switchable named profiles.
- [orbit-03] Built an interactive profile wizard and validated, persistent JSON configuration system with a safe default-profile reset and additive skill discovery.
- [orbit-04] Implemented cross-directory switching that launches a fresh Pi session in the target directory on macOS while preserving the prior session for recovery; provides a portable command fallback on other platforms.
- [orbit-05] Implemented explicit Default Orbit reset semantics that restore baseline model/thinking settings and undo environment-variable overrides, preventing project configuration from leaking between sessions.

### [applyjob-01] pi-apply-job (Evidence-Backed Resume Automation)

Aug 2026

- [applyjob-02] Built an unpublished Pi extension that accepts individual or batched public job URLs, extracts job requirements, and creates isolated per-application artifacts without submitting applications.
- [applyjob-03] Designed an evidence-linked resume-plan and verification workflow: every selected resume claim cites a stable ID from a private master resume before it can be rendered.
- [applyjob-04] Implemented deterministic one-page LaTeX rendering with a content-free user template, Tectonic compilation, PDF page-count validation, and bounded content-only revision attempts.
- [applyjob-05] Added operational guardrails: accepts at most 25 URLs from a 64 KB task list, permits public HTTP(S) targets only, prevents redirects to non-public IP addresses, uses a 30-second scrape timeout, and truncates extracted page text to 40K characters.
- [applyjob-06] Verified the renderer end-to-end: an approved evidence-linked plan compiles to a PDF and must pass an exact one-page assertion; the extension passes TypeScript static type checking.
