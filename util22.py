
# coding: utf-8

# In[37]:

# this file contains the custom functions to finish repeat trivial tasks.
import pandas as pd
import numpy as np
from datetime import datetime
# this function will give the major version of the dota2 game patch for given date

# the version table is imported from http://dota2.gamepedia.com/Game_Versions 
# by Microsoft Excel for convenience. 
version_table = pd.read_csv('dataset/Versions.csv')
# only keep the major patches.
major_table = version_table.loc[version_table['Patch Date'].map(str).map(len) > 6 ]
major_table = major_table.loc[major_table['Version'].map(str).map(len) <= 4]
major_table['Patch Date'] = major_table['Patch Date'].map(str).map(lambda x: datetime.strptime(x, '%m/%d/%Y'))

def version(date):
    # date: string in forms like "14 May 2017"
    # return: string, the version of the date
    
    # transform date string into datetime
    date = datetime.strptime(date, '%d %b %Y')

    # if current version release date is newer than given date, move to next version.
    i = 0
    dlst = major_table['Patch Date'].tolist()
    vlst = major_table['Version'].tolist()
    while i < len(dlst):
        if dlst[i] > date:
            i += 1
        else:
            break
    # return the version
    return vlst[i]

## test
#print (version('14 May 2017'))

            


# In[35]:




# In[ ]:



