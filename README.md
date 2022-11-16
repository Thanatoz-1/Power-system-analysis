# Power-system-analysis

Natural language VD file processing library for Energy data.
This library automates the process of contribution and analysis of VD files and based on the master list generates the output graphs and figures for analysis.


<!-- Calculate the input and output and also calculate the percent contribution of input to individual outputs. -->

```bash
pat --input file/path.VD --masterlist file/path.xlsx --unit PJ/yr --filters
```

Python equivalent

```python
FinalEnergy_Residential_WaterHeating_Coal = single_var(
            template = False,  # 
            var_name= "Final Energy|Residential|Water Heating|Coal",
            unit ="PJ/yr", 
            df_rawdata = Filter(
                            df = df_region_filt,
                            attlist = ["VAR_FIn"],
                            comlist = ["RSDCOA"],
                            processlist = None,
                            cat1list = ['Warmwater'],
                            cat2list = None,
                            cat3list = None,
                            cat4list=None,
                            sectorlist = ["Residential"]
                            )
            )
```