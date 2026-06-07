import os


def audit_paper(cfg):

    issues = []

    # -------------------------
    # Required sections
    # -------------------------

    if not cfg.get("title"):
        issues.append("Missing title")

    if not cfg.get("abstract") and not cfg.get("markdown_file"):
        issues.append("Missing abstract")

    if not cfg.get("sections"):
        issues.append("No sections found")

    if not cfg.get("references"):
        issues.append("No references found")

    # -------------------------
    # Figure validation
    # -------------------------

    if "figures" in cfg:

        for fig in cfg["figures"]:

            if not os.path.exists(fig["file"]):
                issues.append(
                    f"Missing figure file: {fig['file']}"
                )

            if not fig.get("caption"):
                issues.append(
                    f"Missing caption for figure: {fig['file']}"
                )

    # -------------------------
    # Duplicate references
    # -------------------------

    if "references" in cfg:

        seen = set()

        for ref in cfg["references"]:

            if ref in seen:
                issues.append(
                    f"Duplicate reference: {ref}"
                )

            seen.add(ref)

    return issues