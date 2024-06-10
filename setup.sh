#!/bin/bash

if command -v python3 &>/dev/null; then
    echo "Python is installed"
else
    echo "Python is not installed"
    exit 1
fi

pip3 install -r requirements.txt

echo "The setup is complete."