import openai
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def parse_data(data):
    message = [ {
    "role": "system",
    "content": "You are a intelligent assistant here to parse data into a JSON format. \
        You will only output the pure JSON without syntax errors. \
        Parse the following data into a JSON of important information."
    } ]
    message.append({
        "role": "user",
        "content": data
    })
    
    response = client.chat.completions.create(
        messages=message,
        max_tokens=1000,
        temperature=0,
        model="gpt-3.5-turbo"
    )
    return response.choices[0].message.content

# data = """
# John Doe is a 30 year old male living in New York. He is a software engineer.
# """

# parsed_data = parse_data(data)

# print(json.loads(parsed_data))

# with open("data.json", "w") as f:
#     f.write(parsed_data)
