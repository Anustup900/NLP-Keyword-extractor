# Recommendation system based on your Requirement

## Data
Model trainedon dummy data , please change the data points only like [window ID] , [jobID] etc based on your mentioned key names as per your data base . Only change the names of the input points as per your need.

## Dataset I used
The job descriptions have been scraped from linkedin.com and kaggle 
The data has been scraped by providing various keywords for technologies and title. However, there is some redundant data, rows with missing values etc.
This data has been preprocessed to remove redundancies and missing values to get more reliable output.

## Approaches
* Item based collaborative filtering:
In this algorithm, Users are represented as two vectors that contain the user IDE and jobs ID. The similarity between user ID and job ID is calculated by the cosine of the angle between the two vectors. Matrix of vectors is generated with rows and columns as User ID and job ID. Number represented in a row is matched to the User ID.
## Repo Structure
```
|
├── data
|   ├── has script to scrape the data
|
├── Script
|   ├── script to predict Similar users based on requirements using item based collaborative filtering
|
```
## For Output
Only integrate the script by changing the data and the data entry names and integrate it 

