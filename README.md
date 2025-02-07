![Language](https://img.shields.io/badge/Language-Python-yellow)
![Framework](https://img.shields.io/badge/Framework-Flask-brightgreen)
![Framework](https://img.shields.io/badge/API-Google-red)
![Framework](https://img.shields.io/badge/Model-lightGBM-blue)
![Framework](https://img.shields.io/badge/DB-SQLite-pink)
# New York City taxi price prediction 
## Data_Analysis_and_Visualization_Final_Project

### TITLE: Is Lyft really cheaper than Taxi?
    Teammates: S Zhao, H Wang, X Zhang, Y Xiao and Y ke
    Main responsibility: Web construction of Front/back-ends; time/data clustering and experiment; data cleaning and processing; experiment and analysis; regression model design
### Process and features:

1. **Data**: Download from NYC Taxi & Limousine Commission https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page
2. **Data Processing and Refining**: Use Spark on Databricks (coding in Scala) https://community.cloud.databricks.com/login.html
3. **Data Cluster**: k-means(coding in Python), do cluster to time, distance, start position and desination
4. **Model**: Regression machine learning(coding in Python)
5. **Model training**: Microsoft lightGBM framework, regression module
6. **Model test and evaluation**: Cross validation, Morte Carlo Simulation, TP/TN/FP/FN (expected)
7. **Visulization**: Draw bar chart, line chart and heatmap to show the comparation between Lyft and Taxi in NYC based on D3.js and Tableau
8. **Web**: Based on Flask structure, use Google Map APIs to get position information such as latitude, longtitude, trip distance, trip duration; use jQuery to implement the data transfer between frontend and backend; use D3.js to load NYC open data taxi zone json file to transfer coordinate to location id. Uber API price
9. **Document**: Poster design $ report compile

### Run 
$ cd Map_web_with_model   
$ cd map  
$ pipenv install --dev  
$ pipenv shell  
$ export FLASK_ENV=development  
$ export FLASK_APP=map   
$ flask initdb  
$ flask run  
$ Running on(local)http://127.0.0.1:5000/  

### Demo(Interactive web)
![image](https://github.com/SKZhao97/NYC_Taxi_Price_Prediction/blob/master/Demo.gif)
**Future improvement**: Login, register, more pages, more decorations, more database operations and publish

### Structure
![Demo](https://github.com/SKZhao97/NYC_Taxi_Price_Prediction/blob/master/Map_web_with_model/web_structure.jpg)
![Prediction](https://github.com/SKZhao97/NYC_Taxi_Price_Prediction/blob/master/Prediction_Workflow.png)

### License
This project is licensed under the "[MIT License](https://opensource.org/licenses/MIT)" (see the LICENSE file for details).
