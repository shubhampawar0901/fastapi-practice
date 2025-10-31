from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, UniqueConstraint

from sqlalchemy.orm import relationship
from datetime import datetime
from .db import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, nullable=False, default="user")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    bookings = relationship("Booking", back_populates="user")

class Theatre(Base):
    __tablename__ = "theatres"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    screens = relationship("Screen", back_populates="theatre")

class Screen(Base):
    __tablename__ = "screens"
    id = Column(Integer, primary_key=True, index=True)
    theatre_id = Column(Integer, ForeignKey("theatres.id"), nullable=False)
    name = Column(String, nullable=False)
    capacity = Column(Integer, nullable=False)
    theatre = relationship("Theatre", back_populates="screens")
    seats = relationship("Seat", back_populates="screen")
    shows = relationship("Show", back_populates="screen")

class Seat(Base):
    __tablename__ = "seats"
    id = Column(Integer, primary_key=True, index=True)
    screen_id = Column(Integer, ForeignKey("screens.id"), nullable=False)
    label = Column(String, nullable=False) # row + number
    row = Column(String, nullable=False)
    number = Column(Integer, nullable=False)
    screen = relationship("Screen", back_populates="seats")
    __table_args__ = (UniqueConstraint("screen_id", "label", name="unix_screen_seat"),)

class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    duration = Column(Integer, nullable=False) # in minutes
    language = Column(String, nullable=False)
    shows = relationship("Show", back_populates="movie")

class Show(Base):
    __tablename__ = "shows"
    id = Column(Integer, primary_key=True, index=True)
    screen_id = Column(Integer, ForeignKey("screens.id"), nullable=False)
    movie_id = Column(Integer, ForeignKey("movies.id"), nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    price = Column(Integer, nullable=False) # in cents
    is_active = Column(Boolean, nullable=False, default=True)
    screen = relationship("Screen", back_populates="shows")
    movie = relationship("Movie", back_populates="shows")
    bookings = relationship("Booking", back_populates="show")

class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    show_id = Column(Integer, ForeignKey("shows.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    status = Column(String, nullable=False, default="confirmed") # pending, confirmed, cancelled
    user = relationship("User", back_populates="bookings")
    seats = relationship("Seat", secondary="booking_seats", back_populates="bookings")

class BookingSeat(Base):
    __tablename__ = "booking_seats"
    id = Column(Integer, primary_key=True, index=True)
    booking_id = Column(Integer, ForeignKey("bookings.id"), nullable=False)
    show_id = Column(Integer, ForeignKey("shows.id"), nullable=False)
    seat_label = Column(String, nullable=False)
    booking = relationship("Booking", back_populates="seats")
    show = relationship("Show", back_populates="bookings")

    __table_args__ = (UniqueConstraint("show_id", "seat_label", name="unix_booking_seat"),)