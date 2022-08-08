# - - - - - XXXXX PAGE - - - - -
general_pages = [
    "Advisor",
]


# - - - - - XXXXX PAGE - - - - -
feature_strategy = [
    "-Select-Model-",
    "Moving-Average - SMA & EMA",
    "Optimal SMA",
    "OverBought & OverSold",
    "Support & Resistance Lines",
    "Strategy II",
    "Indicators",
]

# - - - - - PORTFOLIO PAGE - - - - -
namer_lst = [
    "max_sharpe_df_1",
    "min_vol_df_1",
    "max_sharpe_df_2",
    "min_vol_df_2",
    "max_sharpe_df_3",
    "min_vol_df_3",
]


def live_dates_model():
    march_2022 = [
    #  |  'MONDAY'  |  'TUESDAY'  | 'WEDNESDAY' | 'THURSDAY'  | 'FRIDAY'    |
                                                  '2022-03-24',
                      '2022-03-29',               '2022-03-31',
    ]
    april_2022 = [               
    #  |  'MONDAY'  |  'TUESDAY'  | 'WEDNESDAY' | 'THURSDAY'  | 'FRIDAY'    |
                      '2022-04-05',               # ---SICK---, 
                      '2022-04-12',                             #--holiday--
                      '2022-04-19',               # ---SICK---,
                      '2022-04-26',               '2022-04-28', 
    ]
    may_2022 = [
    #  |  'MONDAY'  |  'TUESDAY'  | 'WEDNESDAY' | 'THURSDAY'  | 'FRIDAY'    |
                      '2022-05-03',               '2022-05-05',
                      '2022-05-10',                
                                                  '2022-05-19',
                      '2022-05-24', '2022-05-25', '2022-05-26', '2022-05-27',
                      '2022-05-31',
        
    ]
    june_2022 = [
    #  |  'MONDAY'  |  'TUESDAY'  | 'WEDNESDAY' | 'THURSDAY'  | 'FRIDAY'    |
                                    '2022-06-01', '2022-06-02', '2022-06-03',
        '2022-06-06', '2022-06-07', '2022-06-08', '2022-06-09',
                      '2022-06-14',               '2022-06-16',
                      '2022-06-21',               '2022-06-23', '2022-06-24',
                      '2022-06-28',               '2022-06-30',
    ]
    july_2022 = [
    #  |  'MONDAY'  |  'TUESDAY'  | 'WEDNESDAY' | 'THURSDAY'  | 'FRIDAY'    |
                      '2022-07-05',               '2022-07-07', 
                                    '2022-07-13', '2022-07-14',
                      '2022-07-19',               '2022-07-21',
                      '2022-07-26',               '2022-07-28',
    ]
    august_2022 = [
    #  |  'MONDAY'  |  'TUESDAY'  | 'WEDNESDAY' | 'THURSDAY'  | 'FRIDAY'    |
                      '2022-08-02',               '2022-08-04', '2022-08-05',
    ]
    live_months = [
        march_2022, 
        april_2022, 
        may_2022,
        june_2022,
        july_2022,
        august_2022,
    ]
    days = []
    for l in live_months:
        days += l
    return days



def live_dates_updater():
    lst = ['2022-06-28', '2022-06-30', '2022-07-14', '2022-07-19', '2022-07-21', '2022-07-26', '2022-07-28', '2022-08-02',]
    return lst



def live_dates_final():
    #             |  'MONDAY'  |   'TUESDAY'  | 'WEDNESDAY' |  'THURSDAY'   |  'FRIDAY'    |
    #             |------------|--------------|-------------|---------------|--------------|
    march_2022 = [               
                                                             "2022-03-24",
                                 "2022-03-29",               "2022-03-31",
    ]
    april_2022 = [               
                                 "2022-04-05",               # SICK------,
                                 "2022-04-12",                               # holiday-----
                                 "2022-04-19",               # SICK------,
                                 "2022-04-26",               "2022-04-28", 
    ]
    may_2022 = [
                                 '2022-05-03',               '2022-05-05',
                                 '2022-05-10',                
                                                             '2022-05-19',
                                #  '2022-05-24',              
                                                             '2022-05-26',
                                 '2022-05-31',   
    ]
    june_2022 = [
                 '2022-06-06',                               '2022-06-09',
                                 '2022-06-14',               '2022-06-16',
                                #  '2022-06-21',               '2022-06-23',
                                # '2022-06-28',                '2022-06-30',
    ]    
    live_months = [
        march_2022, 
        april_2022, 
        may_2022,
        june_2022,
        ]

    days = []
    for l in live_months:
        days += l

    return days



