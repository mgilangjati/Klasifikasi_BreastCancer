import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('BreastCancer.sav', 'rb'))

st.title('Prediksi Penyakit Kanker Payudara')
c1, c2, c3 = st.columns(3)

with c1:
    Age = st.number_input('Umur Pasien')
    T_Stage = st.number_input('Tahap T (Ukuran Tumor)')
    differentiate = st.number_input('Perbedaan Tumor')
    Tumor_Size = st.number_input('Ukuran Tumor Pasien (mm)')
    Survival_Months = st.number_input('Berapa Bulan Pasien Bertahan Hidup')

with c2:
    Race = st.number_input('Ras Pasien')
    N_Stage = st.number_input('Tahap N (Kanker Menyebar)')
    Grade = st.number_input('Nilai Tumor')
    Estrogen_Status = st.number_input('Status Estrogen')

with c3:
    Marital_Status = st.number_input('Status Pasien dengan Pasangan')
    The_6th_Stage = st.number_input('Tahap Pengelmpokan Kanker Pasien')
    A_Stage = st.number_input('Regional or Distant')
    Progesterone_Status = st.number_input('Status Progesteron')

prediksi = ''
if st.button('Hasil Prediksi'):
    prediksi = model.predict([[Age, Race, Marital_Status, T_Stage, N_Stage,
                               The_6th_Stage, differentiate, Grade, A_Stage, Tumor_Size,
                               Estrogen_Status, Progesterone_Status, Survival_Months]])

    if (prediksi [0] == 1):
        prediksi = ('Pasien meninggal dunia')
    else:
        prediksi = ('Pasien tidak meninggal dunia')
st.success(prediksi)