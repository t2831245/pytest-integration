import os
import requests


def get_order(zuora_header, orderNumber):
    response = requests.get(
        os.getenv("ZUROA_ENDPOINT") + "/v1/orders/" + orderNumber, headers=zuora_header
    )
    assert response.status_code == 200, f"Error response: {response.text}"
    assert response.json()["success"] == True


def get_orde_not_found(zuora_header, orderNumber):
    response = requests.get(
        os.getenv("ZUROA_ENDPOINT") + "/v1/orders/" + orderNumber, headers=zuora_header
    )
    assert response.status_code == 200, f"Error response: {response.text}"
    assert response.json()["success"] == False
