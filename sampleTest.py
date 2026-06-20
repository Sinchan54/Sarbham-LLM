import requests

url = "https://aloe-unneeded-justice.ngrok-free.dev/ask"
data = {"prompt": "What is the capital of Iceland?",
        "API_KEY": "XXXXXXXXXXXX"}

response = requests.post(url, json=data)


# print(f"Message request code: {response}")
# print(f"Full output \n{response.json()}")
print("Answer:", response.json().get("response").get("message").get("content"))
