# Agents From Scratch Learning Notes

Review notes for the `langchain-ai/agents-from-scratch` walkthrough.

- Started: 2026-07-22
- Current estimated curriculum coverage: 51%
- Local repository: `/Users/viksat98/agents-from-scratch`
- Source: <https://github.com/langchain-ai/agents-from-scratch>

## Current Mental Model

An agent combines three distinct pieces:

- **Model:** interprets the current context and proposes a response or tool call.
- **Graph:** owns workflow execution, shared state, routing, loops, pauses, and termination.
- **Tool:** exposes a typed operation to the model; ordinary application code validates and executes it.

Invoking a compiled graph starts with an initial shared state. Nodes read and update that state, edges determine which node runs next, and execution continues until `END` or an interrupt pauses the run.

## Review Questions

### 1. What happens after `app.invoke(initial_state)`?

**Your answer:** The graph already has its states, nodes, and edges compiled. It follows the appropriate edges through the nodes until it reaches the end.

**Review:** Correct overall. The important refinement is that the graph usually carries one evolving shared state object rather than moving among separate "state locations." Each node returns updates that LangGraph merges into that shared state.

### 2. What is the difference between a fixed edge and a conditional edge?

```python
workflow.add_edge("A", "B")
```

**Your answer:** The fixed edge goes from A to B. Conditional routing decides which flow to take based on a condition.

**Review:** Correct. A fixed edge always chooses the same destination. A conditional edge runs routing logic and selects among several destinations.

### 3. Does the model execute a requested tool?

**Your answer:** The tool makes the function runnable with the supplied arguments.

**Review:** Close. The model only produces a structured request containing a tool name and arguments. The graph's tool node or environment looks up the actual function, validates the request, and executes normal Python code.

```text
Model requests tool
    -> runtime finds tool
    -> Python executes tool
    -> result returns to state
```

### 4. Why add tool results to message history?

**Your answer:** So there is a history of how the user interacts for later conversations.

**Review:** That can be useful when persistence is configured, but the immediate purpose is current-run context. The model is stateless between calls. It needs the original request, its tool request, and the tool result to decide the next action. Long-term memory requires a checkpointer, store, or database; message history alone does not guarantee it.

### 5. Why use an email triage router?

**Your answer:** To determine whether an email is spam and make other decisions along the way.

**Review:** Correct. The router classifies each email as:

- `ignore`: irrelevant, spam, or marketing
- `notify`: important but no reply required
- `respond`: send it to the response agent

This prevents the full response agent from processing every email.

### 6. What is the difference between conditional routing and `Command`?

**Your answer:** You did not remember this distinction yet.

**Review:**

- A conditional-edge function chooses the next node separately after a node updates state.
- `Command(goto=..., update=...)` lets the current node update state and select the next node together.

They can implement the same flow. The difference is where the routing decision lives.

### 7. Why put a compiled graph inside another graph?

**Your answer:** Components let us model a bigger workflow as one node and abstract away the internal details.

**Review:** Correct. The outer graph can treat the complete response-agent loop as one reusable node instead of managing all of its internal model and tool nodes.

### 8. Why is binding tools insufficient for safety?

**Your answer:** The model could call the wrong function, so the output structure should be verified.

**Review:** Correct direction. Validate the requested tool name and arguments before execution. Also remember that a call can match the schema and still be harmful, such as sending private information to the wrong valid email address. Consequential tools also need permission checks, allowlists, rate limits, tool-side validation, and often human approval.

### 9. What are the model, graph, and tool?

**Your answer:**

- The model is the AI model, such as GPT.
- The graph describes the ways to reach an outcome.
- A tool exposes functions to the AI agent or LangGraph.

**Review:** Correct overall.

- The model interprets context and proposes output or actions.
- The graph controls execution, shared state, routing, and completion.
- A tool wraps a function with a name, description, and argument schema. The model requests it; the runtime executes it.

### 10. What is a reducer?

**Review:** A reducer is the merge rule for a state field.

- Ordinary fields normally replace their previous value.
- `MessagesState` normally accumulates new messages.
- A new message with the same message ID can replace the existing message.

### 11. Why preserve old messages if the graph can continue to the next node?

**Review:** Each model invocation only knows the context supplied to that invocation. After a calendar lookup, the model still needs the original attendee, requested day, and purpose. Message history preserves this context. A more structured workflow can store those facts in dedicated state fields instead; many systems use both approaches.

### 12. Why configure the same model for two narrow jobs?

**Your answer:** Each model configuration does its own narrow task, making failures easier to locate.

**Review:** Correct. The router uses structured output and cannot take external actions. The response agent receives tools. This improves debugging and follows least privilege.

```text
GPT + RouterSchema -> classify email
GPT + bound tools  -> propose actions
```

### 13. If the router returns a valid but wrong classification, did the schema fail?

**Your answer:** The schema succeeded, but the prompt was not good enough.

**Review:** Correct. The schema enforces the shape of the answer, not its semantic correctness. The prompt, examples, model, and evaluation dataset determine behavioral quality.

