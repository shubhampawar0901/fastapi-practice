from fastapi import BackgroundTasks, FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from .models import Booking, BookingSeat, User
from sqlalchemy.orm import Session 
import time

# def send_confirmation_booking