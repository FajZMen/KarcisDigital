import streamlit as st
from datetime import datetime

def hitungmotor(jammasuk, jamkeluar):
    masuk = datetime.combine(datetime.today(), jammasuk)
    keluar = datetime.combine(datetime.today(), jamkeluar)
    durasi = (keluar - masuk).total_seconds() / 3600
    
    if durasi <= 1:
        harga = 3000
    elif durasi <= 2:
        harga = 4000
    else:
        harga = 5000
    st.write(f"Total Biaya: {harga} Rp.")
    return harga

def hitungmobil(jammasuk, jamkeluar):
    masuk = datetime.combine(datetime.today(), jammasuk)
    keluar = datetime.combine(datetime.today(), jamkeluar)
    durasi = (keluar - masuk).total_seconds() / 3600
    
    if durasi <= 1:
        harga = 4000
    elif durasi <= 2:
        harga = 5000
    else:
        harga = 6000
    st.write(f"Total Biaya: {harga} Rp.")
    return harga

def karcis(karcisid, jenis, platno, jammasuk, jamkeluar):
    st.write("ID Karcis : ", karcisid)
    st.write("Jenis Kendaraan : ", jenis)
    st.write("Plat Nomor Kendaraan : ", platno)
    st.write("Jam Masuk Kendaraan : ", jammasuk)
    st.write("Jam Keluar Kendaraan : ", jamkeluar)