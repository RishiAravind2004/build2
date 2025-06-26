from database.setup import Get_Connection
import psycopg2
import uuid

def Register_User(data):
    connection, cursor = Get_Connection()

    # Generate a unique UUID for the user
    new_uuid = str(uuid.uuid4()) 

    try:
        cursor.execute("""
            INSERT INTO UserTB (
                UUID, Role, Name, Email, Password,
                DOB, Gender, Phone, Address, Country, State,
                Disability_Type, Disability_Severity,
                Assistive_Devices, Preferred_Communication,
                Emergency_Name, Emergency_Phone, Emergency_Relation,
                Additional_Notes
            ) VALUES (%s, %s, %s, %s, %s,
                      %s, %s, %s, %s, %s, %s,
                      %s, %s,
                      %s, %s,
                      %s, %s, %s,
                      %s)
        """, (
            new_uuid, data.role, data.name, data.email, data.password,
            data.dob, data.gender, data.phone, data.address, data.country, data.state,
            data.disability_type or None, data.disability_severity or None,
            data.assistive_devices or None, data.preferred_communication or None,
            data.emergency_name or None, data.emergency_phone or None,
            data.emergency_relation or None,
            data.additional_notes or None
        ))

        connection.commit()
        return "User registered successfully"
    except psycopg2.errors.UniqueViolation:
        connection.rollback()
        return "Email already exists. Please use a different email."
    except Exception as e:
        connection.rollback()
        return f"Error: {str(e)}"




def Login_User(data):
    connection, cursor = Get_Connection()

    try:
        cursor.execute(
            "SELECT * FROM UserTB WHERE Email = %s",
            (data.email,)
        )
        user = cursor.fetchone()
        print(user)
        if user is None:
            return "User not found"
        
        if user["password"] != data.password:
            return "Incorrect password"

        return user

    except Exception as e:
        connection.rollback()
        return f"Error: {str(e)}"
    

def Is_User_Exist(email):
    connection, cursor = Get_Connection()

    try:
        cursor.execute(
            "SELECT * FROM UserTB WHERE Email = %s",
            (email,)
        )
        user = cursor.fetchone()

        if user is None:
            return False
        
        return True

    except Exception as e:
        return False, str(e)
