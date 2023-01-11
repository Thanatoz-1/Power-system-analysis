import os

class Configurations:
    inp_file = os.path.abspath("./data/8GT_Bal.VD")
    masterlist = os.path.abspath("./data/Masterlist.xlsx")
    variables_sheet_name = "Variables"
    scenario_name = os.path.split(inp_file)[-1].split(".")[0]
    region_list = ["DER", "BW"]
    save_by_region = False