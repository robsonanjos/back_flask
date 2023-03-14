import requests
from flask import Flask
import os
import openai

app = Flask(__name__)

@app.route('/members')
def members():

    openai.api_key = os.getenv("openai_api_key")

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt="Escreva uma receita baseada nos ingredientes de forma que não ameace a saúde humana: cenoura, macarrão, batata, óleo tóxico de carro\n\nInstructions:",
    temperature=0.3,
    max_tokens=400,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
    )

    print(response.choices[0].text)
    return response.choices[0].text

if __name__ == "__main__":
    app.run(debug=True)

