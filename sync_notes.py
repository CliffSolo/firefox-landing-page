#!/usr/bin/env python3
"""Copy today's daily note, ASAP and Bills from the ScrapYard vault into notes.js for the homepage.

Firefox won't let a local page read other files, so this writes the note contents
into notes.js next to index.html, which the page loads as a script.

Bill due dates (for the calendar dots), either form on a bill line:
  - [ ] Verizon 📅 2026-11-03     (Obsidian Tasks date)
  - [ ] Verizon due 15            (day of the month, repeats every month)
"""
import datetime as dt
import json
import re
from pathlib import Path

VAULT = Path.home() / "Documents/ScrapYard"
DAILY_DIR = VAULT / "01 - Home/Daily Notes"
ASAP = VAULT / "ASAP.md"
BILLS = VAULT / "Bills Due This Month.md"
OUT = Path(__file__).resolve().parent / "notes.js"
# Current Omarchy theme, for the page's "Match Desktop" theme
DESKTOP_THEME = Path.home() / ".local/state/omarchy/current"

TASK = re.compile(r"^\s*[-*] \[(.)\]\s*(.*)$")
DATE = re.compile(r"📅\s*(\d{4}-\d{2}-\d{2})")
DUE_DAY = re.compile(r"\bdue\s+(\d{1,2})(?:st|nd|rd|th)?\b", re.I)


def read_lines(path):
    if not path.exists():
        return None
    text = path.read_text(encoding="utf-8")
    if text.startswith("---"):  # skip frontmatter
        end = text.find("\n---", 3)
        if end != -1:
            text = text[end + 4:]
    return text.splitlines()


def parse(lines, open_tasks_only):
    """Return items: {kind: task|heading|text, text, done}. Empty checkboxes are skipped."""
    items = []
    for line in lines or []:
        m = TASK.match(line)
        if m:
            done = m.group(1).lower() == "x"
            text = m.group(2).strip()
            if not text or (open_tasks_only and done):
                continue
            items.append({"kind": "task", "text": text, "done": done})
        elif line.lstrip().startswith("#") and not line.lstrip().startswith("#" + "["):
            text = line.lstrip("#").strip()
            if text and not open_tasks_only:
                items.append({"kind": "heading", "text": text})
        elif line.strip() and not open_tasks_only:
            items.append({"kind": "text", "text": line.strip().lstrip("-* ").strip()})
    return items


def bill_dates(item):
    """Due dates for a bill: a fixed 📅 date, or 'due N' meaning that day every month."""
    m = DATE.search(item["text"])
    if m:
        item["due"] = m.group(1)
    m = DUE_DAY.search(item["text"])
    if m:
        item["dueDay"] = int(m.group(1))
    item["text"] = DUE_DAY.sub("", DATE.sub("", item["text"])).strip()
    return item


def obsidian_link(path):
    rel = path.relative_to(VAULT).with_suffix("")
    return "obsidian://open?" + "vault=ScrapYard&file=" + str(rel).replace(" ", "%20").replace("/", "%2F")


def desktop_theme():
    """Name and colors (background, foreground, accent, color0-15) of the current Omarchy theme."""
    colors_file = DESKTOP_THEME / "theme/colors.toml"
    name_file = DESKTOP_THEME / "theme.name"
    colors = {}
    if colors_file.exists():
        for m in re.finditer(r'^\s*(\w+)\s*=\s*"(#[0-9a-fA-F]{6})"', colors_file.read_text(encoding="utf-8"), re.M):
            colors[m.group(1)] = m.group(2)
    name = name_file.read_text(encoding="utf-8").strip() if name_file.exists() else ""
    return {"name": name.replace("-", " ").title(), "colors": colors}


def main():
    today = dt.date.today()
    daily = DAILY_DIR / f"{today.isoformat()}.md"
    data = {
        "synced": dt.datetime.now().isoformat(timespec="seconds"),
        "today": {
            "date": today.isoformat(),
            "exists": daily.exists(),
            "link": obsidian_link(daily),
            "items": parse(read_lines(daily), open_tasks_only=False),
        },
        "asap": {"link": obsidian_link(ASAP), "items": parse(read_lines(ASAP), open_tasks_only=True)},
        "bills": {
            "link": obsidian_link(BILLS),
            "items": [bill_dates(i) for i in parse(read_lines(BILLS), open_tasks_only=True)],
        },
        "desktop": desktop_theme(),
    }
    OUT.write_text("window.HOMEPAGE_NOTES = " + json.dumps(data, ensure_ascii=False, indent=1) + ";\n", encoding="utf-8")
    counts = f"today {len(data['today']['items'])}, ASAP {len(data['asap']['items'])}, bills {len(data['bills']['items'])}"
    print(f"\033[32mSynced notes → {OUT.name} ({counts})\033[0m")


if __name__ == "__main__":
    main()
