import os
import numpy as np
import pandas as pd

from src.utils import vd_reader
from src.framework.varclass import SingleVar as single_var
from src.utils import get_config, filter_any
from src.utils.pylogger import get_pylogger
from tqdm import tqdm
from config import Configurations

logger = get_pylogger(__name__)


logger.debug("Reading VD file and the Master list")
data = vd_reader(path=Configurations.inp_file, masterlist_path=Configurations.masterlist)
d = pd.read_excel(Configurations.masterlist, sheet_name=Configurations.variables_sheet_name)

# Perform all the checks on the data here and log the output.
duplicates = d[d.duplicated()]
if len(duplicates)>0:
    # As index in excel starts from 1 and first row is header, do i-2
    logger.warning(f"Some duplicated values are found at index: {[i-2 for i in duplicates.index]}") 
config = get_config(d)  ## This generates the dict from the variable files in masterlist.

output = {}
for k, v in tqdm(config.items()):
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
        # empty = pd.DataFrame({"":[code]+[""]*(len(output[k]["output"])-1)})
        # output[k]["output"] = pd.concat([empty, output[k]["output"]])
    else:
        logging.error(f"{req_class} not implemented. Skipping {k}")

# for k in output.keys():
#     print(output[k]["output"])
#     print("-" * 80)
if Configurations.save_by_region: #order_by_region:
    writer = pd.ExcelWriter("output.xlsx", engine="xlsxwriter")
    out = pd.concat([output[i]["output"] for i in output.keys()])
    for reg in out.Region.unique():
        sheet = f"{reg}"
        saving = out[out.Region==f"{reg}"]
        offset = 0
        saving.to_excel(writer, sheet_name=sheet, startrow=offset, index=None)
    writer.save()
else:
    writer = pd.ExcelWriter("output.xlsx", engine="xlsxwriter")
    sheet = "some_sheet"
    offset = 0
    pd.concat([output[i]["output"] for i in output.keys()]).to_excel(writer, sheet_name=sheet, startrow=offset, index=None)
    writer.save()
# for key in output.keys():
#     for code in output[k]['config']['code']:
# #         output[k]["output"].insert(0, "code", code*len(output[k]["output"]))
#         output[key]["output"].to_excel(writer, sheet_name=sheet, startrow=offset, index=None)
#         worksheet = writer.sheets[sheet]
# #         worksheet.write_string(0, 1, 'Your text here')
#     offset += len(output[key])+1
