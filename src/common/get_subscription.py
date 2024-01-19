import os
import requests


def get_subscription(zuora_header, order):
    response = requests.get(
        os.getenv("ZUROA_ENDPOINT") + "/v1/orders/" + order.orderNumber,
        headers=zuora_header,
    )
    assert response.status_code == 200, f"Error response: {response.text}"
    assert (
        response.json()["order"]["orderNumber"] == order.orderNumber
    ), f"not assert: {response.text}"
