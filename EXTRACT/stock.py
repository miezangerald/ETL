from requete import requettage_api
import global_variable
import os
import pandas as pd
from datetime import datetime


def get_month_path(subject):
    path_subject = os.path.join(global_variable.projet_path, subject)
    today = datetime.now()
    year_path = os.path.join(path_subject, str(today.year))
    month_path = os.path.join(year_path, str(today.month))
    return month_path


def save_subject_data(subject):
    base_current = requettage_api(subject)
    month_path = get_month_path(subject)
    os.makedirs(month_path, exist_ok=True)
    day_path = os.path.join(month_path, str(datetime.now().day))
    pd.DataFrame(base_current).to_csv(day_path + ".csv")
    return "GOOD"
