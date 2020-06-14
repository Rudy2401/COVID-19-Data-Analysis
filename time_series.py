import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

URL = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series'
df_global_confirmed = pd.read_csv(f'{URL}/time_series_covid19_confirmed_global.csv')
df_us_confirmed = pd.read_csv(f'{URL}/time_series_covid19_confirmed_US.csv')
df_us_deaths = pd.read_csv(f'{URL}/time_series_covid19_deaths_US.csv')
df_global_deaths = pd.read_csv(f'{URL}/time_series_covid19_deaths_global.csv')

GLOBAL_CONFIRMRED_THRESHOLD = 100000
GLOBAL_DEATHS_THRESHOLD = 25000
US_STATES_CONFIRMRED_THRESHOLD = 75000
US_STATES_DEATHS_THRESHOLD = 5000

def us_plot_deaths():
    df = df_us_deaths.melt(id_vars=['UID', 'iso2', 'iso3', 'code3', 'FIPS', 'Admin2', 'Province_State', 'Country_Region', 'Lat', 'Long_', 'Combined_Key', 'Population'],
                           var_name='Date', 
                           value_name='Deaths')
    df['Date'] = pd.to_datetime(df['Date'])

    df_state = df.groupby(by=['Province_State', 'Date']).agg('sum')
    df_state.reset_index(inplace=True)
    df_state = df_state[(df_state['Deaths']>US_STATES_DEATHS_THRESHOLD)]

    df_state.drop(columns=['UID', 'code3', 'FIPS', 'Lat', 'Long_', 'Population'], inplace=True)
    df_state = pd.pivot(df_state, index='Date', columns='Province_State', values='Deaths')
    ax = df_state.plot(title='US States deaths time series',
                       grid=True,
                       lw=2,
                       colormap='jet',
                       markersize=10,
                       x_compat=True)
    ax.legend(loc='upper left', frameon=True, fancybox=True, shadow=True)
    ax.set_xlabel('Date')
    ax.set_ylabel('Confirmed')
    ax.patch.set_edgecolor('black')  
    ax.patch.set_linewidth('1') 

def us_plot_confirmed():
    df = df_us_confirmed.melt(id_vars=['UID', 'iso2', 'iso3', 'code3', 'FIPS', 'Admin2', 'Province_State', 'Country_Region', 'Lat', 'Long_', 'Combined_Key'],
                              var_name='Date', 
                              value_name='Confirmed')
    df['Date'] = pd.to_datetime(df['Date'])

    df_state = df.groupby(by=['Province_State', 'Date']).agg('sum')
    df_state.reset_index(inplace=True)
    df_state = df_state[(df_state['Confirmed']>US_STATES_CONFIRMRED_THRESHOLD)]

    df_state.drop(columns=['UID', 'code3', 'FIPS', 'Lat', 'Long_'], inplace=True)
    df_state = pd.pivot(df_state, index='Date', columns='Province_State', values='Confirmed')
    ax = df_state.plot(title='US States confirmed cases time series',
                       grid=True,
                       lw=2,
                       colormap='jet',
                       markersize=10,
                       x_compat=True)
    ax.legend(loc='upper left', frameon=True, fancybox=True, shadow=True)
    ax.set_xlabel('Date')
    ax.set_ylabel('Confirmed')
    ax.patch.set_edgecolor('black')  
    ax.patch.set_linewidth('1') 

def us_pct_change_confirmed():
    df = df_us_confirmed.melt(id_vars=['UID', 'iso2', 'iso3', 'code3', 'FIPS', 'Admin2', 'Province_State', 'Country_Region', 'Lat', 'Long_', 'Combined_Key'],
                              var_name='Date', 
                              value_name='Confirmed')
    df['Date'] = pd.to_datetime(df['Date'])

    df_state = df.groupby(by=['Province_State', 'Date']).agg('sum')
    df_state.reset_index(inplace=True)
    df_state = df_state[(df_state['Confirmed']>US_STATES_CONFIRMRED_THRESHOLD)]
    df_state.drop(columns=['UID', 'code3', 'FIPS', 'Lat', 'Long_'], inplace=True)
    df_state = pd.pivot(df_state, index='Date', columns='Province_State', values='Confirmed')
    df_pct_change = df_state.pct_change()
    ax = df_pct_change.plot(title='US States day-to-day percent change in confirmed cases',
                            grid=True,
                            lw=2,
                            colormap='jet',
                            markersize=10,
                            x_compat=True)
    ax.legend(loc='upper left', frameon=True, fancybox=True, shadow=True)
    ax.set_xlabel('Date')
    ax.set_ylabel('Percent Change')
    ax.patch.set_edgecolor('black')  
    ax.patch.set_linewidth('1') 

