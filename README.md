# rental_predictor

## Project Overview
Interactive data science project using django / postgresql / various python data science libraries / AWS

The goal here is for me (Doug) to learn more python while teaching my friend Tyler some software engineering strategies
such as model view controller frameworks and testing. At the same time he'll be working on the data science models, while I
work more on the controller's and views. 

The project we've selected is to make is an interactive web application with 2 main features: 
1. Interactive Map - where the user has the ability to mouse-over and see details for over 3000 AirBNB listings in the Boston, USA area.
2. Rental prediction - where the user can enter details of any apartment he chooses in the Boston area and get a prediction for the price he would be able to charge.

## Implementation

#### Django Framework


#### PostgreSQL Database
- Initially stand-alone but may be hosted with Amazon RDS.
- 1 table - listings (16 columns)

#### ETL
- Download listings and reviews files 1 per month.
- cleaned and formatted with pandas
- loaded into db

#### Front-End
- Front-end interactive app pulls data from db
- interactive data viz - map with listings (price, availability, etc.)
- ML interface
- dash, plotly, js, html, css

#### Machine Learning
- ML Prediction - input housing info for new house and algorithm predicts revenue
- db -> ml algorithm -> training -> ml endpoint that sits on it's server in AWS
- Eventually we may host the ML in AWS Sagemaker.

## Architecture					
The project will be hosted in AWS.

The architecture includes:
1 VPC, 1 public subnet, 1 private subnet, 4 EC2 instance servers.									
					
#### VPC					
Public subnet					
- LB Server					
					
Private subnet					
- APP Server
- DB Server
- ML server

## Project Files

## Acknowledgements

