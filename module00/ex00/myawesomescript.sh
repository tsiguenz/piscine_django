#!/bin/sh

# Work with https://www.shorturl.at/

get_location() {
	TITLE="redirect_location_is="
	curl -w "$TITLE%{redirect_url}\n" "$1" 2> /dev/null | grep "$TITLE" | cut -d "=" -f 2
}

FIRST_LOCATION=$(get_location "$1")
REAL_URL=$(get_location "$FIRST_LOCATION")
echo "$REAL_URL"
