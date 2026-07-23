# Hello Interview System Design Progress

Primary goal: finish all current Hello Interview written system-design problem breakdowns. Reading coverage and applied design readiness are tracked separately.

Source catalog: `https://www.hellointerview.com/learn/system-design/in-a-hurry/problem-breakdowns`

## Progress Summary

- Core breakdowns read: 2/30
- Independent designs completed: 0/30
- Timed or peer mocks completed: 0

## Core Breakdown Reading

<!-- core-breakdowns:start -->

### Easy

- [x] Bitly — 2026-07-18
- [x] Dropbox — 2026-07-18
- [ ] Yelp
- [ ] Local Delivery Service

### Medium

- [ ] Ticketmaster
- [ ] Instagram
- [ ] FB News Feed
- [ ] Tinder
- [ ] LeetCode
- [ ] WhatsApp
- [ ] Strava
- [ ] Distributed Cache
- [ ] Rate Limiter
- [ ] Online Auction
- [ ] YouTube
- [ ] Job Scheduler
- [ ] FB Live Comments
- [ ] News Aggregator
- [ ] Price Tracking Service

### Hard

- [ ] YouTube Top K
- [ ] Uber
- [ ] Robinhood
- [ ] Google Docs
- [ ] Web Crawler
- [ ] Ad Click Aggregator
- [ ] FB Post Search
- [ ] Payment System
- [ ] Metrics Monitoring
- [ ] Online Chess
- [ ] ChatGPT

<!-- core-breakdowns:end -->

## Independent Designs

An item belongs here only after attempting the design before reviewing the solution. Record the date and optionally link notes or a diagram.

<!-- independent-designs:start -->
<!-- independent-designs:end -->

## Timed And Peer Mocks

<!-- system-design-mocks:start -->
<!-- system-design-mocks:end -->

## Additional Guided Practice

These are outside the 30 core written breakdowns and do not change the main denominator.

- [ ] Food Review App
- [ ] Game Leaderboard
- [ ] Donations Website
- [ ] GitHub Actions
- [ ] Notification System

## AI FDE Supporting Curriculum

Source: `https://github.com/ombharatiya/ai-system-design-guide`

Use this after or alongside the general Hello Interview foundation. Follow the order below; do not read the repository linearly by folder number.

<!-- ai-fde-curriculum:start -->

1. [ ] `00-interview-prep`
2. [ ] `06-retrieval-systems`
3. [ ] `07-agentic-systems`
4. [ ] `08-memory-and-state`
5. [ ] `11-infrastructure-and-mlops`
6. [ ] `12-security-and-access`
7. [ ] `13-reliability-and-safety`
8. [ ] `14-evaluation-and-observability`
9. [ ] `15-ai-design-patterns`
10. [ ] `16-case-studies`
11. [ ] `17-tool-use-and-computer-agents`

<!-- ai-fde-curriculum:end -->

Model landscape and training chapters are initial skim material. Voice, multimodal generation, and deep inference optimization are optional unless a target FDE posting emphasizes them.

Reading is not sufficient evidence of FDE readiness. Pair the curriculum with production-oriented work involving RAG, agents/tools, evaluation and tracing, security, deployment, debugging, and customer-facing explanation.

## Practical AI Agent Engineering

### Agents From Scratch

- Repository: `https://github.com/langchain-ai/agents-from-scratch`
- Local checkout: `/Users/viksat98/agents-from-scratch`
- Last reviewed: 2026-07-23
- Estimated curriculum coverage: 100%

#### Covered

- [x] LangGraph state, nodes, edges, compilation, invocation, and `END`
- [x] Fixed and conditional routing
- [x] Model tool requests versus runtime tool execution
- [x] Tool schemas, lookup, results, and agent loops
- [x] Structured-output email triage: ignore, notify, or respond
- [x] `Command(goto=..., update=...)` versus conditional edges
- [x] Compiled graphs used as nodes inside larger workflows
- [x] Custom state, `MessagesState`, and reducer fundamentals
- [x] Current-run message history across model/tool turns
- [x] Basic agent safety: validation, allowlists, human approval, and tool-side checks
- [x] Evaluation fundamentals: deterministic tool-call assertions versus LLM-as-judge criteria
- [x] Evaluation datasets and expected behavior across varied inputs
- [x] Evaluation targets, reference outputs, evaluators, and regression testing
- [x] Pytest execution versus LangSmith experiment tracking and comparison
- [x] Output, trajectory, and safety evaluation layers
- [x] HITL interrupt fundamentals and enforced approval boundaries
- [x] Selective approval for consequential tools versus automatic read-only tools
- [x] Checkpoint and thread-ID fundamentals for pausing and resuming graph executions
- [x] HITL accept, edit, ignore, and feedback response paths
- [x] Interrupt resume semantics: the interrupted node re-executes from its beginning
- [x] Stable idempotency keys for protecting approved side effects from retries
- [x] `Command(resume=...)` and matching human responses to paused thread checkpoints
- [x] Thread-scoped checkpoint memory versus cross-thread preference storage
- [x] Store namespaces, keys, values, and per-user memory isolation
- [x] Converting explicit edits and feedback into generalized cross-thread preference profiles
- [x] Retrieving relevant memory categories and keeping safety policy outside user-editable memory
- [x] Development versus production store implementations and persistence guarantees
- [x] Replacing mock tools with Gmail API adapters while preserving graph and tool contracts
- [x] Gmail ingestion: search, full-thread retrieval, latest-message and sender filtering, then graph invocation
- [x] Gmail thread continuity, message-level deduplication, and atomic ingestion claims
- [x] Stable operation-level idempotency keys and the distinction from ingestion deduplication
- [x] OAuth scopes, least privilege, and keeping credentials outside model context
- [x] Gmail reply construction using the source message ID and conversation thread ID
- [x] Calendar read-versus-write boundaries and fail-closed behavior when availability lookup fails
- [x] Timezone-aware calendar queries, comparisons, scheduling, and approval display
- [x] Scheduled Gmail polling, overlapping recovery windows, and deployment secret boundaries
- [x] Run lifecycle observability: created, running, interrupted, completed, failed, and external-action outcomes
- [x] Correlation across Gmail message/thread IDs, graph thread/run IDs, tool-call IDs, and idempotency keys
- [x] End-to-end Gmail failure handling across atomic claims, explicit dependency errors, bounded retries, and monitoring
- [x] Compiled graph behavior versus LangGraph server runtime responsibilities
- [x] Developer debugging in Studio versus operational approvals in Agent Inbox and evaluation in LangSmith
- [x] Layered deployment validation from mocks through failure injection, test accounts, and constrained rollout
- [x] End-to-end trace audit requiring approval before each consequential calendar and email action

