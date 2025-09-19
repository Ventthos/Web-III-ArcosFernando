from fastapi import FastAPI
from fastapi.testclient import TestClient
import pytest
import mongomock
from pytest import monkeypatch

from pymongo import MongoClient


from main import app
import main

client = TestClient(app)
mongo_client = mongomock.MongoClient()
database = mongo_client.practica1
collection_historial = database.historial

@pytest.mark.parametrize(
        "numeroA, numeroB, resultado",
        [
            (5,10,15),
            (0,0,0),
            (-5,5,-15),
            (10,-20,-10)
        ]
)
def test_sumar(numeroA, numeroB, resultado):
    monkeypatch.setattr(main, "collection_historial", collection_historial)
    response = client.get("/calculadora/sum?a=5&b=10")
    monkeypatch.setattr()
    assert response.status_code == 200
    assert response.json() == {"a": {numeroA}, "b": {numeroB}, "resultado": {resultado}}
    assert collection_historial.find_one({"a": numeroA, "b": numeroB, "resultado": resultado}) is not None

