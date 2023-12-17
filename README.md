# CAPSTONE PROJECT - NLP

## PROBLEM STATEMENT

- **DOMAIN** Industrial safety. NLP based Chatbot.
- **CONTEXT** The database comes from one of the biggest industry in Brazil and in the world. It is an urgent need for industries/companies around the globe to understand why employees still suffer some injuries/accidents in plants. Sometimes they also die in such environment.
- **DATA DESCRIPTION** This  The  database  is  basically  records  of  accidents  from  12  different  plants  in  03  different  countries  which  every  line  in  the  data  is  an occurrence of an accident.

### Data set columns description: 

- **Data**: timestamp or time/date information
- **Countries**: which country the accident occurred (anonymised)
- **Local**: the city where the manufacturing plant is located (anonymised)
- **Industry** sector: which sector the plant belongs to
- **Accident** level: from I to VI, it registers how severe was the accident (I means not severe but VI means very severe)
- **Potential** Accident Level: Depending on the Accident Level, the database also registers how severe the accident could have been (due to other factors involved in the accident)
- **Genre**: if the person is male of female
- **Employee** or Third Party: if the injured person is an employee or a third party
- **Critical** Risk: some description of the risk involved in the accident
- **Description**: Detailed description of how the accident happened.

Link to download the dataset: https://www.kaggle.com/ihmstefanini/industrial-safety-and-health-analytics-database

**PROJECT OBJECTIVE** 

Design  a  ML/DL  based  chatbot  utility  which  can  help  the  professionals  to  highlight  the  safety  risk  as  per  the  incident description.

## Run Project
```
docker compose build 
docker compose up -d
```

## FrontEnd - Vite-ReactJS
- The front end chat bot is implemented with the vite-reactJS and dockerized for easy deployment

## Backend - Flask ##
- The back end developed using the flask framework. Flask is used load the pickle file and expose the api which will be consumed by the frond end

## Model Development
- NLP Model is developed using the Google Colab and detailed explanation and the development steps is explained in the .ipynb file
- [.ipynb File](./Others/Chatbot_NLP_Industrial+Safety.ipynb)
- [Report File](./Others/Chatbot_NLP_Industrial+Safety_Interim+Report.pdf)


