from database.setup import Get_Connection
from datetime import datetime

# func to update user geolocation
def Update_User_GeoLocation(data):
    connection, cursor = Get_Connection()

    try:

        # Update latitude, longitude, and timestamp
        cursor.execute(
            """
            UPDATE UserTB
            SET Latitude = %s,
                Longitude = %s,
                Last_Location_Updated = %s
            WHERE UUID = %s
            """,
            (
                data.latitude,
                data.longitude,
                datetime.now(),
                data.uuid
            )
        )
        connection.commit()
        return "Location updated successfully"

    except Exception as e:
        connection.rollback()
        return f"Error: {str(e)}"

# func to get user geoloc informations

def Get_User_location(data):
    connection, cursor = Get_Connection()

    try:
        cursor.execute(
            """
            SELECT 
                Latitude,
                Longitude,
                Last_Location_Updated
            FROM UserTB
            WHERE UUID = %s
            """,
            (data.uuid,)
        )

        user_location = cursor.fetchone()

        if user_location:
            return {
                "latitude": user_location["latitude"],
                "longitude": user_location["longitude"],
                "last_updated": user_location["last_location_updated"]
            }
        else:
            return {"error": "User not found"}

    except Exception as e:
        return {"error": str(e)}
