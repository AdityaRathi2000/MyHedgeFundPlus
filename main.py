import datetime as dt
import matplotlib.pyplot as plt
import mhfPlus_functions as mhf_f
import MHF_Plus_html as mhf_html
from selenium import webdriver


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ######################################## EDIT THIS SECTION - START ########################################
    filePath = "file:////Users/adityarathi/PycharmProjects/MHFPlus/index.html" # WHERE INDEX.HTML IS SAVED
    chromedriver_path = "/Users/adityarathi/Documents/chromedriver"  # WHERE CHROME DRIVER IS SAVED
    ######################################## EDIT THIS SECTION - END ########################################
    filePath_no_idx = filePath.split('index.html')[0]
    figx = 25
    figy = 10
    var = input("Please enter ticker symbol of company you are interested in: ")
    watchList = [var]
    start_year = int(input("Please enter start year: "))
    start_month = int(input("Please enter start month: "))
    num_trades = int(input("# of Shares to buy/sell per trade: "))

    for i in watchList:
        defined_df = mhf_f.get_data_df(i, start_year, start_month)

        plt.figure(figsize=(figx, figy))
        s, b, shares_bought_SMA, shares_sold_SMA, net_SMA = mhf_f.sma_crossover(i, defined_df, 6, 20, num_trades, start_year, start_month);

        plt.figure(figsize=(figx, figy))
        s_rsi, b_rsi, shares_bought_RSI, shares_sold_RSI, net_RSI = mhf_f.rsi_stoch(i, defined_df, 10, 40, num_trades, start_year, start_month)

        plt.figure(figsize=(figx, figy))
        l, s, h, smooth, shares_bought_MACD, shares_sold_MACD, net_MACD = mhf_f.macd_analysis(i, defined_df, 12, 9, 26, 2, num_trades, start_year, start_month);

        plt.figure(figsize=(figx, figy))
        squeeze, std, sma_ema, multi, smooth, shares_bought_TTM, shares_sold_TTM, net_TTM = mhf_f.ttm_squeeze_indicator(i, defined_df, 20, 20, 2, 2, num_trades, start_year, start_month)

    webpage_data = mhf_html.start_html()
    webpage_data += mhf_html.style()

    webpage_data += mhf_html.print_html("<Center><h1> Welcome to MyHedgeFund+ </h1></Center>".format(mhf_html.print_html_bold(watchList[0])))
    webpage_data += mhf_html.print_html("<Center><p> You are now looking at some backtesting algorithms for ticker symbol <r>{}</r> \n</p></Center>".format(mhf_html.print_html_bold(watchList[0])))


    analysis_graph = ["SMA Crossover Stoch", "RSI Stoch", "MACD", "TTM Squeeze"]
    read_more_list = ["https://www.investopedia.com/terms/c/crossover.asp#:~:text=Moving%20averages%20can%20determine%20a,or%20a%20breakout%20or%20breakdown.",
                      "https://www.investopedia.com/terms/s/stochrsi.asp#:~:text=The%20Stochastic%20RSI%20(StochRSI)%20is,than%20to%20standard%20price%20data.",
                      "https://www.investopedia.com/terms/m/macd.asp",
                      "https://www.investopedia.com/articles/technical/04/030304.asp"]
    net_list = [round(net_SMA,2), round(net_RSI,2), round(net_MACD,2), round(net_TTM,2)]
    shares_bought_list = [shares_bought_SMA, shares_bought_RSI, shares_bought_MACD, shares_bought_TTM]
    shares_sold_list = [shares_sold_SMA, shares_sold_RSI, shares_sold_MACD, shares_sold_TTM]

    for i in range(len(analysis_graph)):
        webpage_data += mhf_html.print_html("<div id='graph'>")
        #webpage_data += mhf_html.print_html("{} (Read more <a href = '{}' target='_blank'>here</a> )".format(mhf_html.print_html_bold(analysis_graph[i]), mhf_html.print_html_bold(read_more_list[i])))
        if (net_list[i] > 0):
            webpage_data += mhf_html.print_html("Net made from strategy: <Strong><g>${}</g></Strong>, with {} shares bought and {} shares sold in {} days ({} to {})".format(
                                                net_list[i], shares_bought_list[i], shares_sold_list[i],
                                                (dt.datetime.now() - dt.datetime(start_year, start_month, 1)).days,
                                                dt.datetime(start_year, start_month, 1).date(), dt.datetime.now().date()))
        else:
            webpage_data += mhf_html.print_html("Net made from strategy: <Strong><r>-${}</r></Strong>, with {} shares bought and {} shares sold in {} days ({} to {})".format(
                                                abs(net_list[i]), shares_bought_list[i], shares_sold_list[i],
                                                (dt.datetime.now() - dt.datetime(start_year, start_month, 1)).days,
                                                dt.datetime(start_year, start_month, 1).date(), dt.datetime.now().date()))

        webpage_data += mhf_html.graph_imgs(analysis_graph[i], watchList[0], 1200, 480, filePath_no_idx)
        webpage_data += mhf_html.print_html("<br>")
        webpage_data += mhf_html.print_html("</div>")

    webpage_data += mhf_html.end_html()
    with open('index.html', 'w') as fd:
        fd.write(webpage_data)

    driver = webdriver.Chrome(executable_path=chromedriver_path)
    driver.get(filePath)
