import pandas as pd
import matplotlib.pyplot as plt
import time

'''
# Declare all variables as strings. Spaces must be replaced with '+', i.e., change 'John Smith' to 'John+Smith'.

# Specify Coordinated Universal Time (UTC), 'true' will use UTC, 'false' will use the local time zone of the data.
# NOTE: In order to use the NSRDB data in SAM, you must specify UTC as 'false'. SAM requires the data to be in the
# local time zone.
utc = 'false'

# See metadata for specified properties, e.g., timezone and elevation
#timezone, elevation = df['Local Time Zone'], df['Elevation']

'''

class NREL_API():
    #NSRDB api key, other necessary info
    api_key = 'iaPo35XpUtTy9vaDWJOGr1h5faigaVM1QAvfeei9'
    full_name = 'Chris+Kollias'
    reason_for_use = 'beta+testing'
    affiliation = 'none'
    email = 'chriskollias500@gmail.com'
    mailing_list = 'true'
    utc = 'false'

    def get_monthly_averages(self, lat_input, long_input, year_input, attributes_input):
        lat, lon = lat_input, long_input
        year = year_input

        # Set leap year to true or false. True will return leap day data if present, false will not.
        leap_year = 'false'

        # Set time interval in minutes, i.e., '30' is half hour intervals. Valid intervals are 30 & 60.
        interval = '30'

        # Set the attributes to extract (e.g., dhi, ghi, etc.), separated by commas.
        attributes = attributes_input

        # Uncomment to pull from API
        #solar_data_csv = self.__retrieve_data_from_api(lat, lon, year, interval, leap_year, attributes)
        #df = pd.read_csv(solar_data_csv)

        # For testing
        df = pd.read_csv('solar_info20200228184632.csv')

        graph_image = self.__display_csv_graph(df)

        return graph_image

    def __retrieve_data_from_api(self, lat, lon, year, interval, leap_year, attributes):
        # Declare url string
        url = 'http://developer.nrel.gov/api/solar/nsrdb_psm3_download.csv?wkt=POINT({lon}%20{lat})&names={year}&leap_day={leap}&interval={interval}&utc={utc}&full_name={name}&email={email}&affiliation={affiliation}&mailing_list={mailing_list}&reason={reason}&api_key={api}&attributes={attr}'.format(
            year=year, lat=lat, lon=lon, leap=leap_year, interval=interval, utc=self.utc, name=self.full_name,
            email=self.email, mailing_list=self.mailing_list, affiliation=self.affiliation, reason=self.reason_for_use,
            api=self.api_key, attr=attributes)
        print(url)
        print("CHECKPOINT A")
        df = pd.read_csv(url, nrows=20000)
        timestr = time.strftime("%Y%m%d%H%M%S")
        filename = 'solar_info' + timestr + '.csv'
        df.to_csv(filename)
        print("CHECKPOINT B")
        return filename

    def __display_csv_graph(self, df):
        real_columns = df.iloc[1, :11]

        new_df = pd.DataFrame(columns=real_columns)

        temp_df = df.iloc[2:, :11]
        temp_df.columns = new_df.columns
        new_df = pd.concat([new_df, temp_df])

        # Change the column datatypes to float32
        new_df = new_df.astype('float32')

        # Calculate monthly averages and put them in new dataframe
        monthly_averages = new_df.groupby(['Month']).mean()

        # TODO: Figure out why we have to do this
        monthly_averages.to_csv('help.csv')
        monthly_averages = pd.read_csv('help.csv')

        plt.xlabel('Month')
        plt.xticks(range(1, 13))
        plt.ylabel('Irradiance W/m^2')

        plt.plot(monthly_averages.Month, monthly_averages.GHI, label='GHI')
        plt.plot(monthly_averages.Month, monthly_averages.DHI, label='DHI')
        plt.plot(monthly_averages.Month, monthly_averages.DNI, label='DNI')

        plt.legend()
        filename = 'graph.png'
        return filename

    def __init__(self):
        pass

