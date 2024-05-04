from fastapi import FastAPI

import requests

app = FastAPI()

@app.get("/")
def root():
    URL = "'x-api-key'?api_key=ive_oQmRa1nyv45JtYFmRn7onvEI41iwaBhZZnPZDopjHO5qoAuq7J7fpVKcC4606QrG"
    
    contents = requests.get(URL).text
    
    return { "message": contents }

@app.get("/home")
def home():
    return {"message": "Home!" }