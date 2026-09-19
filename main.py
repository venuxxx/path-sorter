from pathlib import Path

WORK_DIRECTORY = Path().home() / "Downloads"

extensions = {
    ".mp4": "Music",
    ".mp3": "Music",
    ".doc": "Documents",
    ".docx": "Documents",
    ".pdf": "Documents",
    ".xlsx": "Documents",
    ".xls": "Documents",
    ".jpg": "Pictures",
    ".jpeg": "Pictures",
    ".png": "Pictures",
    ".gif": "Pictures",
    ".svg": "Pictures",
}

for item in WORK_DIRECTORY.iterdir():
    print(item.name)