import streamlit as st
import yfinance as yf



def calculate_correlation():
    st.title("Korelasyon Hesaplayıcı")
    st.write("Endeks isimleri ile de  korelasyon bulunabilineceği ve bu korelasyonların günlük getiriler ile hesaplanır(Kullanım yönergesi).")
    tickers = ['CCOLA.IS', 'XU030.IS', 'SISE.IS', 'THYAO.IS', 'XU100.IS']

    new_tickers = st.text_input("Hisse ekleyin:")
    if new_tickers:
        new_tickers = new_tickers.split(',')

    tickers.extend(new_tickers)
    st.write("Girilen Ticker Sembolleri:", tickers)

    print(tickers)


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

def calculate_return():
    st.title("Getiri Hesaplayıcı")
    st.write("Calculate the return:")

tabs = ["Korelasyon Hesaplayıcı", "Çoklu Stok Hesaplayıcı"]
# Hangi sekmenin seçili olduğunu saklayan değişken
active_tab = st.radio("İşleminizi seçin:", tabs)

# İlk sekme içeriği
if active_tab == "Korelasyon Hesaplayıcı":
    calculate_correlation()

# İkinci sekme içeriği
elif active_tab == "Çoklu Stok Hesaplayıcı":
    calculate_return()