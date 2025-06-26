# database/schema.py
from utils.prints import info, error, success, warning

def Define_Tables_Schema():
    from database.setup import Get_Connection

    connection, cursor = Get_Connection()

    try:
        cursor.execute("""
            SELECT EXISTS (
                SELECT FROM information_schema.tables 
                WHERE table_schema = 'public' 
                AND table_name = 'usertb'
            );
        """)
        table_exists = cursor.fetchone()

        if table_exists:
            warning("Table 'UserTB' already exists.")
            info("Skipping table creation....")
        else:
            User_Table = """
                CREATE TABLE UserTB (

                    -- User Information

                    UUID TEXT PRIMARY KEY,
                    Role VARCHAR(10) NOT NULL,

                    Name VARCHAR(30) NOT NULL,
                    Email VARCHAR(100) UNIQUE NOT NULL,
                    Password TEXT NOT NULL,

                    -- Personal Information
                    DOB DATE NOT NULL,
                    Gender VARCHAR(10) NOT NULL,
                    Phone VARCHAR(15) NOT NULL,
                    Address TEXT NOT NULL,
                    Country VARCHAR(50) NOT NULL,
                    State VARCHAR(50) NOT NULL,

                    -- Disability Information

                    Disability_Type TEXT[],
                    Disability_Severity TEXT,
                    Assistive_Devices TEXT,
                    Preferred_Communication TEXT,

                    -- Emergency Contact Information
                    Emergency_Name VARCHAR(30),
                    Emergency_Phone VARCHAR(15),
                    Emergency_Relation VARCHAR(15),

                    -- Additional Notes
                    Additional_Notes TEXT,

                    -- Location Information

                    Latitude DOUBLE PRECISION,
                    Longitude DOUBLE PRECISION,
                    Last_Location_Updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,

                    -- Account Information

                    Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
                    Updated_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
                );
            """
            cursor.execute(User_Table)
            connection.commit()
            success("Table 'UserTB' created successfully.")

    except Exception as e:
        error(f"❌ Error creating table: {e}")
        
        connection.rollback()
