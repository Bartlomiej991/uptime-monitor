#!/bin/bash

while read -r url; do
  code=$(curl -s -o /dev/null -w "%{http_code}" "$url")
  now=$(date '+%Y-%m-%d %H:%M:%S')

  if [ "$code" = "200" ]; then
    echo "$now UP    $url"
  else
    echo "$now DOWN  $url ($code)"
  fi
done < sites.txt
