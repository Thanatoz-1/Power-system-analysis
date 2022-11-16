from typing import List

__all__ = ["Filter", "Filter_com", "Filter_g"]


def Filter(
    df,
    attlist: List = None,
    comlist: List = None,
    processlist: List = None,
    cat1list: List = None,
    cat2list: List = None,
    cat3list: List = None,
    cat4list: List = None,
    sectorlist: List = None,
):
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


def Filter_com(
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


def Filter_g(
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
