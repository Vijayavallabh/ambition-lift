#!/usr/bin/env bash
set -eu
cp -R "$(dirname "$0")/files/." .
python3 gen_data.py
