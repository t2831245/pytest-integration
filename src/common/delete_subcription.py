import os
import requests


def delete_subcription(zuora_header, order):
    response = requests.delete(
        os.getenv("ZUROA_ENDPOINT") + "/v1/orders/" + order.orderNumber,
        headers=zuora_header,
    )
    assert response.status_code == 200, f"Error response: {response.text}"
    response.json()["success"] == True