def live_dates_model_2():
    march_2022 = [
    #  |  'MONDAY'  |  'TUESDAY'  | 'WEDNESDAY' | 'THURSDAY'  | 'FRIDAY'    |
                                                  '2022-03-24',
                      '2022-03-29',               '2022-03-31',
    ]
    april_2022 = [               
    #  |  'MONDAY'  |  'TUESDAY'  | 'WEDNESDAY' | 'THURSDAY'  | 'FRIDAY'    |
                      '2022-04-05',               # ---SICK---, 
                      '2022-04-12',                             #--holiday--
                      '2022-04-19',               # ---SICK---,
                      '2022-04-26',               '2022-04-28', 
    ]
    may_2022 = [
    #  |  'MONDAY'  |  'TUESDAY'  | 'WEDNESDAY' | 'THURSDAY'  | 'FRIDAY'    |
                      '2022-05-03',               '2022-05-05',
                      '2022-05-10',                
                                                  '2022-05-20',
                      '2022-05-24',               '2022-05-26',
                      '2022-05-31',
        
    ]
    june_2022 = [
    #  |  'MONDAY'  |  'TUESDAY'  | 'WEDNESDAY' | 'THURSDAY'  | 'FRIDAY'    |
                                                  '2022-06-02',
                      '2022-06-07',               '2022-06-09',
                      '2022-06-14',               '2022-06-16',
                      '2022-06-21',               '2022-06-23',
                      '2022-06-28',               '2022-06-30',
    ]
    july_2022 = [
    #  |  'MONDAY'  |  'TUESDAY'  | 'WEDNESDAY' | 'THURSDAY'  | 'FRIDAY'    |
                      '2022-07-05',               '2022-07-07', 
                                                  '2022-07-14',
                      '2022-07-19',               '2022-07-21',
                      '2022-07-26',               '2022-07-28',
    ]
    august_2022 = [
    #  |  'MONDAY'  |  'TUESDAY'  | 'WEDNESDAY' | 'THURSDAY'  | 'FRIDAY'    |
                      '2022-08-02',               '2022-08-04',
    ]
    live_months = [
        march_2022, 
        april_2022, 
        may_2022,
        june_2022,
        july_2022,
        august_2022,
    ]
    days = []
    for l in live_months:
        days += l
    return days



def live_dates_model_3():
    march_2022 = [
    #  |  'MONDAY'  |  'TUESDAY'  | 'WEDNESDAY' | 'THURSDAY'  | 'FRIDAY'    |
                                                  '2022-03-24',
                                                  '2022-03-31',
        ]
    april_2022 = [               
    #  |  'MONDAY'  |  'TUESDAY'  | 'WEDNESDAY' | 'THURSDAY'  | 'FRIDAY'    |
                      '2022-04-05',               
                      '2022-04-12',               
                      '2022-04-19',               
                      '2022-04-26',               
        ]
    may_2022 = [
    #  |  'MONDAY'  |  'TUESDAY'  | 'WEDNESDAY' | 'THURSDAY'  | 'FRIDAY'    |
                      '2022-05-03',               
                      '2022-05-10',                
                                                  '2022-05-19',
                                                  '2022-05-26',
                      '2022-05-31',
        
        ]
    june_2022 = [
    #  |  'MONDAY'  |  'TUESDAY'  | 'WEDNESDAY' | 'THURSDAY'  | 'FRIDAY'    |
                                                  '2022-06-02',
                                                  '2022-06-09',
                                                  '2022-06-16',
                                                  '2022-06-23',
                                                  '2022-06-30',
        ]
    july_2022 = [
    #  |  'MONDAY'  |  'TUESDAY'  | 'WEDNESDAY' | 'THURSDAY'  | 'FRIDAY'    |
                      '2022-07-05',               
                                                  '2022-07-14',
                      '2022-07-19',               
                      '2022-07-26',               
        ]
    august_2022 = [
    #  |  'MONDAY'  |  'TUESDAY'  | 'WEDNESDAY' | 'THURSDAY'  | 'FRIDAY'    |
                                                              '2022-08-05',
    ]
    live_months = [
        march_2022, 
        april_2022, 
        may_2022,
        june_2022,
        july_2022,
        august_2022,
    ]
    days = []
    for l in live_months:
        days += l
    return days