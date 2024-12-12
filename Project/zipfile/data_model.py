# The Data Modeling and its GUI code, imports score from survey.py and is imported by result.py
# Project Members: Jike Lu (jikelu), Tanyue Yao (tanyuey), Haowen Weng (hweng), Junxuan Liu (junxuanl), Cecilia Chen (sixuanch)

import pandas as pd
import requests
import json
import yfinance as yf
import pandas as pd
import datetime
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from scipy.optimize import minimize
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from survey import score

popular_assets = [
    'AAPL', 'MSFT', 'AMZN', 'META', 'GOOGL', 'GOOG', 'BRK-B', 'JNJ', 'V', 'PG',
    'JPM', 'UNH', 'MA', 'INTC', 'VZ', 'HD', 'T', 'DIS', 'MRK', 'PFE',
    'BAC', 'PEP', 'KO', 'NVS', 'XOM', 'CSCO', 'CMCSA', 'ORCL', 'ABBV', 'ACN',
    'TMO', 'AVGO', 'CVX', 'GILD', 'NKE', 'LLY', 'COST', 'DHR', 'MDT', 'NEE',
    'MCD', 'TXN', 'QCOM', 'TMUS', 'HON', 'UNP', 'BMY', 'LIN', 'WMT', 'ADBE',
    'AMGN', 'NFLX', 'SBUX', 'ABT', 'AEP', 'PYPL', 'IBM', 'AMD', 'LMT', 'BA',
    'C', 'BLK', 'FIS', 'AMT', 'GE', 'TSLA', 'NVDA', 'CHTR', 'CAT', 'UPS',
    'MMM', 'GS', 'RTX', 'DE', 'AXP', 'SPGI', 'MO', 'NOW', 'SCHW', 'ISRG',
    'ZTS', 'CB', 'GPN', 'TGT', 'BDX', 'CI', 'SYK', 'SO', 'MDLZ', 'MU',
    'PNC', 'NSC', 'CL', 'CSX', 'D', 'EL', 'ADI', 'FI', 'ANTM.JK', 'PLD',
    'GOLD', 'AG',
    'SPY', 'IVV', 'VTI', 'QQQ', 'GLD', 'EFA', 'IEFA', 'VWO', 'VGT', 'XLF',
    'FCNTX', 'VFINX', 'VGTSX', 'PRGFX', 'VTSAX',
    'GC=F', 'SI=F', 'CL=F', 'NG=F',
    'EURUSD=X', 'JPY=X', 'GBPUSD=X', 'AUDUSD=X', 'USDCAD=X',
    'TLT', 'IEF', 'SHY', 'BND', 'AGG',
    'VNQ', 'IYR', 'SCHH', 'RWO',
    'BTC-USD', 'ETH-USD', 'EURJPY=X', 'USO', '^GSPC'

]

