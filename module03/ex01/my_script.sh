#!/bin/bash

set -eu

pip_version="$(pip --version)"
pathlib_url="https://github.com/jaraco/path.git"
pathlib_folder_name="pathlib"

echo "pip version is $pip_version"
if [ ! -d "local_lib/$pathlib_folder_name" ]; then
	mkdir -p local_lib
	echo "Cloning $pathlib_folder_name..."
	git clone --depth 1 "$pathlib_url" "local_lib/$pathlib_folder_name" &>"local_lib/pathlib.log"
	echo "$pathlib_folder_name is cloned!"
else
	echo "$pathlib_folder_name is already here!"
fi
