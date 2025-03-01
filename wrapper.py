import openai
from openai import OpenAI
import os
import json
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


messages = [ {
    "role": "system",
    "content": "You are a intelligent assistant here to parse data into a JSON format. \
        You will only output the pure JSON without syntax errors. \
        Parse the following data into a JSON of important information."
    } ]


def parse_data(data):
    message = messages
    message.append({
        "role": "user",
        "content": data
    })
    
    response = client.chat.completions.create(
        messages=message,
        max_tokens=100,
        temperature=0,
        model="gpt-3.5-turbo"
    )
    return response.choices[0].message.content

data = """
Name: John Doe
Age: 30
Occupation: Software Engineer
Location: New York
"""

parsed_data = parse_data(data)

print(json.loads(parsed_data))

with open("data.json", "w") as f:
    f.write(parsed_data)