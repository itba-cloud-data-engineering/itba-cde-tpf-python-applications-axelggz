from mplfinance.original_flavor import candlestick2_ohlc
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def stockPlot(symbolData, title):
    fig, ax = plt.subplots()
    candlestick2_ohlc(ax, symbolData['Open'], symbolData['High'], symbolData['Low'], symbolData['Close'], width=0.6)

    xdate = symbolData['Time']

    ax.xaxis.set_major_locator(ticker.MaxNLocator(6))

    def mydate(x,pos):
        try:
            return xdate[int(x)]
        except IndexError:
            return ''

    ax.xaxis.set_major_formatter(ticker.FuncFormatter(mydate))

    fig.autofmt_xdate()
    fig.tight_layout()
    fig.set_size_inches(12.5, 10.5)

    plt.title(title)
    plt.xlabel("Fecha")
    plt.ylabel("Stock")
   
    import os; print(os.listdir())
    plt.savefig(f'./dags/Tasks/Exports/{title}.png')