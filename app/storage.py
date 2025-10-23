from typing import Dict, List, Optional
from .models import Session, Exercise
from datetime import datetime

class Manager:
    """
    Gestiona las sesiones de entrenamiento. Esta clase hace que se puedan crear, actualizar, obtener y eliminar sesiones.
    """
    def __init__(self):
        # Diccionario donde se almacenan las sesiones de entrenamiento
        self._store: Dict[str, Session] = {}

    def create_session(self, title: str, date: datetime=datetime.utcnow(), notes: Optional[str]=None):
        # Crea nueva sesión y la guarda en el diccionario anterior
        session = Session(title=title, date=date, notes=notes)
        self._store[session.id]=session
        return session
    
    def get_session(self, session_id: str) -> Optional[Session]:
        # Devuelve la sesión de entrenamiento (la busca por su ID), si no existe, devuelve None
        return self._store.get(session_id)
    
    def list_sessions(self) -> List[Session]:
        # Devuelve una lista con todas las sesiones de entrenamiento almacenadas
        return list(self._store.values())
    
    def update_session(self, session_id: str, title: str, notes: Optional[str]=None) -> Optional[Session]:
        # Cambia una sesión de entrenamiento ya existente
        s = self._store.get(session_id)
        if not s:
            return None
        s.title = title
        if notes is not None:
            s.notes = notes
        return s
    
    def delete_session(self, session_id: str) -> bool:
        # Elimina una sesión de entrenamiento
        return self._store.pop(session_id, None) is not None
    
    def add_exercise_to_session(self, session_id: str, name: str, sets: int, reps: int, weight: Optional[float]=None) -> Optional[Exercise]:
        # Añade un ejercicio a una sesión de entrenamiento
        s = self._store.get(session_id)
        if not s:
            return None
        exercise = Exercise(name=name, sets=sets, reps=reps, weight=weight)
        s.add_exercise(exercise)
        return exercise
    
    def search_by_title(self, keyword: str) -> List[Session]:
        # Permite buscar una sesión de entrenamiento por una keyword en el título (aplica lower para normalizar el texto)
        return [s for s in self._store.values() if keyword.lower in s.title.lower()]