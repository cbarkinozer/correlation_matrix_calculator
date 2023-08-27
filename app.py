import streamlit as st
from correlation_calculator import calculate_correlation
from return_calculator import calculate_return


tabs = ["Korelasyon Hesaplayıcı", "Çoklu Stok Hesaplayıcı"]
# Hangi sekmenin seçili olduğunu saklayan değişken
active_tab = st.radio("İşleminizi seçin:", tabs)

# İlk sekme içeriği
if active_tab == "Korelasyon Hesaplayıcı":
    calculate_correlation()

# İkinci sekme içeriği
elif active_tab == "Çoklu Stok Hesaplayıcı":
    calculate_return()
