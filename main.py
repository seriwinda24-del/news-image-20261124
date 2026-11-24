#!/usr/bin/env python3
"""news-image-20261124 — copy the vendored newspaper front page to the output dir.

Stdlib only. The image itself (entry.png, 1024x1024) is the entry: a one-page
front page summing up 24 November 2026 world news ("THE WORLD IN ONE PAGE").
"""
import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(here, "output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    if os.path.getsize(dst) != os.path.getsize(src):
        print("error: copied file size mismatch", file=sys.stderr)
        return 1
    print("wrote", dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())
