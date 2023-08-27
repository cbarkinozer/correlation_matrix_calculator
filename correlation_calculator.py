import yfinance as yf
import streamlit as st


def calculate_correlation():
    st.title("Korelasyon Hesaplayıcı")
    st.write("Endeks isimleri ile de  korelasyon bulunabilineceği ve bu korelasyonların günlük getiriler ile hesaplanır(Kullanım yönergesi).")
    tickers = ['CCOLA.IS', 'XU030.IS', 'SISE.IS', 'THYAO.IS', 'XU100.IS']
    st.write("Seçilen Ticker Sembolleri:", tickers)
    
    tickers_string = st.text_input("Ticker Sembolleri (Virgülle Ayırın):")

    if tickers_string:
        entered_tickers = tickers_string.split(',')
        entered_tickers = [ticker.strip().upper() for ticker in entered_tickers]
        st.write("Girilen Ticker Sembolleri:", entered_tickers)

        

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
    
    