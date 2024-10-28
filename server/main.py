# Import the FastAPI framework and the generate_sample_recipe function
from fastapi import FastAPI
from data_generation.generate_dummy_data import generate_sample_recipe

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/dummy-data")
def get_dummy_data():
    return generate_sample_recipe()

# Run this with `uvicorn server.main:app --reload`