asset_descriptions = {
    'AAPL': 'Apple Inc. - A leading technology company known for its smartphones, computers, and software.',
    'MSFT': 'Microsoft Corporation - A multinational technology company producing software, electronics, and personal computers.',
    'AMZN': 'Amazon.com, Inc. - An e-commerce and cloud computing company.',
    'META': 'Meta Platforms, Inc. (formerly Facebook, Inc.) - A social media and technology company.',
    'GOOGL': 'Alphabet Inc. (Class A) - The parent company of Google, focusing on internet services and technology.',
    'GOOG': 'Alphabet Inc. (Class C) - The parent company of Google, with no voting rights unlike GOOGL.',
    'BRK-B': 'Berkshire Hathaway Inc. (Class B) - A multinational conglomerate holding company led by Warren Buffett.',
    'JNJ': 'Johnson & Johnson - A multinational corporation that develops medical devices, pharmaceuticals, and consumer packaged goods.',
    'V': 'Visa Inc. - A multinational financial services corporation facilitating electronic funds transfers.',
    'PG': 'Procter & Gamble Co. - A multinational consumer goods corporation.',
    'JPM': 'JPMorgan Chase & Co. - A multinational investment bank and financial services company.',
    'UNH': 'UnitedHealth Group Incorporated - A diversified healthcare company offering health care products and insurance services.',
    'MA': 'Mastercard Incorporated - A multinational financial services corporation facilitating electronic funds transfers.',
    'INTC': 'Intel Corporation - A multinational corporation and technology company, one of the world\'s largest semiconductor chip manufacturers.',
    'VZ': 'Verizon Communications Inc. - A multinational telecommunications company.',
    'HD': 'The Home Depot, Inc. - The largest home improvement retailer in the United States.',
    'T': 'AT&T Inc. - An American multinational conglomerate holding company and telecommunications giant.',
    'DIS': 'The Walt Disney Company - A diversified multinational mass media and entertainment conglomerate.',
    'MRK': 'Merck & Co., Inc. - A leading global pharmaceutical company.',
    'PFE': 'Pfizer Inc. - An American multinational pharmaceutical corporation.',
    'BAC': 'Bank of America Corporation - An American multinational investment bank and financial services company.',
    'PEP': 'PepsiCo, Inc. - An American multinational food, snack, and beverage corporation.',
    'KO': 'The Coca-Cola Company - An American multinational beverage corporation.',
    'NVS': 'Novartis AG - A Swiss multinational pharmaceutical corporation.',
    'XOM': 'Exxon Mobil Corporation - An American multinational oil and gas corporation.',
    'CSCO': 'Cisco Systems, Inc. - An American multinational technology conglomerate.',
    'CMCSA': 'Comcast Corporation - An American telecommunications conglomerate.',
    'ORCL': 'Oracle Corporation - An American multinational computer technology corporation.',
    'ABBV': 'AbbVie Inc. - An American publicly traded biopharmaceutical company.',
    'ACN': 'Accenture plc - A multinational professional services company specializing in IT services and consulting.',
    'TMO': 'Thermo Fisher Scientific Inc. - An American provisioner of scientific instrumentation, reagents and consumables, and software services.',
    'AVGO': 'Broadcom Inc. - An American designer, developer, manufacturer and global supplier of a wide range of semiconductor and infrastructure software products.',
    'CVX': 'Chevron Corporation - An American multinational energy corporation.',
    'GILD': 'Gilead Sciences, Inc. - An American biopharmaceutical company that researches, develops, and commercializes drugs.',
    'NKE': 'NIKE, Inc. - An American multinational corporation engaged in the design, development, manufacturing, and worldwide marketing and sales of footwear, apparel, equipment, accessories, and services.',
    'LLY': 'Eli Lilly and Company - An American pharmaceutical company.',
    'COST': 'Costco Wholesale Corporation - An American multinational corporation which operates a chain of membership-only warehouse clubs.',
    'DHR': 'Danaher Corporation - An American globally diversified conglomerate with its headquarters in Washington, D.C.',
    'MDT': 'Medtronic plc - A medical device company that generates the majority of its sales and profits from the U.S. healthcare system but is headquartered in the Republic of Ireland for tax purposes.',
    'NEE': 'NextEra Energy, Inc. - An American energy company with about 58 GW of generating capacity, revenues of over $17 billion, and about 14,000 employees throughout the US and Canada.',
    'MCD': 'McDonald\'s Corporation - An American fast food company.',
    'TXN': 'Texas Instruments Incorporated - An American technology company that designs and manufactures semiconductors and various integrated circuits.',
    'QCOM': 'Qualcomm Incorporated - An American multinational corporation that creates intellectual property, semiconductors, software, and services related to wireless technology.',
    'TMUS': 'T-Mobile US, Inc. - An American wireless network operator.',
    'HON': 'Honeywell International Inc. - An American publicly traded, multinational conglomerate corporation.',
    'UNP': 'Union Pacific Corporation - An American publicly traded, multinational conglomerate corporation.',
    'BMY': 'Bristol-Myers Squibb Company - An American pharmaceutical company.',
    'LIN': 'Linde plc - A multinational chemical company.',
    'WMT': 'Walmart Inc. - An American multinational retail corporation that operates a chain of hypermarkets, discount department stores, and grocery stores.',
    'ADBE': 'Adobe Inc. - An American multinational computer software company.',
    'AMGN': 'Amgen Inc. - An American multinational biopharmaceutical company.',
    'NFLX': 'Netflix, Inc. - An American technology and media services provider and production company.',
    'SBUX': 'Starbucks Corporation - An American multinational chain of coffeehouses and roastery reserves.',
    'ABT': 'Abbott Laboratories - An American multinational medical devices and health care company.',
    'AEP': 'American Electric Power Company, Inc. - An American electric utility holding company.',
    'PYPL': 'PayPal Holdings, Inc. - An American company operating an online payments system.',
    'IBM': 'International Business Machines Corporation - An American multinational technology company.',
    'AMD': 'Advanced Micro Devices, Inc. - An American multinational semiconductor company.',
    'LMT': 'Lockheed Martin Corporation - An American aerospace, defense, arms, security, and advanced technologies company.',
    'BA': 'The Boeing Company - An American multinational corporation that designs, manufactures, and sells airplanes, rotorcraft, rockets, satellites, telecommunications equipment, and missiles worldwide.',
    'C': 'Citigroup Inc. - An American multinational investment bank and financial services corporation.',
    'BLK': 'BlackRock, Inc. - An American multinational investment management corporation.',
    'FIS': 'Fidelity National Information Services, Inc. - An American multinational financial services technology company.',
    'AMT': 'American Tower Corporation - An American real estate investment trust and an owner and operator of wireless and broadcast communications infrastructure.',
    'GE': 'General Electric Company - An American multinational conglomerate.',
    'TSLA': 'Tesla, Inc. - An American electric vehicle and clean energy company.',
    'NVDA': 'NVIDIA Corporation - An American multinational technology company incorporated in Delaware and based in Santa Clara, California.',
    'CHTR': 'Charter Communications, Inc. - An American telecommunications and mass media company.',
    'CAT': 'Caterpillar Inc. - An American Fortune 100 corporation which designs, develops, engineers, manufactures, markets, and sells machinery, engines, financial products, and insurance.',
    'UPS': 'United Parcel Service, Inc. - An American multinational package delivery and supply chain management company.',
    'MMM': '3M Company - An American multinational conglomerate corporation.',
    'GS': 'The Goldman Sachs Group, Inc. - An American multinational investment bank and financial services company.',
    'RTX': 'Raytheon Technologies Corporation - An American multinational aerospace and defense conglomerate.',
    'DE': 'Deere & Company - An American corporation that manufactures agricultural, construction, and forestry machinery, diesel engines, drivetrains (axles, transmissions, gearboxes) used in heavy equipment, and lawn care equipment.',
    'AXP': 'American Express Company - An American multinational corporation specializing in payment card services.',
    'SPGI': 'S&P Global Inc. - An American publicly traded corporation headquartered in Manhattan, New York City.',
    'MO': 'Altria Group, Inc. - An American corporation and one of the world\'s largest producers and marketers of tobacco, cigarettes, and related products.',
    'NOW': 'ServiceNow, Inc. - An American software company based in Santa Clara, California.',
    'SCHW': 'The Charles Schwab Corporation - An American multinational financial services company.',
    'ISRG': 'Intuitive Surgical, Inc. - An American corporation that develops, manufactures, and markets robotic products designed to improve clinical outcomes of patients through minimally invasive surgery.',
    'ZTS': 'Zoetis Inc. - An American drug company, the world\'s largest producer of medicine and vaccinations for pets and livestock.',
    'CB': 'Chubb Limited - A global provider of insurance products covering property and casualty, accident and health, reinsurance, and life insurance.',
    'GPN': 'Global Payments Inc. - An American company providing financial technology services globally.',
    'TGT': 'Target Corporation - A large retail corporation known for its discount stores.',
    'BDX': 'Becton, Dickinson and Company - A medical technology company manufacturing medical devices, instrument systems, and reagents.',
    'CI': 'Cigna Corporation - A global health service company offering health, pharmacy, and insurance products and services.',
    'SYK': 'Stryker Corporation - A company specializing in medical devices, equipment, and software.',
    'SO': 'Southern Company - An American gas and electric utility holding company.',
    'MDLZ': 'Mondelez International, Inc. - A multinational confectionery, food, and beverage company.',
    'MU': 'Micron Technology, Inc. - A producer of computer memory and computer data storage.',
    'PNC': 'PNC Financial Services Group, Inc. - A bank holding company and financial services corporation.',
    'NSC': 'Norfolk Southern Corporation - A major American railroad transportation company.',
    'CL': 'Colgate-Palmolive Company - A consumer products company focused on the production, distribution, and provision of household, health care, and personal care products.',
    'CSX': 'CSX Corporation - An international transportation company offering a variety of rail, container-shipping, intermodal, trucking, and contract logistics services.',
    'D': 'Dominion Energy, Inc. - An American power and energy company supplying electricity in parts of Virginia, North Carolina, and South Carolina.',
    'EL': 'Estée Lauder Companies Inc. - A multinational manufacturer and marketer of prestige skincare, makeup, fragrance, and hair care products.',
    'ADI': 'Analog Devices, Inc. - A semiconductor company specializing in data conversion, signal processing, and power management technology.',
    'FI': 'Frank\'s International N.V. - A global oil services company that provides a broad range of highly engineered drilling and completions solutions.',
    'ANTM.JK': 'Antam (Aneka Tambang) - An Indonesian mining company involved in the exploration, mining, processing, and marketing of nickel ore, ferronickel, gold, silver, bauxite, and coal.',
    'PLD': 'Prologis, Inc. - A real estate investment trust that invests in logistics facilities.',
    'GOLD': 'Barrick Gold Corporation - One of the largest gold mining companies in the world.',
    'AG': 'First Majestic Silver Corp. - A mining company focused on silver production in Mexico.',

    'SPY': 'SPDR S&P 500 ETF Trust - An ETF that tracks the S&P 500 stock market index.',
    'IVV': 'iShares Core S&P 500 ETF - An ETF that tracks the performance of the S&P 500 index.',
    'VTI': 'Vanguard Total Stock Market ETF - An ETF that tracks the performance of the CRSP US Total Market Index.',
    'QQQ': 'Invesco QQQ Trust - An ETF based on the Nasdaq-100 Index.',
    'GLD': 'SPDR Gold Trust - An ETF that tracks the gold market.',
    'EFA': 'iShares MSCI EAFE ETF - An ETF that tracks large and mid-cap equity performance in developed markets, excluding the U.S. and Canada.',
    'IEFA': 'iShares Core MSCI EAFE ETF - An ETF providing exposure to a broad range of companies in Europe, Australia, Asia, and the Far East.',
    'VWO': 'Vanguard FTSE Emerging Markets ETF - An ETF that tracks the return of the FTSE Emerging Markets All Cap China A Inclusion Index.',
    'VGT': 'Vanguard Information Technology ETF - An ETF that tracks the performance of the MSCI US Investable Market Information Technology 25/50 Index.',
    'XLF': 'Financial Select Sector SPDR Fund - An ETF that provides exposure to the financial sector of the S&P 500 Index.',

    'FCNTX': 'Fidelity Contrafund - A mutual fund investing in large-cap stocks with long-term growth potential.',
    'VFINX': 'Vanguard 500 Index Fund - A mutual fund that tracks the performance of the S&P 500 Index.',
    'VGTSX': 'Vanguard Total International Stock Index Fund - A mutual fund that tracks the performance of non-U.S. equity markets.',
    'PRGFX': 'T. Rowe Price Growth Stock Fund - A mutual fund focused on growth-oriented stocks.',
    'VTSAX': 'Vanguard Total Stock Market Index Fund - A mutual fund that tracks the performance of the entire U.S. stock market.',

    'GC=F': 'Gold Futures - A contract for the future delivery of gold.',
    'SI=F': 'Silver Futures - A contract for the future delivery of silver.',
    'CL=F': 'Crude Oil Futures - A contract for the future delivery of crude oil.',
    'NG=F': 'Natural Gas Futures - A contract for the future delivery of natural gas.',

    'EURUSD=X': 'Euro to US Dollar - The exchange rate from Euro to US Dollar.',
    'JPY=X': 'Japanese Yen to US Dollar - The exchange rate from Japanese Yen to US Dollar.',
    'GBPUSD=X': 'British Pound to US Dollar - The exchange rate from British Pound to US Dollar.',
    'AUDUSD=X': 'Australian Dollar to US Dollar - The exchange rate from Australian Dollar to US Dollar.',
    'USDCAD=X': 'US Dollar to Canadian Dollar - The exchange rate from US Dollar to Canadian Dollar.',

    'TLT': 'iShares 20+ Year Treasury Bond ETF - An ETF that tracks the performance of long-term U.S. Treasury bonds.',
    'IEF': 'iShares 7-10 Year Treasury Bond ETF - An ETF that tracks the performance of medium-term U.S. Treasury bonds.',
    'SHY': 'iShares 1-3 Year Treasury Bond ETF - An ETF that tracks the performance of short-term U.S. Treasury bonds.',
    'BND': 'Vanguard Total Bond Market ETF - An ETF that tracks the performance of the U.S. bond market.',
    'AGG': 'iShares Core U.S. Aggregate Bond ETF - An ETF that tracks an index of U.S. investment-grade bonds.',

    'VNQ': 'Vanguard Real Estate ETF - An ETF that tracks the performance of the MSCI US Investable Market Real Estate 25/50 Index.',
    'IYR': 'iShares U.S. Real Estate ETF - An ETF that provides exposure to U.S. real estate stocks and REITs.',
    'SCHH': 'Schwab U.S. REIT ETF - An ETF that tracks the performance of the Dow Jones U.S. Select REIT Index.',
    'RWO': 'SPDR Dow Jones Global Real Estate ETF - An ETF that provides exposure to global real estate securities.',

    'BTC-USD': 'Bitcoin to US Dollar - The exchange rate from Bitcoin to US Dollar.',
    'ETH-USD': 'Ethereum to US Dollar - The exchange rate from Ethereum to US Dollar.',
    'EURJPY=X': 'Euro to Japanese Yen - The exchange rate from Euro to Japanese Yen.',
    'USO': 'United States Oil Fund - An ETF that tracks the performance of crude oil.',
    '^GSPC': 'S&P 500 index, representing the market trend',

    '30 Yr': "30 year treasure bond",
    '20 Yr': "20 year treasure bond",
    '10 Yr': "10 year treasure bond",
    '7 Yr': "7 year treasure bond",
    '5 Yr': "5 year treasure bond",
    '1 Yr': "1 year treasure bond"
}




