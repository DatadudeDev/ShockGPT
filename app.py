from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Set the OpenAI API key
openai.api_key = "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"

# Define the function to generate the OpenAI API response
def generate_response(prompt, conversation_history):
    model_engine = "text-davinci-002"
    prompt_with_history = '\n'.join(conversation_history + [prompt])  # Concatenate conversation history and prompt
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt_with_history,
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
    conversation_history = request.json["conversationHistory"]  # Get the conversation history from the request
    response = generate_response(user_input, conversation_history)
    conversation_history.append(user_input)  # Add the user input to the conversation history
    conversation_history.append(response)  # Add the response to the conversation history
    return jsonify({"response": response, "conversationHistory": conversation_history})  # Return the response and updated conversation history

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5002')
