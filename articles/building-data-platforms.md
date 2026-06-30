# Building Data Platforms: Lessons from Three Domains

---

## Introduction

Over 13 years, I have built data infrastructure across three distinct domains:
analytical computing, streaming systems, and privacy computing. Each domain
presented different constraints, but the platform engineering principles
remained consistent.

This article distills patterns that transferred across domains and decisions
that were domain-specific.

---

## The Platform Pattern

Every successful data platform I have built follows the same structural pattern:

```
Source → Processing → Storage Abstraction → Serving
```

The specifics change. Hive becomes Flink. Elasticsearch becomes Doris. PQL
replaces SQL. But the layer boundaries persist because they solve the same
fundamental problem: **decoupling producers from consumers so each layer
scales independently**.

At Ping An Securities, the pattern was Hive → Metric Map → Elasticsearch.

At Jiayu Robotics, it was T-Box → Kafka → Flink → Doris.

At Puxin Research Institute, it was PQL → Planner → Execution Engine →
Data Service.

Recognizing this pattern early would have accelerated each subsequent platform
build. Instead, I learned it sequentially across three domains.

---

## Abstraction Is the Product

The most valuable artifact in a data platform is not the pipeline. It is the
abstraction layer.

At Ping An, the Metric Map was more valuable than any individual Hive job.
It translated 2000+ physical columns into 100000+ logical metrics that business
teams could search without understanding Hive schema complexity.

At Jiayu, Kafka was more valuable than any individual Flink job. It created
a stable ingestion boundary that survived traffic bursts from 1M+ connected
vehicles without cascading failures.

At Puxin, the Data Service was more valuable than any individual execution
engine. It provided unified data access that allowed new engines to integrate
through a stable interface rather than per-backend custom code.

**Lesson:** Invest in abstraction layers early. They compound in value as the
platform grows.

---

## Schema Is an Architecture Problem

At 100K+ metric scale, schema management cannot be a configuration task.
It is an architecture problem requiring dedicated design.

The dynamic schema expansion mechanism at Ping An solved a constraint that
no amount of Elasticsearch tuning could address: the field limit. The solution
was not better indexing. It was a Map-based translation layer that indirection
between physical and logical schema.

At Jiayu, schema evolution across vehicle models required metadata and data
governance as platform primitives, not per-team conventions. Without platform-level
schema registration, downstream teams could not trust telemetry datasets.

**Lesson:** When schema count exceeds hundreds, design a schema management
architecture. Do not rely on manual processes.

---

## Measure Before Optimize

The benchmark platform at Puxin exists because execution planning involves
multiple optimization dimensions: planner logic, DAG structure, engine selection,
storage access patterns. Optimizing any dimension without measurement produces
incorrect conclusions.

At Jiayu, Flink cluster tuning on 1000+ vCore required monitoring consumer
lag, checkpoint duration, and backpressure metrics before adjusting parallelism
or state backend configuration.

At Ping An, Hive optimization on PB-scale data required measuring partition
scan volumes and column read patterns before rewriting query plans.

**Lesson:** Build measurement infrastructure alongside the platform. Benchmark
platforms and monitoring are not overhead — they are prerequisites for
correct optimization.

---

## Operational Tooling Scales Non-linearly

At Jiayu, managing Flink jobs on a 1000+ vCore cluster with custom scripts
does not scale. Integrating Dinky for job lifecycle management reduced
operational cost more than any individual job optimization.

This pattern repeats: as platform scale increases, operational tooling becomes
a larger fraction of engineering effort than feature development.

**Lesson:** Budget for operational platform integration from the start of
cluster scaling, not after operational pain becomes acute.

---

## Trade-offs Are the Engineering Content

Every platform decision I document includes explicit trade-offs:

- Kafka decoupling vs. operational overhead
- Batch freshness vs. interactive search latency
- Storage abstraction vs. push-down optimization
- Platform standardization vs. team autonomy

Hiring managers and staff engineers evaluate platform engineers by their
ability to articulate trade-offs, not by their technology list.

**Lesson:** Document why you chose an architecture, what you gave up, and
what you would change with hindsight. This is the content that demonstrates
engineering maturity.

---

## What Transfers vs. What Does Not

**Transfers across domains:**

- Layer boundary design (ingestion / compute / serve)
- Abstraction as primary product
- Schema management architecture
- Measurement-driven optimization
- Platform standardization over per-team conventions

**Domain-specific:**

- Privacy computing requires execution planning and cross-party isolation
- Streaming requires state management and exactly-once semantics
- Analytical computing requires batch optimization and search serving separation

The platform engineering mindset transfers. The specific technology choices
do not.

---

## Conclusion

Building data platforms is not about knowing Kafka, Flink, or Hive. It is
about recognizing recurring structural patterns, investing in abstractions
that compound, treating schema as architecture, measuring before optimizing,
and documenting trade-offs explicitly.

Three domains. Same principles. Different implementations.

That is platform engineering.
