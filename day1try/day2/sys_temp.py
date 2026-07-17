import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("NO API KEY:ERROR")

client = Groq(api_key=my_api_key)
model = "llama-3.3-70b-versatile"
role = "user"

promptx = "I love You"
prompty = "Suggest a name for my food company"

#system roles just change the content of message_system to prompt2 or 3 and message to promptx and remove temperature
prompt2 = "You are my Loving girlfriend"
prompt3 = "You are my strict office collegue who is also my manager"

#temperature just change the content of message_system to prompt4 or 5
#temperature by default is 0 and max=2
prompt4="You are a brand manager who suggest name for my food company"

message_system={
    "role":"system",
    "content":prompt4
}
message = {
    "role": role,
    "content": prompty
}

messages=[message_system,message]

response=client.chat.completions.create(model=model, messages=messages,temperature=1.25)
#print(response)

print("###################$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$&&&&&&&&&&&&&&&&&&&&&&&&&###################")

answer = response.choices[0].message.content
print(answer)