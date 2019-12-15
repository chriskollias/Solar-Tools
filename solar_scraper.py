import pandas as pd
import matplotlib.pyplot as plt

'''
# Declare all variables as strings. Spaces must be replaced with '+', i.e., change 'John Smith' to 'John+Smith'.
# Define the lat, long of the location and the year
lat, lon, year = 33.2164, -97.1292, 2010
# You must request an NSRDB api key from the link above
api_key = 'iaPo35XpUtTy9vaDWJOGr1h5faigaVM1QAvfeei9'
# Set the attributes to extract (e.g., dhi, ghi, etc.), separated by commas.
attributes = 'ghi,dhi,dni,wind_speed,air_temperature,solar_zenith_angle'
# Choose year of data
year = '2010'
# Set leap year to true or false. True will return leap day data if present, false will not.
leap_year = 'false'
# Set time interval in minutes, i.e., '30' is half hour intervals. Valid intervals are 30 & 60.
interval = '30'
# Specify Coordinated Universal Time (UTC), 'true' will use UTC, 'false' will use the local time zone of the data.
# NOTE: In order to use the NSRDB data in SAM, you must specify UTC as 'false'. SAM requires the data to be in the
# local time zone.
utc = 'false'
# Your full name, use '+' instead of spaces.
your_name = 'Chris+Kollias'
# Your reason for using the NSRDB.
reason_for_use = 'beta+testing'
# Your affiliation
your_affiliation = 'none'
# Your email address
your_email = 'chriskollias500@gmail.com'
# Please join our mailing list so we can keep you up-to-date on new developments.
mailing_list = 'true'

# Declare url string
url = 'http://developer.nrel.gov/api/solar/nsrdb_psm3_download.csv?wkt=POINT({lon}%20{lat})&names={year}&leap_day={leap}&interval={interval}&utc={utc}&full_name={name}&email={email}&affiliation={affiliation}&mailing_list={mailing_list}&reason={reason}&api_key={api}&attributes={attr}'.format(year=year, lat=lat, lon=lon, leap=leap_year, interval=interval, utc=utc, name=your_name, email=your_email, mailing_list=mailing_list, affiliation=your_affiliation, reason=reason_for_use, api=api_key, attr=attributes)
# Return just the first 2 lines to get metadata:
df = pd.read_csv(url, nrows=20000)
# See metadata for specified properties, e.g., timezone and elevation
#timezone, elevation = df['Local Time Zone'], df['Elevation']

df.to_csv('solar_info.csv')
'''

class NREL_API():

    def __init__(self):
        pass

    def get_monthly_averages(self, lat, long, year, attributes=['GHI', 'DHI', 'DNI']):


df = pd.read_csv('solar_info.csv')

#print(df.columns)

real_columns = df.iloc[1, :11]

new_df = pd.DataFrame(columns=real_columns)

temp_df = df.iloc[2:, :11]
temp_df.columns = new_df.columns
new_df = pd.concat([new_df, temp_df])

#Change the column datatypes to float32
new_df = new_df.astype('float32')

#print('new_df columns ', new_df.columns)

#Calculate monthly averages and put them in new dataframe
monthly_averages = new_df.groupby(['Month']).mean()
#print(monthly_averages)

monthly_averages.to_csv('help.csv')


monthly_averages = pd.read_csv('help.csv')

#print('monnthly avgs columns ', cols)
#monthly_averages = monthly_averages[[cols[0]] + cols[4:]]
#monthly_averages.to_csv('new_df.csv')

#print(cols)
#print(monthly_averages.columns)

#['Year', 'GHI', 'DHI', 'DNI', 'Wind Speed', 'Temperature', 'Solar Zenith Angle']

plt.xlabel('Month')
plt.ylabel('Irradiance w/m^2')


plt.plot(monthly_averages.Month, monthly_averages.GHI, label='GHI')
plt.plot(monthly_averages.Month, monthly_averages.DHI, label='DHI')
plt.plot(monthly_averages.Month, monthly_averages.DNI, label='DNI')

plt.legend()
plt.show()

