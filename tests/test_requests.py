import requests
import json
import time

BASE = "http://127.0.0.1:8000"

def pretty(r):
    print(f"HTTP {r.status_code}")
    try:
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
    except:
        print(r.text)

def main():
    print("1. Crear entrenamiento (POST /trainings)")
    payload = {"title": "Cuadriceps", "notes": "Sentadilla fuerte"}
    r = requests.post(f"{BASE}/trainings", json=payload)
    pretty(r)
    assert r.status_code==201
    session = r.json()
    session_id = session['id']

    time.sleep(0.3)

    print("\n2. Lista de entrenamientos (GET /trainings)")
    r = requests.get(f"{BASE}/trainings")
    pretty(r)
    assert r.status_code == 200
    assert any(s["id"] == session_id for s in r.json())

    print("\n3. Añadir ejercicio (POST /trainings/{id}/exercises)")
    ex_payload = {"name": "Sentadilla", "sets": 3, "reps": 5, "weight": 73.0}
    r = requests.post(f"{BASE}/trainings/{session_id}/exercises", json=ex_payload)
    pretty(r)
    assert r.status_code == 201
    ex = r.json()
    ex_id = ex["id"]

    print("\n4. Devuelve entrenamiento (GET /trainings/{id})")
    r = requests.get(f"{BASE}/trainings/{session_id}")
    pretty(r)
    assert r.status_code == 200
    assert any(e["id"] == ex_id for e in r.json().get("exercises", []))

    print("\n5. Actualizar entrenamiento (PUT /trainings/{id})")
    update_payload = {"title": "Pierna (update)", "notes": "Menos carga por lesión"}
    r = requests.put(f"{BASE}/trainings/{session_id}", json=update_payload)
    pretty(r)
    assert r.status_code == 200
    assert r.json()["title"].startswith("Pierna (update)")

    print("\n6. Eliminar entrenamiento (DELETE /trainings/{id})")
    r = requests.delete(f"{BASE}/trainings/{session_id}")
    print(f"HTTP {r.status_code}")
    assert r.status_code == 204

    print("\n7. Comprobar que ya no existe (GET)")
    r = requests.get(f"{BASE}/trainings/{session_id}")
    pretty(r)
    assert r.status_code == 404

    print("\n Todas las pruebas ok")

if __name__ == "__main__":
    main()