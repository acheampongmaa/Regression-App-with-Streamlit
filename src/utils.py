import numpy as np
import pickle




def payday(row):
    if row.DayOfMonth == 15 or row.Is_month_end == 1:
        return 1
    else:
        return 0
        

def date_extracts(data):
    data['Year'] = data.index.year
    data['Month'] = data.index.month
    data['DayOfMonth'] = data.index.day
    data['DaysInMonth'] = data.index.days_in_month
    data['DayOfYear'] = data.index.day_of_year
    data['DayOfWeek'] = data.index.dayofweek
    data['Week'] = data.index.isocalendar().week
    data['Is_weekend'] = np.where(data['DayOfWeek'] > 4, 1, 0)
    data['Is_month_start'] = data.index.is_month_start.astype(int)
    data['Is_month_end'] = data.index.is_month_end.astype(int)
    data['Quarter'] = data.index.quarter
    data['Is_quarter_start'] = data.index.is_quarter_start.astype(int)
    data['Is_quarter_end'] = data.index.is_quarter_end.astype(int)
    data['Is_year_start'] = data.index.is_year_start.astype(int)
    data['Is_year_end'] = data.index.is_year_end.astype(int)
