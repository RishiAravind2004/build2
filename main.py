
# API application of BumbleBeeZ

# app.py
from fastapi import FastAPI
from core.auth import auth_router
from core.geo_loc import geoloc_router
from database.setup import Setup_Database
from smtp.mail import Setup_Email_Test
from utils.prints import warning



# Initialize the database connection
warning("=============  Database Setup  =============")
Setup_Database()
warning("=============  End of Database Setup  =============")

Setup_Email_Test()
app = FastAPI()

app.include_router(auth_router) 
app.include_router(geoloc_router)
# Root route
@app.get("/")
def read_root():
    return {"message": "Welcome to BumbleBeeZ API 🐝"}


