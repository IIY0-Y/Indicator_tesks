import csv
import os
import importlib
import traceback
import pandas as pd
from Lobby import Ind

def IndicatorTester(csv_path, root_dir):
    """
    Look into the csv file, and then call every function
    """
    expected_tests = []

    with open(csv_path, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for idx, row in enumerate(reader, start=1):
            indicator_class = row.get('indicator_class')
            indicator_name = row.get('indicator_name')

            if indicator_class and indicator_name:
                folder = indicator_class.lower().replace(' ', '_')
                module_name = f"{folder}.{indicator_name.lower().replace(' ', '_')}"
                function_name = "run"
                expected_tests.append((module_name, function_name))
            else:
                print(f"[WARNING] Skipping row {idx} due to missing data: {row}")

    get_obj = Ind.Get(root_dir)
    test_results = {}


    test_data = pd.DataFrame({"price": [100, 102, 104, 103, 101]})

    for module_name, function_name in expected_tests:
        success, output = get_obj.test_indicator(module_name, function_name, test_data)
        test_results[module_name] = {"success": success, "output": output}


    print("\n~~~~~~~~~~~~ Indicator Testing Summary ~~~~~~~~~~~~~")
    for module, result in test_results.items():
        status = "✅ Passed" if result["success"] else "❌ Failed"
        print(f"{status}: {module} -> {result['output']}")


    failed_tests = {k: v for k, v in test_results.items() if not v["success"]}
    if failed_tests:
        print("\n~~~~~~~~~~~~ Failed Indicators ~~~~~~~~~~~~")
        for module, result in failed_tests.items():
            print(f"❌ {module}: {result['output']}")

if __name__ == "__main__":
    csv_path = "./inds_updated.csv"
    root_dir = "./"
    IndicatorTester(csv_path, root_dir)
