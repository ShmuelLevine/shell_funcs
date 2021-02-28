#!/usr/bin/zsh

sudo zgrep Ban $1 | zgrep -v Restore | cut -f 16 -d' ' | cut -f 1,2 -d'.'