def download_adjusted_close(symbols):
    end_date = datetime.date.today()
    start_date = end_date - datetime.timedelta(days=365)

    # Initialize an empty DataFrame to hold all adjusted close prices
    all_adj_close = pd.DataFrame()
    adj_close_list = []

    for symbol in symbols:
        stock_data = yf.download(symbol, start=start_date, end=end_date)
        # Convert the 'Adj Close' Series to a DataFrame with the symbol as its column name
        adj_close = pd.DataFrame(stock_data['Adj Close'])
        adj_close.columns = [symbol]
        adj_close_list.append(adj_close)

    all_adj_close = pd.concat(adj_close_list, axis=1)
    return all_adj_close


# Download data
adj_close_prices = download_adjusted_close(popular_assets)

pd.set_option('display.max_columns', None)
adj_close_prices

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}

url = 'https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value=2022'

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.text, 'html.parser')

data = []
table = soup.find('table')
table_body = table.find('tbody')

rows = table.find_all('tr')
for row in rows:
    cols = row.find_all(['td', 'th'])
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])

daily_treasury_2022 = pd.DataFrame(data)

url = 'https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value=2023'

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.text, 'html.parser')

data = []
table = soup.find('table')
table_body = table.find('tbody')

rows = table.find_all('tr')
for row in rows:
    cols = row.find_all(['td', 'th'])
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])

