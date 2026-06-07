import os


def load_markdown(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.readlines()


def markdown_to_sections(path):
    lines = load_markdown(path)

    sections = []

    current_title = None
    current_content = []

    for line in lines:
        line = line.strip()

        if line.startswith("# "):

            if current_title:
                sections.append({
                    "title": current_title,
                    "content": "\n".join(current_content)
                })

            current_title = line[2:]
            current_content = []

        else:
            current_content.append(line)

    if current_title:
        sections.append({
            "title": current_title,
            "content": "\n".join(current_content)
        })

    return sections