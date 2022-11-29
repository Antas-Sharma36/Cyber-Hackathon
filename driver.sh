#!/bin/bash
chmod +x new.py
set +o history
python3 ./new.py
set -o history
cp hist.txt .zsh_history
