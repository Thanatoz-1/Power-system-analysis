import os
import numpy as np
import pandas as pd

from src.utils import vd_reader
from src.framework.varclass import SingleVar as single_var
from src.utils import get_config, filter_any


class Configurations:
    inp_file = os.path.abspath("./data/8GT_Bal.VD")
    masterlist = os.path.abspath("./data/Masterlist.xlsx")
    scenario_name = os.path.split(inp_file)[-1].split(".")[0]
    region_list = ["DER", "BW"]


data = vd_reader(path=Configurations.inp_file, masterlist_path=Configurations.masterlist)
d = pd.read_excel(Configurations.masterlist, sheet_name="Variables")

config = get_config(d)  ## This generates the dict fro the variable files in masterlist.

output = {}
for k, v in config.items():
    output[k] = {}
    var_name = v.pop("Name")  # The name is generated in the config file.
    unit = v.pop("Unit")[0]  # The unit also has to be scalar as it is not supported by single_var class for now.
    req_class = v.pop("Class")[0]  # This means that the class cannot be multiple
    code = v.pop("Code")  # Code to be used later on for arrangement.
    filtered_data = filter_any(data, **v)
    if req_class == "single_var":
        output[k]["raw"] = filtered_data
        output[k]["output"] = single_var(
            template=False, var_name=var_name, unit=unit, df_rawdata=filtered_data
        ).results
    else:
        print(f"{req_class} not implemented. Skipping {k}")

for k in output.keys():
    print(output[k]["output"])
    print("-" * 80)
