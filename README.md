# TP6 — Interoperabilidad FHIR

Trabajo Práctico N°6 de Informática Médica (16.22) 

Actividad 3: creación de recursos FHIR mediante Python, comunicándose con el servidor público HAPI FHIR.

## Estructura del repositorio

| Archivo | Descripción |
|---------|-------------|
| base.py | Funciones base: enviar recurso, leer por ID, buscar por DNI |
| patient.py | Creación del recurso Patient con identifier (Act. 3.a) |
| condition.py | Creación del recurso Condition - Grupo 3 (Act. 3.c) |
| workflow.py | Script principal que ejecuta 3.a + 3.b + 3.c en orden |
| requirements.txt | Dependencias (fhir.resources, requests) |

## Cómo ejecutar

pip install -r requirements.txt

python workflow.py

## Recurso asignado: Condition (Grupo 3)

El recurso Condition representa una condición clínica, problema o diagnóstico relevante para el cuidado del paciente. En este TP se creó una Condition de hipertensión arterial esencial (SNOMED CT 59621000) asociada a un paciente registrado en el servidor.

## Integrantes

Martín Porjolovsky - Thiago Sayegh - Alessandra Rodríguez
