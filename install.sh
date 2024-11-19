#!/bin/bash
if [-f venv/ ]; then
	echo "found venv"
else
	echo "setting up venv"
	python3 -m venv/
fi
pip3 install torch transformers kivy[base] kivy_examples kivymd
