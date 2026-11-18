import os
import pathlib
import shutil


def main():
    program_dir = pathlib.Path(__file__).resolve().parent
    art_path = program_dir / "art.jpg"
    output_dir = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.png"
    shutil.copyfile(art_path, entry_path)


if __name__ == "__main__":
    main()
