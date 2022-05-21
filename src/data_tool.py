from cProfile import label
import pandas as pd
from datetime import datetime

class DataTool:
    def __init__(self) -> None:
        pass
    
    def read_base_file(self) -> pd.DataFrame:
        """Reads the base file that would be used for the merging

        Returns:
            pd.DataFrame: A dataframe from the xlsx file
        """
        base_file_path = "../data/Daily_CAD_Reconciliation.xlsx"
        file_df = pd.read_excel(f"{base_file_path}")
        return file_df

    def merge_to_base(self, daily_report_path: str) -> pd.DataFrame:
        """Merge data to the base file

        Args:
            daily_report_path (str): The path to the daily report file

        Returns:
            pd.DataFrame: A dataframe with the merged data to the base file
        """
        base_file_path = "../data/Daily_CAD_Reconciliation.xlsx"

        daily_report = pd.read_csv(f"{daily_report_path}")
        number_of_incidents = daily_report.shape[1]
        
        file_df = pd.read_excel(f"{base_file_path}")

        new_daily_report = pd.DataFrame({"Date": [datetime.today().replace(hour=0, minute=0, second=0)], "Number of Incidents": [number_of_incidents]})
        results = pd.concat([file_df, new_daily_report], ignore_index=True)
        return results


