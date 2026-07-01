# Interview Stories

Structured narratives for behavioral and system design interviews.
All facts sourced from RESUME_FACTS.md.

---

## Story 1: Dynamic Schema at 100K+ Metric Scale

**Domain:** Analytical Computing — Ping An Securities

**Situation**

Enterprise metric platform needed to expose 100000+ searchable metric fields
to business applications. Hive tables contained 2000+ physical columns per
table. Elasticsearch per-index field limits (~1000 fields) made direct
column-to-field mapping infeasible.

**Task**

Design a schema architecture that supports dynamic metric addition without
manual index migration, while maintaining sub-second search performance for
business users.

**Action**

- Separated analytical computation (Hive) from search serving (Elasticsearch)
  so each layer optimized independently
- Designed Map-based schema translation layer between Hive outputs and
  Elasticsearch indices
- Built Metric Map catalog mapping logical metric IDs to Hive column references
- Implemented dynamic schema expansion triggered on metric onboarding, not
  manual index rebuild

**Result**

- 100,000+ searchable metric fields served through Elasticsearch
- Reduced 1000+ vCore batch computation time from 2.5 hours to 1.5 hours
- New metrics onboard through Map layer without cross-system schema migration
- Business applications query metrics without Hive or SQL expertise
- PB-scale batch computation and interactive search operate independently

**Key Trade-off**

Batch freshness latency (compute-serve separation) accepted in exchange for
sub-second search performance and independent layer scaling.

**Interview Angle:** Architecture under constraint. How do you solve problems
that configuration cannot address?

---

## Story 2: Ingestion Decoupling at 1M+ Device Scale

**Domain:** Streaming Infrastructure — Jiayu Robotics

**Situation**

Connected vehicle platform ingesting telemetry from 1M+ T-Box devices at 10B+
events per day. Traffic bursts during peak hours exceeded steady-state
processing capacity. Direct device-to-Flink coupling caused backpressure
propagating to device connectivity.

**Task**

Design ingestion architecture that absorbs traffic bursts without cascading
failures to vehicle connectivity, while supporting multiple downstream
consumers.

**Action**

- Established Kafka as mandatory ingestion boundary between T-Box producers
  and all downstream consumers
- Designed topic partitioning by vehicle ID for per-device ordering
- Isolated consumer groups for Flink processing, archival, and monitoring
- Integrated metadata schema registration at topic level for downstream discovery
- Monitored consumer lag as primary signal for Flink scaling response

**Result**

- Scaled Apache Flink platform from 10,000 to 1,000,000+ connected vehicles
  with stable production output
- Platform processes 10B+ events/day without device connectivity failures
  during peak traffic
- Multiple downstream pipelines consume independently via isolated consumer
  groups
- 1000+ vCore Flink cluster scales based on measurable consumer lag metrics

**Key Trade-off**

Kafka cluster operational overhead accepted as necessary cost for decoupling
at national device scale.

**Interview Angle:** Scale-driven architecture. What changes when you go from
thousands to millions of producers?

---

## Story 3: Execution Planning as Platform Primitive

**Domain:** Privacy Computing — Puxin Research Institute

**Situation**

MIRA privacy computing platform required executing analytical workloads across
multiple parties with strict data isolation. Application teams were writing
custom orchestration scripts for each query pattern. Integration cost grew
linearly with query diversity.

**Task**

Design an execution layer that transforms declarative queries into distributed
execution plans, eliminating per-workload orchestration code.

**Action**

- Designed PQL execution planning pipeline: PQL → Planner → Execution DAG →
  Scheduler → Execution Engine → Data Service → Storage
- Built query planner separating query semantics from execution strategy
- Defined distributed DAG model with stage-level retry semantics
- Established Data Service and storage abstraction as reusable platform
  interfaces
- Built benchmark platform for evidence-based optimization decisions
- Standardized platform interfaces across planner, scheduler, engine, and
  data service before multi-team integration

**Result**

- Application teams submit declarative PQL queries instead of orchestration
  scripts
- Data Service supports 10+ data source types, billion-scale table reads,
  and S3 object storage access
- New execution backends integrate through documented platform interfaces
- Optimization driven by benchmark evidence across planning and runtime
  dimensions

**Key Trade-off**

Planner engineering complexity accepted in exchange for eliminating per-query
orchestration code and enabling backend portability through storage abstraction.

**Interview Angle:** Platform vs. feature. When do you invest in a planning
layer vs. template-based execution?

---

## Story 4: Operational Tooling at 1000+ vCore Scale

**Domain:** Streaming Infrastructure — Jiayu Robotics

**Situation**

Flink streaming cluster grew to 1000+ vCore. Custom scripts for job deployment,
monitoring, savepoint management, and rollback did not scale with cluster size
or team growth.

**Task**

Reduce operational overhead for Flink job lifecycle management without
 sacrificing deployment velocity or state recovery capability.

**Action**

- Evaluated operational tooling options against 1000+ vCore management requirements
- Integrated Dinky platform for standardized job submission, versioning, and
  rollback workflows
- Established savepoint-triggered upgrade process for job logic changes without
  state loss
- Defined monitoring standards: consumer lag, checkpoint duration, backpressure

**Result**

- Standardized Flink job operations across 1000+ vCore cluster
- Job upgrades via savepoint without full state reconstruction
- Operational cost reduced compared to custom script maintenance

**Key Trade-off**

Third-party platform dependency (Dinky) accepted in exchange for standardized
operations at scale where custom tooling cost exceeded integration cost.

**Interview Angle:** Operational engineering. When does tooling become more
important than feature development?

---

## Story 5: Platform Standardization Before Multi-Team Integration

**Domain:** Privacy Computing — Puxin Research Institute

**Situation**

Multiple teams preparing to integrate with MIRA platform components (planner,
scheduler, execution engine, data service). Without defined interfaces, each
integration risked becoming a bespoke negotiation.

**Task**

Define platform interfaces and engineering standards before integration
proliferation creates retrofit cost.

**Action**

- Defined interface contracts between planner, scheduler, execution engine,
  and data service
- Documented integration requirements for new execution backend registration
- Established engineering standards for platform component development
- Built benchmark platform as shared measurement infrastructure

**Result**

- New execution backends integrate through documented interfaces
- Cross-team delivery consistency improved through shared standards
- Integration cost reduced compared to per-team bespoke agreements

**Key Trade-off**

Upfront interface design investment accepted to avoid exponential retrofit
cost after multi-team integration.

**Interview Angle:** Technical leadership. How do you prevent integration
debt in platform engineering?

---

## Quick Reference: Story Selection Guide

| Interview Question Type | Recommended Story |
|------------------------|-------------------|
| Architecture under constraint | Dynamic Schema (Story 1) |
| Scale and reliability | Ingestion Decoupling (Story 2) |
| Platform design | Execution Planning (Story 3) |
| Operational excellence | Operational Tooling (Story 4) |
| Technical leadership | Platform Standardization (Story 5) |
| Trade-off reasoning | Any story — each includes explicit trade-off |
| Failure recovery | Story 2 (burst traffic) or Story 3 (stage retry) |
