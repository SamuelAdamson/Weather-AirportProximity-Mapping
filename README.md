### Weather/Proximity to Airport Mapping

#### Prompt
This project was completed as a response to an interview task. The prompt was to find optimal location in the continental US to live based on quality of weather and close proximity to an airport. Additionally, data sources were limited to BigQuery public datasets, and the interviewer requested the project be completed using python and associated libraries. <br>

#### Planning
The posed prompt was fairly open ended (probably intentionally), so I felt as though I had a lot of directions I could go with the solution. I knew that I wanted my solution to have two charactersitics - a visual component and a range of options rather than one singular result. The first visual that came to mind was a heat map that showed a darker shade for regions that were more optimal in the scope of airport proximity and weather quality. I felt that building this visual alongside quantitave data would provide the interviewer with several options to choose from for the "optimal location". Additionally, setting this visual component as the goal for the project provided me with a clear path forward - 
* Collect, clean, and parse source data
* Compute an location score based on data characteristics
* Visualize data geographically based on location score
Completing each of these steps would allow me to display an aptitude for data cleaning, drawing conclusions from data, and visualizing data to demonstrate said conclusions. Additionally, in the process I would be able to demonstrate knowledge of SQL, Python, Pandas, and various plotting tools in python. <br>

#### Solution
With a plan in mind I began the implementation of my solution. To start off, I identified two different BigQuery public datasets which would enable me to execute my plan: [NOAA Global Surface Sumary of Day](https://console.cloud.google.com/marketplace/details/noaa-public/gsod) - weather reports associated with geographic coordinates and FAA US Airports - location of airports in the US. After building queries for these datasets to extract the data that would be valuable to our end goal, I calculated a "weather" score for each location available in the NOAA dataset based on the amount of precipitation received during the calendar year and closeness of the average annual temperature to 72 Farenheit. Each score was an unbounded floating point value greater than or equal to 0. The closer the score to 0, the more optimal that location is based on weather. <br><br>
At this point it is worth noting that this scoring system is very rudimentary. Some flaws in the system include the fact that average annual temperature does not really indicate that a location has mild temperatures, as the temperatures could fluctuate greatly throughout the year, but still average to 72 Farenheit. Additionally, there are many more factors to consider outside of preceiptation and weather when considering "good" weather. If I were to complete this project with a larger time frame, I would spend more time developing the scoring model. Primarily I would consider factors such as number of sunny days (without rain), number of days with temperature within a certain range, average humidity, and average air quality index. <br><br>
After computing a weather score for each location, I computed a location score using the distance from said location to the nearest airport. To compute this distance, I utilized the [haversine formula](https://en.wikipedia.org/wiki/Haversine_formula). This formula allows for calculating distance between two geographic coordinates while accounting for the curvature of the earth. The weather score and airport proximity scores are added together to produce the location's final score. <br><br>
With the scores in hand, I created our final visualizations using geopandas, geoplot, and matplotlib. The visualizations overlay the weather score data on maps of the continental US utilizing their geopgraphic locations. <br>

#### Figures
<div align="center">
  <img src="https://user-images.githubusercontent.com/70236734/177066693-9db0fc1d-05f8-48ba-a802-31f079bab0ec.png" />
  <img src="https://user-images.githubusercontent.com/70236734/177066723-8978e68c-ffed-4d51-9e43-e9b3af406d8d.png" />
</div>
The first figure depicted here is the heat map. Darker shades in this map represent densely packed locations with "good" weather and airport proximity scores. The second figure here shows each location for which data was available. Each location's hue is determined by its weather and airport proximity score.
