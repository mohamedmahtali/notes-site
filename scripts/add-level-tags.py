#!/usr/bin/env python3
"""Add level frontmatter tags to DevOps notes based on folder depth."""

import os
import re

CONTENT_DIR = os.path.join(os.path.dirname(__file__), "..", "content")
SKIP_FILES = {"index.md", "about.md", "roadmap.md"}

# Override levels for specific paths (relative to content/)
OVERRIDES = {
    # Top-level concept pages → beginner
    "Linux.md": "beginner",
    "Git.md": "beginner",
    "Docker.md": "beginner",
    "Cloud.md": "beginner",
    "CI-CD.md": "beginner",
    "Kubernetes.md": "intermediate",
    "Observability.md": "intermediate",
    "Infrastructure as Code.md": "intermediate",
    "Security.md": "intermediate",
    # Cloud computing concepts → beginner
    "Cloud/Cloud computing": "beginner",
    # Kubernetes deeper topics → advanced
    "Kubernetes/": "intermediate",
}


def get_level(rel_path: str) -> str:
    # Check overrides first
    for pattern, level in OVERRIDES.items():
        if rel_path == pattern or rel_path.startswith(pattern):
            return level

    # Depth-based fallback
    depth = rel_path.count(os.sep)
    if depth == 0:
        return "beginner"
    elif depth == 1:
        return "intermediate"
    else:
        return "advanced"


def has_frontmatter(content: str) -> bool:
    return content.startswith("---")


def add_frontmatter(content: str, level: str) -> str:
    title_match = re.search(r"^# (.+)$", content, re.MULTILINE)
    title = title_match.group(1) if title_match else None

    frontmatter_lines = ["---"]
    if title:
        frontmatter_lines.append(f"title: {title}")
    frontmatter_lines.append(f"tags:")
    frontmatter_lines.append(f"  - {level}")
    frontmatter_lines.append("---")
    frontmatter_lines.append("")

    return "\n".join(frontmatter_lines) + content


def update_frontmatter(content: str, level: str) -> str:
    """Add level tag to existing frontmatter if not already present."""
    end = content.find("---", 3)
    if end == -1:
        return content

    fm = content[3:end]

    if "tags:" in fm:
        # Tags block already exists — add level if not present
        if level in fm:
            return content  # already tagged
        # Append to tags list
        new_fm = fm.rstrip()
        new_fm += f"\n  - {level}\n"
        return "---" + new_fm + "---" + content[end + 3:]
    else:
        # No tags block — add one
        new_fm = fm.rstrip() + f"\ntags:\n  - {level}\n"
        return "---" + new_fm + "---" + content[end + 3:]


def process_file(filepath: str) -> bool:
    rel_path = os.path.relpath(filepath, CONTENT_DIR)

    if os.path.basename(filepath) in SKIP_FILES:
        return False

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    level = get_level(rel_path)

    if has_frontmatter(content):
        new_content = update_frontmatter(content, level)
    else:
        new_content = add_frontmatter(content, level)

    if new_content != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        return True

    return False


def main():
    modified = 0
    total = 0

    for root, _, files in os.walk(CONTENT_DIR):
        for filename in files:
            if not filename.endswith(".md"):
                continue
            filepath = os.path.join(root, filename)
            total += 1
            if process_file(filepath):
                modified += 1

    print(f"Done: {modified}/{total} files updated.")


if __name__ == "__main__":
    main()
