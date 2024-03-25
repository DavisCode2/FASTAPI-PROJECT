from datetime import datetime
from typing import Literal
from pydantic import BaseModel, EmailStr


class PostBase(BaseModel):
    """Define the pydantic model for input data validation"""

    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    """Creating a post"""

    pass


class UserOut(BaseModel):
    """Response model to user input data"""

    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        """For the pydantic model to read the sqlalchemy data"""

        from_attributes = True


class Post(PostBase):
    """The schema of the response to the user"""

    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        """For the pydantic model to read the sqlalchemy data"""

        from_attributes = True


class PostResponse(BaseModel):
    Post: Post
    votes: int

    class Config:
        """For the pydantic model to read the sqlalchemy data"""

        from_attributes = True


class UserCreate(BaseModel):
    """Schema for the user data"""

    email: EmailStr
    password: str


class UserLogin(BaseModel):
    """model for the user login information"""

    email: EmailStr
    password: str


class Token(BaseModel):
    """Response model for the generated user token"""

    access_token: str
    token_type: str


class TokenData(BaseModel):
    """Data contained in the user token"""

    username: str | None = None


class Vote(BaseModel):
    """Schema for the vote route"""

    post_id: int
    dir: Literal[0, 1]
