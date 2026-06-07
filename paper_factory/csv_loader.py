import csv
import os


def load_csv_table(csv_path):
    """
    Load a CSV file and return headers and rows.

    Expected CSV format:

        Order,Cross Entropy,Information Gain
        0,0.336184,0
        1,0.330224,0.005960

    Returns:
        headers: list[str]
        rows: list[list[str]]
    """

    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"CSV file not found: {csv_path}")

    headers = []
    rows = []

    with open(csv_path, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.reader(f)

        for row_index, row in enumerate(reader):
            # Skip completely empty rows
            if not row or all(str(cell).strip() == "" for cell in row):
                continue

            if row_index == 0:
                headers = [str(cell).strip() for cell in row]
            else:
                rows.append([str(cell).strip() for cell in row])

    return headers, rows


def csv_to_table_data(csv_path, title=None):
    """
    Convert a CSV file into PaperFactory table_data format.

    Returns:
        {
            "title": "...",
            "headers": [...],
            "rows": [...]
        }
    """

    headers, rows = load_csv_table(csv_path)

    if title is None:
        base_name = os.path.basename(csv_path)
        title = os.path.splitext(base_name)[0].replace("_", " ").title()

    return {
        "title": title,
        "headers": headers,
        "rows": rows
    }