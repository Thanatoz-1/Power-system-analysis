import os
from typing import List, Optional
import pandas as pd


__all__ = ["vd_reader", "vd_multi_read"]


def vd_reader(path: str, *args, **kwargs) -> pd.DataFrame:
    """
    Single VD file reader. This reads files and returns a pandas dataframe.
    When using this function, please add the arguments as well.

    Args:
        path: str = Absolute path of the file.
        name: Optional[List] = Name of columns in the dataframe.
                This defaults to the default value in sample vd file.
        dtype: Optional[dict] = Dict of name of columns and their datatypes.
                This defaults to default datatype in the sample vd file.
    """
    if os.path.exists(path):
        name = (
            kwargs["name"]
            if "name" in kwargs
            else (
                "Attribute",
                "Commodity",
                "Process",
                "Period",
                "Region",
                "Vintage",
                "TimeSlice",
                "UserConstraint",
                "PV",
            )
        )
        dtype = (
            kwargs["dtype"]
            if "dtype" in kwargs
            else {
                "Attribute": "category",
                "Commodity": "category",
                "Process": str,
                "Period": "category",
                "Region": "category",
                "Vintage": "category",
                "TimeSlice": "category",
                "UserConstraint": "category",
                "PV": float,
            }
        )
        df = pd.read_csv(path, skiprows=(13), names=name, dtype=dtype, index_col=None)
        if "Szenario" in kwargs:
            df["Szenario"] = kwargs["Szenario"]
    else:
        raise "Path incorrect. Please check your path and use absolute path"
    if "masterlist_path" in kwargs:
        print(f"Found masterlist at {kwargs['masterlist_path']}")
        df_master_process = pd.read_excel(kwargs["masterlist_path"], sheet_name="Processes", usecols="B:K")
        try:
            df_master_process["MIMO"].astype("category")
            df_master_process["Category1"].astype("category")
            df_master_process["Category2"].astype("category")
            df_master_process["Category3"].astype("category")
            df_master_process["Category4"].astype("category")
            df_master_process["TechCapUnit"].astype("category")
            df_master_process["TechActUnit"].astype("category")
            df = df.merge(df_master_process, on="Process", how="outer")
        except:
            print(f"Error in parsing masterlist processes")
        try:
            df_master_commodity = pd.read_excel(kwargs["masterlist_path"], sheet_name="Commodities", usecols="B:H")
            df_master_commodity["Commodity"].astype("category")
            df_master_commodity["Commodity_Description"].astype("category")
            df_master_commodity["Com_Sector"].astype("category")
            df_master_commodity["Com_Type1"].astype("category")
            df_master_commodity["Com_Type2"].astype("category")
            df_master_commodity["Com_Type3"].astype("category")
            df_master_commodity["Com_Unit"].astype("category")
            df = df.merge(df_master_commodity, on="Commodity", how="outer")
        except:
            print(f"Error parsing masterlist commodity.")
    else:
        print(f"No masterlist is provided. Please pass Masterlist path in variable 'masterlist_path'. Else continue")
    return df


def vd_multi_read(paths: List[str], *kwargs) -> pd.DataFrame:
    """
    Multiple vd file reader.
    Please pass the value of multi vd files such that the names and dtypes are all same.
    Args:
        paths: List = List of absolute path to the vd files.
        name: Optional[List[str]] = lits of name of columns in each vd file.
        dtypes: Optional[dict[str]] = dict of column name and their data types
    """
    dfs = []
    for path in paths:
        dfs.append(vd_reader(path, **kwargs))
    return pd.concat(dfs)
