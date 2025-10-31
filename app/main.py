from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import datetime
from typing import List
from . import models, schemas
from .db import Base, engine
from fastapi import FastAPI
from .routers import auth_router, admin_router, user_router
from .exceptions import BookingException, booking_exception_handler, integrity_error_handler
from sqlalchemy.exc import IntegrityError

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Movie Booking System")

app.include_router(auth_router.router)
app.include_router(admin_router.router)
app.include_router(user_router.router)

app.add_exception_handler(BookingException, booking_exception_handler)
app.add_exception_handler(IntegrityError, integrity_error_handler)