def merge_lines(lines: list[str]) -> str:
    """
    Utility to merge scene-wise lines into one narration
    """
    return " ".join(
        line.strip() for line in lines if line.strip()
    )
