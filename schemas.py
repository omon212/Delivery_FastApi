from pydantic import BaseModel
from typing import Optional

class Signupmodel(BaseModel):
    id: Optional[int]
    username: str
    email: str
    password: str
    is_staff: Optional[bool]
    is_active: Optional[bool]


    class Config:
        from_attributes = True
        json_schema_extra = {
            'example': {
                'username': 'omonullo',
                'email': 'omonnuloraimkulov@gmail.com',
                'password': 'omonullo66',
                'is_staff': False,
                'is_active': True
            }
        }
