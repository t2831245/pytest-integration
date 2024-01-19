import pytest
import requests


@pytest.fixture(scope="session", autouse=True)
def zuora_header():
    auth_url = "https://rest.sandbox.na.zuora.com/oauth/token"
    client_id = "*****************"
    client_secret = "*****************"
    grant_type = "client_credentials"

    response = requests.post(
        auth_url,
        data={
            "client_id": client_id,
            "client_secret": client_secret,
            "grant_type": grant_type,
        },
    )

    assert (
        response.status_code == 200
    ), f"Failed to obtain access token: {response.text}"

    token_data = response.json()
    access_token = token_data.get("access_token")
    assert access_token, f"Access token not found in response: {token_data}"
    headers = {"Authorization": f"Bearer {access_token}"}
    return headers
