#!/bin/bash
chmod +x new.py
set +o history
history > hist.txt
python3 ./new.py
set -o history
cp hist.txt .zsh_history
