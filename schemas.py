from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, EmailStr


## Base schema for user creation and response
class UserBase(BaseModel):
    username: str = Field(min_length=1, max_length=50)
    email: EmailStr = Field(max_length=120)

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    image_file: str | None
    image_path: str


# Base schema for posts creation 
class PostBase(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    content: str = Field(min_length=1)

# Schema for creating a new post
class PostCreate(PostBase):
    User_id: int    ##### TEMPORARY

# Schema for responding with a post
class PostResponse(PostBase):
    id: int
    user_id: int
    date_posted: datetime
    author: UserResponse



