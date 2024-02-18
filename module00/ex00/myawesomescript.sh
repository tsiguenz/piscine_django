#!/bin/sh

URL=$(curl --silent --location --head "$1" --output /dev/null -w "%{url_effective}\n")

if [ $? -ne 0 ]; then
	echo "Error bad url!"
	exit 1
fi

echo "$URL"
