#!/usr/bin/env python3
"""
Test Suite Runner for Spark Experiments
"""

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

import tests.test_notebook_integrity as t_nb

def main():
    print("▶ Running Spark Experiments Test Suite...")
    passed = 0
    failed = 0
    test_funcs = [
        ("test_notebooks_json_valid", t_nb.test_notebooks_json_valid),
        ("test_notebooks_python_ast_syntax", t_nb.test_notebooks_python_ast_syntax),
        ("test_no_git_leaks", t_nb.test_no_git_leaks)
    ]
    for name, fn in test_funcs:
        try:
            fn()
            print(f"  ✓ {name} passed")
            passed += 1
        except Exception as e:
            print(f"  ✗ {name} failed: {e}")
            failed += 1
    
    print(f"\nResults: {passed} passed, {failed} failed")
    if failed > 0:
        sys.exit(1)
    print("🎉 ALL TESTS PASSED SUCCESSFULLY!")

if __name__ == "__main__":
    main()
