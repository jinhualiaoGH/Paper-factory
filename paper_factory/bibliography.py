def format_references(refs, style="IEEE"):
    """
    style:
        IEEE
        APA
        NATURE
    """

    formatted = []

    for i, ref in enumerate(refs, start=1):

        if style.upper() == "IEEE":
            formatted.append(f"[{i}] {ref}")

        elif style.upper() == "APA":
            formatted.append(ref)

        elif style.upper() == "NATURE":
            formatted.append(f"{i}. {ref}")

        else:
            formatted.append(f"[{i}] {ref}")

    return formatted