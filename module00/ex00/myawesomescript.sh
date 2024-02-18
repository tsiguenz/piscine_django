#!/bin/sh

curl --silent --location --head "$1" --output /dev/null -w "%{url_effective}\n"
