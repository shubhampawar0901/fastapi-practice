from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..deps import get_db, require_admin
from .. import models, schemas
from datetime import datetime

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