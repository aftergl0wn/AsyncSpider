from datetime import datetime

from .settings import BASE_DIR

data = {
    'total': 0
}

filename = (
    f'{BASE_DIR}/results/status_summary_'
    f'{datetime.strftime(datetime.now(), "%Y-%m-%d_%H-%M-%S")}.csv'
)
