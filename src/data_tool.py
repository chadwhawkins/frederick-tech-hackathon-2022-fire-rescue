import pandas as pd
from datetime import datetime

class DataTool:
    def __init__(self) -> None:
        pass

    def merge_to_base(self, daily_report_path: str):
        base_file_path = "../data/Daily_CAD_Reconciliation.xlsx"
        daily_report = pd.read_csv(f"{daily_report_path}")
        number_of_incidents = daily_report.shape[1]
        
        file_df = pd.read_excel(f"{base_file_path}")
        # add the new daily data to the base
        new_daily_report = pd.Series([datetime.today().strftime('%Y-%m-%d'), number_of_incidents])
        file_df.append(new_daily_report, ignore_index=True)
        print(file_df.tail())

if __name__ == "__main__":
    dt = DataTool()
    dt.merge_to_base("../data/Daily-EMS-CAD-Reconciliation-Report---CAD-EMS-Responses-without-EMS-Reports---previous-24-hours_2022-05-20_051007.CSV")


