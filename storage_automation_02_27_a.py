from sys import *
from openpyxl import *
import xlsxwriter
import os
import pandas as pd
import numpy as np

###READ ME
### Takes two arguements the Orphans spreadsheet and the Shares
###TODO add type for mfts or SUB
orphans = argv [1] 
shares = argv [2]
report_type = argv [3] #mfts or sub                                                                                                                                                                                                                                          


if report_type == "sub":
    df_share = pd.read_excel(shares)
    shares_mod = (df_share[['blocks','last_accessed','path']])
    writer = pd.ExcelWriter('analysis.xlsx', engine='xlsxwriter')
    shares_mod.to_excel(writer, sheet_name='shares_mod')
    
    df_orphan = pd.read_excel(orphans)
    df_orphan.to_excel(writer, sheet_name='orphans')
    
    merged = [shares_mod,df_orphan]
    df_merged = pd.DataFrame()
    for f in merged:
        df_merged = df_merged.append(f)
    
    b_sum =0
    for b in df_merged['blocks']:
        b_sum = b_sum + b
    #bsum = total sum for blocks
    df_merged['percentage'] = df_merged['blocks']* 100 / b_sum
    
    df_merged.to_excel(writer, sheet_name='merged')
    df_trim_pct = pd.DataFrame()
    df_trim_pct = df_merged[df_merged['percentage'] > 2.5]
    
    df_trim_pct.to_excel(writer,sheet_name='trim_percent')    
    
    i=0
    for pat in df_trim_pct['path']:
        #num=  (len(df_trim_pct))
        i = i+1    
        if ("SAS") in pat:
            int_sas = (int((df_trim_pct.path[df_trim_pct.path == pat].index.values)))
            df_trim_pct.set_value(int_sas,'group','SAS')
        elif ("venner") in pat:
            int_v = (int((df_trim_pct.path[df_trim_pct.path == pat].index.values)))
            df_trim_pct.set_value(int_v,'group','venner')
        elif ("TCRB") in pat:
            int_tcrb = (int((df_trim_pct.path[df_trim_pct.path == pat].index.values)))
            df_trim_pct.set_value(int_tcrb,'group','TCRB')
        elif ("CAfGEN") in pat:
            int_Caf = (int((df_trim_pct.path[df_trim_pct.path == pat].index.values)))
            df_trim_pct.set_value(int_Caf,'group','Cafv')
        else:
            print ("----------------------")
            print (pat +  " was not found")
            custom = input('Please enter group to assign to value:  ')
            int_custom = (int((df_trim_pct.path[df_trim_pct.path == pat].index.values)))
            df_trim_pct.set_value(int_custom,'group',custom)
    df_trim_pct_group = pd.DataFrame()
    df_trim_pct_group = df_trim_pct
    df_trim_pct_group.to_excel(writer,sheet_name='groups')    
    
    writer.save()
    print (df_trim_pct_group)
else:
    print ("dam")



