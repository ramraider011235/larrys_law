from yahooquery import Ticker
import statistics as stats
import streamlit as st



def display_as_percent(val):
    return str(round(val * 100, 1)) + "%"


def company_longName(ticker):
    d = Ticker(ticker).quote_type
    return list(d.values())[0]["longName"]


def str_tic_lst(port_tics):
    string_tickers = ''
    for i in port_tics:
        if i != port_tics[-1]:
            string_tickers += (i+' ')
        else:
            string_tickers += (i)
    return string_tickers


def get_diff(a, b):
    return list(set(a) ^ set(b))


def true_false(var1):
    if var1 == "Yes":
        return True
    elif var1 == "No":
        return False    


def exception_response(crossover_1, p, x, sheen_lst, crap_lst, df1):
    try:
        if x == p:
            sheen_lst.append(p)
            return sheen_lst, crap_lst, df1
        else:
            crap_lst.append(p)
            df1 = df1.drop(df1[df1["ticker"] == p].index)
            return sheen_lst, crap_lst, df1
    except Exception:    
        st.write(f'FAILURE = {crossover_1}')
        crap_lst.append(p)
        df1 = df1.drop(df1[df1["ticker"] == p].index)
        return sheen_lst, crap_lst, df1



def clean_data_1(data):
    short_list = ['Earnings Date', 'Change', 'Change from Open', 'IPO Date', 'After-Hours Close', 'After-Hours Change',]
    for s in short_list:
        try:
            del data[f"{s}"]
        except Exception:
            pass
    return data


def clean_data_2(d1, percent_list, number_list):
    def clean(list1):
        temp = []
        for i in list1:
            if type(i) == int:
                temp.append(float(i))
            if type(i) == float:
                temp.append(i)
            elif type(i) == str:
                temp.append(float(i[:-1]))
        return temp

    def clean_percent(list1):
        temp = []
        for i in list1:
            if type(i) == int:
                x = float(i)
                temp.append(x/100)
            if type(i) == float:
                temp.append(i/100)
            elif type(i) == str:
                x = float(i[:-1])
                temp.append(x/100)
        return temp
        
    try:
        data = d1.copy()
        for x in data[percent_list]:           
            val1 = clean_percent(data[x])
            del data[x]
            data[x] = val1   
        for x in data[number_list]:           
            val1 = clean(data[x])
            del data[x]
            data[x] = val1
    except Exception:
        pass    
    return data    


def clean_data_3(data):
    data.columns = [x.lower() for x in data.columns]
    data.columns = [x.replace(" ", "_") for x in data.columns]
    data.columns = [x.replace("(", "") for x in data.columns]
    data.columns = [x.replace(")", "") for x in data.columns]
    data.columns = [x.replace("/", "") for x in data.columns]
    data.columns = [x.replace("-", "_") for x in data.columns]
    data.columns = [x.replace(".", "") for x in data.columns]
    return data


def clean_data_4(data, a_lst):    
    def clean69(data, target1):
        d_lst_1, d_lst_2 = data[target1], data['price']
        aaa_lst = []
        for r in range(len(d_lst_1)):
            r1 = 1 + d_lst_1[r]
            x = d_lst_2[r] / r1
            aaa_lst.append(x)
        return aaa_lst  
    try:
        for a in a_lst:
            val = clean69(data, a)
            del data[a]
            data[a] = val
        return data
    except Exception:
        pass    
    
    
def clean_data_5(data):    
    short_lst = ["earnings_date", "ipo_date", "index", "rank", "afterhours_close", "change", "afterhours_change", "change_from_open"]
    for s in short_lst:
        try:
            del data[f"{s}"]
        except Exception:
            pass         
    try:
        data = data.rename(columns={"symbol": "ticker"})
    except Exception:
        pass    
    try:
        data = data.rename(columns={"52_week_low": "low_52_week"})
    except Exception:
        pass    
    try:
        data = data.rename(columns={"52_week_high": "high_52_week"})
    except Exception:
        pass    
    try:
        data = data.rename(columns={"50_day_high": "high_50_day"})
    except Exception:
        pass    
    try:
        data = data.rename(columns={"50_day_low": "low_50_day"})
    except Exception:
        pass    
    try:
        data = data.rename(columns={"20_day_simple_moving_average": "sma_20"})
    except Exception:
        pass    
    try:
        data = data.rename(columns={"50_day_simple_moving_average": "sma_50"})
    except Exception:
        pass    
    try:
        data = data.rename(columns={"200_day_simple_moving_average": "sma_200"})
    except Exception:
        pass   
    try:
        data["over_50day_low"] = data["current_price"] / data["low_50_day"]
    except Exception:
        pass
    return data        


