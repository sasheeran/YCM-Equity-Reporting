import os
from pathlib import Path
from dotenv import load_dotenv


load_dotenv()

class DataPaths:
    BASE_PATH = Path(os.getenv("BASE_PATH", "C:/Users/DefaultUser/"))
    ONEDRIVE_PATH = Path(os.getenv("ONEDRIVE_PATH", BASE_PATH / "OneDrive"))

