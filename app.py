import subprocess

# Jalankan perintah instalasi dependensi
subprocess.call(['pip', 'install', '-r', 'requirements.txt'])

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('dailybrentoil.csv')
kolom_yang_dihapus = ['Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9']
data = data.drop(kolom_yang_dihapus, axis=1)

def create_plot():
    numerical_col = [col for col in data.columns if data[col].dtypes == 'float64']
    plt.subplots(figsize=(10,7))
    sns.boxplot(data=data[numerical_col]).set_title("Gold Price")
    plt.show()
    return plt

def main():
    st.title("Prediksi Harga Minyak Dunia By Muhaimin\n Mini Project Data Scientist Kalla")
    #st.table(data)
    st.pyplot(create_plot())

if __name__ == '__main__':
    main()
