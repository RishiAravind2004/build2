import random
from smtp.mail import Send_Email



def Send_Verification_Code(email: str):

    # Generate a random 6-digit verification code
    code = ''.join(random.choices("0123456789", k=6))

    subject = "🐝 BumbleBeeZ Email Verification"

    Body = f"""
Hi there! 👋

Thanks for joining **BumbleBeeZ** — where helpers and challengers connect to make life easier and more inclusive 💛.

🔐 Your email verification code is: **{code}**

Please enter this code in the app to complete your registration.

Need help or have questions? We’re always here for you!

With care,  
The BumbleBeeZ Team 🐝
"""

    Send_Email(email, subject, Body)
    return code
    
    