daily_treasury_2023 = pd.DataFrame(data)

from datetime import datetime, timedelta
def fetch_esgu_historical_data():
    ## Get the date of today and format it
    end_date = datetime.now().strftime('%Y-%m-%d')

    ## Calaulate the date one year ago and format it
    start_date = (datetime.now() - timedelta(days=365)).strftime('%Y-%m-%d')

    ## Creat a new URL
    url = f"https://api.nasdaq.com/api/quote/ESGU/historical?assetclass=etf&fromdate={start_date}&limit=600&todate={end_date}"

    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to retrieve data: Status code {response.status_code}")
        return None


historical_data_esgu = fetch_esgu_historical_data()

# Extracting the rows for the DataFrame
rows = historical_data_esgu['data']['tradesTable']['rows']

# Creating a DataFrame
daily_esgu = pd.DataFrame(rows)

## Create the treasury dataset match the timeframe
# df_treasury = daily_treasury_2022.concat(daily_treasury_2023,ignore_index = True)
df_treasury = pd.concat([daily_treasury_2022, daily_treasury_2023], ignore_index=True)

df_treasury = df_treasury.iloc[:, list(range(1)) + list(range(-8, 0))]
df_treasury.columns = df_treasury.iloc[0]
df_treasury.drop(0, inplace=True)
df_treasury = df_treasury.loc[229:]
df_treasury = df_treasury.set_index(df_treasury.columns[0])

