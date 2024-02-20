# Note: The openai-python library support for Azure OpenAI is in preview.
# Note: This code sample requires OpenAI Python library version 0.28.1 or lower.
import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_type = os.getenv("OPENAI_API_TYPE")
openai.api_base = os.getenv("OPENAI_API_BASE")
openai.api_version = os.getenv("OPENAI_API_VERSION")
openai.api_key = os.getenv("OPENAI_API_KEY")

question = "What is the capital of the United States?"
message_text = [{"role": "system",
                 "content": "You are an AI assistant that helps people find information."},
                {"role": "user",
                 "content": question},
                ]

completion = openai.ChatCompletion.create(
    engine="gpt35-turbo",
    messages=message_text,
    temperature=0.7,
    max_tokens=800,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None
)

print(completion.choices[0].message['content'])
