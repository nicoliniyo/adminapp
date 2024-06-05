import requests
import json
import os

# Replace with your actual API key
AWANLLM_API_KEY = os.getenv('AWANLLM_API_KEY')


# @app.route("/ask", methods=["POST"])
# def handle_request():
#     user_input = request.form["user_input"]
#     if user_input:
#         response = send_request(user_input)
#         api_response = process_response(response)
#         return json.dumps({"response": api_response})
#     else:
#         return json.dumps({"error": "Please enter some text"})

def send_request(user_input):
    url = "https://api.awanllm.com/v1/chat/completions"

    payload = json.dumps({
        "model": "Meta-Llama-3-8B-Instruct",
        "messages": [
            {
                "role": "user",
                "content": user_input
            }
        ]
    })

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f"Bearer {AWANLLM_API_KEY}"
    }

    try:
        response = requests.post(url, headers=headers, data=payload)
        response.raise_for_status()  # Raise an exception for non-2xx status codes
        return response.json().get("choices")[0].get("message").get("content")
    except requests.exceptions.RequestException as e:
        # Handle different error types
        if response.status_code == 401:
            return "Unauthorized access. Please check your API key."
        elif response.status_code == 302:
            return "Resource has been moved. This functionality might be unavailable."
        elif response.status_code == 403:
            return "Forbidden access. You might not have permission to perform this action."
        else:
            # Handle other errors
            return f"An error occurred: {e}"


# def process_response(response):
#     # Extract the API response from the JSON
#     api_response = response.get("choices")[0].get("content")
#     return api_response
