# Guan Chen

Staff Data Platform Engineer | Shanghai, China | Open to Global Remote

jromeguan@gmail.com | https://github.com/jlty258

---

## Summary

Platform architect with 13+ years designing enterprise data infrastructure
across analytical, streaming, and privacy computing domains. Defined
execution planning architectures, platform abstractions, and engineering
standards that enabled teams to build on shared infrastructure rather than
one-off implementations. Operated platforms at 10B+ events/day and PB-scale
analytical scale.

---

## Experience

### Senior Data Platform Engineer

Shanghai Puxin Future Internet Research Institute | Dec 2024 – Present

- Defined platform architecture for privacy computing execution: PQL → Planner
  → Execution DAG → Scheduler → Execution Engine → Data Service → Storage
- Established execution planning as a first-class platform capability,
  enabling declarative queries across heterogeneous compute and storage
  backends without per-workload orchestration
- Designed storage abstraction and Data Service interfaces as reusable
  platform contracts, reducing integration cost for new execution backends
- Standardized platform interfaces across planner, scheduler, execution
  engine, and data service, improving cross-component delivery consistency
- Built benchmark platform to drive optimization decisions with measurable
  evidence rather than assumption-based tuning

### Senior Data Platform Engineer / Technical Architect

Shanghai Jiayu Intelligent Robotics | Jun 2020 – Sep 2024

- Owned end-to-end streaming platform architecture for 1M+ connected vehicles
  processing 10B+ telemetry events/day on 1000+ vCore cluster
- Defined platform boundaries between ingestion (Kafka), computation (Flink),
  storage (Doris), and serving (Business APIs), enabling independent scaling
  of each layer
- Established metadata and data governance standards as platform primitives,
  not per-team conventions, across national-scale telemetry datasets
- Architected real-time warehouse on Apache Doris, selecting columnar storage
  for high-volume time-series query patterns over row-oriented alternatives
- Enabled operational scalability through Dinky platform integration for
  Flink job lifecycle management across the streaming cluster

### Senior Data Platform Engineer

Ping An Securities | May 2017 – Apr 2020

- Defined enterprise metric platform architecture bridging PB-scale Hive
  analytics with Elasticsearch serving 100000+ searchable fields
- Solved dynamic schema problem at 2000+ Hive column scale through Map-based
  translation layer, avoiding manual schema migration for each metric addition
- Optimized 1000+ vCore analytical cluster utilization through Hive execution
  tuning and Hadoop workload isolation standards
- Abstracted analytical computation from search serving, establishing a
  reusable pattern: compute in batch layer, serve through search layer

### Data Platform Engineer

Shanghai Jiayin Data Technology

- Built foundational streaming and batch pipelines for restaurant intelligence
  analytics using Storm, Hive, and Hadoop

### Research Engineer

Shanghai Ship and Shipping Research Institute

- Applied distributed computing to hydrodynamic simulation, establishing early
  foundation in large-scale data processing

---

## Skills

Platform Architecture | Execution Planning | Storage Abstraction | Distributed
Systems | Kafka, Flink, Spark, Hive, Hadoop | Doris, Hudi, Elasticsearch, HDFS
| Metadata, Data Governance | Linux, Docker, Kubernetes | Java, Python, C

---

## Education

Master, Naval Architecture and Ocean Engineering — Shanghai Ship and Shipping
Research Institute

Bachelor, Hydraulic Engineering — Tianjin University