df_treasury.columns.tolist()

## Reverse the dataframe
df_reversed = daily_esgu.iloc[::-1]
df_reversed = df_reversed.reset_index(drop=True)

## Create the esgu dataset match the timeframe
df_esgu = df_reversed.iloc[:, :2]
df_esgu = df_esgu.set_index(df_esgu.columns[0])
df_esgu.columns = ['ESGU']

## Change the date index to the same format
df_esgu.index = pd.to_datetime(df_esgu.index, errors='coerce')
df_esgu.index = df_esgu.index.strftime('%Y-%m-%d')

df_treasury.index = pd.to_datetime(df_treasury.index, errors='coerce')
df_treasury.index = df_treasury.index.strftime('%Y-%m-%d')

adj_close_prices.index = pd.to_datetime(adj_close_prices.index, errors='coerce')
adj_close_prices.index = adj_close_prices.index.strftime('%Y-%m-%d')

## Concate the dataframes and clean the missing values
df = pd.concat([adj_close_prices, df_treasury, df_esgu], axis=1)
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    df.isnull().sum()

## Drop the rows with any missing value
df.dropna(inplace=True)

with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    df.isnull().sum()

## Create the expected return dataset
for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')

return_df = df.pct_change().dropna()

def score_to_beta(score):
    max_beta = 2.37  ## According to the betas of all the assets
    min_beta = 0  ## Theoretical lower bound
    score_neutral = 28 / 47 * 100  ## According to the risk survey benchmark
    if score <= score_neutral:
        beta = 1 - (score_neutral - score) / score_neutral * 1
    else:
        beta = 1 + (score - score_neutral) / (100 - score_neutral) * (max_beta - 1)

    return beta





