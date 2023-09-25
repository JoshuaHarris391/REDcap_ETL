# Load packages
import pandas as pd
import numpy as np
import os
import plotly_express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
import seaborn as sns
import matplotlib.pyplot as plt

# Getting wd
os.getcwd()
# Reading in clinical data
clinDF = pd.read_csv("data/ELIMINATE/NEW_ELIMINATE_Data_22jun22_30.csv")

# basic stats for age
type(clinDF)
vars(clinDF)
dir(clinDF)
colnames = clinDF.columns.tolist
print(colnames)
clinDF.dtypes
clinDF.iloc[1:10, ]

# Getting age
clinDFAgeDF = clinDF[['age_diagnosis']]
clinDFAgeDF.info()
type(clinDFAgeDF)
clinDFAgeDF.shape
clinDFAgeDF.dtypes

clinDFAgeVec = clinDF['age_diagnosis']
type(clinDFAgeVec)
clinDFAgeVec.shape
clinDFAgeVec[1]

clinDFAgeVec.info()

np.ndim(clinDFAgeVec)
# basic stats
clinDFAgeVec.mean()
np.mean(clinDFAgeVec)
clinDFAgeVec.std()
clinDFAgeVecDensPlot = px.density_contour(clinDFAgeDF, x="age_diagnosis)
clinDFAgeVecDensPlot.show()

# Investigating surgery_histo_grade
surgHistDF = clinDF.loc[:, 'surgery_histo_grade']
type(surgHistDF)
surgHistDF.shape
np.ndim(surgHistDF)
# getting summary
pd.value_counts(surgHistDF)



# Creating density plot
surgHistDensity = px.histogram(clinDF, x="age_diagnosis")
surgHistDensity.show()

sns.kdeplot(clinDF, x="age_diagnosis", hue="res_cancer_burden_class", fill=True, common_norm=False, palette="crest",
   alpha=.5, linewidth=0)
