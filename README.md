# MyHedgeFund+

After being able to do fundamental research with MHF, I wanted to try and be able to test common trading strategies (and backtesting them) and figure out the best technical analysis strategies for a particular stock. There are a lot of strategies out there, however after testing on several stocks and tuning the parameters, I decided to look at 4. Introducing, MyHedgeFund+

# What will I be able to see using MHF+

You will be able to do some technical analysis and see how well the company does with the indicator strategies: SMA Crossovers, RSI indicator, MACD indicator and TTM squeeze. You will also be able to back test and see how much money you would have earned, had you used that particular strategy to buy and sell at the points where the graph tells you to do so. Look at sample_website.html to see a preview of this information for the company Square (TICKER: SQ)

# How do I use it

You can download the code on your system and run it from there, or for ease of use, just use this streamlit version of the same: https://share.streamlit.io/adityarathi2000/myhedgefundplus_s/main/main.py

Just download main.py, mhfPlus_functions.py, MHF_Plus_html.py and double-bubble-outline.png. Open main.py and appropriately edit the file path to point to wherever you have downloaded the files to. Additionally, using this tutorial (http://www.automationtestinghub.com/download-chrome-driver/) download the chromedriver for your device, and edit the path for that. This will automatically open the html file when you run the code and act as a dashboard for you to easily view the results!

Then navigate to main.py from terminal and run it (Using python3 main.py). You will be prompted to type in the ticker symbol you are interested in (AAPL, MSFT, CAKE, BABA, etc.), as well as start year and month for the backtesting duration and number of shares you would want to invest per entry and exit of a position. After a few seconds, you should see an html file open up with all the relevant information.

# Disclaimers

This project is still developing. It does not do well with stock splits yet.
