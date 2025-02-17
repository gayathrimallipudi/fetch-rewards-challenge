import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_process_receipt():
    response = client.post("/receipts/process", json={
        "retailer": "Target",
        "purchaseDate": "2022-01-01",
        "purchaseTime": "13:01",
        "total": "35.35",
        "items": [
            {"shortDescription": "Mountain Dew 12PK", "price": "6.49"},
            {"shortDescription": "Emils Cheese Pizza", "price": "12.25"},
	    {"shortDescription": "Knorr Creamy Chicken", "price": "1.26"},
            {"shortDescription": "Doritos Nacho Cheese", "price": "3.35"},
            {"shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ", "price": "12.00"}
        ]
    })
    assert response.status_code == 200
    assert "id" in response.json()

def test_get_points():
    post_response = client.post("/receipts/process", json={
        "retailer": "M&M Corner Market",
        "purchaseDate": "2022-03-20",
        "purchaseTime": "14:33",
        "total": "9.00",
        "items": [
            {"shortDescription": "Gatorade", "price": "2.25"},
            {"shortDescription": "Gatorade", "price": "2.25"},
            {"shortDescription": "Gatorade", "price": "2.25"},
            {"shortDescription": "Gatorade", "price": "2.25"}
        ]
    })
    receipt_id = post_response.json().get("id")
    response = client.get(f"/receipts/{receipt_id}/points")
    assert response.status_code == 200
    assert "points" in response.json()
