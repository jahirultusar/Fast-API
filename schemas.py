from pydantic import BaseModel, ConfigDict, Field

# Base schema for posts creation 
class PostBase(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    content: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=50)

# Schema for creating a new post
class PostCreate(PostBase):
    pass

# Schema for responding with a post
class PostResponse(PostBase):
    id: int
    date_posted: str

    model_config = ConfigDict(from_attributes=True)

