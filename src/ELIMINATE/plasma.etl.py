import pandas as np
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os as os

# reading in data
wd = os.getcwd()
plasmaCollectDF = pd.read_csv(wd + "/data/ELIMINATE/20230207_ELIMINATE_plasmacollection_fixed.csv")
plasmaCollectDF.info()
plasmaCollectDF.iloc[0:10, :]

plasmaVialDF = pd.read_csv(wd + "/data/ELIMINATE/230209_ELIMINATE_plasmavial_cleaned.csv")
plasmaVialDF.info()
plasmaVialDF.head()
plasmaVialDF.loc[0:10, ['patient_id', 'plasma_vial_specimen_id', 'plasma_tube_loc', 'redcap_repeat_instance']]
plasmaVialDF.loc[0:10, ['patient_id', 'plasma_vial_specimen_id', 'plasma_box_no', 'redcap_repeat_instance']]



print(wd + "/data")