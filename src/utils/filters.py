import os
import pandas as pd
from typing import List
from src.utils import get_pylogger

logger = get_pylogger()

__all__ = ["filter_any", "filter", "filter_com", "filter_g"]


def filter_any(df, **kwargs) -> pd.DataFrame:
    """
    Filter the dataframe with keywords as arguments.
    This function can filter the dataframe with arguments and value as list.

    Example:
    filter_any(df, name=["residence","industrial"], region=["bw", "nrw"])
    """
    for arg in kwargs:
        if type(kwargs[arg]) != type([]):
            kwargs[arg] = [kwargs[arg]]
        df = df[df[arg].isin(kwargs[arg])]
    return df


def filter_from_csv(data: pd.DataFrame, path: str) -> pd.DataFrame:
    """
    Apply filter directly from the csv/xls file.
    """
    # Read either the csv or xlsx file and then apply the filters from the file itself.
    if os.path.splitext(path)[-1] == ".csv":
        df = pd.read_csv(path)
    elif os.path.splitext(path)[-1] == ".xlsx":
        df = pd.read_excel(path)
    else:
        print(f"Please check your {os.path.splitext(path)[-1]} path again!")
    kw = {k: [str(i) for i in v.values()] for k, v in df.to_dict().items()}
    df = filter_any(data, **kw)
    return df


def filter(
    df,
    attlist: List = None,
    comlist: List = None,
    processlist: List = None,
    cat1list: List = None,
    cat2list: List = None,
    cat3list: List = None,
    cat4list: List = None,
    sectorlist: List = None,
) -> pd.DataFrame:
    """
    Function to apply filters over the dataframe.
    """
    if attlist != None:
        df = df[df["Attribute"].isin(attlist)]
    if comlist != None:
        df = df[df["Commodity"].isin(comlist)]
    if processlist != None:
        df = df[df["Process"].isin(processlist)]
    if cat1list != None:
        df = df[df["Category1"].isin(cat1list)]
    if cat2list != None:
        df = df[df["Category2"].isin(cat2list)]
    if cat3list != None:
        df = df[df["Category3"].isin(cat3list)]
    if cat4list != None:
        df = df[df["Category4"].isin(cat4list)]
    if sectorlist != None:
        df = df[df["Sector"].isin(sectorlist)]

    df = df.sort_values(by=["Period"])

    df_filter = df

    return df_filter


def filter_com(
    df,
    attlist: List = None,
    comlist: List = None,
    comtype1list: List = None,
    comtype2list: List = None,
    comtype3list: List = None,
    sectorcomlist: List = None,
):
    # Diese Funktion filtert den gesamten, merged Dataframe nach bestimmten Kategorien.
    # So kann genau bestimmt werden, welche Prozesse/Commodities ausgwählt werden sollen
    # Filtern nach den Kategorien der Masterliste|Commodities
    if attlist != None:
        df = df[df["Attribute"].isin(attlist)]
    if comlist != None:
        df = df[df["Commodity"].isin(comlist)]
    if comtype1list != None:
        df = df[df["Com_Type1"].isin(comtype1list)]
    if comtype2list != None:
        df = df[df["Com_Type2"].isin(comtype2list)]
    if comtype3list != None:
        df = df[df["Com_Type3"].isin(comtype3list)]
    if sectorcomlist != None:
        df = df[df["Com_Sector"].isin(sectorcomlist)]

    df = df.sort_values(by=["Period"])

    df_filter = df

    return df_filter


def filter_g(
    df,
    attlist: List = None,
    comlist: List = None,
    processlist: List = None,
    cat1list: List = None,
    cat2list: List = None,
    cat3list: List = None,
    cat4list: List = None,
    sectorlist: List = None,
    comtype1list: List = None,
    comtype2list: List = None,
    comtype3list: List = None,
    sectorcomlist: List = None,
):
    # Diese Funktion filtert den gesamten, merged Dataframe nach bestimmten Kategorien. So kann genau bestimmt werden, welche Prozesse/Commodities ausgwählt werden sollen
    # Filtern nach den Kategorien der Masterliste|Commodities
    if attlist != None:
        df = df[df["Attribute"].isin(attlist)]
    if comlist != None:
        df = df[df["Commodity"].isin(comlist)]
    if processlist != None:
        df = df[df["Process"].isin(processlist)]
    if cat1list != None:
        df = df[df["Category1"].isin(cat1list)]
    if cat2list != None:
        df = df[df["Category2"].isin(cat2list)]
    if cat3list != None:
        df = df[df["Category3"].isin(cat3list)]
    if cat4list != None:
        df = df[df["Category4"].isin(cat4list)]
    if sectorlist != None:
        df = df[df["Sector"].isin(sectorlist)]
    if comtype1list != None:
        df = df[df["Com_Type1"].isin(comtype1list)]
    if comtype2list != None:
        df = df[df["Com_Type2"].isin(comtype2list)]
    if comtype3list != None:
        df = df[df["Com_Type3"].isin(comtype3list)]
    if sectorcomlist != None:
        df = df[df["Com_Sector"].isin(sectorcomlist)]

    df = df.sort_values(by=["Period"])

    df_filter = df

    return df_filter
