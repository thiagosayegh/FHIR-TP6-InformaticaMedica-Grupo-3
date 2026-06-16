from patient import create_patient
from condition import create_condition
from base import send_resource, get_resource, search_patient_by_document

if __name__ == "__main__":

    # =========================================================
    # ACTIVIDAD 3.a — Crear y leer un recurso Patient con DNI
    # =========================================================

    print("=" * 50)
    print("3.a — Crear Patient con DNI")
    print("=" * 50)

    patient = create_patient(
        family_name="Sayegh",
        given_name="Thiago",
        birth_date="1999-05-15",
        gender="male",
        phone="11-1234-5678",
        documento="40123456"
    )

    print("\nJSON del recurso Patient a enviar:\n")
    print(patient.json(indent=2, ensure_ascii=False))

    patient_id = send_resource(patient, "Patient")

    # Si ya existe, buscarlo por DNI
    if not patient_id:
        print("\nEl paciente ya existe. Buscando por DNI...")
        results = search_patient_by_document("40123456")
        if results:
            patient_id = results[0]["resource"]["id"]

    if patient_id:
        print(f"\nLeyendo Patient {patient_id}:\n")
        get_resource(patient_id, "Patient")

    # =========================================================
    # ACTIVIDAD 3.b — Buscar paciente por documento
    # =========================================================

    print("\n" + "=" * 50)
    print("3.b — Buscar paciente por documento")
    print("=" * 50 + "\n")

    search_patient_by_document("40123456")

    # =========================================================
    # ACTIVIDAD 3.c — Crear recurso Condition (Grupo 3)
    # =========================================================

    print("\n" + "=" * 50)
    print("3.c — Crear Condition (Grupo 3)")
    print("=" * 50)

    if patient_id:
        condition = create_condition(
            patient_id=patient_id,
            snomed_code="59621000",
            snomed_display="Hipertension arterial esencial",
            clinical_status="active",
            verification_status="confirmed",
            category_code="encounter-diagnosis",
            severity="moderate",
            onset_date="2024-06-15",
            recorded_date="2024-06-15",
            note_text="Paciente con PA 150/95 mmHg. Se indica Losartan."
        )

        print("\nJSON del recurso Condition a enviar:\n")
        print(condition.json(indent=2, ensure_ascii=False))

        condition_id = send_resource(condition, "Condition")

        if condition_id:
            print(f"\nLeyendo Condition {condition_id}:\n")
            get_resource(condition_id, "Condition")
    else:
        print("No se pudo crear la Condition porque no se obtuvo el ID del paciente.")

    print("\nFin del workflow")
