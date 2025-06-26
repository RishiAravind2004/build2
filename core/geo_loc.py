from fastapi import APIRouter
from pydantic import BaseModel
import reverse_geocoder as rg
import datetime 
from database.geo_loc import Update_User_GeoLocation, Get_User_location

geoloc_router = APIRouter(
    prefix="/loc",          
    tags=["GeoLocation"],       
)

@geoloc_router.get("/")
def geo_loc():
    return {"message": "Geo Location endpoint"}


class UpdateGeoLoc(BaseModel):
    uuid: str
    lat: float
    lon: float

@geoloc_router.post("/geoloc_update")
def update_user_geolocation(data: UpdateGeoLoc):
    res = Update_User_GeoLocation(data)
    return {"message": res}



class GetGeoLoc(BaseModel):
    uuid: str

# reverse the coordinates to location information
def reverseGeocode(lat, lon, last_update_date):
    results = rg.search([(lat, lon)])

    if results:
        loc = results[0]

        # Format date to dd/mm/yyyy HH:MM:SS
        formatted_date = last_update_date.strftime('%d/%m/%Y %H:%M:%S')

        description = (
            f"📍 You are near '{loc['name']}', "
            f"in the district 🏙️ '{loc['admin2']}', "
            f"state 🗺️ '{loc['admin1']}', "
            f"country 🌍 '{loc['cc']}'.\n"
            f"🕒 Last location update was on 📆 {formatted_date}."
        )

        print(description)
        return description

    else:
        error_msg = "❌ No location found for the given coordinates."
        print(error_msg)
        return error_msg



@geoloc_router.post("/get_geoloc")
def get_user_geolocation(data: GetGeoLoc):
    res = Get_User_location(data)
    if res == "User not found":
        return {"message": "User not found with this uuid"}
    elif res.get("latitude") is None or res.get("longitude") is None:
        return {"message": "User location data not available"}

    else:
        # Perform reverse geocoding
        rev_res = reverseGeocode(
            res["latitude"], res["longitude"], res["last_updated"]
        )

        return {
            "message": "User location fetched successfully",
            "location_details": rev_res,
            "coordinates": res
        }