#!/bin/sh
echo "Installing packages from requirements.txt"
pip install -r requirements.txt
sleep 5
python main.py