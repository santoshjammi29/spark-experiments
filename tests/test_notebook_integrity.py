"""
Test Suite: Spark Experiments Notebook Integrity & Standards Verification
"""

import ast
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def test_notebooks_json_valid():
    nb_files = list((BASE_DIR / "spark").rglob("*.ipynb"))
    assert len(nb_files) > 0, "No notebooks found in spark directory"
    for nb in nb_files:
        content = nb.read_text(encoding="utf-8")
        data = json.loads(content)
        assert "cells" in data, f"{nb.name}: Missing cells array"
        assert "metadata" in data, f"{nb.name}: Missing metadata"

def test_notebooks_python_ast_syntax():
    nb_files = sorted(list((BASE_DIR / "spark").rglob("*.ipynb")))
    syntax_errors = []
    for nb in nb_files:
        try:
            data = json.loads(nb.read_text(encoding="utf-8"))
        except Exception as e:
            syntax_errors.append(f"{nb.name}: JSON parse failure: {e}")
            continue
        for idx, cell in enumerate(data.get("cells", [])):
            if cell.get("cell_type") != "code":
                continue
            source_lines = cell.get("source", [])
            code_lines = [
                line for line in source_lines
                if not line.strip().startswith("%") and not line.strip().startswith("!")
            ]
            code_str = "".join(code_lines).strip()
            if code_str:
                try:
                    ast.parse(code_str)
                except SyntaxError as se:
                    syntax_errors.append(f"{nb.name} cell {idx}: {se}")
    assert not syntax_errors, "Syntax errors in notebooks:\n" + "\n".join(syntax_errors)

def test_no_git_leaks():
    import subprocess
    res = subprocess.run(["git", "ls-files"], cwd=BASE_DIR, capture_output=True, text=True)
    tracked_files = res.stdout.strip().split("\n") if res.stdout.strip() else []
    venv_files = [f for f in tracked_files if ".venv" in f]
    parquet_files = [f for f in tracked_files if f.endswith(".parquet")]
    assert not venv_files, f".venv files tracked in git: {venv_files}"
    assert not parquet_files, f"Raw parquet files tracked in git: {parquet_files}"

if __name__ == "__main__":
    test_notebooks_json_valid()
    test_notebooks_python_ast_syntax()
    test_no_git_leaks()
    print("All spark-experiments integrity tests passed!")
