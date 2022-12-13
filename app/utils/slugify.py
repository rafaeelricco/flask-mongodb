import re


def slugify(text):
    """Slugify a string."""
    return re.sub(r"[\s_]", "-", text).strip("-").lower()
