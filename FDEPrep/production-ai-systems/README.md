# Production AI Systems Learning Guide

A combined, prerequisite-aware walkthrough of:

- [LLM Zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp)
- [AI System Design Guide](https://github.com/ombharatiya/ai-system-design-guide)
- Prior foundation: [Agents From Scratch learning notes](../agents-from-scratch/README.md)

This is the next practical AI track for Google FDE preparation. The AI System
Design Guide supplies architecture, tradeoffs, failure modes, and interview
language. LLM Zoomcamp supplies concrete pipelines, evaluation, monitoring, and
an end-to-end project. Overlapping material is taught once.

- Started: not started
- Current conceptual coverage: 0/12 sections (0%)
- Applied checkpoints completed: 0/12
- Source versions reviewed: 2026-07-27

## How We Will Use This

This follows the same method as the Agents From Scratch walkthrough:

1. Read one focused section together.
2. Explain it in ordinary language before introducing detailed terminology.
3. Ask short retrieval questions about the overall mental model.
4. Record your answer and a correction or refinement in this file.
5. Report the cumulative course percentage after the section.
6. Track reading, demonstrated understanding, and implementation separately.

A section is conceptually complete only after you can explain its central idea.
Displaying or reading the material alone does not count. Applied checkpoints are
useful evidence, but they can remain deferred while the current goal is learning.

## The System We Are Learning

Most production AI applications are a pipeline, not just a model:

```text
User request
    -> permissions and input checks
    -> retrieve useful private or current information
    -> construct model context
    -> generate or choose an action
    -> validate the result
    -> return or execute it
    -> record quality, latency, cost, and failures
```

The course progressively answers six questions:

1. What problem are we solving, and what must the system guarantee?
2. How does the system find the right information?
3. How do we know the answer is good?
4. What happens when a dependency, model, or workflow step fails?
5. How do we protect users and data?
6. How do we explain the complete design under interview pressure?

## Prior Knowledge We Will Not Repeat

The completed Agents From Scratch walkthrough already established:

- models request tools while application code executes them;
- graph state, nodes, edges, routing, loops, checkpoints, and interrupts;
- thread-scoped state versus cross-thread memory;
- tool validation, human approval, least privilege, and idempotency;
- output, trajectory, and safety evaluation;
- ingestion deduplication, bounded retries, and operational identifiers.

Those concepts will be reused in RAG and production design instead of retaught.

## Course Map

| Section | Topic | AI System Design Guide | LLM Zoomcamp | Coverage after completion |
|---:|---|---|---|---:|
| 1 | Frame the AI system | `00-interview-prep` | Orientation | 8% |
| 2 | RAG foundations | `06/01` | Module 1, lessons 1-10 | 17% |
| 3 | Ingestion and chunking | `06/02`, `06/15` | Module 1 ingestion | 25% |
| 4 | Embeddings and vector search | `06/03`, `06/04` | Module 2 | 33% |
| 5 | Better retrieval | `06/05`, `06/06` | Module 6 | 42% |
| 6 | Agentic RAG | `06/08`, selected `07` | Module 1, lessons 11-16 | 50% |
| 7 | Orchestration, state, and memory | selected `07`, `08` | Module 3 | 58% |
| 8 | Evaluation | `06/13`, `14/01` | Module 4 | 67% |
| 9 | Monitoring and observability | `14/02` | Module 5 | 75% |
| 10 | Production reliability, scale, and cost | `06/14`, `11`, `13/03` | production patterns | 83% |
| 11 | Security, access, and guardrails | `07/09`, `12`, `13/01` | security review | 92% |
| 12 | End-to-end FDE design | `15`, selected `16` | Module 7/capstone | 100% |

Paths such as `06/01` mean chapter `01` inside the guide's
`06-retrieval-systems` directory.

---

## Section 1: Frame the AI System

### Plain-English Model

Before choosing a model or database, define what the user needs, what data the
system may use, how success will be measured, and what failure would be
unacceptable. AI does not remove normal system-design work; it adds uncertain
outputs, evaluation data, safety boundaries, and model cost.

A useful interview order is **SPIDER**:

- **Scope:** clarify users, use cases, constraints, and prohibited behavior.
- **Prioritize:** separate required behavior from optional improvements.
- **Initial architecture:** draw the request, data, model, and response paths.
- **Deep dive:** examine the riskiest or most important component.
- **Evaluation:** define offline quality tests and production signals.
- **Reliability:** cover scale, failures, recovery, security, and cost.

### Read

- AI guide: [`00-interview-prep/02-answer-frameworks.md`](https://github.com/ombharatiya/ai-system-design-guide/blob/main/00-interview-prep/02-answer-frameworks.md)
- AI guide: [`00-interview-prep/03-common-pitfalls.md`](https://github.com/ombharatiya/ai-system-design-guide/blob/main/00-interview-prep/03-common-pitfalls.md)
- Zoomcamp: root introduction and module map

### You Should Be Able To Explain

- Why "use an LLM" is not a system requirement.
- Why the data pipeline, evaluation layer, and fallback path belong in the first
  architecture, not as afterthoughts.
- The difference between product success, model quality, and system reliability.

### Retrieval Check

1. What four questions should you answer before selecting a model?
2. Why does an AI design need both offline evaluation and production monitoring?
3. If an interviewer asks for an internal support assistant, what would you
   clarify before drawing the architecture?

### Applied Checkpoint

- [ ] Write a one-page scope for an internal document-answering assistant.

---

## Section 2: RAG Foundations

### Plain-English Model

A language model knows what was in its training and what fits in the current
request. Retrieval-augmented generation, or RAG, first searches an external
knowledge source and then gives the useful results to the model as evidence.

```text
Question -> search knowledge -> select context -> model answers from context
```

RAG is useful when information is private, frequently changing, too large to
place in every prompt, or needs citations. A long context window can hold more
text, but it does not decide which text is relevant, enforce document access, or
keep an index current.

### Read

- AI guide: [`06-retrieval-systems/01-rag-fundamentals.md`](https://github.com/ombharatiya/ai-system-design-guide/blob/main/06-retrieval-systems/01-rag-fundamentals.md)
- Zoomcamp Module 1: lessons `01-intro.md` through `10-rag-next-steps.md`

### You Should Be Able To Explain

- The difference between training the model and giving it retrieved evidence.
- The four basic RAG stages: ingest, retrieve, construct context, generate.
- Why an answer can fail even when the model itself is capable.
- When direct model context, ordinary search, or RAG is the simpler choice.

### Retrieval Check

1. What problem does RAG solve that a larger model does not automatically solve?
2. If the correct document was never retrieved, which layer failed?
3. Why should retrieved text be treated as data rather than trusted instructions?

### Applied Checkpoint

- [ ] Run a minimal retrieve-then-generate pipeline over a small document set.

---

## Section 3: Ingestion and Chunking

### Plain-English Model

The retrieval system cannot search raw business data reliably without preparing
it. Ingestion collects documents, cleans them, removes duplicates, preserves
permissions and metadata, divides them into searchable units, and updates the
index when sources change.

Chunking creates the units returned by search. Tiny chunks lose the surrounding
meaning. Huge chunks contain more noise and consume more model context. The best
boundary usually follows the document's structure: sections for prose, functions
for code, rows plus headers for tables, and layout-aware blocks for PDFs.

### Read

- AI guide: [`06-retrieval-systems/02-chunking-strategies.md`](https://github.com/ombharatiya/ai-system-design-guide/blob/main/06-retrieval-systems/02-chunking-strategies.md)
- AI guide: [`06-retrieval-systems/15-data-engineering-for-ai.md`](https://github.com/ombharatiya/ai-system-design-guide/blob/main/06-retrieval-systems/15-data-engineering-for-ai.md)
- Zoomcamp Module 1: `09-data-ingestion.md`
- Zoomcamp Module 7: `07-chunking.md`

### You Should Be Able To Explain

- Why parsing and chunking quality can dominate model quality.
- Why every chunk needs source, ownership, timestamp, and permission metadata.
- How updates, deletions, and duplicate documents reach the index.
- Why a fixed token size is a baseline rather than a universal solution.

### Retrieval Check

1. What goes wrong when a table row is separated from its headers?
2. Why must document deletion also remove its indexed chunks?
3. What metadata is needed to prevent one customer from retrieving another
   customer's documents?

### Applied Checkpoint

- [ ] Build a repeatable ingestion step with stable document IDs and deduplication.

---

## Section 4: Embeddings and Vector Search

### Plain-English Model

An embedding model turns text into a list of numbers whose geometry represents
meaning. Similar meanings should produce nearby vectors. A vector index searches
those vectors for approximate nearest neighbors.

```text
document text -> embedding model -> vector + metadata -> vector index
question      -> embedding model -> query vector    -> nearest vectors
```

The vector database does not know whether an answer is true. It efficiently
returns nearby items. Search quality still depends on the embedding model,
chunking, distance metric, filters, and index settings.

### Read

- AI guide: [`06-retrieval-systems/03-embedding-models.md`](https://github.com/ombharatiya/ai-system-design-guide/blob/main/06-retrieval-systems/03-embedding-models.md)
- AI guide: [`06-retrieval-systems/04-vector-databases.md`](https://github.com/ombharatiya/ai-system-design-guide/blob/main/06-retrieval-systems/04-vector-databases.md)
- Zoomcamp Module 2: all core lessons

### You Should Be Able To Explain

- What an embedding represents and what it does not prove.
- Exact versus approximate search and the recall-versus-latency tradeoff.
- Why metadata filtering must happen without violating tenant isolation.
- When a database extension is sufficient and when a dedicated vector system is
  justified.

### Retrieval Check

1. Why can two semantically similar passages have few words in common?
2. What do you sacrifice when approximate search is tuned for lower latency?
3. Why is a vector database not automatically the right database for every AI
   product?

### Applied Checkpoint

- [ ] Compare lexical and vector retrieval on the same ten test questions.

---

## Section 5: Better Retrieval

### Plain-English Model

Semantic search understands meaning but can miss exact identifiers, names, or
rare terms. Keyword search handles exact text but can miss paraphrases. Hybrid
search runs both, combines their rankings, and then may rerank a smaller candidate
set with a more accurate model.

```text
                 -> keyword candidates --
Question -> route                        +-> fuse -> rerank -> context
                 -> vector candidates  --
```

The first retrieval stage favors speed and broad recall. Reranking spends more
work only on the best candidates to improve final ordering.

### Read

- AI guide: [`06-retrieval-systems/05-hybrid-search.md`](https://github.com/ombharatiya/ai-system-design-guide/blob/main/06-retrieval-systems/05-hybrid-search.md)
- AI guide: [`06-retrieval-systems/06-reranking-strategies.md`](https://github.com/ombharatiya/ai-system-design-guide/blob/main/06-retrieval-systems/06-reranking-strategies.md)
- Zoomcamp Module 6: hybrid search and reranking lessons

### You Should Be Able To Explain

- Dense search, sparse search, rank fusion, and reranking.
- Why retrieval often uses a fast first pass and a slower second pass.
- The quality, latency, and cost effect of candidate count.
- Why improvements must be verified on a representative test set.

### Retrieval Check

1. Which search method is likely to find an exact error code, and why?
2. Why not run an expensive reranker over every document?
3. What evidence would justify adding hybrid search to an existing system?

### Applied Checkpoint

- [ ] Measure baseline, hybrid, and reranked retrieval on one fixed test set.

---

## Section 6: Agentic RAG

### Plain-English Model

Ordinary RAG always performs a predefined search. Agentic RAG lets a controller
decide whether to search, reformulate a poor query, use another source, perform
multiple retrieval steps, or stop. This can solve harder questions but introduces
more latency, cost, nondeterminism, and failure paths.

The agent concepts are already known. The new idea is applying the loop to
retrieval:

```text
plan -> retrieve -> inspect evidence -> refine or answer
```

### Read

- AI guide: [`06-retrieval-systems/08-agentic-rag.md`](https://github.com/ombharatiya/ai-system-design-guide/blob/main/06-retrieval-systems/08-agentic-rag.md)
- AI guide: selected review from `07-agentic-systems`, especially error handling,
  security, evaluation, and durable execution
- Zoomcamp Module 1: lessons `11-agents-intro.md` through `16-other-frameworks.md`

### You Should Be Able To Explain

- Linear RAG versus an iterative retrieval loop.
- When query decomposition or multiple searches are worth their cost.
- Termination conditions and limits that prevent wandering loops.
- Why a flexible agent needs stronger evaluation and observability.

### Retrieval Check

1. When is a fixed RAG pipeline preferable to an agent?
2. How should the loop react when retrieved evidence is insufficient?
3. What limits would you enforce before allowing repeated searches?

### Applied Checkpoint

- [ ] Add a bounded retrieve-evaluate-retry loop to the baseline RAG system.

---

## Section 7: Orchestration, State, and Memory

### Plain-English Model

Orchestration coordinates work that spans services or time: ingesting documents,
waiting for jobs, retrying dependencies, pausing for approval, and resuming after
a process restart. State records the current workflow. Memory stores information
that should influence later interactions. They are related but not interchangeable.

This section extends the earlier graph and checkpoint concepts into a complete
data and AI workflow. Kestra is one implementation example, not the concept itself.

### Read

- AI guide: `07-agentic-systems/07-error-handling-and-recovery.md`
- AI guide: `07-agentic-systems/11-durable-execution.md`
- AI guide: selected chapters from `08-memory-and-state`
- Zoomcamp Module 3: focus on context engineering, RAG workflows, agentic
  workflows, and best practices

### You Should Be Able To Explain

- Workflow state versus conversational context versus durable user memory.
- When a queue, workflow engine, graph runtime, or scheduled job owns a step.
- Why retries around side effects require stable operation identities.
- How a long-running workflow recovers after a worker dies.

### Retrieval Check

1. Where should an unfinished ingestion job store its progress?
2. Why is user preference memory not the same thing as workflow state?
3. What must be durable before acknowledging completion of a workflow step?

### Applied Checkpoint

- [ ] Draw and test one restart-safe ingestion or agent workflow.

---

## Section 8: Evaluation

### Plain-English Model

Evaluation turns "the demo looked good" into repeatable evidence. Test the
retriever and generator separately before judging the combined answer:

- **Retrieval:** did useful evidence appear, and how highly was it ranked?
- **Groundedness:** does the answer follow from the supplied evidence?
- **Answer relevance:** did the answer address the question?
- **Agent behavior:** did the system take valid, efficient, safe steps?

A golden test set contains representative questions and human-reviewed expected
evidence or behavior. LLM judges can scale qualitative checks, but their rubric
and calibration must themselves be tested.

### Read

- AI guide: [`06-retrieval-systems/13-rag-evaluation-patterns.md`](https://github.com/ombharatiya/ai-system-design-guide/blob/main/06-retrieval-systems/13-rag-evaluation-patterns.md)
- AI guide: [`14-evaluation-and-observability/01-llm-evaluation.md`](https://github.com/ombharatiya/ai-system-design-guide/blob/main/14-evaluation-and-observability/01-llm-evaluation.md)
- Zoomcamp Module 4: search, RAG, LLM-judge, and agent evaluation

### You Should Be Able To Explain

- Why combined answer quality cannot locate the failing component by itself.
- Recall, ranking quality, groundedness, relevance, and task success.
- Deterministic evaluation versus model-based evaluation.
- Golden sets, regression gates, and human review.

### Retrieval Check

1. The final answer is wrong, but the correct passage was ranked first. Which
   component should you inspect?
2. Why should synthetic evaluation questions receive human review?
3. What metric would reveal an agent that succeeds but takes excessive steps?

### Applied Checkpoint

- [ ] Create a reviewed evaluation set and compare two pipeline configurations.

---

## Section 9: Monitoring and Observability

### Plain-English Model

Evaluation measures known examples before release. Monitoring observes real
traffic afterward. Logs record events, metrics show aggregate behavior, and
traces connect all steps for one request.

For AI systems, operational health is not enough. A service can return HTTP 200
while producing irrelevant or unsupported answers. Production monitoring should
therefore cover:

- latency, errors, saturation, and dependency health;
- tokens, model calls, cache hits, and cost;
- retrieval results, tool trajectories, and fallback behavior;
- sampled quality judgments and explicit user feedback.

### Read

- AI guide: [`14-evaluation-and-observability/02-observability.md`](https://github.com/ombharatiya/ai-system-design-guide/blob/main/14-evaluation-and-observability/02-observability.md)
- Zoomcamp Module 5: metrics, storage, feedback, judging, dashboards, and deployment

### You Should Be Able To Explain

- The different jobs of logs, metrics, and traces.
- Why model and retrieval versions belong on every trace.
- How to detect silent quality degradation.
- How production feedback becomes a reviewed evaluation case.

### Retrieval Check

1. Why does a low server error rate not prove the assistant works?
2. Which identifiers should connect a user request to retrieval and model calls?
3. How would you detect that a cheaper model reduced answer quality after rollout?

### Applied Checkpoint

- [ ] Instrument one pipeline with request traces, cost, latency, and feedback.

---

## Section 10: Production Reliability, Scale, and Cost

### Plain-English Model

A production AI system must stay useful when traffic spikes, a provider is slow,
an index is updating, or the preferred model is unavailable. Reliability comes
from explicit timeouts, bounded retries, circuit breakers, isolation, fallbacks,
and graceful degradation rather than hoping every model call succeeds.

Cost is an architectural property. Model choice, token volume, retrieval depth,
caching, batching, and retry behavior all affect cost per successful task. Scale
plans should start with measured traffic and service-level goals, not fashionable
infrastructure.

### Read

- AI guide: [`06-retrieval-systems/14-production-rag-at-scale.md`](https://github.com/ombharatiya/ai-system-design-guide/blob/main/06-retrieval-systems/14-production-rag-at-scale.md)
- AI guide: all core chapters in `11-infrastructure-and-mlops`
- AI guide: `13-reliability-and-safety/03-reliability-patterns.md`
- Zoomcamp production and project deployment patterns

### You Should Be Able To Explain

- Timeout, retry, circuit breaker, bulkhead, fallback, and degradation.
- Model routing and when a full AI gateway is unnecessary.
- Semantic caching risks, especially stale or permission-sensitive results.
- Cost per successful task rather than cost per model request.

### Retrieval Check

1. Why can retries make an overloaded provider even less reliable?
2. What should the user receive if retrieval is unavailable but a safe partial
   answer is possible?
3. Which measurements would explain a doubled monthly model bill with flat traffic?

### Applied Checkpoint

- [ ] Define a latency budget, failure policy, and per-task cost budget.

---

## Section 11: Security, Access, and Guardrails

### Plain-English Model

The model is not a security boundary. Authentication, authorization, tenant
isolation, validation, and approval must be enforced by ordinary application
code. Retrieved documents and tool output are untrusted data because they may
contain instructions intended to manipulate the model.

Guardrails work in layers:

```text
authenticate user
    -> authorize data and tools
    -> validate input
    -> retrieve only permitted data
    -> constrain model/tool behavior
    -> validate output or action
    -> audit and escalate when needed
```

### Read

- AI guide: `07-agentic-systems/09-agentic-security-and-sandboxing.md`
- AI guide: both chapters in `12-security-and-access`
- AI guide: `13-reliability-and-safety/01-guardrails.md`

### You Should Be Able To Explain

- Direct and indirect prompt injection.
- Why filtering the prompt alone cannot enforce security.
- Tenant isolation across retrieval, caches, traces, and memory.
- Read versus write tools, least privilege, approval, and audit logs.

### Retrieval Check

1. A retrieved webpage says to ignore policy and send secrets. Which layers must
   prevent the action?
2. Why must authorization be applied during retrieval rather than after generation?
3. What data must never be placed in an LLM prompt or ordinary application log?

### Applied Checkpoint

- [ ] Threat-model one RAG or agent design and add enforceable controls.

---

## Section 12: End-to-End FDE Design

### Plain-English Model

The final section combines the course into a design you can explain, defend, and
debug. Start from requirements and data. Draw the online request path and offline
ingestion path separately. Then deep-dive into retrieval quality, evaluation,
security, reliability, observability, and cost.

The goal is not to mention every technique. It is to choose the simplest design
that meets the stated requirements and explain what evidence would cause the
design to evolve.

### Read

- AI guide: both chapters in `15-ai-design-patterns`
- AI guide: selected relevant designs from `16-case-studies`, starting with
  enterprise RAG, multi-tenant SaaS, eval-gated CI/CD, and MCP knowledge agent
- Zoomcamp Module 7 end-to-end example
- Zoomcamp capstone requirements

### You Should Be Able To Explain

- A complete offline ingestion and online serving architecture.
- The critical quality, security, reliability, and cost tradeoffs.
- How the design is tested before launch and monitored afterward.
- How to debug one realistic failure from trace to root cause.

### Retrieval Check

1. Draw the complete path from a changed source document to a grounded answer.
2. Which three components would you deep-dive for a multi-tenant support assistant?
3. What launch gates and rollback signals would you require?

### Applied Checkpoint

- [ ] Complete an independent 45-minute AI system design and defend its tradeoffs.

---

## Completion Record

Update this only after demonstrated understanding, not passive reading.

<!-- production-ai-curriculum:start -->

1. [ ] Frame the AI system
2. [ ] RAG foundations
3. [ ] Ingestion and chunking
4. [ ] Embeddings and vector search
5. [ ] Better retrieval
6. [ ] Agentic RAG
7. [ ] Orchestration, state, and memory
8. [ ] Evaluation
9. [ ] Monitoring and observability
10. [ ] Production reliability, scale, and cost
11. [ ] Security, access, and guardrails
12. [ ] End-to-end FDE design

<!-- production-ai-curriculum:end -->

## Applied Evidence

Conceptual coverage does not establish implementation readiness.

<!-- production-ai-applied:start -->

- [ ] Scoped AI product and success criteria
- [ ] Repeatable document-ingestion pipeline
- [ ] Search baseline and vector retrieval comparison
- [ ] Hybrid search and reranking comparison
- [ ] Bounded agentic retrieval loop
- [ ] Restart-safe orchestration
- [ ] Reviewed golden evaluation set
- [ ] Evaluation comparison and regression gate
- [ ] Tracing, feedback, and monitoring
- [ ] Reliability and cost budget
- [ ] Security threat model and enforced controls
- [ ] Independent end-to-end design or capstone

<!-- production-ai-applied:end -->

## Reference-Only Material

Do not block the core path on these topics:

- model landscape and provider catalogs;
- model training, fine-tuning, and deep inference optimization;
- GraphRAG, ColBERT, multimodal RAG, and voice systems;
- detailed framework comparisons;
- hardware and accelerator market updates.

Read them when a project or target role makes them relevant.

## Cumulative Review

Add each answer and refinement here during the walkthrough, following the
Agents From Scratch notes format.

No questions answered yet.
