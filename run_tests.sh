#!/bin/bash
echo "Running all tests..."
python -m unittest discover -s tests -p "*.py"
echo "Tests completed!"