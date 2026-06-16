from fhir.resources.condition import Condition


def create_condition(patient_id, snomed_code, snomed_display,
                     clinical_status="active", verification_status="confirmed",
                     category_code="encounter-diagnosis", severity=None,
                     onset_date=None, recorded_date=None, note_text=None):
    """
    Crear un recurso FHIR Condition.

    El recurso Condition representa una condicion clinica, problema, diagnostico
    o situacion relevante para el cuidado del paciente. Se utiliza para registrar
    diagnosticos, antecedentes patologicos, problemas activos y hallazgos clinicos.

    Partes principales:
    - clinicalStatus: estado clinico (active, resolved, inactive, remission)
    - verificationStatus: certeza diagnostica (confirmed, provisional, differential)
    - category: tipo (encounter-diagnosis, problem-list-item)
    - severity: gravedad (severe, moderate, mild) codificada en SNOMED CT
    - code: la condicion en si, codificada en SNOMED CT
    - subject: referencia al paciente (Patient/id)
    - onsetDateTime: cuando comenzo la condicion
    - recordedDate: cuando se registro en el sistema
    - note: notas clinicas en texto libre
    """

    condition_data = {
        "subject": {"reference": f"Patient/{patient_id}"},
        "clinicalStatus": {
            "coding": [{"system": "http://terminology.hl7.org/CodeSystem/condition-clinical",
                        "code": clinical_status, "display": clinical_status.capitalize()}]
        },
        "verificationStatus": {
            "coding": [{"system": "http://terminology.hl7.org/CodeSystem/condition-ver-status",
                        "code": verification_status, "display": verification_status.capitalize()}]
        },
        "category": [{
            "coding": [{"system": "http://terminology.hl7.org/CodeSystem/condition-category",
                        "code": category_code,
                        "display": "Encounter Diagnosis" if category_code == "encounter-diagnosis"
                        else "Problem List Item"}]
        }],
        "code": {
            "coding": [{"system": "http://snomed.info/sct",
                        "code": snomed_code, "display": snomed_display}],
            "text": snomed_display
        }
    }

    # Severity (opcional)
    if severity:
        severity_map = {
            "severe":   {"code": "24484000",  "display": "Severe"},
            "moderate": {"code": "6736007",   "display": "Moderate"},
            "mild":     {"code": "255604002", "display": "Mild"}
        }
        if severity in severity_map:
            condition_data["severity"] = {
                "coding": [{"system": "http://snomed.info/sct",
                            "code": severity_map[severity]["code"],
                            "display": severity_map[severity]["display"]}]
            }

    if onset_date:
        condition_data["onsetDateTime"] = onset_date
    if recorded_date:
        condition_data["recordedDate"] = recorded_date
    if note_text:
        condition_data["note"] = [{"text": note_text}]

    return Condition(**condition_data)
