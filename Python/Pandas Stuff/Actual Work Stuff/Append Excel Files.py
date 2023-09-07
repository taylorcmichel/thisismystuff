# This uses Pandas 2.0

import pandas as pd
import glob
import warnings

warnings.simplefilter('ignore')

path = 'base filepath goes here'
filenames = glob.glob(path + "\\*.xlsx")

# for file_elim in os.listdir(path):
#     if file_elim.startswith('~') and file_elim.endswith('.xlsx'):
#         print(file_elim)

excel_list = []

for file in filenames:
    excel_list.append(pd.read_excel(file))

# pd.DataFrame.append() has been deprecated, removed, and replaced with .concat()
excel_merged = pd.concat(excel_list, ignore_index = True)

excel_merged.to_excel(path + 'resulting file name goes here', index = False)
