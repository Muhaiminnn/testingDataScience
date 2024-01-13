import subprocess

# Jalankan perintah instalasi dependensi
subprocess.call(['pip', 'install', '-r', 'requirements.txt'])

import streamlit as st
import gspread

spreadsheet_key = '1T90XmDuGPtkPtQwC2b1Yt0e5cJiPNfgPcSGvMfLEtDk'
worksheet_name = 'dailybrentoil'
gc = gspread.service_account()

sh = gc.open_by_key(spreadsheet_key)
worksheet = spreadsheet.worksheet(worksheet_name)
# Ambil data
data = worksheet.get_all_records()

def main():
    st.title("Prediksi Harga Minyak Dunia By Muhaimin\n Mini Project Data Scientist Kalla")
    st.table(data)

if __name__ == '__main__':
    main()
