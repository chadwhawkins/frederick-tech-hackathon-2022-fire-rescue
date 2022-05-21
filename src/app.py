from typing import Optional, Dict
import streamlit as st
import pandas as pd
import yaml

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
    
    def parse_template(template_path: str) -> Dict:
        """Parse the template file to create a map

        Args:
            template_path (str): Path where template is saved (this part could be automated)
        
        Returns:
            Dict: A dictionary mapping the various column names 
        """
        with open(f"{template_path}", mode="read") as template:
            try:
                template_map = yaml.safe_load(template)
            except yaml.YAMLError as e:
                print("An error occurred while reading the template file")
        return template_map

    def run(self) -> None:
        """Run the streamlit application
        """
        st.title("Fire Rescue App")
        input_file_data = st.file_uploader("Choose a file", type=['csv'])
        pass

if __name__ == "__main__":
    app = App()
    app.run()