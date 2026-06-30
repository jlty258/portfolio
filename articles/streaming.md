# Streaming Infrastructure at National Scale

---

## Scale Context

The connected vehicle platform at Shanghai Jiayu Intelligent Robotics operates
at scale that changes engineering constraints:

- 1M+ connected vehicles
- 10B+ telemetry events per day
- 1000+ vCore Flink streaming cluster

At this scale, design decisions that are acceptable at prototype scale become
production failures. This article documents the decisions that matter at
national device scale, not streaming technology tutorials.

---

## The Ingestion Boundary Problem

The first architectural decision: where to place the boundary between device
producers and downstream processing.

**Option considered:** Direct T-Box to Flink connection.

**Why rejected:** At 1M+ devices, traffic bursts during peak hours exceed
steady-state processing capacity by orders of magnitude. Direct coupling
propagates backpressure to device connectivity, causing cascading failures
across the fleet.

**Decision:** Kafka as mandatory ingestion boundary.

**Result:** Kafka absorbs burst traffic. Flink consumer lag increases during
peaks but device connectivity remains stable. Consumer lag monitoring triggers
Flink scaling response rather than device disconnection.

This is the single most important architectural decision in the platform.
Everything downstream depends on ingestion decoupling working correctly.

---

## Stream Processing Design

### Stateful vs. Stateless Jobs

Three job categories with different state requirements:

**Aggregation jobs** require RocksDB state backend. Windowed metrics over
telemetry streams accumulate state that exceeds in-memory Task Manager capacity
at 10B+ events/day.

**Enrichment jobs** use broadcast state for low-cardinality reference data
(vehicle model, fleet assignment). Reference data loaded once, joined against
high-volume event stream.

**Routing jobs** are stateless. High throughput, no checkpoint overhead.

Mixing state requirements in a single job template creates operational
complexity. Job type classification precedes implementation.

### Exactly-Once Semantics

Aggregation workloads require exactly-once processing. Duplicate events from
1M+ devices would corrupt windowed metrics used for business decisions.

Flink checkpointing with exactly-once sink configuration to Apache Doris.
Checkpoint interval tuned by measuring recovery time under realistic state
sizes, not default configuration.

---

## The Real-time Warehouse Layer

**Question:** Why not serve business APIs directly from Flink state or Kafka?

**Answer:** Business applications require ad-hoc analytical queries over
historical and real-time data. Flink state serves processing, not analytical
query patterns. Kafka serves ingestion, not sub-second query latency.

**Decision:** Apache Doris as real-time warehouse layer.

Columnar storage optimized for time-series query patterns. Business APIs query
Doris, not Flink internals.

**Trade-off:** Additional data movement from Flink to Doris adds seconds-level
freshness latency. Acceptable for fleet management and operational analytics
use cases. Not acceptable for sub-second alerting — those consume directly
from Flink side outputs.

---

## Metadata at Streaming Scale

At 1M+ device scale, schema evolution is continuous, not episodic. New vehicle
models, firmware updates, and telemetry categories change message formats
regularly.

Metadata and data governance as platform primitives:

- Schema registration per topic and vehicle model
- Lineage from Kafka topic through Flink job to Doris table
- Data quality rules at ingestion boundary

Without platform-level metadata, downstream teams cannot discover or trust
telemetry datasets. Every integration requires direct platform team
coordination — which does not scale.

---

## Operational Reality at 1000+ vCore

Custom Flink management scripts fail at 1000+ vCore scale. Job deployment,
monitoring, savepoint management, and rollback require standardized operational
tooling.

Dinky platform integration provided:

- Job submission and versioning workflows
- Cluster monitoring and alerting
- Savepoint-triggered upgrades without state loss

**Lesson:** Operational platform integration becomes a larger engineering
investment than individual job optimization at this scale. Budget for it when
planning cluster growth, not after operational pain becomes acute.

---

## Key Metrics That Matter

| Metric | Why It Matters |
|--------|----------------|
| Kafka consumer lag | Early signal of processing capacity gap |
| Flink checkpoint duration | Recovery time bound; state size indicator |
| Operator backpressure | Bottleneck identification per job |
| Doris query latency | Business API SLA compliance |
| Schema validation failure rate | Data quality at ingestion boundary |

Optimize based on these metrics, not assumptions about where bottlenecks exist.

---

## Lessons Learned

1. Ingestion decoupling is non-negotiable at national device scale.
2. Layered storage (Kafka → Flink → Doris) outperforms single-store designs
   because access patterns differ between ingestion, computation, and serving.
3. Metadata must be a platform capability from initial deployment.
4. Operational tooling scales non-linearly with cluster size.
5. Measure consumer lag and checkpoint duration before tuning parallelism.

---

## Conclusion

Streaming infrastructure at 10B+ events/day is an architecture problem first
and a technology problem second. The technologies (Kafka, Flink, Doris) are
implementation choices. The architecture (ingestion boundary, layered storage,
platform metadata, operational tooling) is what determines whether the system
survives production scale.
