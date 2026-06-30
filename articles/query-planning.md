# Query Planning and Execution Planning

---

## Why Execution Planning Matters

In traditional data systems, users write queries and the engine executes them.
In privacy computing and multi-party computation platforms, the gap between
"what computation is needed" and "how to orchestrate it across parties" is
large enough to require a dedicated planning layer.

At the MIRA privacy computing platform, I designed the execution planning
pipeline that bridges this gap:

```
PQL → Planner → Execution DAG → Scheduler → Execution Engine → Data Service → Storage
```

This article explains why execution planning is a platform primitive, not an
optional optimization.

---

## The Problem with Template-Based Execution

The alternative to a query planner is template-based job configuration: pre-defined
execution templates for common computation patterns.

**Why templates fail in privacy computing:**

- Query structures vary based on computation semantics, not fixed patterns
- Cross-party workflows have different dependency graphs per query
- New computation patterns require new templates, not template parameter changes
- Template proliferation creates maintenance cost equivalent to ad-hoc scripts

A planner adapts execution graphs to query semantics. Templates require manual
updates for each new pattern. At platform scale, the planner wins.

---

## PQL to Execution DAG

### Query Planner Responsibilities

The query planner converts PQL (platform query language) into executable
distributed plans:

1. **Parse** PQL into logical operator tree
2. **Rewrite** operators for execution efficiency
3. **Construct** cost-aware execution graph
4. **Separate** query semantics from execution strategy selection

The separation of semantics from strategy is the highest-leverage abstraction
in the platform. Application teams define what computation is needed. The
planner determines how to orchestrate it.

### Execution DAG Model

The planner output is a distributed directed acyclic graph:

- **Nodes:** computation stages with resource requirements
- **Edges:** data dependencies between stages
- **Stage boundaries:** units of retry, checkpoint, and parallel dispatch

DAG semantics defined during planner design directly determine scheduler
retry granularity and recovery cost. Stage boundary decisions are planner
decisions with downstream consequences.

---

## Design Decisions

### Declarative Interface (PQL)

Application teams submit declarative queries describing computation requirements.
They do not orchestrate distributed jobs, manage stage dependencies, or
configure storage access paths.

**Benefit:** Lower integration cost for application teams.

**Cost:** Planner must handle diverse query patterns without manual template
creation for each new pattern.

### Cost-Aware Graph Construction

The planner constructs execution graphs with cost awareness — selecting
operator order, parallelism, and stage boundaries based on estimated
execution cost.

**Current state:** Cost estimation based on query structure and configured
engine capabilities.

**Future direction:** Historical execution statistics from benchmark platform
inform cost models.

### Planner-Scheduler Interface

The planner produces DAGs; the scheduler dispatches stages. Interface
standardization between these components enables independent evolution:

- Planner logic improves without scheduler changes
- Scheduler scaling strategies change without planner changes
- New execution engine types integrate through scheduler, not planner

Platform interfaces defined before multiple teams integrated. Retrofit
standardization across planner and scheduler would have been significantly
more expensive.

---

## Benchmark Platform Integration

Execution planning optimization involves multiple dimensions:

- Planner operator rewriting strategies
- DAG stage boundary placement
- Execution engine selection per stage
- Storage access patterns via Data Service

Optimizing any dimension without measurement produces incorrect conclusions.

The benchmark platform measures execution planning and runtime performance
across query patterns and hardware configurations. Optimization decisions
are driven by benchmark evidence, not assumptions.

**Lesson:** Build measurement infrastructure alongside the planner, not after
production performance incidents reveal incorrect planning assumptions.

---

## Trade-offs

| Decision | Benefit | Cost |
|----------|---------|------|
| Dedicated planner vs. templates | Adaptive execution per query | Planner engineering complexity |
| Declarative PQL vs. imperative scripts | Lower app team integration cost | Planner handles diverse patterns |
| Stage-level DAG vs. task-level | Meaningful retry granularity | DAG model complexity |
| Cost-aware planning vs. naive plans | Better resource utilization | Cost model maintenance |

---

## Lessons Learned

1. Execution planning is a platform primitive when query-to-orchestration gap
   is large. In simple single-engine systems, the engine's built-in planner
   suffices. In multi-party, multi-engine platforms, dedicated planning is
   required.

2. Separate query semantics from execution strategy early. Coupling them makes
   both harder to evolve independently.

3. Stage boundary definition in the DAG model is a planner decision with
   scheduler and recovery consequences. Design stage semantics during planner
   architecture, not during scheduler implementation.

4. Benchmark infrastructure for the planner pays for itself when optimization
   involves multiple interacting dimensions.

---

## Conclusion

Query planning and execution planning transform "write a distributed job" into
"submit a declarative query." That transformation is what makes a privacy
computing platform a platform rather than a collection of orchestration scripts.

The engineering content is not the planner implementation. It is the decision
to treat execution planning as a first-class platform capability, the interface
design between planner and scheduler, and the benchmark infrastructure that
makes optimization decisions evidence-based.
