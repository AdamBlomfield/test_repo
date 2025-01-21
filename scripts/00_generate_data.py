"""
Script Description:
 - Generate raw dummy data
"""

# ========================== IMPORTS ==========================
# Standard library imports
from pathlib import Path
import sys
import traceback
import random
import pandas as pd

# Third-party imports
import logging
from faker import Faker

# Local application/library-specific imports
sys.path.append(str(Path(__file__).parents[1]))
import config as c
import utils.setup_utils as su

# ========================== CONSTANTS ==========================
# Set script_name variable including the extension
SCRIPT_NAME = Path(__file__).stem + ".py"

ROW_COUNT = 1000

faker = Faker('en_GB') # Set Faker to UK locale

# ========================== FUNCTIONS ==========================
def generate_data(row_count: int, output_file: str) -> None:
    logging.info(f"Generating Data...")
    try:
        logging.info(f"\tRow Count:\t{row_count:,}")
        
        # Generate data
        data = {
            "id": [i for i in range(row_count)],
            "name": [faker.first_name() for _ in range(row_count)],
            "age": [random.randint(18, 65) for _ in range(row_count)],
            "email": [faker.email() for _ in range(row_count)],
            "phone": [faker.phone_number() for _ in range(row_count)],
            "address": [faker.address() for _ in range(row_count)],
            "city": [faker.city() for _ in range(row_count)],
            "postcode": [faker.postcode() for _ in range(row_count)],
            "country": [faker.country() for _ in range(row_count)]
        }
        
        # Create DataFrame
        df = pd.DataFrame(data)
        
        # Write DataFrame to CSV
        df.to_csv(output_file, index=False)
        
        logging.info(f"\tOutput file:\t{output_file}")
        
        # Log the first row of the DataFrame, transposed
        logging.info(f"\tFirst row:\n{df.head(1).T}")
    
    except Exception as e:
        raise e

# ========================== MAIN EXECUTION ==========================
if __name__ == "__main__":
    try:
        su.setup_logging(SCRIPT_NAME)
        
        generate_data(ROW_COUNT, c.RAW_DATA_FILEPATH)
        
        logging.info("Script complete")
        
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        logging.error(f"Traceback: {traceback.format_exc()}")
        raise e
