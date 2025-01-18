"""
Configuration file for the data processing pipeline.
Contains all necessary configurations including:
- Date and time formats
- Directory paths for data, logs, models, and other project resources
- File paths for raw and processed data
"""

# Standard Library Imports
import os
import sys
import datetime as dt
from pathlib import Path

# Third-Party Imports
import pandas as pd

# =============================================================================
# DATE AND TIME CONFIGURATIONS
# =============================================================================
NOW = dt.datetime.now()
DATE = {
    'yyyy-mm-dd-hh-mm-ss': NOW.strftime('%Y-%m-%d-%H-%M-%S'),
    'yyyy-mm-dd hh:mm:ss': NOW.strftime('%Y-%m-%d %H:%M:%S'),
    'yyyy-mm-dd': NOW.strftime('%Y-%m-%d'),
    'hh:mm:ss': NOW.strftime('%H:%M:%S')
}

# =============================================================================
# BASE DIRECTORY PATHS
# =============================================================================
ROOT_DIR = Path(__file__).resolve().parent
DATA_DIR = os.path.join(ROOT_DIR, "data")
LOGS_DIR = os.path.join(ROOT_DIR, "logs")
MODELS_DIR = os.path.join(ROOT_DIR, "models")
REPORTS_DIR = os.path.join(ROOT_DIR, "reports")
SCRIPTS_DIR = os.path.join(ROOT_DIR, "scripts")
TESTS_DIR = os.path.join(ROOT_DIR, "tests")
UTILS_DIR = os.path.join(ROOT_DIR, "utils")
VISUALISATIONS_DIR = os.path.join(ROOT_DIR, "visualisations")

# =============================================================================
# DATA PATHS
# =============================================================================
RAW_DATA_DIR = os.path.join(DATA_DIR, "raw")
RAW_DATA_FILEPATH = os.path.join(RAW_DATA_DIR, "raw_data.csv")
PROCESSED_DATA_DIR = os.path.join(DATA_DIR, "processed")
PROCESSED_DATA_FILEPATH = os.path.join(PROCESSED_DATA_DIR, "processed_data.csv")

# =============================================================================
# LOG PATHS
# =============================================================================
LOG_FILEPATH = os.path.join(LOGS_DIR, f"{DATE['yyyy-mm-dd-hh-mm-ss']}.log")
