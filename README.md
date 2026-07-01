# Guan Chen

Senior Data Platform Engineer building distributed data infrastructure.

Shanghai, China | Open to Global Remote

[jromeguan@gmail.com](mailto:jromeguan@gmail.com) |
[LinkedIn](https://www.linkedin.com/in/jrome-guan-47888241a) |
[GitHub](https://github.com/jlty258) |
[Portfolio](https://github.com/jlty258/portfolio)

---

## About

I build enterprise data infrastructure — platforms that abstract complexity
behind stable interfaces so product teams can move faster.

Over 13 years, my work has progressed through analytical computing,
streaming infrastructure, and privacy computing. Each phase deepened my focus
on platform engineering: reusable abstractions, execution planning, storage
layers, and engineering standards that scale across organizations.

---

## Career Highlights

| Domain | Scale | Key Architecture |
|--------|-------|------------------|
| Privacy Computing | Execution planning platform | PQL → Planner → DAG → Scheduler → Engine |
| Streaming | 1M+ vehicles, 10B+ events/day | T-Box → Kafka → Flink → Doris → APIs |
| Analytical | PB-scale Hadoop, 100K+ metrics | Hive → Dynamic Schema → Elasticsearch |

---

## Core Expertise

- **Distributed Systems** — Platform architecture, execution planning, DAG
  scheduling, storage abstraction
- **Streaming Infrastructure** — Kafka ingestion, Flink processing, real-time
  warehouse, metadata and data governance
- **Analytical Computing** — PB-scale batch processing, dynamic schema,
  metric platforms, search serving layers
- **Privacy Computing** — Query planning, distributed execution, benchmark
  platforms, platform standardization

---

## Featured Architecture

### Privacy Computing Platform (MIRA / ChainWeaver)

Designed the execution planning pipeline for a privacy computing platform.
Declarative PQL queries flow through a query planner into distributed DAGs,
scheduled across execution engines with unified data access via storage
abstraction.

[Architecture Details →](./architecture/privacy-computing.md)

### Connected Vehicle Streaming Platform

Architected end-to-end streaming infrastructure for connected vehicle
telematics. Kafka decouples ingestion from Flink computation; Apache Doris
serves as the real-time warehouse layer for business APIs.

[Architecture Details →](./architecture/streaming-platform.md)

### Enterprise Metric Platform

Built a metric platform bridging PB-scale Hive analytics with Elasticsearch
search. Dynamic schema expansion maps 2000+ Hive columns to 100000+
searchable fields without manual migration.

[Architecture Details →](./architecture/analytical-platform.md)

---

## Portfolio

| Document | Description |
|----------|-------------|
| [Master Resume](./resume/Master_Resume.md) | Comprehensive career narrative |
| [Senior Resume](./resume/Senior_US_Resume.md) · [PDF](./resume/Senior_US_Resume.pdf) | ATS-optimized, 2-page format |
| [Staff Resume](./resume/Staff_US_Resume.md) · [PDF](./resume/Staff_US_Resume.pdf) | Platform architecture focus |
| [Deploy Guide](./DEPLOY.md) | GitHub Pages setup instructions |
| [System Design](./system-design/) | Deep-dive design documents |
| [Articles](./articles/) | Engineering blog posts |
| [Interview Stories](./interview-stories.md) | STAR format narratives |
| [LinkedIn Profile](./linkedin.md) | Copy-ready profile content |
| [Cover Letter](./cover-letter.md) | Application templates |
| [GitHub Pages](./GITHUB_PAGES.md) | Deployment guide |

### System Design

| Topic | Description |
|-------|-------------|
| [Privacy Computing](./system-design/privacy-computing.md) | Execution platform design |
| [Stream Processing](./system-design/stream-processing.md) | End-to-end streaming design |
| [Analytical Platform](./system-design/analytical-platform.md) | Metric platform design |
| [Kafka](./system-design/kafka.md) | Ingestion layer at 10B+ events/day |
| [Flink](./system-design/flink.md) | 1000+ vCore cluster design |
| [Metadata](./system-design/metadata.md) | Platform-level data governance |
| [Scheduler](./system-design/scheduler.md) | DAG stage dispatch |
| [Storage](./system-design/storage.md) | Storage abstraction layer |

### Articles

| Article | Description |
|---------|-------------|
| [Building Data Platforms](./articles/building-data-platforms.md) | Cross-domain platform patterns |
| [Engineering Philosophy](./articles/engineering-philosophy.md) | Core engineering principles |
| [Platform Engineering](./articles/platform-engineering.md) | Reusable infrastructure |
| [Streaming at Scale](./articles/streaming.md) | National device scale |
| [Query Planning](./articles/query-planning.md) | Execution planning design |
| [Data Infrastructure](./articles/data-infrastructure.md) | Three domains, one career |

---

## Engineering Philosophy

Infrastructure should simplify complexity. Reusable platforms create more
long-term value than one-off implementations. Every architectural decision
has trade-offs — good engineering documents them explicitly.

[Engineering Philosophy →](./articles/engineering-philosophy.md)

---

## Contact

- Email: jromeguan@gmail.com
- GitHub: https://github.com/jlty258
- Location: Shanghai, China
- Availability: Open to global remote opportunities
