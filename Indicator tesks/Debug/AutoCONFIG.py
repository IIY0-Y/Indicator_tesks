import os
import json
import pandas as pd

def clean_str(s):
    return s.strip().strip("'").strip('"')

def try_convert(val):
    try:
        return int(val)
    except ValueError:
        try:
            return float(val)
        except ValueError:
            return val

def parse_cell(cell):
    if isinstance(cell, str):
        if cell.startswith("{") and cell.endswith("}"):
            cell = cell[1:-1].strip()
        if ";" in cell:
            items = [item.strip() for item in cell.split(";") if item.strip()]
            result = {}
            for item in items:
                if ":" in item:
                    key, value = item.split(":", 1)
                    result[clean_str(key)] = try_convert(clean_str(value))
                else:
                    result[str(len(result))] = clean_str(item)
            return result
    return cell

def rebuild_config_from_row(row):
    config = {}
    for col in row.index:
        config[col] = parse_cell(row[col])
    return config

def get_target_file(row, idx):
    indicator_class = row.get('indicator_class')
    indicator_name = row.get('indicator_name')
    if pd.isna(indicator_class):
        indicator_class = ""
    if pd.isna(indicator_name):
        indicator_name = ""
    if indicator_class and not indicator_name:
        parts = [p.strip() for p in indicator_class.split(',')]
        if len(parts) >= 2:
            folder = parts[0].lower().replace(' ', '_')
            filename = parts[1].lower().replace(' ', '_') + ".py"
        else:
            print(f"[DEBUG] Row {idx} incomplete data, skipping: {row.to_dict()}")
            return None, None
    elif indicator_class and indicator_name:
        folder = indicator_class.lower().replace(' ', '_')
        filename = indicator_name.lower().replace(' ', '_') + ".py"
    else:
        print(f"[DEBUG] Skipping row {idx} (missing 'indicator_class'/'indicator_name'): {row.to_dict()}")
        return None, None
    return folder, filename

def insert_config_in_file(file_path, config):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    config_str = "CONFIG = " + json.dumps(config, indent=4) + "\n"
    lines.insert(2, config_str)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    print(f"Updated {file_path}")

def process_files(csv_path, root_dir):
    df = pd.read_csv(csv_path, sep=';')
    for idx, row in df.iterrows():
        config = rebuild_config_from_row(row)
        folder, filename = get_target_file(row, idx + 1)
        if folder is None or filename is None:
            continue
        file_path = os.path.join(root_dir, folder, filename)
        if os.path.exists(file_path):
            insert_config_in_file(file_path, config)
        else:
            print(f"[DEBUG] File not found: {file_path}")



csv_path = r"CSV_PATH"
root_dir = r"ROOT_INDICATORS_FOLDER"
process_files(csv_path, root_dir)