def calculate_portfolio_beta(weights, betas):
    return np.sum(np.dot(weights.T, betas))


# Calculate average daily returns
data = return_df.copy()
average_returns = data.mean()
cov_matrix = data.cov()
max_beta_tolerance = score_to_beta(score())

# Define the risk-free rate and market return
risk_free_rate = df['30 Yr'].mean() * 0.01
market_return = (df['^GSPC'][-1] - df['^GSPC'][0]) / df['^GSPC'][0]

# Calculate beta for each asset
market_variance = data['^GSPC'].var()
betas = data.apply(lambda x: x.cov(data['^GSPC']) / market_variance)

# Calculate expected returns using CAPM
expected_returns = risk_free_rate + betas * (market_return - risk_free_rate)


# Portfolio optimization
def objective(weights):
    portfolio_return = np.dot(weights, expected_returns)
    return -portfolio_return


# Constraints: Weights sum to 1
constraints = ({'type': 'eq', 'fun': lambda weights: np.sum(weights) - 1})
risk_constraints = (
{'type': 'ineq', 'fun': lambda weights: max_beta_tolerance - calculate_portfolio_beta(weights, betas)})

# Bounds: Each weight is between 0 and 1
bounds = tuple((0, 1) for _ in range(len(data.columns)))

# Initial guess
initial_weights = np.array([1 / len(data.columns)] * len(data.columns))

# Perform the optimization
optimal_weights = minimize(objective, initial_weights, method='SLSQP', bounds=bounds,
                           constraints=[constraints, risk_constraints])

# Print the optimal weights for the portfolio
optimal_portfolio = optimal_weights.x
for i in range(len(optimal_portfolio)):
    print()
print(optimal_weights.x)

# Calculate the expected portfolio return
portfolio_return = -objective(optimal_weights.x)
portfolio_beta = calculate_portfolio_beta(optimal_weights.x, betas)
print(f"Expected Portfolio Return: {portfolio_return}")
print(f"Expected Portfolio beta: {portfolio_beta}")

sorted_weight_df = pd.DataFrame({
    'Asset': return_df.columns,
    'Weights': pd.Series(optimal_weights.x)
})
sorted_weight_df = sorted_weight_df.sort_values(by='Weights', ascending=False)
top10_assets = list(sorted_weight_df.Asset[:10])
top10_assets
print(top10_assets)


def show_description():
    global sorted_weight_df
    print("The Top 10 assets in our investment portfolio")
    top10_assets = list(sorted_weight_df.Asset[:10])
    top10_assets
    i = 0

    output = []
    # new list store output(string)
    for asset in top10_assets:
        weight = "{:.2f}".format(list(sorted_weight_df.Weights)[i] * 100)
        description = asset_descriptions.get(asset)
        i += 1
        output.append(description + " ------ " + str(weight) + "%")
    return output


# show_description(sorted_weight_df)

import matplotlib.pyplot as plt

data_2 = return_df.copy()
df_values = data_2.values
result_portfolio = []
for i in range(len(df_values)):
    result_portfolio.append(sum([a * b for a, b in zip(df_values[i], optimal_weights.x)]))

cumulative_return = []
cumulative_return.append(result_portfolio[0] + 1)
for i in range(len(result_portfolio) - 1):
    cumulative_return.append((result_portfolio[i] + 1) * (result_portfolio[1 + i] + 1))

row_index = data_2.index
data_portfolio_dict = {'Daily Return': result_portfolio, 'Cumulative Return': cumulative_return}
data_portfolio = pd.DataFrame(data_portfolio_dict, index=row_index)

