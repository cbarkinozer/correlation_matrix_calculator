import yfinance as yf
import streamlit as st


def calculate_correlation():
    st.title("Korelasyon Hesaplayıcı")
    st.write("Endeks isimleri ile de  korelasyon bulunabilineceği ve bu korelasyonların günlük getiriler ile hesaplanır(Kullanım yönergesi).")
    tickers = ['CCOLA.IS', 'XU030.IS', 'SISE.IS', 'THYAO.IS', 'XU100.IS']

    start_date = st.date_input("Başlangıç Tarihi", None)
    end_date = st.date_input("Bitiş Tarihi", None)

    if st.button("Korelasyonu Hesapla"):
        if start_date and end_date:
            stock_data = yf.download(tickers, start=start_date, end=end_date)['Adj Close']
            correlation_matrix = stock_data.corr()
            st.title("Matrix Data Display App")
            st.write("Matrix Data:")
            st.table(correlation_matrix)
        else:
            st.write("Lütfen önce bir aralık seçin!")
    
    