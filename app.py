import streamlit as st
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import math

def calculate_correlation():

    st.title("Korelasyon Hesapla")

    start_date = st.date_input("Başlangıç Tarihi", None)
    end_date = st.date_input("Bitiş Tarihi", None)

    st.write("Endeks isimleri ile korelasyon bulabilirsiniz ve bu korelasyonların günlük getirilerini hesaplayabilirsiniz.")

    tickers = ['CCOLA.IS', 'XU030.IS', 'SISE.IS', 'THYAO.IS', 'XU100.IS']
    st.write("Girilecek Hisse Sembolleri:", tickers)

    # Add tickers
    new_tickers_str = st.text_input("Hisse ekleyin (hisselerin arasına virgül koyabilirsiniz):")
    remove_tickers = st.text_input("Hisse çıkarın:")
    
    if st.button("Hisseleri Güncelle ve Korelasyon Hesapla"):
        
        if new_tickers_str:
            new_tickers_list = new_tickers_str.split(',')
            new_tickers_set = set(new_tickers_list)
            temp_array = set(tickers)  # Initialize with existing tickers
            for new_ticker in new_tickers_set:
                temp = new_ticker.strip().upper()
                if not temp.endswith(".IS"):
                    temp += ".IS"
                temp_array.add(temp)
            tickers = list(temp_array)
        
        if remove_tickers:
            remove_tickers_list = remove_tickers.split(',')
            remove_tickers_set = set(remove_tickers_list)
            temp_array = set(tickers)
            for new_ticker in remove_tickers_set:
                temp = new_ticker.strip().upper()
                if not temp.endswith(".IS"):
                    temp += ".IS"
                try:
                    temp_array.remove(temp)
                except ValueError:
                    st.write(f"'{remove_tickers}' not found in the list.")
            tickers = list(temp_array)           
        
        st.write("Girilecek Hisse Sembolleri:", tickers)

        if start_date and end_date:
            stock_data = yf.download(tickers, start=start_date, end=end_date)['Adj Close']
            correlation_matrix = stock_data.corr()
            st.title("Matrix Data Display App")
            st.write("Matrix Data:")
            st.table(correlation_matrix)
        else:
            st.write("Lütfen önce bir aralık seçin!")     

def plot_return():

    st.title("Getiri Analizi")

    start_date = st.date_input("Başlangıç Tarihi", None)
    end_date = st.date_input("Bitiş Tarihi", None)

    new_ticker_str = st.text_input("Tek bir hisse ekleyin:")
    stock = None
    if st.button("Getiri Hesapla"):
        stock_symbol = new_ticker_str.strip().upper()
        if not stock_symbol.endswith(".IS"):
            stock_symbol += ".IS"
        stock = stock_symbol
        st.write("Seçilen Hisse:", stock_symbol)
        print(stock)
        stock_data = yf.download(stock, start=start_date, end=end_date)
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
    
        #sürekli getiri
        return_display_continious= math.log(final_price/initial_price)

        # Determine the color based on the value
        continous_color = "green" if return_display_continious >= 0 else "red"
        discrete_color = "green" if return_display_discrete >= 0 else "red"

        continous_percentage = return_display_continious*100
        discrete_percentage = return_display_discrete*100
    
        # Display the value with the determined color
        st.write(f"Sürekli Getiri: <span style='color:{continous_color}'>{continous_percentage:.2f}%</span>", unsafe_allow_html=True)
        st.write(f"Ayrık Getiri: <span style='color:{discrete_color}'>{discrete_percentage:.2f}%</span>", unsafe_allow_html=True)
        

def main():

    tabs = ["Korelasyon Hesaplayıcı", "Getiri Analizi"]
    # Hangi sekmenin seçili olduğunu saklayan değişken
    active_tab = st.radio("İşleminizi seçin:", tabs)
    
    # İlk sekme içeriği
    if active_tab == "Korelasyon Hesaplayıcı":
        calculate_correlation()
    
    # İkinci sekme içeriği
    elif active_tab == "Getiri Analizi":
        plot_return()
        

if __name__ == "__main__":
    main()