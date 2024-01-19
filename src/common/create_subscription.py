import os
import json
import requests


def create_subscription(zuora_header, order):
    data = json.dumps(order.__dict__, indent=4)
    response = requests.post(
        os.getenv("ZUROA_ENDPOINT") + "/v1/orders",
        headers=zuora_header,
        json=json.loads(data),
    )
    print("xxx : ", response.text)
    assert response.status_code == 200, f" == assert failed ==: {response.text}"
    assert response.json()["success"] == True
