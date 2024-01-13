import subprocess

# Jalankan perintah instalasi dependensi
subprocess.call(['pip', 'install', '-r', 'requirements.txt'])

import streamlit as st
import pandas as pd
import numpy as np

from matplotlib import pyplot as plt
import seaborn as sns
%matplotlib inline

import zipfile

from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import GridSearchCV, train_test_split, cross_val_score
from sklearn.metrics import mean_squared_error
from sklearn.impute import SimpleImputer

from sklearn.svm import SVR
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.neighbors import KNeighborsRegressor

spreadsheet_link = 'https://docs.google.com/spreadsheets/d/1T90XmDuGPtkPtQwC2b1Yt0e5cJiPNfgPcSGvMfLEtDk/edit?usp=sharing'

# Buka spreadsheet menggunakan tautan
sh = gspread.open_by_url(spreadsheet_link)
worksheet_name = 'dailybrentoil'
worksheet = sh.worksheet(worksheet_name)

# Ambil data
data = worksheet.get_all_records()

def main():
    st.title("Prediksi Harga Minyak Dunia By Muhaimin\n Mini Project Data Scientist Kalla")
    st.table(data)

if __name__ == '__main__':
    main()
