from pydantic import BaseModel, EmailStr, Field, HttpUrl, constr, validator
from datetime import datetime, timedelta
from typing import List, Optional

#Auth
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr
    role: str

    class Config:
        orm_mode = True

# Theatres

class TheaterCreate(BaseModel):
    name: str
    address: Optional[str]

class TheaterOut(BaseModel):
    id: int


    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

# Screens

class ScreenCreate(BaseModel):
    id: int
    capacity: Optional[int] =0
    theatre_id: int

class ScreenOut(BaseModel):
    id: int
    screen_id: int
    label: str
    class Config:
        orm_mode = True

# Seats
    
class SeatCreate(BaseModel):
    id: int
    screen_id: int
    label: str
    class Config:
        orm_mode = True

class SeatOut(BaseModel):
    id: int
    screen_id: int
    label: str

    class Config:
        orm_mode = True

# Movies

class MovieCreate(BaseModel):
    title: str
    description: Optional[str]
    duration_minutes: Optional[int] = 0

class MovieOut(BaseModel):
    id: int

    class Config:
        orm_mode = True

# Shows

class ShowCreate(BaseModel):
    moview_id: int
    screen_id: int
    start_time: datetime
    price: float

class ShowOut(BaseModel):
    id: int
    movie_id: int
    screen_id: int
    start_time: datetime
    price: float
    is_active: bool

    class Config:
        orm_mode = True

# Bookings

class BookingRequest(BaseModel):
    show_id: int
    seat_labels: List[str]


class BookingSeatOut(BaseModel):
    id: int
    seat_label: str

    class Config:
        orm_mode = True
class BookingOut(BaseModel):
    id:int
    user_id: int
    show_id: int
    created_at: datetime
    status: str
    seats: List[BookingSeatOut]

    class Config:
        orm_mode = True
