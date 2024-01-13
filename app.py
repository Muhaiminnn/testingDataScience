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
data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)

plt.figure(figsize=(12, 6))
plt.plot(data['Open'], label='Open Price')
plt.title('Harga Open over Time')
plt.xlabel('Tanggal')
plt.ylabel('Harga Open')
plt.legend()
plt.show()

def main():
    st.title("Mini Project Prediksi Harga Minyak Dunia By Muhaimin")
    #st.table(data)
    st.write("Deskripsi Data")
    st.write(data.describe())
    st.pyplot(plt)

if __name__ == '__main__':
    main()
