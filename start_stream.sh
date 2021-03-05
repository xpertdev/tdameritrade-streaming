#!/bin/sh

if ! pgrep -f "python stream.py"; then
	python stream.py &
fi
