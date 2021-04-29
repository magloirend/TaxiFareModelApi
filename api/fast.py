import joblib

# write some code for the API here
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)
@app.get("/")
def index():
    return {"greeting": "Hello world"}

@app.get("/predict_fare")
def predict(key,pickup_datetime,pickup_longitude,pickup_latitude,dropoff_longitude,dropoff_latitude,passenger_count):


    x = dict(
      key= key,
      pickup_datetime= pickup_datetime,
      pickup_longitude= float(pickup_longitude),
      pickup_latitude= float(pickup_latitude),
      dropoff_longitude= float(dropoff_longitude),
      dropoff_latitude= float(dropoff_latitude),
      passenger_count= int(passenger_count)
    )
    # data_dict = pd.DataFrame.from_records(data)
    data = pd.DataFrame.from_records([x])
    # print(data_dict)


    pipeline = joblib.load('./model.joblib')
    y_pred = float(pipeline.predict(data)[0])

    return { 'prediction' : y_pred}

