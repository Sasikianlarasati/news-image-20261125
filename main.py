#!/usr/bin/env python3
"""Entry point for the news-image-20261125 make.fun submission.

Copies the pre-rendered entry.png (drawn by render.py) to /output/entry.png
and verifies the copy byte-for-byte against the source. Deterministic:
same input, same output, every run. Standard library only, no network.
"""
import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST_DIR = "/output"
DST = os.path.join(DST_DIR, "entry.png")


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    if not os.path.isfile(SRC):
        print(f"missing source image: {SRC}", file=sys.stderr)
        return 1
    os.makedirs(DST_DIR, exist_ok=True)
    shutil.copyfile(SRC, DST)
    src_hash = sha256(SRC)
    dst_hash = sha256(DST)
    if src_hash != dst_hash:
        print(f"hash mismatch: {src_hash} != {dst_hash}", file=sys.stderr)
        return 1
    print(f"wrote {DST} ({os.path.getsize(DST)} bytes)")
    print(f"sha256 {dst_hash}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
