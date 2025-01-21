# ========================== IMPORTS ==========================
# Standard library imports
from pathlib import Path
import sys

# Third-party imports
import logging

# Local application/library-specific imports
sys.path.append(str(Path(__file__).parents[1]))
import config as c


# ========================== FUNCTIONS ==========================
def setup_logging(script_name: str) -> None:
    # Create log directory if it doesn't exist
    Path(c.LOG_FILEPATH).parent.mkdir(parents=True, exist_ok=True)
    
    logging.basicConfig(
        filename=c.LOG_FILEPATH,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%y-%m-%d %H:%M:%S'
    )
    logging.getLogger(script_name).setLevel(logging.INFO)
    
    # Beging Log file with a title
    with open(c.LOG_FILEPATH, 'r') as file:
        lines = file.readlines()
    with open(c.LOG_FILEPATH, 'w') as file:
        file.write(f">>> Running: {script_name} \n")
        file.writelines(lines)
    