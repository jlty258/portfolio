# Guan Chen

Senior Data Platform Engineer | Shanghai, China | Open to Global Remote

jromeguan@gmail.com | https://github.com/jlty258 | https://github.com/jlty258/portfolio

---

## Summary

Platform engineer with 13+ years building distributed data infrastructure,
transitioning from scientific computing to enterprise platform engineering.
Designed PB-scale analytical platforms, streaming systems at 10B+ events/day
and 1M+ connected vehicles, and privacy computing execution pipelines with
query planning and storage abstraction.

---

## Experience

### Senior Data Platform Engineer

Shanghai Puxin Future Internet Research Institute | Dec 2024 – Present

*MIRA / ChainWeaver — Privacy Computing Platform*

- Designed PQL execution planning pipeline converting declarative queries into
  distributed DAGs, enabling application teams to submit queries instead of
  custom orchestration scripts
- Architected query planner separating query semantics from execution strategy,
  allowing execution engine evolution without upstream contract changes
- Built reusable Data Service and storage abstraction layers, enabling new
  storage backends to integrate through stable interfaces
- Established platform interfaces and engineering standards across planner,
  scheduler, execution engine, and data service components
- Built benchmark platform to drive execution planning and runtime optimization
  with measurable evidence

### Senior Data Platform Engineer / Technical Architect

Shanghai Jiayu Intelligent Robotics | Jun 2020 – Sep 2024

*Connected Vehicle Telematics — National-Scale Streaming Platform (China)*

- Owned end-to-end streaming platform architecture serving 1M+ connected
  vehicles and 10B+ telemetry events/day on a 1000+ vCore Flink cluster
- Designed Kafka ingestion boundary decoupling millions of vehicle T-Box
  producers from downstream stream processing and storage consumers
- Built Flink pipelines for real-time aggregation and enrichment; Apache Doris
  serves as real-time warehouse for business-facing analytical queries
- Established metadata and data governance as platform-wide standards across
  national-scale telemetry datasets
- Integrated Dinky for Flink job lifecycle management across the 1000+ vCore
  cluster

### Senior Data Platform Engineer

Ping An Securities | May 2017 – Apr 2020

*Enterprise Financial Analytics — Metric Platform (China)*

- Architected metric platform unifying PB-scale Hive analytics with
  Elasticsearch serving 100000+ searchable metric fields to business
  applications without direct Hive access
- Designed dynamic schema expansion mapping 2000+ Hive physical columns to
  Elasticsearch through a Map-based translation layer
- Optimized Hive and Hadoop on 1000+ vCore cluster across PB-scale storage,
  improving query latency and cluster resource utilization
- Established compute-serve separation pattern: batch computation in Hive,
  interactive search in Elasticsearch

### Data Platform Engineer

Shanghai Jiayin Data Technology | Restaurant Intelligence / Wi-Fi Analytics

- Built streaming and batch pipelines for restaurant intelligence and commercial
  Wi-Fi analytics using Storm, Hive, and Hadoop

### Research Engineer

Shanghai Ship and Shipping Research Institute | Scientific Computing

- Applied Hadoop and Hive to large-scale hydrodynamic simulation workloads

---

## Skills

**Platform:** Distributed Systems, Execution Planning, Storage Abstraction,
Metadata, Data Governance

**Streaming & Compute:** Kafka, Flink, Spark, Hive, Hadoop

**Storage & Search:** HDFS, Doris, Hudi, Elasticsearch

**Infrastructure:** Linux, Docker, Kubernetes

**Languages:** Java, Python, C

---

## Education

Master, Naval Architecture and Ocean Engineering — Shanghai Ship and Shipping
Research Institute

Bachelor, Hydraulic Engineering — Tianjin University

---

## Portfolio

Architecture documents, system design deep-dives, and interview preparation
materials: https://github.com/jlty258/portfolio
