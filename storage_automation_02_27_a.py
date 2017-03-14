from sys import *
from openpyxl import *
import xlsxwriter
import os
import pandas as pd
import numpy as np


orphans = argv [1]
shares = argv [2]
#report_type = argv [3] #mfts or sub                                                                                                                                                                                                                                          

#excel_names = [orphans,shares] here made a list of the spreadsheets]
#df_share.rename(columns={persons: people})
#shares_mod.to_excel(shares_new)   ###attempt at trying to save to an excel 
#print (df_share.columns)

df_share = pd.read_excel(shares)
shares_mod = (df_share[['blocks','last_accessed','path']])
#writer = pd.ExcelWriter('analysis.xlsx', engine='xlsxwriter')
#shares_mod.to_excel(writer, sheet_name='shares_mod')

df_orphan = pd.read_excel(orphans)
#df_orphan.to_excel(writer, sheet_name='orphans')

merged = [shares_mod,df_orphan]
df_merged = pd.DataFrame()
for f in merged:
    df_merged = df_merged.append(f)

b_sum =0
for b in df_merged['blocks']:
    b_sum = b_sum + b
#bsum = total sum for blocks
df_merged['percentage'] = df_merged['blocks']* 100 / b_sum
#print (df_merged)
#df_merged.to_excel(writer, sheet_name='merged')
df_trim_pct = pd.DataFrame()
df_trim_pct = df_merged[df_merged['percentage'] > 2.5]
#print (df_trim_pct)
#df_trim_pct.to_excel(writer,sheet_name='trim_percent')    

for path in df_trim_pct['path']:
    path_s (str(path))
    if ("SAS") in path_s:
        print ("True")
        df_trim_pct['group'] = ("SAS")
    else:
        df_trim_pct['group'] = ("NA")
        print ("False")
#print (df_trim_pct['group'])













#writer.save()


