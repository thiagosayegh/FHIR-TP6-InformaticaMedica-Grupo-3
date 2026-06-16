# FHIR-TP6-InformaticaMedica-Grupo-3
Actividad 3: creación de recursos FHIR mediante Python, comunicándose con el servidor público HAPI FHIR (http://hapi.fhir.org/baseR4).
Estructura del repositorio
├── base.py           — Funciones base: enviar recurso, leer por ID, buscar por DNI
├── patient.py        — Creación del recurso Patient con identifier (Act. 3.a)
├── condition.py      — Creación del recurso Condition - Grupo 3 (Act. 3.c)
├── workflow.py       — Script principal que ejecuta 3.a + 3.b + 3.c en orden
└── requirements.txt  — Dependencias (fhir.resources, requests)
Cómo ejecutar
bashpip install -r requirements.txt
python workflow.py
Recurso asignado: Condition (Grupo 3)
El recurso Condition representa una condición clínica, problema o diagnóstico relevante para el cuidado del paciente. En este TP se creó una Condition de hipertensión arterial esencial (SNOMED CT 59621000) asociada a un paciente registrado en el servidor.
Integrantes
Martín Porjolovsky · Thiago Sayegh · Alessandra Rodríguez
