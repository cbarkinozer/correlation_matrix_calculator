import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import math

# Hisse senedi sembolü ve zaman aralığı
stock_symbol = "GARAN.IS"  # Örnek olarak Garanti Bankası'nın sembolü
start_date = "2020-01-01"
end_date = "2023-01-01"

# Yahoo Finance'den hisse senedi verilerini alın
stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

# Veri çerçevesini kullanarak fiyat grafiğini çizin
plt.figure(figsize=(10, 6))
plt.plot(stock_data['Close'])
plt.title(f"{stock_symbol} Hisse Senedi Fiyatı")
plt.xlabel("Tarih")
plt.ylabel("Fiyat")
plt.grid()
plt.show()

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

#En son gösterilecek return
initial_price = stock_data['Adj Close'][0]
final_price = stock_data['Adj Close'][-1]

#ayrık getiri
return_display_discrete= (final_price/initial_price - 1)
print(return_display_discrete)
#sürekli getiri
return_display_continious= math.log(final_price/initial_price)
print(return_display_continious)