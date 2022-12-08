import pandas as pd


def get_config(dataframe: pd.DataFrame):
    """
    Function to generate configuration files from the dataframe.
    """
    columns = dataframe.columns  # Read columns and create config file
    config = {}
    for i in range(len(dataframe)):  # For all the values in dataframe, read non-empty vales and split.
        p = dataframe.iloc[i]
        config[p[columns[0]]] = {}
        if "name" not in columns or "Name" not in columns:  # Create name if name of column name is not given
            config[p[columns[0]]]["Name"] = "|".join(str(p[columns[0]]).split("_"))

        for col in columns[1:]:
            if (col == "name" or col == "Name") and config[p[columns[0]]].get("Name"):
                if pd.isnull(p[col]):
                    config[p[columns[0]]]["Name"] = "|".join(str(p[columns[0]]).split("_"))
                else:
                    config[p[columns[0]]]["Name"] = str(p[col])
                continue
            if not pd.isnull(p[col]):
                config[p[columns[0]]][col] = str(p[col]).split(",")

    return config
