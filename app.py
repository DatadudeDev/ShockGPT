from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Set the OpenAI API key
openai.api_key = "YOUR-API-KEYE-HERE" #you can obtain an API key here --> https://platform.openai.com/account/api-keys


# Define the function to generate the OpenAI API response
def generate_response(prompt):
    model_engine = "text-davinci-002"
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

# Define the home page route
@app.route("/")
def home():
    return render_template("home.html")

# Define the route to handle the chat requests
@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.json["userInput"]
    response = generate_response(user_input)
    return jsonify(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0') #to run on localhost use host='0.0.0.0'. Remove to default to 127.0.0.1. 
