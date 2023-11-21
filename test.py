from utils.twelve_data import get_dates

# os.remove('inputs/1min.log`')
(start_date, end_date) = get_dates("1min", 5000)
print(f"start_date : {start_date}")
print(f"end_date : {end_date}")
