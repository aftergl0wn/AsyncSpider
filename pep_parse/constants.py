from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

data = {
    'total': 0
}

filename = (
    f'{BASE_DIR}/results/status_summary_'
    f'{datetime.strftime(datetime.now(), "%Y-%m-%d_%H-%M-%S")}.csv'
)