#### Demonstrated Understanding

- Can explain the overall graph execution model
- Can distinguish fixed edges from conditional routing
- Can explain why subgraphs make larger workflows manageable
- Understands that models request tools while Python runtime executes them
- Recognizes that schema-valid tool calls can still be wrong or unsafe
- Can select deterministic checks for exact behavior and LLM judging for semantic response quality
- Can explain why full-suite regression testing is required after agent changes
- Can identify which tool actions should normally require human approval
- Understands that thread IDs isolate and resume the correct paused workflow
- Can distinguish direct argument editing from feedback that asks the model to generate a new proposal
- Understands why non-idempotent side effects must not occur before an interrupt
- Understands why retry deduplication requires a stable logical-operation key
- Can distinguish checkpoint selection by `thread_id` from the resume value returned by `interrupt()`
- Can place pending workflow state and conversation messages in checkpoints while keeping reusable preferences in a store
- Understands why cross-thread memory namespaces must include stable user identity and memory category
- Understands why a situation-specific feedback event should not automatically become a global preference
- Understands that stored memory is untrusted data and cannot override application-enforced approval policy
- Understands why process-local memory cannot provide durable or multi-instance production behavior
- Understands that OAuth, API encoding, and credential refresh belong inside the integration layer rather than graph logic
- Understands why ingestion should avoid separately processing stale messages and the user's own sent replies
- Understands how concurrent pollers can both process one message when check-and-insert is not atomic
- Understands why retries of one logical external action must reuse the same idempotency key
- Understands why read-only workloads should not receive Gmail modification permissions
- Can distinguish the specific Gmail message being answered from the thread that preserves conversation continuity
- Understands why production integrations must not substitute realistic mock availability after a real API failure
- Understands why trusted user timezone must be explicit throughout calendar lookup and event creation
- Understands how overlapping polling windows recover missed runs while atomic deduplication prevents duplicate processing
- Understands why accepted graph runs do not establish completed workflows or successful external effects
- Can identify which IDs remain stable for one logical operation and which change for a new processing attempt
- Can explain why calendar failure must block scheduling, remain observable, and use bounded retries without duplicating incoming work
- Can distinguish workflow declarations from the server that manages threads, runs, persistence, and interrupts
- Can select Agent Inbox for constrained human review without exposing developer graph internals
- Understands why real API validation begins with isolated accounts and minimal permissions before production access
- Can identify separate approval boundaries for meeting creation and outbound email content

#### Reinforce

- State is one evolving shared object, not a series of state locations
- Tool results return to message history primarily for current-run context, not automatic long-term memory
- Reducers define how field updates merge; ordinary fields replace while message updates accumulate
- `Command` routing versus separate conditional-edge routing

#### Remaining

- [x] Basic email-agent architecture and trace-audit curriculum
- [x] Evaluation module concepts and test-dataset workflow
- [x] Human-in-the-loop module concepts (local execution/testing remains optional practice)
- [x] Memory and persistence module concepts (production implementation remains applied practice)
- [x] Gmail integration and deployment concepts (credentialed execution remains applied practice)

#### Applied Evidence

Deferred by user until a later build phase. Do not treat these items as remaining conceptual curriculum or prompt for execution unless requested.

- [ ] Local test-suite execution verified
- [ ] Local LangGraph server and interrupt-resume flow verified
- [ ] Cross-thread memory behavior verified
- [ ] Gmail and Calendar test-account integration verified
- [ ] Production deployment or independent extension implemented

Update this section only from completed work or concepts demonstrated during the walkthrough. Keep exposure, demonstrated understanding, and applied project evidence separate.

Detailed review notes: [`FDEPrep/agents-from-scratch/README.md`](FDEPrep/agents-from-scratch/README.md)

## Assessment Rule

Reading a breakdown increases topic exposure but does not prove design ability. Applied readiness is assessed from independent designs, tradeoff reasoning, deep dives, and spoken or timed practice. Do not infer applied readiness from reading completion alone.
