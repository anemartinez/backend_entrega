from typing import List, Optional
from datetime import datetime
import uuid


class Exercise:
    """
    Clase para definir un ejercicio (elementos: name, sets, reps, weight (valor opcional, ya que no todos los ejercicios tienen peso))
    """
    def __init__(self, name: str, sets: int, reps: int, weight: Optional[float]=None):
        # Definir elementos
        self._id = str(uuid.uuid4()) # ID único para cada ejercicio
        # Características principales de los ejercicios
        self.name = name
        self.sets = sets
        self.reps = reps
        self.weight = weight # Puede ser None (por ej. en ejercicios que no requieren peso)

    @property
    def id(self):
        # Propiedad para acceder al ID
        return self._id
    
    def to_dict(self):
        # Formato de datos (diccionario)
        return {"id": self._id, "name": self.name, "sets": self.sets, "reps": self.reps, "weight": self.weight}
    
class Session:
    """
    Clase para sesión de entrenamiento completa. Elementos: título, fecha, notas (opcional) y lista de ejercicios
    """
    def __init__(self, title: str, date: datetime=datetime.utcnow(), notes: Optional[str]=None):
        self._id = str(uuid.uuid4()) # ID único para cada sesión de entrenamiento
        self.title = title
        self.date = date
        self.notes = notes or ""
        self._exercises: List[Exercise] = [] # Aquí se guardan los ejercicios de la sesión de enternamiento

    @property
    def id(self):
        # Propiedad para acceder al ID (sólo lectura)
        return self._id
    
    def add_exercise(self, exercise: Exercise):
        # Añade un ejercicio a la sesión de entrenamiento
        self._exercises.append(exercise)

    def remove_exercise(self, exercise_id: str):
        # Elimina un ejercicio por su ID
        for i, exer in enumerate(self._exercises):
            if exer.id == exercise_id:
                del self._exercises[i]
                return True # Si el ejercicio se ha eliminado: True
        return False # Si no encuentra el ejercicio: False
    
    def exercises(self) -> List[Exercise]:
        # Devuelve lista con todos los ejercicios (devuelve copia para no tocar la lista original)
        return list(self._exercises)
    
    def to_dict(self):
        # Sesión de entrenamiento en formato diccionario
        return {"id": self._id, "title": self.title, "date": self.date.isoformat(), "notes": self.notes, "exercises": [ej.to_dict() for ej in self._exercises]}
