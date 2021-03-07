#!/bin/sh

if ! pgrep -f "python forever.py stream.py"; then
	python forever.py stream.py &
fi
