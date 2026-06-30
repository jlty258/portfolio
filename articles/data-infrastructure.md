# Data Infrastructure: Three Domains, One Career

---

## The Through-Line

Distributed data infrastructure is not one technology stack. It is a set of
architectural patterns applied to different domain constraints across a career.

My work spans three domains with different access patterns, scale profiles,
and correctness requirements:

| Domain | Company | Scale | Core Pattern |
|--------|---------|-------|--------------|
| Analytical Computing | Ping An Securities | PB-scale, 100K+ metrics | Compute → Translate → Serve |
| Streaming | Jiayu Robotics | 10B+ events/day, 1M+ devices | Ingest → Process → Warehouse → API |
| Privacy Computing | Puxin Research | Multi-party execution | Query → Plan → Schedule → Execute |

The technologies differ. The platform engineering mindset persists.

---

## Analytical Computing Infrastructure

### Domain Constraints

Enterprise securities analytics requires querying thousands of metrics across
PB-scale historical data. Business users need interactive search, not batch
query submission.

Structural challenge: 2000+ Hive physical columns must become 100000+
searchable Elasticsearch fields — exceeding Elasticsearch per-index field
limits through direct mapping.

### Architecture

```
Hive → Metric Map → Dynamic Schema Expansion → Elasticsearch
```

**Compute-serve separation.** Hive handles PB-scale batch computation. Elasticsearch
handles sub-second interactive search. Each layer optimizes for its access pattern.

**Dynamic schema as architecture.** Map-based translation layer solves field
limit constraints. New metrics onboard through the Map without manual index
restructuring.

**Cluster optimization.** 1000+ vCore Hadoop cluster tuned through partition
pruning, column pruning, and workload isolation — leveraging existing PB-scale
investment rather than migration risk.

---

## Streaming Infrastructure

### Domain Constraints

Connected vehicle telematics at national scale: heterogeneous messages from
1M+ devices, burst traffic patterns, real-time and analytical access to the
same data domain.

Structural challenge: direct device-to-processing coupling fails during peak
traffic. Schema evolution across vehicle models requires governance, not
ad-hoc fixes.

### Architecture

```
Vehicle T-Box → Kafka → Flink → Doris → Business APIs
```

**Ingestion boundary.** Kafka decouples producers from consumers. Non-negotiable
at 1M+ device scale.

**Layered storage.** Kafka for ingestion, Flink state for processing, Doris
for serving. No single store serves all access patterns optimally.

**Platform metadata.** Schema registration, lineage, and data quality as
platform primitives from initial deployment.

**Operational tooling.** Dinky integration for Flink job management at 1000+
vCore scale.

---

## Privacy Computing Infrastructure

### Domain Constraints

Privacy computing requires executing workloads across multiple parties without
exposing raw data. Query structures vary; storage backends differ across
deployments; performance optimization requires measurement.

Structural challenge: without unified execution planning, each workload
requires custom orchestration code.

### Architecture

```
PQL → Planner → Execution DAG → Scheduler → Execution Engine → Data Service → Storage
```

**Execution planning as platform primitive.** Query planner converts declarative
PQL into distributed DAGs. Application teams submit queries, not orchestration
scripts.

**Storage abstraction.** Data Service decouples execution engines from physical
storage. Backend portability across deployment environments.

**Platform standardization.** Interfaces across planner, scheduler, engine, and
data service defined before multi-team integration.

**Benchmark platform.** Measurable evidence for optimization across planning,
scheduling, and storage dimensions.

---

## Patterns That Transfer

### Layer Decoupling

Every domain separates concerns into independent layers:

- Analytical: compute (Hive) / translate (Map) / serve (Elasticsearch)
- Streaming: ingest (Kafka) / process (Flink) / serve (Doris)
- Privacy: plan / schedule / execute / access (Data Service)

Layers scale independently. Failures isolate to layer boundaries.

### Abstraction as Product

The highest-value artifact is never the pipeline:

- Metric Map > individual Hive jobs
- Kafka boundary > individual Flink jobs
- Data Service > individual execution engines

Invest in abstractions early. They compound as the platform grows.

### Schema as Architecture

At 100K+ metrics and 1M+ device schemas, schema management requires dedicated
design. Dynamic schema expansion and platform metadata governance are
architectural decisions, not configuration tasks.

### Measure Before Optimize

Benchmark platforms, consumer lag monitoring, partition scan measurement.
Optimization without measurement optimizes the wrong dimension confidently.

---

## What Does Not Transfer

Domain-specific constraints require domain-specific decisions:

- Privacy computing requires cross-party isolation and execution planning
- Streaming requires state management and exactly-once semantics at event scale
- Analytical computing requires batch optimization and search serving separation

The platform engineering principles transfer. The specific technology and
architecture choices do not.

---

## Career Evolution

```
Scientific Computing (Hadoop/Hive for simulation)
    ↓
Analytical Computing (PB-scale metric platform)
    ↓
Streaming Infrastructure (national vehicle telematics)
    ↓
Privacy Computing (execution planning platform)
```

Each transition expanded the scope of platform ownership: from batch analytics
to real-time national infrastructure to privacy-preserving distributed
execution with query planning and storage abstraction.

---

## Conclusion

Data infrastructure engineering is not about accumulating technology
experience. It is about recognizing recurring architectural patterns, applying
them to domain-specific constraints, and building platforms that abstract
complexity for the teams that depend on them.

Three domains. Same principles. Different implementations.

That is the career this portfolio represents.
