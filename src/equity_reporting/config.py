import os
from pathlib import Path
from dotenv import load_dotenv


load_dotenv()

class DataPaths:
    BASE_PATH = Path(os.getenv("BASE_PATH", "C:/Users/DefaultUser/"))
    ONEDRIVE_PATH = Path(os.getenv("ONEDRIVE_PATH", BASE_PATH / "OneDrive"))
    monthly_distributions=Path(os.getenv("ONEDRIVE_PATH"),"Portsys//reporting data//monthly distributions.xlsx")
    dont_invest_dividends=Path(os.getenv("ONEDRIVE_PATH"),"Portsys//reporting data//dont invest dividends.xlsx")
