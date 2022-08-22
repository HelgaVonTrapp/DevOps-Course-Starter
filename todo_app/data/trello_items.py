import requests
import json
def get_items():
    url = "https://api.trello.com/1/boards/62f2b96de0b99c00aff27ae6/lists?"

    headers = {
    "Accept": "application/json"
    }

    query = {
    'key': '9c0d3be68129cbe4d579fe32310123a5',
    'token': '58a1a2bc161d2f86b519250c5d11683a103222c98d6f53830b29acba9abf0a21',
    'cards': 'open'
    }

    response = requests.request(
    "GET",
    url,
    headers=headers,
    params=query
    )

    print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
get_items()
