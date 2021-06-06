import glob 
import pandas as pd

path_to_excel_files = glob.glob('*.xlsx')
for excel in path_to_excel_files:
 out = excel.split('.')[0]+'.csv'
 df = pd.read_excel(excel)
 df.to_csv(out, index=False) 