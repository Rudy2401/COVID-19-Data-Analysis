import pandas as pd
import matplotlib.pyplot as plt


URL = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series'
df_global_confirmed = pd.read_csv(f'{URL}/time_series_covid19_confirmed_global.csv')
df_us_confirmed = pd.read_csv(f'{URL}/time_series_covid19_confirmed_US.csv')
df_us_deaths = pd.read_csv(f'{URL}/time_series_covid19_deaths_US.csv')
df_global_confirmed = pd.read_csv(f'{URL}/time_series_covid19_confirmed_global.csv')

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
    df_state.plot()
    plt.grid()

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
    df_state.plot()
    plt.grid()

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
    df_pct_change.plot()
    plt.grid()

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
    df_pct_change.plot()
    plt.grid()

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
    df_state.plot()
    plt.grid()

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
    df_pct_change.plot()
    plt.grid()


def main():
    us_plot_deaths()
    us_plot_confirmed()
    us_pct_change_confirmed()
    us_pct_change_deaths()
    global_plot_confirmed()
    global_pct_change_confirmed()
    plt.show()

if __name__ == '__main__':
    main()