def us_pct_change_deaths():
    df = df_us_deaths.melt(id_vars=['UID', 'iso2', 'iso3', 'code3', 'FIPS', 'Admin2', 'Province_State', 'Country_Region', 'Lat', 'Long_', 'Combined_Key', 'Population'],
                           var_name='Date', 
                           value_name='Deaths')
    df['Date'] = pd.to_datetime(df['Date'])

    df_state = df.groupby(by=['Province_State', 'Date']).agg('sum')
    df_state.reset_index(inplace=True)
    df_state = df_state[(df_state['Deaths']>US_STATES_DEATHS_THRESHOLD)]
    df_state.drop(columns=['UID', 'code3', 'FIPS', 'Lat', 'Long_', 'Population'], inplace=True)
    df_state = pd.pivot(df_state, index='Date', columns='Province_State', values='Deaths')
    df_pct_change = df_state.pct_change()
    print(df_pct_change)
    ax = df_pct_change.plot(title='US States day-to-day percent change in deaths',
                            grid=True,
                            lw=2,
                            colormap='jet',
                            markersize=10,
                            x_compat=True)
    ax.legend(loc='upper left', frameon=True, fancybox=True, shadow=True)
    ax.set_xlabel('Date')
    ax.set_ylabel('Percent Change')
    ax.patch.set_edgecolor('black')  
    ax.patch.set_linewidth('1') 

def us_top_7_day_increase():
    df = df_us_confirmed.melt(id_vars=['UID', 'iso2', 'iso3', 'code3', 'FIPS', 'Admin2', 'Province_State', 'Country_Region', 'Lat', 'Long_', 'Combined_Key'],
                              var_name='Date', 
                              value_name='Confirmed')
    df['Date'] = pd.to_datetime(df['Date'])

    df_state = df.groupby(by=['Province_State', 'Date']).agg('sum')
    df_state.reset_index(inplace=True)
    df_state.drop(columns=['UID', 'code3', 'FIPS', 'Lat', 'Long_'], inplace=True)
    df_state = pd.pivot(df_state, index='Date', columns='Province_State', values='Confirmed')
    end_date = df_state.tail(1).index
    start_date = end_date - np.timedelta64(7, 'D')
    df_7 = df_state.loc[start_date].append(df_state.loc[end_date])
    df_7 = df_7.pct_change().multiply(100).tail(1)
    df_7 = df_7.T
    df_7 = df_7.reset_index()
    df_7.rename(columns={df_7.columns[1]: 'Percent Change'}, inplace=True)
    df_7.sort_values('Percent Change', ascending=False, inplace=True)
    df_7 = df_7.head(10)
    df_7 = df_7.reset_index(drop=['index']).set_index('Province_State')

    ax = df_7.plot(title='US States highest percent increase in confirmed cases in the last 7 days',
                   kind='bar',
                   grid=True,
                   lw=2,
                   color=[plt.cm.Paired(np.arange(len(df_7)))])
    ax.legend(loc='upper right', frameon=True, fancybox=True, shadow=True)
    ax.set_xlabel('State')
    ax.set_ylabel('Percent Change')
    ax.patch.set_edgecolor('black')  
    ax.patch.set_linewidth('1') 

def us_top_7_day_increase_deaths():
    df = df_us_deaths.melt(id_vars=['UID', 'iso2', 'iso3', 'code3', 'FIPS', 'Admin2', 'Province_State', 'Country_Region', 'Lat', 'Long_', 'Combined_Key', 'Population'],
                              var_name='Date', 
                              value_name='Deaths')
    df['Date'] = pd.to_datetime(df['Date'])

    df_state = df.groupby(by=['Province_State', 'Date']).agg('sum')
    df_state.reset_index(inplace=True)
    df_state.drop(columns=['UID', 'code3', 'FIPS', 'Lat', 'Long_'], inplace=True)
    df_state = pd.pivot(df_state, index='Date', columns='Province_State', values='Deaths')
    end_date = df_state.tail(1).index
    start_date = end_date - np.timedelta64(7, 'D')
    df_7 = df_state.loc[start_date].append(df_state.loc[end_date])
    df_7 = df_7.pct_change().multiply(100).tail(1)
    df_7 = df_7.T
    df_7 = df_7.reset_index()
    df_7.rename(columns={df_7.columns[1]: 'Percent Change'}, inplace=True)
    df_7.sort_values('Percent Change', ascending=False, inplace=True)
    df_7 = df_7.head(10)
    df_7 = df_7.reset_index(drop=['index']).set_index('Province_State')

    ax = df_7.plot(title='US States highest percent increase in deaths in the last 7 days',
                   kind='bar',
                   grid=True,
                   lw=2,
                   color=[plt.cm.Paired(np.arange(len(df_7)))])
    ax.legend(loc='upper right', frameon=True, fancybox=True, shadow=True)
    ax.set_xlabel('State')
    ax.set_ylabel('Percent Change')
    ax.patch.set_edgecolor('black') 
    ax.patch.set_linewidth('1') 

