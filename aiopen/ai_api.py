import requests
import json
import os

# Replace with your actual API key
api_key = os.getenv('GROQ_API_KEY')
api_url = os.getenv('GROQ_API_URL')
api_model = os.getenv('GROQ_API_MODEL')


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
    payload = json.dumps({
        "model": api_model,
        "messages": [
            {
                "role": "user",
                "content": f"{user_input}"
            }
        ],
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f"Bearer {api_key}"
    }

    try:
        response = requests.post(api_url, headers=headers, data=payload)
        print("RESPONSE")
        print(response)
        response.raise_for_status()  # Raise an exception for non-2xx status codes
        result = response.json().get("choices")[0].get("message").get("content")

        print('RESULT')
        print(result)

        return result
    except requests.exceptions.RequestException as e:
        # Handle different error types
        if response.status_code == 401:
            return "Unauthorized access. Please check your API key."
        elif response.status_code == 302:
            return response.json().get("choices")[0].get("message").get("content")
            # return "Resource has been moved. This functionality might be unavailable."
        elif response.status_code == 403:
            return "Forbidden access. You might not have permission to perform this action."
        else:
            # Handle other errors
            return f"An error occurred: {e}"

# def process_response(response):
#     # Extract the API response from the JSON
#     api_response = response.get("choices")[0].get("content")
#     return api_response
