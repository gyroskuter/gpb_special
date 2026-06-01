from CONFIG import api_key
from instructions import instructions
from groq import Groq

def get_answer(question):
    client = Groq(api_key=api_key)


    response = client.chat.completions.create(
        model='openai/gpt-oss-120b',
        messages=[
            {'role': 'system', 'content': instructions},
            {'role': 'user', 'content': f'{question}'}
        ]
    )

    return response.choices[0].message.content
