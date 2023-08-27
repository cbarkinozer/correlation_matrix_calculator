import streamlit as st
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import math


tickers = ['CCOLA.IS', 'XU030.IS', 'SISE.IS', 'THYAO.IS', 'XU100.IS']
start_date = None
end_date = None

def calculate_correlation(tickers, start_date, end_date):

    st.title("Calculate Correlation")
    st.write("Endeks isimleri ile de  korelasyon bulunabilineceği ve bu korelasyonların günlük getiriler ile hesaplanır(Kullanım yönergesi).")
    
    # Add tickers
    new_tickers_str = st.text_input("Hisse ekleyin (hisselerin arasına virgül koyabilirsiniz):")
    if st.button("Hisse Ekle"):
        if new_tickers_str:
            new_tickers_list = new_tickers_str.split(',')
            new_tickers_set = set(new_tickers_list)
            temp_array = set(tickers)  # Initialize with existing tickers
            for new_ticker in new_tickers_set:
                temp = new_ticker.strip().upper()
                if not temp.endswith(".IS"):
                    temp += ".IS"
                temp_array.add(temp)
            tickers = list(temp_array)  # Convert set back to list

    # Remove tickers
    remove_tickers = st.text_input("Hisse çıkarın:")
    if st.button("Hisse Çıkar"):
        if remove_tickers:
            try:
                tickers.remove(remove_tickers)
            except ValueError:
                st.write(f"'{remove_tickers}' not found in the list.")
    
    st.write("Girilen Ticker Sembolleri:", tickers)

    start_date = st.date_input("Başlangıç Tarihi", None)
    end_date = st.date_input("Bitiş Tarihi", None)

    # Calculate Correlation
    if st.button("Korelasyonu Hesapla"):
        if start_date and end_date:
            stock_data = yf.download(tickers, start=start_date, end=end_date)['Adj Close']
            correlation_matrix = stock_data.corr()
            st.title("Matrix Data Display App")
            st.write("Matrix Data:")
            st.table(correlation_matrix)
        else:
            st.write("Lütfen önce bir aralık seçin!")

def plot_return(stock_symbol, start_date, end_date):

    st.title("Plot Return")
    stock_data = yf.download(stock_symbol, start=start_date, end=end_date)
    
    # Veri çerçevesini kullanarak fiyat grafiğini çizin
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data['Close'])
    plt.title(f"{stock_symbol} Hisse Senedi Fiyatı")
    plt.xlabel("Tarih")
    plt.ylabel("Fiyat")
    plt.grid()
    plt.show()

    st.pyplot(plt.gcf())

    # Getiri hesaplamak için günlük fiyatları kullanın
    daily_returns = stock_data['Close'].pct_change()
    
    # Getiri grafiğini çizin
    plt.figure(figsize=(10, 6))
    plt.plot(daily_returns)
    plt.title(f"{stock_symbol} Hisse Senedi Günlük Getirileri")
    plt.xlabel("Tarih")
    plt.ylabel("Getiri")
    plt.grid()
    plt.show()

    st.pyplot(plt.gcf())
    
    # En son gösterilecek return
    initial_price = stock_data['Adj Close'][0]
    final_price = stock_data['Adj Close'][-1]
    
    #ayrık getiri
    return_display_discrete= (final_price/initial_price - 1)

    st.write("Ayrık Getiri", return_display_discrete)
    
    #sürekli getiri
    return_display_continious= math.log(final_price/initial_price)
    st.write("Sürekli Getiri", return_display_continious)

def main():
    global tickers
    global start_date
    global end_date

    tabs = ["Korelasyon Hesapla", "Plot Returns"]
    active_tab = st.radio("İşleminizi seçin:", tabs)
    if active_tab == "Korelasyon Hesapla":
        calculate_correlation(tickers, start_date, end_date)
    elif active_tab == "Plot Returns":
        plot_return(tickers, start_date, end_date)

if __name__ == "__main__":
    main()