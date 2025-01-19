# Chosen technologies

This document explain why each technology has been used. 

---
# Python

Python is used cause :
- Large Ecosystem of Libraries and Tools
- Flexibility and integration with various systems
- Active community
- Support for Cloud Environments

---
# Libs 

## pytest and unittest 
Although `unittest` is the standard test framework supplied with Python, `pytest` was also chosen because : 
- Fixture support
- Parameterization
- Rich plugin architecture
- Concise syntax

And unittest.mock is used to mock services.

>It is known for its simplicity, scalability, and ability to handle complex test scenarios while significantly reducing the boilerplate code required for testing.
> --- <cite>[jetbrains][1]</cite>


[1] : https://blog.jetbrains.com/pycharm/2024/03/pytest-vs-unittest/

## fastapi
Very popular Python for developing fast, modern web APIs.
- Simplicity
- Intuitive 
- Native asynchronous support

[Official doc](https://fastapi.tiangolo.com/)

Utilisation des routes : 
Explication des changements
Router (routes.py) :

Nous avons déplacé la route /load dans un APIRouter pour mieux organiser les routes et éviter de surcharger la classe Server.
Le router contient maintenant la route /load, et cette approche permet une meilleure évolutivité.
Server (server.py) :

Le serveur inclut maintenant le router avec self.app.include_router(router), ce qui permet d'ajouter facilement de nouvelles routes à l'avenir.
La classe Server reste responsable de la gestion de l'instance de FastAPI, ainsi que de la connexion et déconnexion du service cloud.



## google-cloud-storage
Official library to connect to google cloud storage.

[Official doc](https://cloud.google.com/storage/docs/reference/libraries)

## boto3
Chosen because it is the official library for python.

> Boto3 is the Amazon Web Services (AWS) Software Development Kit (SDK) for Python, which allows Python developers to write software that makes use of services like Amazon S3 and Amazon EC2. You can find the latest, most up to date, documentation at our doc site, including a list of services that are supported.
> -- <cite>[Amazon][2]


[2] : https://github.com/boto/boto3


## Uvicorn
Uvicorn est un serveur ASGI (Asynchronous Server Gateway Interface) léger et performant, conçu pour exécuter des applications Python modernes comme FastAPI ou Starlette. 