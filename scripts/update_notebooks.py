import json
import os

# Paths
base_dir = '/Users/santosh/Documents/antigravity/spark-experiments'
nb3_path = os.path.join(base_dir, 'spark/1_data_skew/3_solving_data_skew_aqe_broadcast.ipynb')
nb4_path = os.path.join(base_dir, 'spark/1_data_skew/4_salting.ipynb')

# --- 1. Update 3_solving_data_skew_aqe_broadcast.ipynb ---
with open(nb3_path, encoding='utf-8') as f:
    nb3 = json.load(f)

nav_ribbon_3 = [
    '> 🧭 **Modern Data Engineering Ecosystem Navigation**\n',
    '> - 📘 **Architecture & Concept:** [Data System Design — Storage Optimization & Clustering](https://github.com/santoshjammi29/data-system-design-handbook/tree/main/modules/04_storage_optimization_and_clustering)\n',
    '> - 💻 **Hands-On Recipe:** [PySpark Handbook — Notebook 08_03: Data Skew Mitigation](https://github.com/santoshjammi29/pyspark-handbook/blob/main/notebooks/08_performance_and_tuning/08_03_data_skew_mitigation_salting.py)\n',
    '> - 🔬 **Empirical Lab:** [Spark Experiments — 1_data_skew: AQE & Broadcast Join](https://github.com/santoshjammi29/spark-experiments/blob/main/spark/1_data_skew/3_solving_data_skew_aqe_broadcast.ipynb) *(You are here)*\n',
    '> - 🚨 **Incident Runbook:** [PySpark Runbook 03: Data Skew & Two-Phase Salting](https://github.com/santoshjammi29/pyspark-handbook/blob/main/runbooks/03_data_skew_and_two_phase_salting.md)\n',
    '> - 🎯 **Interview Defense:** [Interview Handbook — Pillar 01: Spark & Databricks Q12](https://github.com/santoshjammi29/data-engineering-interview-handbook/blob/main/pillars/01_spark_and_databricks.md#q12)\n',
    '> - 🌐 **Interactive Web Practice:** [Practice on moderndataengineer.uk](https://moderndataengineer.uk/practice/pyspark?topic=data-skew)\n',
    '> - 📐 **Architecture Blueprint:** [Data Skew Mitigation & Key Salting Architecture](https://moderndataengineer.uk/whiteboards?id=data_skew_salting_repartition)\n'
]

# Check existing banner and update
found_banner = False
for cell in nb3['cells']:
    if cell['cell_type'] == 'markdown' and any('Ecosystem Navigation' in line or 'Visual Learning Journey' in line for line in cell.get('source', [])):
        cell['source'] = nav_ribbon_3
        found_banner = True
        break

if not found_banner:
    banner_cell = {'cell_type': 'markdown', 'metadata': {}, 'source': nav_ribbon_3}
    nb3['cells'].insert(1, banner_cell)

with open(nb3_path, 'w', encoding='utf-8') as f:
    json.dump(nb3, f, indent=1)
print(f'nb3 updated successfully! Cell count: {len(nb3["cells"])}')

# --- 2. Update 4_salting.ipynb ---
with open(nb4_path, encoding='utf-8') as f:
    nb4 = json.load(f)

nav_ribbon_4 = [
    '> 🧭 **Modern Data Engineering Ecosystem Navigation**\n',
    '> - 📘 **Architecture & Concept:** [Data System Design — Storage Optimization & Clustering](https://github.com/santoshjammi29/data-system-design-handbook/tree/main/modules/04_storage_optimization_and_clustering)\n',
    '> - 💻 **Hands-On Recipe:** [PySpark Handbook — Notebook 08_03: Data Skew Mitigation](https://github.com/santoshjammi29/pyspark-handbook/blob/main/notebooks/08_performance_and_tuning/08_03_data_skew_mitigation_salting.py)\n',
    '> - 🔬 **Empirical Lab:** [Spark Experiments — 1_data_skew: Salting Benchmarks](https://github.com/santoshjammi29/spark-experiments/blob/main/spark/1_data_skew/4_salting.ipynb) *(You are here)*\n',
    '> - 🚨 **Incident Runbook:** [PySpark Runbook 03: Data Skew & Two-Phase Salting](https://github.com/santoshjammi29/pyspark-handbook/blob/main/runbooks/03_data_skew_and_two_phase_salting.md)\n',
    '> - 🎯 **Interview Defense:** [Interview Handbook — Pillar 01: Spark & Databricks Q12](https://github.com/santoshjammi29/data-engineering-interview-handbook/blob/main/pillars/01_spark_and_databricks.md#q12)\n',
    '> - 🌐 **Interactive Web Practice:** [Practice on moderndataengineer.uk](https://moderndataengineer.uk/practice/pyspark?topic=data-skew)\n',
    '> - 📐 **Architecture Blueprint:** [Data Skew Mitigation & Key Salting Architecture](https://moderndataengineer.uk/whiteboards?id=data_skew_salting_repartition)\n'
]

found_banner = False
for cell in nb4['cells']:
    if cell['cell_type'] == 'markdown' and any('Ecosystem Navigation' in line or 'Visual Learning Journey' in line for line in cell.get('source', [])):
        cell['source'] = nav_ribbon_4
        found_banner = True
        break

if not found_banner:
    banner_cell = {'cell_type': 'markdown', 'metadata': {}, 'source': nav_ribbon_4}
    nb4['cells'].insert(1, banner_cell)

with open(nb4_path, 'w', encoding='utf-8') as f:
    json.dump(nb4, f, indent=1)
print(f'nb4 updated successfully! Cell count: {len(nb4["cells"])}')
