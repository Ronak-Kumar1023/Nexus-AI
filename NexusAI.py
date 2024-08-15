import os
from dotenv import load_dotenv
from openai import OpenAI
from datetime import datetime

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def stream_response(user_prompt):
    try:
        # Create a streaming completion request
        stream = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": user_prompt}],
            stream=True
        )
        
        # Print streamed responses
        print("Response:")
        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                print(chunk.choices[0].delta.content, end="", flush=True)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    user_prompt = input("Message Nexus A.I.: ")
    stream_response(user_prompt)
