import os


def make_caption_from_filename(file_name):
    base_name = os.path.splitext(file_name)[0]

    caption = (
        base_name.replace("_", " ")
        .replace("-", " ")
        .title()
    )

    return caption


def load_caption(base_name, caption_folder="captions"):
    caption_file = os.path.join(caption_folder, base_name + ".txt")

    if os.path.exists(caption_file):
        with open(caption_file, "r", encoding="utf-8") as f:
            return f.read().strip()

    return None


def discover_figures(folder="figures"):
    figures = []

    if not os.path.exists(folder):
        return figures

    valid_ext = [".png", ".jpg", ".jpeg"]

    files = sorted(os.listdir(folder))

    for file in files:
        ext = os.path.splitext(file)[1].lower()

        if ext in valid_ext:
            path = os.path.join(folder, file)
            base_name = os.path.splitext(file)[0]

            caption = load_caption(base_name)

            if caption is None:
                caption = make_caption_from_filename(file)

            figures.append({
                "file": path,
                "caption": caption
            })

    return figures


def discover_csv_tables(folder="data"):
    tables = []

    if not os.path.exists(folder):
        return tables

    files = sorted(os.listdir(folder))

    for file in files:
        ext = os.path.splitext(file)[1].lower()

        if ext == ".csv":
            path = os.path.join(folder, file)
            base_name = os.path.splitext(file)[0]

            title = load_caption(base_name)

            if title is None:
                title = make_caption_from_filename(file)

            tables.append({
                "title": title,
                "csv": path
            })

    return tables

def discover_references(folder="references"):
    references = []

    if not os.path.exists(folder):
        return references

    files = sorted(os.listdir(folder))

    for file in files:
        ext = os.path.splitext(file)[1].lower()

        if ext == ".txt":
            path = os.path.join(folder, file)

            with open(path, "r", encoding="utf-8") as f:
                ref = f.read().strip()

            if ref:
                references.append(ref)

    return references

def load_caption(base_name, caption_folder="captions"):
    caption_file = os.path.join(caption_folder, base_name + ".txt")

    if os.path.exists(caption_file):
        with open(caption_file, "r", encoding="utf-8") as f:
            return f.read().strip()

    return None