#!/bin/bash

echo "Running data pipeline..."

echo "Importing data..."
python scripts/import_data.py

echo "Exploring data..."
python scripts/explore_data.py

echo "Cleaning data..."
python scripts/clean_data.py

echo "Training logistic regression model..."
python scripts/train_model.py

echo "Evaluating model..."
python scripts/evaluate_model.py

echo "Deploying model..."
python scripts/deploy_model.py

echo "Running tests..."
python -m unittest discover -s tests -p "*.py"

echo "Pipeline execution completed!"
