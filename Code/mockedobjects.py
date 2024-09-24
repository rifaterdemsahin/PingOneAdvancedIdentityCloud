import requests
from unittest.mock import patch

PINGONE_API_BASE = "https://api.pingone.com/v1"
TENANT_ID = "mocked-tenant-id"
ACCESS_TOKEN = "mocked-access-token"
LOCK_STATE_URL = f"{PINGONE_API_BASE}/environments/{TENANT_ID}/promotion/lock/state"
PROMOTE_URL = f"{PINGONE_API_BASE}/environments/{TENANT_ID}/promotion/promote"

def check_lock_state():
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    response = requests.get(LOCK_STATE_URL, headers=headers)
    return response.json() if response.status_code == 200 else {"error": "Failed to check lock status"}

def promote_configuration(dry_run=True):
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {"dryRun": dry_run}
    response = requests.post(PROMOTE_URL, headers=headers, json=payload)
    return response.json() if response.status_code == 200 else {"error": "Failed to promote configuration"}

@patch("requests.get")
@patch("requests.post")
def run_poc(mock_post, mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "description": "Environment unlocked",
        "lowerEnv": {"state": "unlocked"},
        "upperEnv": {"state": "unlocked"}
    }

    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {
        "result": "Promotion process initiated successfully",
        "status": "RUNNING"
    }

    lock_status = check_lock_state()
    print(f"Lock Status: {lock_status}")

    promotion_result = promote_configuration(dry_run=True)
    print(f"Promotion Result (Dry Run): {promotion_result}")

    promotion_result_real = promote_configuration(dry_run=False)
    print(f"Promotion Result (Real): {promotion_result_real}")

if __name__ == "__main__":
    run_poc()
