import os
import openai

openai.api_key = "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"

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Escreva uma receita baseada nos ingredientes: cenoura, macarrão, batata\n\nInstructions:",
  temperature=0.3,
  max_tokens=400,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

print(response.choices[0].text)