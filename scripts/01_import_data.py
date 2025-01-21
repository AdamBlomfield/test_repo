"""
Script Description:
 - Import raw data
"""

# ========================== IMPORTS ==========================
# Standard library imports
import sys
from pathlib import Path
import logging
import pandas as pd

# Local application/library-specific imports
sys.path.append(str(Path(__file__).parents[1]))
import config as c
import utils.setup_utils as su

# ========================== CONSTANTS ==========================
# Set script_name variable including the extension
SCRIPT_NAME = Path(__file__).stem + ".py"

# ========================== FUNCTIONS ==========================
def import_data(input_file: str) -> None:
    logging.info(f"Importing Data...")
    logging.info(f"\tInput file:\t{input_file}")
    
    df = pd.read_csv(input_file)
    logging.info(f"\tData imported successfully")
    logging.info(f"\tFirst row:\n{df.head(1).T}")

# ========================== MAIN ==========================
if __name__ == "__main__":
    su.setup_logging(SCRIPT_NAME)
    import_data(c.RAW_DATA_FILEPATH)
    logging.info("Script complete")
