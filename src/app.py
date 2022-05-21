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
            file_path (str): The filepath from the disk

        Returns:
            pd.DataFrame: A dataframe of the CSV file
        """
        file_data_frame = pd.read_csv(file_path, sep=",")
        return file_data_frame


    def create_dropdown(self, templates: tuple):
        """Create a dropdown menu for the user to select from the different templates

        Args:
            templates (tuple): A list of template names

        Returns:
            st.selectbox: A dropdown menu for the templates
        """
        options = st.selectbox("Select Template", ("A", "B", "C"))
        return options

        templateList = []
        templatePath = self.parse_template("config/mapping.yaml")

        # Iterate through the yaml dictionary
        for template in templatePath["templates"]:
            templateList.append(template['name'])  # Add each name to the list

        # create the dropdown menu with the list as a tuple
        dropdown = st.selectbox("Select Template", tuple(templateList))
        return dropdown

    def run(self) -> None:
        """Run the streamlit application
        """
        st.title("Fire Rescue App")
        dropdown_menu = self.create_dropdown(self.parse_yaml())
        input_file_data = st.file_uploader("Choose a file")
        pass

if __name__ == "__main__":
    app = App()
    app.run()