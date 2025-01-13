#!/bin/bash

set -eu

pip_version="$(pip --version)"
lib_folder="local_lib"
pathlib_url="https://github.com/jaraco/path.git"
pathlib_folder_name="path"

function main {
	if [ ! -d "$lib_folder/$pathlib_folder_name" ]; then
		mkdir -p $lib_folder
		echo "Cloning $pathlib_folder_name..."
		git clone -v --depth 1 "$pathlib_url" "$lib_folder/$pathlib_folder_name" &>"$lib_folder/path.log"
		echo "$pathlib_folder_name is cloned!"
		python3 my_program.py
	else
		echo "$pathlib_folder_name is already here, removing it!"
		rm -rf "$lib_folder"
		main
	fi
}

echo "pip version is $pip_version"
main
