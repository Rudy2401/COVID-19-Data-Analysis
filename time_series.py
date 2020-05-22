import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pandas_profiling import ProfileReport


URL = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series'
df_global_confirmed = pd.read_csv(f'{URL}/time_series_covid19_confirmed_global.csv')
df_us_confirmed = pd.read_csv(f'{URL}/time_series_covid19_confirmed_US.csv')
df_us_deaths = pd.read_csv(f'{URL}/time_series_covid19_deaths_US.csv')
df_global_deaths = pd.read_csv(f'{URL}/time_series_covid19_deaths_global.csv')


def us_plot_deaths():
    df = df_us_deaths.melt(id_vars=['UID', 'iso2', 'iso3', 'code3', 'FIPS', 'Admin2', 'Province_State', 'Country_Region', 'Lat', 'Long_', 'Combined_Key', 'Population'],
                           var_name='Date', 
                           value_name='Deaths')
    df['Date'] = pd.to_datetime(df['Date'])

    df_state = df.groupby(by=['Province_State', 'Date']).agg('sum')
    df_state.reset_index(inplace=True)
    df_state = df_state[(df_state['Deaths']>3000)]

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
    df_state = df_state[(df_state['Confirmed']>50000)]

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
    df_state = df_state[(df_state['Confirmed']>50000)]
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
    df_state = df_state[(df_state['Deaths']>3000)]

    df_state.drop(columns=['UID', 'code3', 'FIPS', 'Lat', 'Long_', 'Population'], inplace=True)
    df_state = pd.pivot(df_state, index='Date', columns='Province_State', values='Deaths')
    df_pct_change = df_state.pct_change()
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

def global_plot_confirmed():
    df = df_global_confirmed.melt(id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'],
                                  var_name='Date', 
                                  value_name='Confirmed')
    df['Date'] = pd.to_datetime(df['Date'])

    df_state = df.groupby(by=['Country/Region', 'Date']).agg('sum')
    df_state.reset_index(inplace=True)
    df_state = df_state[(df_state['Confirmed']>50000)]

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
    df_state = df_state[(df_state['Confirmed']>75000)]

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
    df_state = df_state[(df_state['Deaths']>10000)]

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
    df_state = df_state[(df_state['Deaths']>10000)]

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
    us_pct_change_confirmed()
    us_pct_change_deaths()
    global_plot_confirmed()
    global_pct_change_confirmed()
    global_plot_deaths()
    global_pct_change_deaths()
    plt.show()

if __name__ == '__main__':
    main()
