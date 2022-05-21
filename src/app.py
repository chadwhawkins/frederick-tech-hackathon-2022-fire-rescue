from typing import Optional, Dict
import streamlit as st
import pandas as pd

class App:
    def __init__(self) -> None:
        """Init app
        """
        pass
    
    def data_import(self, file_path: str) -> pd.DataFrame:
        """Import data from csv and output a pandas dataframe

        Args:
            file_path (str): The filepath from  disk

        Returns:
            pd.DataFrame: A dataframe of the CSV file
        """
        file_data_frame = pd.read_csv(file_path, sep=",")
        return file_data_frame
    
    def run(self) -> None:
        """Run the streamlit application
        """
        st.title("Fire Rescue App")
        input_file_data = st.file_uploader("Choose a file")
        pass

if __name__ == "__main__":
    app = App()
    app.run()