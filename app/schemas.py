from pydantic import BaseModel, Field
from typing import Optional, List

# Estos modelos definen cómo se representan los ejercicios y las sesiones de entrenamiento

class ExerciseIn(BaseModel):
    """
    Modelo de entrada para crear un ejercicio. Define los cambios que el usuario debe rellenar.
    """
    name: str = Field(..., example="peso muerto")
    sets: int = Field(..., example=3)
    reps: int = Field(..., example=6)
    weight: Optional[float] = Field(None, example=100.)

class ExerciseOut(ExerciseIn):
    """
    Salida para devolver un ejercicio. Heereda los campos de ExerciseIn y añade el ID
    """
    id: str

class TrainingCreate(BaseModel):
    """
    Modelo de entrada para crear una sesión de entrenamiento.
    """
    title: str = Field(..., example="Femoral-glúteo")
    notes: Optional[str] = Field(None, example="Control técnica")

class TrainingOut(BaseModel):
    """
    Modelo de salida para devolver sesión de entrenamiento con todos los ejercicios.
    """
    id: str
    title: str
    date: str
    notes: Optional[str]
    exercises: List[ExerciseOut] = []