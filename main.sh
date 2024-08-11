#!/bin/bash

# conda activate scrap

# Name folder where to store data
folder="data"
# Date range, follow example structure: YEAR-MONTH-DAY
start_date="2024-4-24"
end_date="2024-4-27"

# Running script for OKX news parsing
python main.py --folder=${folder} --start_date=${start_date} --end_date=${end_date}

