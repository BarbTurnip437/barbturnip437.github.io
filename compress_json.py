import json
from pathlib import Path
from typing import Optional


def compress_json(input_file: Path, output_file: Optional[Path] = None):
    with input_file.open("r", encoding="utf-8") as f:
        data = json.load(f)

    if output_file is None:
        output_file = input_file

    with output_file.open("w", encoding="utf-8") as f:
        json.dump(data, f, separators=(",", ":"))


if __name__ == "__main__":
    compress_json(next(Path().glob("hrt-dosages*.json")))