def global_plot_confirmed():
    df = df_global_confirmed.melt(id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'],
                                  var_name='Date', 
                                  value_name='Confirmed')
    df['Date'] = pd.to_datetime(df['Date'])

    df_state = df.groupby(by=['Country/Region', 'Date']).agg('sum')
    df_state.reset_index(inplace=True)
    df_state = df_state[(df_state['Confirmed']>GLOBAL_CONFIRMRED_THRESHOLD)]

    df_state.drop(columns=['Lat', 'Long'], inplace=True)
    df_state = pd.pivot(df_state, index='Date', columns='Country/Region', values='Confirmed')
    ax = df_state.plot(title='Global confirmed cases time series',
                       grid=True,
                       lw=2,
                       colormap='jet',
                       markersize=10,
                       x_compat=True)
    ax.legend(loc='upper left', frameon=True, fancybox=True, shadow=True)
    ax.set_xlabel('Date')
    ax.set_ylabel('Confirmed')
    ax.patch.set_edgecolor('black')  
    ax.patch.set_linewidth('1') 

def global_pct_change_confirmed():
    df = df_global_confirmed.melt(id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'],
                                  var_name='Date', 
                                  value_name='Confirmed')
    df['Date'] = pd.to_datetime(df['Date'])

    df_state = df.groupby(by=['Country/Region', 'Date']).agg('sum')
    df_state.reset_index(inplace=True)
    df_state = df_state[(df_state['Confirmed']>GLOBAL_CONFIRMRED_THRESHOLD)]

    df_state.drop(columns=['Lat', 'Long'], inplace=True)
    df_state = pd.pivot(df_state, index='Date', columns='Country/Region', values='Confirmed')
    df_pct_change = df_state.pct_change()

    ax = df_pct_change.plot(title='Global day-to-day percent change in confirmed cases',
                            grid=True,
                            lw=2,
                            colormap='jet',
                            markersize=10,
                            x_compat=True)
    ax.legend(loc='upper left', frameon=True, fancybox=True, shadow=True)
    ax.set_xlabel('Date')
    ax.set_ylabel('Percent Change')
    ax.patch.set_edgecolor('black')  
    ax.patch.set_linewidth('1') 

def global_plot_deaths():
    df = df_global_deaths.melt(id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'],
                                  var_name='Date', 
                                  value_name='Deaths')
    df['Date'] = pd.to_datetime(df['Date'])

    df_state = df.groupby(by=['Country/Region', 'Date']).agg('sum')
    df_state.reset_index(inplace=True)
    df_state = df_state[(df_state['Deaths']>GLOBAL_DEATHS_THRESHOLD)]

    df_state.drop(columns=['Lat', 'Long'], inplace=True)
    df_state = pd.pivot(df_state, index='Date', columns='Country/Region', values='Deaths')
    ax = df_state.plot(title='Global deaths time series',
                       grid=True,
                       lw=2,
                       colormap='jet',
                       markersize=10,
                       x_compat=True)
    ax.legend(loc='upper left', frameon=True, fancybox=True, shadow=True)
    ax.set_xlabel('Date')
    ax.set_ylabel('Deaths')
    ax.patch.set_edgecolor('black')  
    ax.patch.set_linewidth('1') 

def global_pct_change_deaths():
    df = df_global_deaths.melt(id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'],
                                  var_name='Date', 
                                  value_name='Deaths')
    df['Date'] = pd.to_datetime(df['Date'])

    df_state = df.groupby(by=['Country/Region', 'Date']).agg('sum')
    df_state.reset_index(inplace=True)
    df_state = df_state[(df_state['Deaths']>GLOBAL_DEATHS_THRESHOLD)]

    df_state.drop(columns=['Lat', 'Long'], inplace=True)
    df_state = pd.pivot(df_state, index='Date', columns='Country/Region', values='Deaths')
    df_pct_change = df_state.pct_change()

    ax = df_pct_change.plot(title='Global day-to-day percent change in deaths',
                            grid=True,
                            lw=2,
                            colormap='jet',
                            markersize=10,
                            x_compat=True)
    ax.legend(loc='upper left', frameon=True, fancybox=True, shadow=True)
    ax.set_xlabel('Date')
    ax.set_ylabel('Percent Change')
    ax.patch.set_edgecolor('black')  
    ax.patch.set_linewidth('1') 

def main():
    us_plot_deaths()
    us_plot_confirmed()
    us_pct_change_deaths()
    us_pct_change_confirmed()
    global_plot_confirmed()
    global_pct_change_confirmed()
    global_plot_deaths()
    global_pct_change_deaths()
    us_top_7_day_increase()
    us_top_7_day_increase_deaths()
    plt.show()

if __name__ == '__main__':
    main()