### 14. Which evaluation checks exact tool use versus response quality?

**Your answer:** Use a variable or assertion to check whether the tool was called, and use another LLM for response quality.

**Review:** Correct.

- Deterministic assertion: verify exact facts such as whether `write_email` was called.
- LLM-as-judge: evaluate semantic criteria such as politeness, completeness, or groundedness.

### 15. Which layer catches a correct final reply reached through an unsafe action?

**Your answer:** The trajectory layer.

**Review:** Correct. Final-output evaluation can miss an unwanted meeting or unnecessary write action. Trajectory and safety checks inspect how the result was produced.

### 16. What is the difference between Pytest and LangSmith?

**Your answer:** Pytest runs the checks; LangSmith is the second system used for comparison.

**Review:** Correct.

- Pytest executes test cases and assertions locally or in CI.
- LangSmith records traces, results, latency, token use, and experiment comparisons.

### 17. What changes when the underlying model is replaced?

**Your answer:** Initially, you thought none of the target, reference, or evaluator changed.

**Review:** The target system changes because the model is part of the agent being tested. The target function's Python interface may remain identical. References and evaluators should stay stable for a fair comparison.

### 18. Why rerun the entire dataset after fixing one production failure?

**Your answer:** The change could have affected other areas.

**Review:** Correct. Regression testing confirms the reported failure is fixed without breaking previously correct cases.

### 19. Why is `interrupt()` stronger than a prompt asking the model to seek approval?

**Your answer:** It lets a human interact with the workflow and approve continuation.

**Review:** Correct. More importantly, application code enforces the pause. The model cannot bypass the approval boundary by ignoring an instruction.

### 20. Which actions normally require approval?

**Your answer:**

- Search documentation: no
- Delete a calendar event: yes
- Read calendar availability: no
- Send a customer email: yes

**Review:** Correct. Read-only tools can usually run automatically. External writes, deletion, communication, purchases, and other consequential actions normally require stronger controls.

### 21. Why does every paused workflow need a unique thread ID?

**Your answer:** It identifies the particular process when multiple processes exist.

**Review:** Correct. The thread ID isolates each workflow's checkpoint, messages, pending action, and resume location. Without it, an approval could be applied to the wrong conversation.

### 22. When should a human edit arguments instead of giving model feedback?

**Question:** The email draft is good, but the recipient is wrong.

**Your answer:** Edit the sender argument.

**Review:** Use `edit` to change the recipient's `to` argument and execute the corrected proposal. Use feedback when the model needs to generate a new draft or reconsider its approach.

### 23. What happens if an edited AI message receives a new message ID?

**Status:** Not answered before the session ended.

**Answer:** The message reducer would normally append it as a second message instead of replacing the original proposal. Keeping the original message ID allows the reducer to replace the stale version and preserve truthful history.

## Architecture Summary

```text
Incoming email
      |
      v
Triage router
  |       |       |
ignore  notify  respond
  |       |       |
 END   interrupt  response-agent subgraph
                   |
                   v
                LLM call
                   |
          requested tool or Done?
            |              |
          tool           END
            |
    safe read or consequential write?
       |                    |
    execute              interrupt
                            |
                   accept/edit/ignore/feedback
                            |
                        resume loop
```

## Evaluation Summary

A useful evaluation suite checks different failure surfaces:

| Layer | Main Question | Example |
|---|---|---|
| Output | Is the final answer good? | Did the email answer every request? |
| Trajectory | Did the agent take the right path? | Did it check availability before proposing a time? |
| Safety | Did it avoid forbidden actions? | Did it send or schedule without approval? |
| Performance | Is operation practical? | What were latency and token cost? |

Each dataset example can contain:

- Input email
- Ground-truth classification
- Expected tool calls
- Forbidden tool calls
- Semantic response criteria

Pytest runs assertions. LangSmith stores traces and compares experiments. Regression tests rerun the full dataset after prompt, model, tool, or graph changes.

## Current Strengths

- Clear high-level understanding of graph execution
- Correct distinction between fixed and conditional routing
- Correct reason for composing workflows from subgraphs
- Correct model-request versus runtime-execution boundary
- Good instinct for tool validation and human approval
- Correct selection of deterministic versus semantic evaluation
- Correct understanding of trajectory and regression testing
- Correct approval boundaries for read-only and consequential tools

## Topics to Reinforce

- Treat state as one evolving shared object.
- Distinguish current-run message context from long-term memory.
- Remember reducers as per-field merge rules.
- Revisit `Command` versus conditional-edge routing.
- Remember that schema validity does not establish semantic correctness.
- Preserve message and tool-call IDs when editing recorded actions.

## Next Session

Continue the human-in-the-loop module:

1. Review how edited messages replace earlier messages through matching IDs.
2. Trace accept, edit, ignore, and feedback from interrupt to resume.
3. Finish HITL tests and deployment behavior.
4. Begin memory: thread-scoped checkpoints versus cross-thread stores.
