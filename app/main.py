from fastapi import FastAPI, HTTPException, status
from typing import List
from .storage import Manager
from .schemas import TrainingCreate, TrainingOut, ExerciseIn, ExerciseOut
from .models import Exercise
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title='Control entrenamiento API', version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
)

manager = Manager()

@app.post("/trainings", response_model = TrainingOut, status_code = status.HTTP_201_CREATED)
def create_training(payload: TrainingCreate):
    s = manager.create_session(title=payload.title, notes=payload.notes)
    return s.to_dict()

@app.get("/trainings", response_model=List[TrainingOut])
def list_trainings():
    return [s.to_dict() for s in manager.list_sessions()]

@app.get("/trainings/{training_id}", response_model=TrainingOut)
def get_training(training_id: str):
    s = manager.get_session(training_id)
    if not s:
        raise HTTPException(status_code=404, detail='Training not found')
    return s.to_dict()

@app.put("/trainings/{training_id}", response_model=TrainingOut)
def update_training(training_id: str, payload: TrainingCreate):
    s = manager.update_session(training_id, title=payload.title, notes=payload.notes)
    if not s:
        raise HTTPException(status_code=404, detail="Training not found")
    return s.to_dict()

@app.delete("/trainings/{training_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_training(training_id: str):
    ok = manager.delete_session(training_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Training not found")
    return

@app.post("/trainings/{training_id}/exercises", response_model=ExerciseOut, status_code=status.HTTP_201_CREATED)
def add_exercise(training_id: str, payload: ExerciseIn):
    ex = manager.add_exercise_to_session(training_id, name=payload.name, sets=payload.sets, reps=payload.reps, weight=payload.weight)
    if not ex:
        raise HTTPException(status_code=404, detail="Training not found")
    return ex.to_dict()