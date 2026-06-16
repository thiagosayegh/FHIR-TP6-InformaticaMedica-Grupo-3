import requests
import json

HAPI_FHIR_URL = "http://hapi.fhir.org/baseR4"
HEADERS = {"Content-Type": "application/fhir+json", "Accept": "application/fhir+json"}


def send_resource(resource, resource_type):
    """Enviar un recurso FHIR al servidor HAPI FHIR (POST)."""
    url = f"{HAPI_FHIR_URL}/{resource_type}"
    response = requests.post(url, headers=HEADERS, data=resource.json())
    if response.status_code == 201:
        resource_id = response.json()["id"]
        print(f"Recurso {resource_type} creado exitosamente. ID: {resource_id}")
        return resource_id
    else:
        print(f"Error al crear el recurso: {response.status_code}")
        try:
            print(response.json())
        except:
            print(response.text)
        return None


def get_resource(resource_id, resource_type):
    """Leer un recurso FHIR del servidor por ID (GET)."""
    url = f"{HAPI_FHIR_URL}/{resource_type}/{resource_id}"
    response = requests.get(url, headers={"Accept": "application/fhir+json"})
    if response.status_code == 200:
        resource = response.json()
        print(json.dumps(resource, indent=2, ensure_ascii=False))
        return resource
    else:
        print(f"Error al obtener el recurso: {response.status_code}")
        return None


def search_patient_by_document(documento):
    """Buscar pacientes por numero de documento (GET con query param identifier)."""
    url = f"{HAPI_FHIR_URL}/Patient"
    params = {"identifier": documento}
    response = requests.get(url, headers={"Accept": "application/fhir+json"}, params=params)
    if response.status_code == 200:
        bundle = response.json()
        total = bundle.get("total", 0)
        print(f"Se encontraron {total} paciente(s) con documento {documento}.")
        if total > 0 and "entry" in bundle:
            for entry in bundle["entry"]:
                p = entry["resource"]
                nombre = p.get("name", [{}])[0]
                family = nombre.get("family", "N/A")
                given = nombre.get("given", ["N/A"])[0]
                print(f"  -> ID: {p['id']} | Nombre: {given} {family}")
            return bundle["entry"]
        return []
    else:
        print(f"Error en la busqueda: {response.status_code}")
        return []
