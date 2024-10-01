from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Define the data model for a package
class Package(BaseModel):
    packageid: int
    packagename: str
    hotelname: str
    country: str
    destination: str

# Sample list of packages
packages = [
    Package(packageid=1, packagename="Beach Getaway", hotelname="Seaside Resort", country="USA", destination="Miami"),
    Package(packageid=2, packagename="Mountain Adventure", hotelname="Mountain Lodge", country="Canada", destination="Banff"),
    Package(packageid=3, packagename="Cultural Experience", hotelname="City Center Hotel", country="Italy", destination="Rome"),
]

@app.get("/")
async def index():
    return {"message": "Hello World"}

@app.get("/package", response_model=List[Package])
async def get_packages():
    return packages
