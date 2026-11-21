# 🧠 Apache Spark Visual Execution, Memory & Tuning Experiments — Curriculum Topics Directory

> **Curriculum Scope**: **34 Production Topics** verified against real-world lakehouse internals, query engines, and distributed architectures.
> **Live Web Hub**: Explore interactive search and full visual graph at [moderndataengineer.uk/concepts](https://moderndataengineer.uk/concepts).

---

## 📖 Overview & Learning Path

Advanced Apache Spark execution engine, Tungsten memory management, and Catalyst optimizer concepts benchmarked across visual experiment suites.

### 🎯 Difficulty Progression
- `🟢 Easy`: Foundational primitives, syntax, and operational core concepts.
- `🟡 Intermediate`: Production configuration, optimization patterns, and pipeline resiliency.
- `🔴 Advanced`: Engine internals, memory management, shuffle mechanics, and fault recovery.
- `🟣 Architect`: Cross-region distributed systems, enterprise governance, high-availability, and FinOps.

---

## 📑 Topics Directory at a Glance

| Module / Pillar | Topics | Key Primitives Covered | Reference Links |
|:---|:---:|:---|:---|
| ⚡ **[Apache Spark Execution, Memory & Query Optimization](#apache-spark-execution-memory--query-optimization)** | **34** | Adaptive Query Execution (AQE), Cache vs Persist Operations, coalesce() vs repartition(), and 31 more | [Jump to Section](#apache-spark-execution-memory--query-optimization) |

---

## 📚 Comprehensive Topic Specifications

### ⚡ Apache Spark Execution, Memory & Query Optimization

**Total Topics**: 34

| # | Topic / Concept | Difficulty | Architectural Definition & Core Principle |
|:---:|---|:---:|---|
| 1 | **Adaptive Query Execution (AQE)** | `🟡 Intermediate` | An optimization framework that dynamically adjusts Spark physical execution plans during runtime based on intermediate stage statistics. |
| 2 | **Cache vs Persist Operations** | `🟡 Intermediate` | DataFrame operations used to store intermediate execution results in memory or disk to avoid recalculations. |
| 3 | **coalesce() vs repartition()** | `🟡 Intermediate` | Two Spark functions for changing partition count: coalesce() reduces partitions without a full shuffle by merging local partitions, while repartition() performs a full shuffle to evenly redistribute data across any number of partitions. |
| 4 | **EXPLAIN Plan (Spark Query Plan)** | `🟡 Intermediate` | A Spark debugging tool that displays the logical and physical execution plan for a DataFrame or SQL query, enabling engineers to verify optimisations, diagnose performance issues, and understand data flow. |
| 5 | **Lazy Evaluation** | `🟡 Intermediate` | An execution strategy where Spark delays query executions until an action is explicitly requested. |
| 6 | **PySpark Vectorized Pandas UDF Architecture** | `🟡 Intermediate` | Using Apache Arrow record batches to pass columnar data between the JVM and Python worker processes with high efficiency. |
| 7 | **Reading the Spark UI** | `🟡 Intermediate` | The web-based performance monitoring and telemetry dashboard used to inspect execution plans, identify straggler tasks, detect memory spill, and profile shuffle I/O across Spark Jobs, Stages, and SQL DAGs. |
| 8 | **Shuffle Operations** | `🟡 Intermediate` | The distributed physical data redistribution process across cluster executor nodes triggered by wide transformations such as `groupBy()`, `join()`, `distinct()`, and `repartition()`. |
| 9 | **Spark Broadcast Hash Join (BHJ)** | `🟡 Intermediate` | A distributed join strategy in Apache Spark that distributes an entire small DataFrame to all executor nodes to eliminate costly shuffle operations. |
| 10 | **Stage Boundary** | `🟡 Intermediate` | A stage boundary in Spark marks the point where a wide transformation (shuffle) separates two stages, requiring all tasks in the upstream stage to complete before the downstream stage begins. |
| 11 | **Storage Level: MEMORY_AND_DISK** | `🟡 Intermediate` | A Spark cache storage level that stores partitions in JVM heap memory and spills remaining partitions to local executor disk if memory is insufficient. |
| 12 | **AQE Dynamic Join Strategy Switching** | `🔴 Advanced` | A runtime optimization in Adaptive Query Execution that converts planned SortMergeJoins into BroadcastHashJoins based on post-shuffle partition size statistics. |
| 13 | **AQE Shuffle Partition Coalescing** | `🔴 Advanced` | An Adaptive Query Execution feature that merges small post-shuffle partitions at runtime into larger ones, eliminating the small-file and task-overhead problem from over-partitioning. |
| 14 | **BroadcastNestedLoopJoin Anti-Pattern** | `🔴 Advanced` | The most dangerous physical join operator in Apache Spark, executing an $O(M \times N)$ Cartesian product comparison when equi-join conditions are missing. |
| 15 | **Bucket Join** | `🔴 Advanced` | A Spark join optimisation that eliminates shuffle entirely by pre-bucketing both tables on the join key with the same number of buckets, co-locating matching keys on the same partitions. |
| 16 | **Catalyst Optimizer — Analysis Phase** | `🔴 Advanced` | The first phase of Spark's Catalyst Optimizer where unresolved logical plans are validated against the catalog to produce a resolved logical plan. |
| 17 | **Catalyst Optimizer — Physical Planning** | `🔴 Advanced` | The phase of Spark's Catalyst Optimizer that selects the most efficient physical execution strategy from multiple candidate plans using a cost model. |
| 18 | **Data Skew: Detection & Mitigation** | `🔴 Advanced` | The process of diagnosing uneven record distributions across executor partitions using Spark UI percentiles, resolved via Adaptive Query Execution (AQE) skew join splitting or two-phase key salting. |
| 19 | **G1GC Garbage Collector in Spark** | `🔴 Advanced` | The Garbage-First (G1) GC is the recommended JVM garbage collector for Spark executors, offering predictable pause times and better heap region management than the older ParallelGC. |
| 20 | **Memory Spill to Disk** | `🔴 Advanced` | A performance degradation state where Spark runs out of executor RAM and writes execution buffers to disk. |
| 21 | **Off-Heap Memory** | `🔴 Advanced` | Memory allocated outside the JVM heap using native OS memory, bypassing garbage collection entirely and managed explicitly by Project Tungsten's memory manager. |
| 22 | **Shuffle Hash Join (SHJ)** | `🔴 Advanced` | A Spark join strategy that shuffles both tables by join key and builds an in-memory hash table from the smaller side of each partition to probe with the larger side. |
| 23 | **Sort Merge Join (SMJ)** | `🔴 Advanced` | Spark's default join strategy for large-to-large table joins, where both datasets are shuffled by join key, sorted, and merged partition-by-partition on executor cores. |
| 24 | **Spark Partitioning vs. Bucketing Architecture** | `🔴 Advanced` | The two primary storage organization techniques in Apache Spark that govern physical directory layouts, file pruning, and shuffle elimination. |
| 25 | **Speculative Execution** | `🔴 Advanced` | A Spark fault-tolerance feature that launches a duplicate copy of a slow (straggler) task on another executor, using whichever copy finishes first and killing the other. |
| 26 | **Task Duration Skew Detection** | `🔴 Advanced` | Using Spark Web UI task duration percentiles (75th vs Max) to diagnose unbalanced partition distributions. |
| 27 | **Tungsten Binary Row Format (UnsafeRow)** | `🔴 Advanced` | Apache Spark's off-heap binary row format that stores data as raw bytes using sun.misc.Unsafe, bypassing JVM object overhead and enabling cache-efficient processing. |
| 28 | **Tungsten Engine** | `🔴 Advanced` | Spark's physical execution optimizer that manages memory directly using raw off-heap byte arrays. |
| 29 | **Whole-Stage Code Generation** | `🔴 Advanced` | A Project Tungsten optimisation that compiles an entire pipeline of Spark operators into a single Java function, eliminating virtual function dispatch overhead and enabling JIT optimisation. |
| 30 | **Shuffle Fetch Failed** | `🟣 Architect` | A Spark task failure that occurs when a downstream task cannot retrieve shuffle data from an upstream executor, typically caused by executor loss, OOM, or network partition. |
| 31 | **Skewed Shuffle Partition Splitting** | `🟣 Architect` | A dynamic AQE mechanism that identifies disproportionately large shuffle partitions and divides them into parallel sub-tasks while duplicating opposing join data. |
| 32 | **Spark Data Skew Remediation: Salting & Isolated Broadcast Patterns** | `🟣 Architect` | Algorithmic architectural strategies to balance severely uneven data distributions across Spark cluster worker cores during shuffle-intensive joins. |
| 33 | **Spark Unified Memory Manager** | `🟣 Architect` | The memory management subsystem introduced in Apache Spark that unifies execution and storage memory into a single shared pool with dynamic borrowing. |
| 34 | **The 5 S's of Apache Spark Performance** | `🟣 Architect` | The 5 S's of Spark is a diagnostic framework categorizing all distributed big data bottlenecks into Storage, Skew, Spill, Shuffle, and Serialization. |

---

## 📐 Related Whiteboard Blueprints
For deep visual architecture walkthroughs of these topics, consult:
- 🖼️ [Master Whiteboard Blueprints](../docs/whiteboard_diagrams/handbook_whiteboard_blueprints.md)
- 📊 [Spark Catalyst & Architecture Cheatsheet](../assets/whiteboards/spark_architecture_catalyst_cheatsheet.jpg)
- 🔀 [Join Strategies Decision Matrix](../assets/whiteboards/spark_join_strategies_decision_matrix.jpg)
- ⚡ [Skew & Spill Memory Triage](../assets/whiteboards/spark_performance_skew_spill_triage.jpg)

---

## 🌐 Ecosystem Interlinking
All curriculum topics are synchronized across the 14-repository Modern Data Engineering ecosystem:
- [Modern Data Engineer Hub](https://github.com/santoshjammi29/moderndataengineer) — Central edge web platform and 921-topic encyclopedia
- [PySpark Handbook](https://github.com/santoshjammi29/pyspark-handbook) — Distributed compute & PySpark internals
- [Databricks Handbook](https://github.com/santoshjammi29/databricks-handbook) — Unity Catalog, Delta Lake 3.x, and Lakeflow
- [SQL Handbook](https://github.com/santoshjammi29/sql-handbook) — Query engine optimization & relational internals
- [Streaming Handbook](https://github.com/santoshjammi29/streaming-handbook) — Event streaming, Kafka, and Flink
- [Security Handbook](https://github.com/santoshjammi29/security-handbook) — Zero-trust, IAM, and lakehouse governance
- [Data System Design Handbook](https://github.com/santoshjammi29/data-system-design-handbook) — Distributed architecture and scalability
- [DataOps & CI/CD Handbook](https://github.com/santoshjammi29/dataops-cicd-handbook) — Airflow, orchestration, and infrastructure
- [dbt Handbook](https://github.com/santoshjammi29/dbt-handbook) — Analytics engineering, contracts, and modeling
- [Azure Cheat Sheet](https://github.com/santoshjammi29/azure-cheat-sheet) — Fabric, OneLake, and ADF enterprise blueprints
- [Data Engineering Interview Handbook](https://github.com/santoshjammi29/data-engineering-interview-handbook) — 20 Knowledge Pillars & architectural defense
