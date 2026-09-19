from pathlib import Path

WORK_DIRECTORY = Path().home() / "Downloads"
MAIN_DIRECTORY = Path().home()
EXTENSIONS = {
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

def move_file_to_its_directory(item: Path):
    if not item.is_file():
        return
    suffix = item.suffix.lower()
    if suffix not in EXTENSIONS:
        return
    target_directory: Path = MAIN_DIRECTORY / EXTENSIONS[suffix]
    target_directory.mkdir(parents=True, exist_ok=True)
    item.rename(target_directory / item.name)


def main():
    if WORK_DIRECTORY.exists():
        for item in WORK_DIRECTORY.iterdir():
          move_file_to_its_directory(item)

if __name__ == "__main__":
    main()