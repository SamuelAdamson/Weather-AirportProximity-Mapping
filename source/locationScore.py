# Calculate location score for each weather station
# Libraries used - haversine, sys

from haversine import haversine, Unit
import sys

# Scoring:
#   Each weather station location is given a score based on temp, precipitation
#       with 0 being the ideal place to live (perfect weather, at an airport)
#    Portion of the score is based on proximity the airport
#       - haversine formula to find distance
#       - closer to the airport, lower score
#    Portion of the score is based on Weather
#       - lower precipitation, lower score
#       - mild temperatures, lower score

def calculateScores(stations, airports):
    # Initialize array for score for each station
    scores = [0] * len(stations)
    namingFlags = ["AIRPORT", "ARPT", "REGIONAL AIR", "MUNICIPAL AIR"]


    # For each weather station
    for i in range(0,len(stations)):

        # Multiplier for temperature and precipitation scores
        tempScore = 0.327 * abs(stations[i][1] - 72.0)
        precipScore = 0.234 * stations[i][0]

        # Distance to airport score
        airpScore = -1
        # Check proximity - if airport is in station name, score is 0
        for substr in namingFlags:
            if substr in stations[i][2]:
                airpScore = 0.0 # Station is 0 miles from airport, 0 score


        # Find minimum distance to nearest airport
        airpDist = sys.float_info.max
        # If airport score has not been updated
        if airpScore < 0.0:
            for airp in airports:
                # Distance to airport
                dist = haversine((airp[1], airp[2]), (stations[i][3], stations[i][4]))
                if dist < airpDist:
                    airpDist = dist

            # Airport distance multiplier
            airpScore =  0.20 * airpDist


        # Update score to sum of scores
        scores[i] = airpScore + tempScore + precipScore


    return scores
