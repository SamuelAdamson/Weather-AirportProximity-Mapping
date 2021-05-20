# Make API Requests for data, store data in lists
# Libraries used - google cloud

from google.cloud import bigquery
from authenticateGCloud import authenticate

# Query for weather data
#   Get avg temp for each station along with precipitation sum
#   Get latitude and longitude for station
#   Ignore data entries with missing precipitation/temperature mesaurements
queryWeath = """
        SELECT
            SUM(prcp), AVG(temp), name, lat, lon
        FROM(
            SELECT
                temp, prcp, name, lat, lon
            FROM
                `bigquery-public-data.noaa_gsod.gsod2020` weath
            JOIN
                `bigquery-public-data.noaa_gsod.stations` sta
            ON
                weath.stn = sta.usaf
                AND weath.wban = sta.wban
            WHERE
                country = 'US'
                AND state NOT IN ('AK', 'AS', 'BC', 'CR', 'FM', 'GU', 'HI', 'JQ',
                    'ON', 'PC', 'PR', 'PW', 'QC', 'UM', 'VI', 'YK', 'YT', 'NULL')
                AND prcp < 90
                AND temp < 1000)
        GROUP BY
            name, lat, lon
        ORDER BY
            name
"""

# Query for airport data
#   Get name, latitude, and longitude for each US airport
queryAirp = """
        SELECT
            name, latitude, longitude
        FROM
            `bigquery-public-data.faa.us_airports`
        WHERE
            country = 'United States'
            AND state_abbreviation != 'AK'
            AND state_abbreviation != 'HI'
            AND airport_type = 'Aerodome'
"""

# Create authenticated client
client = authenticate();

# Execute query for weather data and return data as list
def queryWeatherJob():
    # Store API request result
    queryWeathResult = client.query(queryWeath)

    # Convert Data to list
    weathList = [[row[0],row[1],row[2],row[3],row[4]]
                  for row in queryWeathResult]

    # Return our result
    return weathList


# Execute query for weather data and return data as list
def queryAirportJob():
    # Store API request result
    queryAirpResult = client.query(queryAirp)

    # Convert Data to list
    airpList = [[row[0], row[1], row[2]]
                 for row in queryAirpResult]

    # Return our result
    return airpList
