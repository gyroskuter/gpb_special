from CONFIG import api_key
from CONFIG import instructions
from groq import Groq

client = Groq(api_key=api_key)

question = input('Enter ur question pls \n')

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role": "system", "content": instructions},
        {"role": "user", "content": "ваш вопрос на русском"}
    ]
)

print(response.choices[0].message.content)