# data_portfolio.plot(y='Daily Return', kind='line', linestyle='-')
# plt.xlabel('Date')
# plt.ylabel('Return')
# plt.title('Plot of a Daily Return')
# plt.show()
#
# data_portfolio.plot(y='Cumulative Return', kind='line', linestyle='-')
# plt.xlabel('Date')
# plt.ylabel('Cumulative Return')
# plt.title('Plot of a Cumulative Return')
# plt.show()

# cumulative_average = data_portfolio.values[-1][0]
# categories = ['Our Portfolio', 'Average Portfolio']
# values = [portfolio_return, cumulative_average]
#
# plt.bar(categories, values, color=['blue', 'green'])
#
# plt.xlabel('Categories')
# plt.ylabel('Values')
# plt.title('Bar Chart of Portfolios')
#
# plt.show()

import random


#
def bar_chart():
    global df, portfolia_return, popular_assets
    random_values = random.sample(popular_assets, 5)

    asset_return_list = [portfolio_return]

    categories = ['Our Portfolio']

    for column in random_values:
        change_rate = (df[column].iloc[-1] - df[column].iloc[0]) / df[column].iloc[0]
        asset_return_list.append(change_rate)
        categories.append(column)

    # Create a new figure and a set of subplots
    fig, ax = plt.subplots()
    ax.bar(categories,
           asset_return_list,
           color=['blue', 'green', 'red', 'purple', 'orange', 'cyan'])
    ax.set_xlabel('Categories')
    ax.set_ylabel('Values')
    ax.set_title('Bar Chart of Random Portfolios vs Ours')
    # Remove this line if you want to display the plot in a Tkinter canvas instead of a standalone window #

    return fig


# plt.show()

data_3 = return_df.copy()
df_values_3 = data_3.values
average_portfolio = []
for i in range(len(df_values_3)):
    average_portfolio.append(sum([a * 1 / len(df_values_3[0]) for a in df_values_3[i]]))

average_cumulative_return = []
average_cumulative_return.append(average_portfolio[0] + 1)
for i in range(len(average_portfolio) - 1):
    average_cumulative_return.append((average_portfolio[i] + 1) * (average_portfolio[1 + i] + 1))

bar_chart()
# row_index_2 = data_3.index
# data_portfolio_dict_2 = {'Daily Return': average_portfolio, 'Cumulative Return': average_cumulative_return}
# data_portfolio_2 = pd.DataFrame(data_portfolio_dict_2, index=row_index_2)
#
# data_portfolio_2.plot(y='Daily Return', kind='line', linestyle='-')
# plt.axhline(y=portfolio_return/365, color='red', linestyle='--', label='Straight Line')
# plt.xlabel('Date')
# plt.ylabel('Return')
# plt.title('Plot of a Daily Return, Expected vs Average Out')
# plt.show()
#
# data_portfolio_2.plot(y='Cumulative Return', kind='line', linestyle='-')
# plt.axhline(y=portfolio_return+1, color='red', linestyle='--', label='Straight Line')
# plt.xlabel('Date')
# plt.ylabel('Cumulative Return')
# plt.title('Plot of a Cumulative Return, Expected vs Average Out')
# # plt.show()

import matplotlib.pyplot as plt

