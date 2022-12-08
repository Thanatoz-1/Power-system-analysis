import os
import pandas as pd
from src.utils.pylogger import get_pylogger

logger = get_pylogger(__name__)
__all__ = ["SingleVar"]

region_list = ["DER", "BW"]
# logger.debug(f"Region list has been set to {region_list}")


class SingleVar(object):
    """
    single Var class to operate on the powerframe.
    """

    # This needs optimizations.
    # Create a list in which all attributes of the class are stored, so a loop can be run over it later on
    _registry = []
    # The init function is always called. Here the assignments of the variables are defined within the class.
    # The variables must be given always in the order as in the next line, "self" can be ignored thereby.
    def __init__(self, template, var_name, unit, df_rawdata, scenario=None):
        self._registry.append(self)
        self.var_name = var_name
        self.scenario = scenario
        # df rawdata wird mit oben stehender Filter Methode erstellt und beeinhaltet alle einzelnen Zeilen aus der VD Datei
        self.df_rawdata = df_rawdata
        # Wenn template "True" ist, dann wird die Variable im Template ausgegeben, sonst auf "False" setzen
        self.template = template

        # Übernimmt die Einheiten aus der Masterliste
        self.unit = unit
        # yearlist wird später über GUI ausgewählt
        yearlist = ["2010", "2015", "2020", "2025", "2030", "2035", "2040", "2045", "2050"]
        # Bereitet die spätere Struktur vor
        dict_df = {
            "Model": "TIMES",
            "Scenario": self.scenario,
            "Region": "Placeholder",
            "Variable": self.var_name,
            "Unit": self.unit,
            "2010": "0",
            "2015": "0",
            "2020": "0",
            "2025": "0",
            "2030": "0",
            "2035": "0",
            "2040": "0",
            "2045": "0",
            "2050": "0",
        }
        df_temp = pd.DataFrame(data=dict_df, index=[0])

        df_region_sum = []
        # Creates for each region and year the sum of all values and thus the total value of the variable
        for region in region_list:
            dict_df = {
                "Model": "TIMES PanEU v1.0",
                "Scenario": self.scenario,
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
            mask_region = df_rawdata.Region == region
            df_region = df_rawdata.loc[mask_region]

            for year in yearlist:
                mask_year = df_region.Period == year
                df_year = df_region.loc[mask_year]
                year_sum = df_year["PV"].sum()

                df_temp_region[year] = year_sum

            df_region_sum.append(df_temp_region)

        # Die oben erstellte und befüllte Tabelle wird immer als Variable.results gespeichert
        results = pd.concat(df_region_sum)
        self.results = results

    def add_Germany(self):
        # Diese Funktion ist notwendig, um die beiden deutschen Regionen DER und BW zu addieren. Dabei bleiben die Regionen vorerst enthalten
        # Einfache Möglichkeit, um 2 versch. Filter miteinander zu kombinieren
        mask1 = self.results.Region == "DER"
        mask2 = self.results.Region == "BW"
        df_temp = self.results.loc[mask1 | mask2]

        # df_temp = self.results.loc[self.results["Region"] == ["DER", "BW"]]
        dict_df = {
            "Model": "TIMES PanEU v1.0",
            "Scenario": self.scenario,
            "Region": "DEU",
            "Variable": self.var_name,
            "Unit": self.unit,
            "2010": df_temp["2010"].sum(axis=0),
            "2015": "0",
            "2020": "0",
            "2025": "0",
            "2030": "0",
            "2035": "0",
            "2040": "0",
            "2045": "0",
            "2050": "0",
        }
        yearlist = ["2010", "2015", "2020", "2025", "2030", "2035", "2040", "2045", "2050"]

        df_temp_DEU = pd.DataFrame(dict_df, index=[0])

        neu = pd.concat([self.results, df_temp_DEU])

        for year in yearlist:
            df_year = df_temp[year]
            year_sum = df_year.sum()
            df_temp_DEU[year] = year_sum
        # Verbinde die bisherigen Results mit dem DF für Deutschland
        results_DEU = pd.concat([self.results, df_temp_DEU])
        self.results = results_DEU

    def change_unit(self, target_unit, operation, number):
        self.target_unit = target_unit
        self.operation = operation
        self.number = number
        df_temp = self.results
        print(df_temp)
        # Try to make this list dynamic
        yearlist = ["2010", "2015", "2020", "2025", "2030", "2035", "2040", "2045", "2050"]

        if operation == "multiplication":
            for year in yearlist:
                df_temp[year] = df_temp[year].apply(lambda x: x * self.number)

        if operation == "division":
            for year in yearlist:
                df_temp[year] = df_temp[year].apply(lambda x: x / self.number)

        df_temp["Unit"] = self.target_unit
        print(df_temp)
        self.results = df_temp
