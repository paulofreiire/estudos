from pydantic import BaseModel, EmailStr, HttpUrl, ValidationError

class User(BaseModel):
    email: EmailStr
    website: HttpUrl

# Valid
user = User(email="jdoe@example.com", website="https://www.example.com")
# email='jdoe@example.com' website=HttpUrl('https://www.example.com', scheme='https', host='www.example.com',tld='com', host_type='domain')
print(user)