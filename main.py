import os
import shutil

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    art_path = os.path.join(base_dir, "art.jpg")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not output_dir:
        output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.png")
    shutil.copyfile(art_path, entry_path)

if __name__ == "__main__":
    main()
