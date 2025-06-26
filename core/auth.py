from fastapi import APIRouter
from pydantic import BaseModel, EmailStr

from database.auth import Register_User, Login_User, Is_User_Exist

from smtp.auth import Send_Verification_Code

auth_router = APIRouter(
    prefix="/auth",          
    tags=["Authentication"],       
)

@auth_router.get("/")
def register():
    return {"message": "Authentication endpoint"}


# User registration model
class UserRegister(BaseModel):
    role: str
    name: str
    email: EmailStr
    password: str

    dob: str
    gender: str
    phone: int
    address: str
    country: str
    state: str

    disability_type: list[str] = []
    disability_severity: str = None
    assistive_devices: str = None
    preferred_communication: str = None

    emergency_name: str = None
    emergency_phone: str = None
    emergency_relation: str = None

    additional_notes: str = None

# Register endpoint
@auth_router.post("/register")
def register(data: UserRegister):
    msg = Register_User(data)
    return {"message": msg}


class UserLogin(BaseModel):
    email: EmailStr
    password: str

@auth_router.post("/login")
def login(data: UserLogin):
    result =  Login_User(data)
    return {"message": result}


class UserVerification(BaseModel):
    email: EmailStr

@auth_router.post("/verify_code")
def verify_code(data: UserVerification):
    if Is_User_Exist(data.email):
        return {"message": "User already exists with this email."}
    else:
        code = Send_Verification_Code(data.email)
        return {
            "message": f"Verification code sent to your email: {data.email}.",
            "code": code
        }
    

class UserPasswordReset(BaseModel):
    email: EmailStr

@auth_router.post("/password_reset")
def verify_code(data: UserPasswordReset):
    if Is_User_Exist(data.email):
        return {"message": True}
    else:
        return {"message": False}