from openrouter import OpenRouter
from dotenv import load_dotenv
from rich.markdown import Markdown
from rich.console import Console
import json
import os

load_dotenv()

DB_Path="overallassistantDB.json"

def readDB():
    if not os.path.exists(DB_Path):
        return []
    with open(DB_Path, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def saveDB(message):
    with open(DB_Path, "w") as file:
        json.dump(message,file,indent=4)

message=readDB()

while True:
    with OpenRouter(api_key=os.getenv("OPEN_ROUTER_KEY_FOR_OVERALLASSISTENCE")) as client:
        prompt=input("Enter your prompt. ")

        if prompt == "Quit" or prompt == "Bye" or prompt == "Exit":
            print("Exiting Chatbot")
            break
        else:
            message.append({
                "role": "user",
                "content": prompt
            })
            response = client.chat.send(
                model="nvidia/nemotron-3-ultra-550b-a55b:free",
                messages=message
            )
            answer=response.choices[0].message.content
            message.append({
                "role": "assistant",
                "content": answer
            })

    md=Markdown(answer)
    saveDB(message)

    Console().print(md)