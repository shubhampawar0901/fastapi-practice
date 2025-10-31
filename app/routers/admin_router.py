from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..deps import get_db, require_admin
from .. import models, schemas
from datetime import datetime
from typing import List

router = APIRouter(prefix="/admin", tags=["Admin"],  dependencies=[Depends(require_admin)])

#Theatres
@router.post("/theatres", response_model=schemas.TheaterOut)
def create_theatre(theatre_in: schemas.TheaterCreate, db: Session = Depends(get_db)):
    theatre = models.Theatre(**theatre_in.dict())
    db.add(theatre)
    db.commit()
    db.refresh(theatre)
    return theatre

@router.put("/theatres/{theatre_id}", response_model=schemas.TheaterOut)
def update_theatre(theatre_id: int, theatre_in: schemas.TheaterCreate, db: Session = Depends(get_db)):
    theatre = db.query(models.Theatre).filter(models.Theatre.id == theatre_id).first()
    if not theatre:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Theatre not found")
    for key, value in theatre_in.dict().items():
        setattr(theatre, key, value)
    db.commit()
    db.refresh(theatre)
    return theatre

@router.delete("/theatres/{theatre_id}", response_model=schemas.TheaterOut)
def delete_theatre(theatre_id: int, db: Session = Depends(get_db)):
    theatre = db.query(models.Theatre).filter(models.Theatre.id == theatre_id).first()
    if not theatre:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Theatre not found")
    db.delete(theatre)
    db.commit()
    return theatre

#Screens
@router.post("/screens", response_model=schemas.ScreenOut)
def create_screen(screen_in: schemas.ScreenCreate, db: Session = Depends(get_db)):
    screen = models.Screen(**screen_in.dict())
    db.add(screen)
    db.commit()
    db.refresh(screen)
    return screen

@router.put("/screens/{screen_id}", response_model=schemas.ScreenOut)
def update_screen(screen_id: int, screen_in: schemas.ScreenCreate, db: Session = Depends(get_db)):
    screen = db.query(models.Screen).filter(models.Screen.id == screen_id).first()
    if not screen:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Screen not found")
    for key, value in screen_in.dict().items():
        setattr(screen, key, value)
    db.commit()
    db.refresh(screen)
    return screen

@router.delete("/screens/{screen_id}", response_model=schemas.ScreenOut)
def delete_screen(screen_id: int, db: Session = Depends(get_db)):
    screen = db.query(models.Screen).filter(models.Screen.id == screen_id).first()
    if not screen:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Screen not found")
    db.delete(screen)
    db.commit()
    return screen    

@router.post("/screens/{screen_id}/seats", response_model=schemas.SeatOut)
def create_seat(screen_id: int, seat_in: schemas.SeatCreate, db: Session = Depends(get_db)):
    seat = models.Seat(**seat_in.dict())
    db.add(seat)
    db.commit()
    db.refresh(seat)
    return seat

@router.post("/movies", response_model=schemas.MovieOut)
def create_movie(movie_in: schemas.MovieCreate, db: Session = Depends(get_db)):
    movie = models.Movie(**movie_in.dict())
    db.add(movie)
    db.commit()
    db.refresh(movie)
    return 

@router.put("/movies/{movie_id}", response_model=schemas.MovieOut)
def update_movie(movie_id: int, movie_in: schemas.MovieCreate, db: Session = Depends(get_db)):
    movie = db.query(models.Movie).filter(models.Movie.id == movie_id).first()
    if not movie:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")
    for key, value in movie_in.dict().items():
        setattr(movie, key, value)
    db.commit()
    db.refresh(movie)
    return movie

@router.delete("/movies/{movie_id}", response_model=schemas.MovieOut)
def delete_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = db.query(models.Movie).filter(models.Movie.id == movie_id).first()
    if not movie:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")
    db.delete(movie)
    db.commit()
    return movie    

@router.post("/shows", response_model=schemas.ShowOut)
def create_show(show_in: schemas.ShowCreate, db: Session = Depends(get_db)):
    show = models.Show(**show_in.dict())
    db.add(show)
    db.commit()
    db.refresh(show)
    return show 

@router.put("/shows/{show_id}", response_model=schemas.ShowOut)
def update_show(show_id: int, show_in: schemas.ShowCreate, db: Session = Depends(get_db)):
    show = db.query(models.Show).filter(models.Show.id == show_id).first()
    if not show:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Show not found")
    for key, value in show_in.dict().items():
        setattr(show, key, value)
    db.commit()
    db.refresh(show)
    return show

@router.get("/bookings", response_model=List[schemas.BookingOut])
def get_bookings(db: Session = Depends(get_db)):
    bookings = db.query(models.Booking).all()
    return bookings