import requests
from twilio.rest import Client


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

ALPHAVANTAGE_API_KEY = ""
NEWS_API_KEY = ""

# Twilio details
account_sid = ""
auth_token = ""

    ## https://www.alphavantage.co/documentation/#dailyadj
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then get the most three recent articles.

# Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol" : STOCK_NAME,
    "apikey": ALPHAVANTAGE_API_KEY,
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
data = response.json()
yersterday_stock_price = float(data["Time Series (Daily)"]["2023-01-12"]["4. close"])
print(yersterday_stock_price)

#Get the day before yesterday's closing stock price
day_before_yesterday_stock_price = float(data["Time Series (Daily)"]["2023-01-13"]["4. close"])
print(day_before_yesterday_stock_price)

#Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
positive_difference = abs((yersterday_stock_price) - (day_before_yesterday_stock_price))
if positive_difference > 0:
    up_down = "⬆️"
else:
    up_down = "⬇️"
print(f"Positive difference between two days: {positive_difference}")

#Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
# porcentage difference = abs/average x 100
porcentage_difference = positive_difference /(day_before_yesterday_stock_price + positive_difference/2) * 100
porcentage_difference_round_value = round(porcentage_difference, 2)
print(f"porcentage changes between two days: {porcentage_difference_round_value}")



# use the News API to get articles related to the COMPANY_NAME.
    ## https://newsapi.org/
if porcentage_difference_round_value > 0.93:
    news_params = {
        "q": "Tesla",
        "qInTitle": COMPANY_NAME,
        "from": "2023-01-13",
        "sortBy": "popularity",
        "apiKey": NEWS_API_KEY

    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    data_news = news_response.json()


    # get the first 3 news pieces for the COMPANY_NAME.

    articles = (data_news["articles"])
    three_articles = articles[:3]


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#list of the first 3 article's headline and description using list comprehension.
    formatted_articles = [f"{STOCK_NAME}:{up_down}{porcentage_difference_round_value}%\nHeadline: {article['title']}.\nBrief: {article['description']}" for article in three_articles]
    print(formatted_articles)

# Send each article as a separate message via Twilio.
    client = Client(account_sid, auth_token)
    for article in formatted_articles:
        message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=article,
        to='whatsapp:+myphone'
    )




#Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

