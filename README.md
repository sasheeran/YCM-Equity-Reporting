# YCM Equity Reporting

Portfolio analysis and reporting tools for Yousif Capital Management's equity strategies, including Dividend Growers and Dividend Aristocrats products.

## Features

- Portfolio performance analysis and metrics calculation
- Automated factsheet generation (PowerPoint)
- Integration with FactSet and APX APIs
- Data processing and analysis workflows
- Ad-hoc analysis notebooks

## Project Structure
```
ycm-equity-reporting/
├── src/
│   └── equity_reporting/       # Main package
│       ├── config.py           # Configuration and path management
│       ├── portfolio_analysis.py
│       ├── factsheet_generation.py
│       └── api_clients.py
├── notebooks/
│   ├── exploratory/            # Ad-hoc analysis
│   └── reports/                # Production notebooks
├── data/
│   ├── raw/                    # Raw data files
│   └── processed/              # Processed datasets
├── outputs/                    # Generated reports and files
└── tests/                      # Unit tests
```

## Setup Instructions

### 1. Clone the Repository
```bash
git clone 
cd ycm-equity-reporting
```

### 2. Create Virtual Environment
```bash
python -m venv venv
```

### 3. Activate Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### 4. Install Package
```bash
pip install -e .
```

This installs all required dependencies including pandas, numpy, matplotlib, jupyter, and more.

### 5. Configure Environment Variables

Copy the example environment file and customize it:
```bash
cp .env.example .env
```

Edit `.env` with your personal settings:
```bash
# Your local paths
BASE_PATH = "C:\\Users\\YourName\\"
ONEDRIVE_PATH = "C:\\Users\\YourName\\Yousif Capital Management\\Yousif Capital Mgmt - Documents\Yousif Capital Management\\"