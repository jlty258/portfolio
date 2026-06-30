# Engineering Philosophy

---

## Infrastructure Should Simplify Complexity

The purpose of infrastructure is not to exist. It is to make complex systems
simple for the teams that build on top of them.

When I designed the Data Service layer for the MIRA privacy computing platform,
the goal was not to add another component. It was to eliminate the need for
every execution engine to implement its own storage integration logic.

When I established Kafka as the ingestion boundary for connected vehicle
telemetry, the goal was not to operate a message broker. It was to prevent
1M+ device producers from coupling directly to downstream processing systems.

Infrastructure that adds complexity without simplifying something upstream
is failed infrastructure.

---

## Build Platforms, Not Features

One-off implementations solve today's problem. Platforms solve tomorrow's
problems too.

The Metric Map at Ping An Securities was a platform decision. Individual Hive
jobs could compute metric values. But without the Map layer translating
physical columns to logical metrics, every new metric required manual schema
work across Hive and Elasticsearch.

The query planner at Puxin is a platform decision. Individual execution scripts
could run privacy computations. But without the planner converting PQL into
distributed DAGs, every new query pattern required custom orchestration.

Reusable platforms create compounding value. One-off features create
compounding maintenance cost.

---

## Abstraction First

Well-designed abstractions make systems easier to evolve. Poor abstractions
make systems harder to change than no abstraction at all.

The storage abstraction in MIRA separates execution logic from physical storage.
New storage backends integrate through a stable interface. Execution engine
code does not change.

The dynamic schema expansion at Ping An separates logical metrics from physical
Hive columns. New metrics onboard through the Map layer. Elasticsearch index
structures adapt automatically.

Good abstractions have thin interfaces and clear contracts. They hide
complexity without hiding necessary control.

---

## Standardization Enables Productivity

Engineering standards reduce communication cost and improve delivery efficiency.

At Puxin, platform interfaces across planner, scheduler, execution engine, and
data service components establish consistent integration contracts. Teams
building new execution backends follow documented interfaces rather than
negotiating per-integration agreements.

At Jiayu, metadata and data governance standards apply platform-wide rather
than per-team. Downstream consumers discover and trust datasets through
consistent catalog conventions.

Standardization is not bureaucracy. It is the mechanism that allows multiple
teams to build on shared infrastructure without coordination overhead on
every change.

---

## Measure Before Optimize

Performance improvements should be based on benchmarking and measurable evidence.

The benchmark platform at Puxin exists because execution planning optimization
involves multiple variables. Changing planner logic without measuring impact
on end-to-end query latency is engineering guesswork.

Hive optimization at Ping An required measuring partition scan volumes before
rewriting query plans. Flink tuning at Jiayu required monitoring checkpoint
duration and consumer lag before adjusting cluster configuration.

Optimization without measurement optimizes the wrong thing confidently.

---

## Reliability Is a Feature

Correctness, observability, and operational stability are first-class
engineering concerns — not afterthoughts added when production incidents occur.

At Jiayu, exactly-once Flink processing semantics, Kafka replication, and
Doris replica serving were architectural requirements from the start of
platform design, not reliability patches added after data loss incidents.

At Puxin, idempotent Data Service operations and stage-level DAG retry were
designed into the execution model, not bolted on after failed query recovery
attempts.

Reliability designed in is cheaper than reliability patched in.

---

## Engineering Is About Trade-offs

Every architectural decision has costs and benefits. Good engineers understand
and document those trade-offs.

| Decision | Benefit | Cost |
|----------|---------|------|
| Kafka ingestion decoupling | Independent scaling | Operational overhead |
| Batch compute + search serve | Optimized per access pattern | Freshness latency |
| Storage abstraction | Backend portability | Push-down optimization limits |
| Platform standardization | Consistent delivery | Upfront design investment |

Trade-offs are not failures. They are the content of engineering judgment.

---

## Architecture Over Implementation

Frameworks are implementation details. Architecture is the focus.

I have used Kafka, Flink, Hive, Elasticsearch, Doris, and Kubernetes across
different platforms. The specific technologies changed. The architectural
patterns — layer decoupling, abstraction, compute-serve separation, platform
standardization — persisted.

When evaluating an engineer's work, ask what architecture they designed and
why, not which frameworks they used.

---

## The Goal

When someone finishes reading this portfolio, they should conclude:

"This engineer designs large-scale distributed platforms."

Not:

"This engineer knows Java and Flink."

Everything here reinforces the first conclusion.