# Pie chart of weights
def Pie_chart_of_weights():
    ## Categorize our assets
    def locate_at(a):
        return popular_assets.index(a) + 1

    asset_categories = {
        'Company Stock': [popular_assets[i] for i in range(locate_at('AG'))],
        'ETF': [popular_assets[i] for i in range(locate_at('AG'), locate_at('XLF'))],
        'Index Fund': [popular_assets[i] for i in range(locate_at('XLF'), locate_at('VTSAX'))],
        'Futures': [popular_assets[i] for i in range(locate_at('VTSAX'), locate_at('NG=F'))],
        'Exchange Rate': [popular_assets[i] for i in range(locate_at('NG=F'), locate_at('USDCAD=X'))] + [
            popular_assets[popular_assets.index('EURJPY=X')]],
        'Bond ETF': [popular_assets[i] for i in range(locate_at('USDCAD=X'), locate_at('AGG'))],
        'Real Estate ETF': [popular_assets[i] for i in range(locate_at('AGG'), locate_at('RWO'))],
        'Virtual Currency': [popular_assets[i] for i in range(locate_at('BTC-USD'), locate_at('ETH-USD'))],
        'Oil Fund': [popular_assets[popular_assets.index('USO')]],
        'S&P 500 index': [popular_assets[popular_assets.index('^GSPC')]],
        'Treasury Bond': df_treasury.columns.tolist(),
        'ESGU': ['ESGU']
    }

    asset_weights = dict(zip(df.columns.tolist(), optimal_weights.x))

    ## Calculate the weight of each category
    def calculate_category_weights(asset_categories, asset_weights):
        category_weights = {}
        for category, assets in asset_categories.items():
            total_weight = sum(asset_weights.get(asset, 0) for asset in assets)
            category_weights[category] = total_weight
        return category_weights

    category_weights = calculate_category_weights(asset_categories, asset_weights)

    # Create the labels and sizes for the pie chart
    labels = category_weights.keys()
    sizes = category_weights.values()

    # Create a new label that contains the data
    labels_with_data = [f'{label}: {size * 100:.2f}%' for label, size in zip(labels, sizes)]

    # Generate a list of distinct colors
    colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple',
              'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan',
              'yellowgreen', 'yellow']

    # Create the figure and axes for the pie chart
    fig, ax = plt.subplots(figsize=(10, 7))
    wedges, texts = ax.pie(sizes, colors=colors, startangle=140)

    # Add the legend with the custom labels
    ax.legend(wedges, labels_with_data, title="Categories", loc="upper right")

    # Set the title of the pie chart
    ax.set_title('Portfolio Category Weights')

    # Equal aspect ratio ensures that pie is drawn as a circle
    ax.axis('equal')

    return fig


Pie_chart_of_weights()

from datetime import date, timedelta
import yfinance as yf
import pandas as pd

from datetime import datetime, timedelta
def download_user_data(symbol,days):
    end_date = date.today()
    start_date = end_date - timedelta(days=days)

    # Initialize an empty DataFrame to hold all adjusted close prices
    stock_data = yf.download(symbol, start=start_date, end=end_date)

    # Convert the 'Adj Close' Series to a DataFrame with the symbol as its column name
    adj_close = pd.DataFrame(stock_data['Adj Close'])
    adj_close.columns = [symbol]

    return adj_close

# Plot the return of the stock of user's choice
def plot_returns(user_input, df_user, df_user_percent_change):
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 5))
    df_user.plot(ax=axes[0], y='VALUE', linestyle='-', color='b', label='Sample Data')
    axes[0].set_title(user_input + ' Data')
    axes[0].set_xlabel('Index')
    axes[0].set_ylabel('Value')
    axes[0].legend()

    # Plot for the second DataFrame
    df_user_percent_change.plot(ax=axes[1], y='VALUE', linestyle='-', color='b', label='Sample Data')
    axes[1].set_title(user_input + ' Return Change Data')
    axes[1].set_xlabel('Index')
    axes[1].set_ylabel('Value')
    axes[1].legend()

    # Adjust layout
    plt.tight_layout()

    # Display the plots
    return fig


# plt.show()

# Search a stock based on user's input
def stock_search(user_input, days):
        # user_input = input("Enter your stock code, QUIT to exit: ")
        plt.close('all')

        if user_input == "QUIT":
            exit()


        # days = int(input("How many days to visualize: "))

        df_user = download_user_data(user_input, int(days))
        df_user.columns = ['VALUE']
        df_user.index = pd.to_datetime(df_user.index, errors='coerce')
        df_user.index = df_user.index.strftime('%Y-%m-%d')
        df_user.dropna(inplace=True)

        for col in df_user.columns:
            df_user[col] = pd.to_numeric(df_user[col], errors='coerce')

        df_user_percent_change = df_user.pct_change().dropna()
        df_user_percent_change.columns = ['VALUE']

        # plot_returns(user_input, df_user, df_user_percent_change)
        fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 5))
        df_user.plot(ax=axes[0], y='VALUE', linestyle='-', color='b', label='Sample Data')
        axes[0].set_title(user_input + ' Data')
        axes[0].set_xlabel('Index')
        axes[0].set_ylabel('Value')
        axes[0].legend()

        # Plot for the second DataFrame
        df_user_percent_change.plot(ax=axes[1], y='VALUE', linestyle='-', color='b', label='Sample Data')
        axes[1].set_title(user_input + ' Return Change Data')
        axes[1].set_xlabel('Index')
        axes[1].set_ylabel('Value')
        axes[1].legend()

        # Adjust layout
        plt.tight_layout()
        plt.show()

        # Display the plots


        # df_user.plot(y='VALUE', linestyle='-', color='b', label='Sample Data')
        # df_user_percent_change.plot(y='VALUE', linestyle='-', color='b', label='Sample Data')