def clean_sort(d0):    
    string_list = ['Ticker', 'Company', 'Sector', 'Industry', 'Country']
    percent_list = ['Dividend Yield', 'Payout Ratio', 'Insider Ownership', 'Insider Transactions', 'Institutional Ownership', 'Institutional Transactions', 'Float Short', 'Return on Assets', 'Return on Equity', 'Return on Investment', 'Gross Margin', 'Operating Margin', 'Profit Margin', 'Performance (Half Year)', 'Performance (Year)', 'Performance (YTD)', 'Volatility (Week)', 'Volatility (Month)', '52-Week Low', 'Gap','20-Day Simple Moving Average', '50-Day Simple Moving Average', '200-Day Simple Moving Average', '50-Day High', '50-Day Low', '52-Week High','EPS growth this year', 'EPS growth next year', 'EPS growth past 5 years', 'EPS growth next 5 years', 'Sales growth past 5 years', 'EPS growth quarter over quarter', 'Sales growth quarter over quarter', 'Performance (Week)', 'Performance (Month)', 'Performance (Quarter)']
    number_list = ['No.', 'Market Cap', 'P/E', 'Forward P/E', 'PEG', 'P/S', 'P/B', 'P/Cash', 'P/Free Cash Flow', 'EPS (ttm)',   'Current Ratio', 'Quick Ratio', 'LT Debt/Equity', 'Total Debt/Equity', 'Shares Outstanding', 'Shares Float', 'Short Ratio', 'Beta','Average True Range', 'Relative Strength Index (14)', 'Analyst Recom', 'Average Volume', 'Relative Volume', 'Price', 'Volume', 'Target Price']
    a_lst = ['20_day_simple_moving_average',  '50_day_simple_moving_average', '200_day_simple_moving_average',  '50_day_high',  '50_day_low', '52_week_high',  '52_week_low']
    data = d0.copy()
    data = clean_data_1(data)
    data = clean_data_2(data, percent_list, number_list)            
    data = clean_data_3(data)
    data = clean_data_4(data, a_lst)
    data = clean_data_5(data)
    return data 




def get_stats1(df1, choice_1, style):
    # MEAN - my_mean = round(df1['my_score'].sum() / len(df1),4)
    my_mean = df1['my_score'].mean()
    
    # DEVIATION
    df1['deviation'] = df1['my_score'] - my_mean
    
    # DEVIATION**2
    df1['deviation_sq'] = df1['deviation'] ** 2
    
    # VARIANCE - Variance = round((df1['deviation_sq'].sum()) / len(df1),4)
    variance = stats.variance(df1['my_score'])
    
    # STANDARD DEVIATION - # sd = round(variance ** 0.5    ,4)
    sd = stats.stdev(df1['my_score'])
    
    print(choice_1)
    if style == 'Minimum':
        res007 = round(my_mean + (sd * choice_1), 4)
        return res007, my_mean, variance, sd
    elif style == 'Range':    
        res006 = round(my_mean + (sd * choice_1[0]),2)
        res007 = round(my_mean + (sd * choice_1[1]),2)
        return res006, res007, my_mean, variance, sd
    
    
def get_stats11(df1, choice_1, style):
    my_score_mean = df1['my_score'].mean()
    my_score_var = df1['my_score'].var()
    my_score_std = df1['my_score'].std()
    
    if style == 'Minimum':
        res007 = round(my_score_mean + (my_score_std * choice_1), 4)
        return res007, my_score_mean, my_score_var, my_score_std
    elif style == 'Range':    
        res006 = round(my_score_mean + (my_score_std * choice_1[0]),2)
        res007 = round(my_score_mean + (my_score_std * choice_1[1]),2)
        return res006, res007, my_score_mean, my_score_var, my_score_std    
