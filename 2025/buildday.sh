#!/bin/bash

source .env

if [[ -z $1 ]]; then
  echo day param is missing
  exit 1
fi

mkdir -p day$1
curl https://adventofcode.com/2025/day/$1/input \
  -H "Cookie: session=${AOC_SESSION}" \
  -o day$1/input.txt
