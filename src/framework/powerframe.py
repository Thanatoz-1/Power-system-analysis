import pandas as pd
from typing import Optional

from src.utils import vd_reader

__all__ = ["PowerFrame"]


class PowerFrame:
    """
    Powerframe for managing and handling all the functionalities of a dataframe with specific operations.
    """

    _registry = []

    def __init__(self, **kwargs) -> None:
        """
        Important kwrags are:
        1. path/data: The path of the vd file.
        2. name: Name of the variables
        3. Unit: Unit to the showcased.
        """
        self._registry.append(self)
        if "path" in kwargs:
            self.data = vd_reader(kwargs["path"]) if kwargs["path"] else pd.DataFrame()
        if "data" in kwargs:
            self.data = kwargs["data"]
        self.var_name = kwargs["name"] if "name" in kwargs else ""
        self.unit = kwargs["unit"] if "unit" in kwargs else ""
        self.backup_data = self.data

        self.yearlist = ["2010", "2015", "2020", "2025", "2030", "2035", "2040", "2045", "2050"]
        self.df_region_sum = []
        self.data = self.process_region()

    def set_unit(self, unit: str):
        self.set_unit

    @classmethod
    def show(self):
        """
        Function to retreive the dataframe view.
        """
        self.data

    def __repr__(self):
        """
        repr to see the output of the dataframe
        """
        return repr(self.data)

    def reset(self):
        """
        Reset the dataframe if any issue persists.
        """
        self.data = self.backup_data

    def __getitem__(self, key):
        """
        Obtain the value of a required key.
        """
        self.varname = key

    def process_region(self, region_list: list = ["DER", "BW"]) -> None:
        df_region_sum = []
        for region in region_list:
            dict_df = {
                "Model": "TIMES PanEU v1.0",
                "Region": region,
                "Variable": self.var_name,
                "Unit": self.unit,
                "2010": "0",
                "2015": "0",
                "2020": "3",
                "2025": "0",
                "2030": "0",
                "2035": "0",
                "2040": "0",
                "2045": "0",
                "2050": "0",
            }
            df_temp_region = pd.DataFrame(data=dict_df, index=[0])
            mask_region = self.data.Region == region
            df_region = self.data.loc[mask_region]

            for year in self.yearlist:
                mask_year = df_region.Period == year
                df_year = df_region.loc[mask_year]
                year_sum = df_year["PV"].sum()

                df_temp_region[year] = year_sum

            df_region_sum.append(df_temp_region)
        self.data = pd.concat(self.df_region_sum)

    def change_unit(self, target_unit, operation, number):
        """
        Takes in a unit and the conversion operation and generates output.

        TODO:
        1. Convert the operation to lambda function or method
        """
        target_unit = target_unit
        operation = operation
        number = number
        df_temp = self.data

        if operation == "multiplication":
            for year in self.yearlist:
                df_temp[year] = df_temp[year].apply(lambda x: x * number)

        if operation == "division":
            for year in self.yearlist:
                df_temp[year] = df_temp[year].apply(lambda x: x / number)

        df_temp["Unit"] = target_unit
        self.data = df_temp
