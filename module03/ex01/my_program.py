#!/usr/bin/python3

from local_lib.path.path import Path

if __name__ == "__main__":
    new_dir = Path("test")
    new_dir.mkdir_p()
    new_file = Path("test/test")
    new_file.touch()
    new_file.write_bytes(b"Hello world!\n")
    print(new_file.read_bytes().decode())
