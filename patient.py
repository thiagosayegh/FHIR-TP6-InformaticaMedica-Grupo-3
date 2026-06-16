from fhir.resources.patient import Patient
from fhir.resources.humanname import HumanName
from fhir.resources.contactpoint import ContactPoint
from fhir.resources.identifier import Identifier


def create_patient(family_name, given_name, birth_date, gender, phone=None, documento=None):
    """Crear un recurso FHIR Patient con identifier de DNI."""
    patient = Patient()

    # Identifier (DNI)
    if documento:
        identifier = Identifier()
        identifier.system = "http://www.renaper.gob.ar/dni"
        identifier.value = documento
        identifier.use = "official"
        patient.identifier = [identifier]

    # Nombre
    name = HumanName()
    name.family = family_name
    name.given = [given_name]
    patient.name = [name]

    # Fecha de nacimiento y genero
    patient.birthDate = birth_date
    patient.gender = gender

    # Telefono (opcional)
    if phone:
        contact = ContactPoint()
        contact.system = "phone"
        contact.value = phone
        contact.use = "mobile"
        patient.telecom = [contact]

    return patient
