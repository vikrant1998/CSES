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
- Last reviewed: 2026-07-22
- Estimated curriculum coverage: 51%

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

#### Reinforce

- State is one evolving shared object, not a series of state locations
- Tool results return to message history primarily for current-run context, not automatic long-term memory
- Reducers define how field updates merge; ordinary fields replace while message updates accumulate
- `Command` routing versus separate conditional-edge routing

#### Remaining

- [ ] Finish and test the basic email agent (architecture covered; execution remains)
- [x] Evaluation module concepts and test-dataset workflow
- [ ] Finish the human-in-the-loop module (interrupt, approval, edit, and checkpoint concepts covered)
- [ ] Memory and persistence
- [ ] Gmail integration and deployment

Update this section only from completed work or concepts demonstrated during the walkthrough. Keep exposure, demonstrated understanding, and applied project evidence separate.

Detailed review notes: [`FDEPrep/agents-from-scratch/README.md`](FDEPrep/agents-from-scratch/README.md)

## Assessment Rule

Reading a breakdown increases topic exposure but does not prove design ability. Applied readiness is assessed from independent designs, tradeoff reasoning, deep dives, and spoken or timed practice. Do not infer applied readiness from reading completion alone.
