# Spark Performance Tuning

This repository is the ultimate guide for mastering advanced Spark Performance Tuning and Optimization concepts and for anyone preparing for Data Engineering Interviews involving Spark. Additionally, this repository serves as a reference for all the code snippets used in my [Spark Performance Tuning Playlist](https://www.youtube.com/playlist?list=PLWAuYt0wgRcLCtWzUxNg4BjnYlCZNEVth) on YouTube. The goal of the playlist and the accompanying code snippets is to make complex concepts in Apache Spark easy to understand, while also developing a deep understanding of how things work under the hood.


## Concepts Covered

| Concept             | YouTube Link                                            | Code                                                     |
|---------------------|---------------------------------------------------------|----------------------------------------------------------|
| Spark 30 Concepts           | [![YouTube](https://img.shields.io/badge/YouTube-red?style=flat-square&logo=youtube)](https://youtu.be/z4Owc8RRApg) | |
| Spark Query Plans           | [![YouTube](https://img.shields.io/badge/YouTube-red?style=flat-square&logo=youtube)](https://youtu.be/KnUXztKueMU) | [![Python](https://img.shields.io/badge/Code-Python-blue?style=flat-square&logo=python&logoColor=white)](/spark/2_reading_query_plans.ipynb) |
| Spark DAGs           | [![YouTube](https://img.shields.io/badge/YouTube-red?style=flat-square&logo=youtube)](https://youtu.be/O_45zAz1OGk) | [![Python](https://img.shields.io/badge/Code-Python-blue?style=flat-square&logo=python&logoColor=white)](/spark/3_reading_query_DAGs.ipynb) |
| Spark Memory Management           | [![YouTube](https://img.shields.io/badge/YouTube-red?style=flat-square&logo=youtube)](https://youtu.be/sXL1qgrPysg) |  |
| Spark Executor Tuning  | [![YouTube](https://img.shields.io/badge/YouTube-red?style=flat-square&logo=youtube)](https://youtu.be/mA96gUESVZc) |  |
| Shuffle Partitions      | [![YouTube](https://img.shields.io/badge/YouTube-red?style=flat-square&logo=youtube)](https://youtu.be/q1LtBU_ca20) |  |
| Data Partitioning        | [![YouTube](https://img.shields.io/badge/YouTube-red?style=flat-square&logo=youtube)](https://youtu.be/fZndmQasykk) | [![Python](https://img.shields.io/badge/Code-Python-blue?style=flat-square&logo=python&logoColor=white)](/spark/5_0_partitioning.ipynb) |
| Bucketing       | [![YouTube](https://img.shields.io/badge/YouTube-red?style=flat-square&logo=youtube)](https://youtu.be/1kWl6d1yeKA) | [![Python](https://img.shields.io/badge/Code-Python-blue?style=flat-square&logo=python&logoColor=white)](/spark/6_0_bucketing.ipynb) |
| Caching           | [![YouTube](https://img.shields.io/badge/YouTube-red?style=flat-square&logo=youtube)](https://youtu.be/FujwRYkBwM4) | [![Python](https://img.shields.io/badge/Code-Python-blue?style=flat-square&logo=python&logoColor=white)](/spark/4_caching.ipynb) |
| Data Skew                 | [![YouTube](https://img.shields.io/badge/YouTube-red?style=flat-square&logo=youtube)](https://youtu.be/9Ss-_y7njKE) | [![Python](https://img.shields.io/badge/Code-Python-blue?style=flat-square&logo=python&logoColor=white)](/spark/1_data_skew/) |
| Salting                 | [![YouTube](https://img.shields.io/badge/YouTube-red?style=flat-square&logo=youtube)](https://youtu.be/rZGsc5y8AQk) | [![Python](https://img.shields.io/badge/Code-Python-blue?style=flat-square&logo=python&logoColor=white)](/spark/1_data_skew/4_salting.ipynb) |
| AQE & Broadcast Joins                 | [![YouTube](https://img.shields.io/badge/YouTube-red?style=flat-square&logo=youtube)](https://youtu.be/bRjVa7MgsBM) | [![Python](https://img.shields.io/badge/Code-Python-blue?style=flat-square&logo=python&logoColor=white)](/spark/1_data_skew/3_solving_data_skew_aqe_broadcast.ipynb) |
| Dynamic Partition Pruning                 | [![YouTube](https://img.shields.io/badge/YouTube-red?style=flat-square&logo=youtube)](https://youtu.be/s8Z8Gex7VFw) | [![Python](https://img.shields.io/badge/Code-Python-blue?style=flat-square&logo=python&logoColor=white)](/spark/5_1_dynamic_partition_pruning.ipynb) |


## 🧠 Core Curriculum Concepts & Topics (34 Spark Tuning Topics Covered)

> 💡 **Enterprise Knowledge Base Integration**: Advanced Apache Spark optimization and execution engine concepts covered throughout the visual experiments, cross-linked with the [Modern Data Engineering Systems Encyclopedia (921 Topics)](https://moderndataengineer.uk/concepts).

<details open>
<summary><b>⚡ Apache Spark Execution, Memory & Query Optimization (34 Topics)</b> — <i>Click to collapse/expand</i></summary>

| # | Topic / Concept | Level | Architectural Definition & Core Principle |
|:---:|---|:---:|---|
| 1 | **EXPLAIN Plan (Spark Query Plan)** | 🟡<br>Intermediate | A Spark debugging tool that displays the logical and physical execution plan for a DataFrame or SQL query, enabling engineers to verify optimisations, diagnose performance issues, and understand data flow. |
| 2 | **Catalyst Optimizer — Analysis Phase** | 🔴<br>Advanced | The first phase of Spark's Catalyst Optimizer where unresolved logical plans are validated against the catalog to produce a resolved logical plan. |
| 3 | **Catalyst Optimizer — Physical Planning** | 🔴<br>Advanced | The phase of Spark's Catalyst Optimizer that selects the most efficient physical execution strategy from multiple candidate plans using a cost model. |
| 4 | **Whole-Stage Code Generation** | 🔴<br>Advanced | A Project Tungsten optimisation that compiles an entire pipeline of Spark operators into a single Java function, eliminating virtual function dispatch overhead and enabling JIT optimisation. |
| 5 | **Stage Boundary** | 🟡<br>Intermediate | A stage boundary in Spark marks the point where a wide transformation (shuffle) separates two stages, requiring all tasks in the upstream stage to complete before the downstream stage begins. |
| 6 | **Tungsten Engine** | 🔴<br>Advanced | Spark's physical execution optimizer that manages memory directly using raw off-heap byte arrays. |
| 7 | **Tungsten Binary Row Format (UnsafeRow)** | 🔴<br>Advanced | Apache Spark's off-heap binary row format that stores data as raw bytes using sun.misc.Unsafe, bypassing JVM object overhead and enabling cache-efficient processing. |
| 8 | **Off-Heap Memory** | 🔴<br>Advanced | Memory allocated outside the JVM heap using native OS memory, bypassing garbage collection entirely and managed explicitly by Project Tungsten's memory manager. |
| 9 | **Spark Unified Memory Manager** | 🟣<br>Architect | The memory management subsystem introduced in Apache Spark that unifies execution and storage memory into a single shared pool with dynamic borrowing. |
| 10 | **Memory Spill to Disk** | 🔴<br>Advanced | A performance degradation state where Spark runs out of executor RAM and writes execution buffers to disk. |
| 11 | **Shuffle Operations** | 🟡<br>Intermediate | What triggers a shuffle (groupBy, join, repartition, distinct). |
| 12 | **Shuffle Fetch Failed** | 🟣<br>Architect | A Spark task failure that occurs when a downstream task cannot retrieve shuffle data from an upstream executor, typically caused by executor loss, OOM, or network partition. |
| 13 | **Spark Partitioning vs. Bucketing Architecture** | 🔴<br>Advanced | The two primary storage organization techniques in Apache Spark that govern physical directory layouts, file pruning, and shuffle elimination. |
| 14 | **coalesce() vs repartition()** | 🟡<br>Intermediate | Two Spark functions for changing partition count: coalesce() reduces partitions without a full shuffle by merging local partitions, while repartition() performs a full shuffle to evenly redistribute data across any number of partitions. |
| 15 | **Bucket Join** | 🔴<br>Advanced | A Spark join optimisation that eliminates shuffle entirely by pre-bucketing both tables on the join key with the same number of buckets, co-locating matching keys on the same partitions. |
| 16 | **Cache vs Persist Operations** | 🟡<br>Intermediate | DataFrame operations used to store intermediate execution results in memory or disk to avoid recalculations. |
| 17 | **Storage Level: MEMORY_AND_DISK** | 🟡<br>Intermediate | A Spark cache storage level that stores partitions in JVM heap memory and spills remaining partitions to local executor disk if memory is insufficient. |
| 18 | **Data Skew: Detection & Mitigation** | 🔴<br>Advanced | Recognizing skew in Spark UI (one task takes 10x longer). |
| 19 | **Spark Data Skew Remediation: Salting & Isolated Broadcast Patterns** | 🟣<br>Architect | Algorithmic architectural strategies to balance severely uneven data distributions across Spark cluster worker cores during shuffle-intensive joins. |
| 20 | **Adaptive Query Execution (AQE)** | 🟡<br>Intermediate | An optimization framework that dynamically adjusts Spark physical execution plans during runtime based on intermediate stage statistics. |
| 21 | **AQE Shuffle Partition Coalescing** | 🔴<br>Advanced | An Adaptive Query Execution feature that merges small post-shuffle partitions at runtime into larger ones, eliminating the small-file and task-overhead problem from over-partitioning. |
| 22 | **Skewed Shuffle Partition Splitting** | 🟣<br>Architect | A dynamic AQE mechanism that identifies disproportionately large shuffle partitions and divides them into parallel sub-tasks while duplicating opposing join data. |
| 23 | **AQE Dynamic Join Strategy Switching** | 🔴<br>Advanced | A runtime optimization in Adaptive Query Execution that converts planned SortMergeJoins into BroadcastHashJoins based on post-shuffle partition size statistics. |
| 24 | **Spark Broadcast Hash Join (BHJ)** | 🟡<br>Intermediate | A distributed join strategy in Apache Spark that distributes an entire small DataFrame to all executor nodes to eliminate costly shuffle operations. |
| 25 | **Shuffle Hash Join (SHJ)** | 🔴<br>Advanced | A Spark join strategy that shuffles both tables by join key and builds an in-memory hash table from the smaller side of each partition to probe with the larger side. |
| 26 | **Sort Merge Join (SMJ)** | 🔴<br>Advanced | Spark's default join strategy for large-to-large table joins, where both datasets are shuffled by join key, sorted, and merged partition-by-partition on executor cores. |
| 27 | **BroadcastNestedLoopJoin Anti-Pattern** | 🔴<br>Advanced | The most dangerous physical join operator in Apache Spark, executing an $O(M 	imes N)$ Cartesian product comparison when equi-join conditions are missing. |
| 28 | **PySpark Vectorized Pandas UDF Architecture** | 🟡<br>Intermediate | Using Apache Arrow record batches to pass columnar data between the JVM and Python worker processes with high efficiency. |
| 29 | **Reading the Spark UI** | 🟡<br>Intermediate | The tabs that matter: Jobs, Stages, Tasks, SQL. |
| 30 | **Task Duration Skew Detection** | 🔴<br>Advanced | Using Spark Web UI task duration percentiles (75th vs Max) to diagnose unbalanced partition distributions. |
| 31 | **G1GC Garbage Collector in Spark** | 🔴<br>Advanced | The Garbage-First (G1) GC is the recommended JVM garbage collector for Spark executors, offering predictable pause times and better heap region management than the older ParallelGC. |
| 32 | **Speculative Execution** | 🔴<br>Advanced | A Spark fault-tolerance feature that launches a duplicate copy of a slow (straggler) task on another executor, using whichever copy finishes first and killing the other. |
| 33 | **The 5 S's of Apache Spark Performance** | 🟣<br>Architect | The 5 S's of Spark is a diagnostic framework categorizing all distributed big data bottlenecks into Storage, Skew, Spill, Shuffle, and Serialization. |
| 34 | **Lazy Evaluation** | 🟡<br>Intermediate | An execution strategy where Spark delays query executions until an action is explicitly requested. |

</details>

---

## Contact

- [LinkedIn](https://www.linkedin.com/in/afaque-ahmad-5a5847129/)
- [YouTube](https://www.youtube.com/@afaqueahmad7117)