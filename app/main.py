from fastapi import FastAPI, Body
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests
import json

app = FastAPI()


def get_payload(data):
    payload = {
        "messages": [
            {"content": data, "role": "user"},
            # Add other messages here if needed
        ],
        "id": "W8oxIjG",
        "previewToken": None,
        "agentMode": {},
        "clickedAnswer2": False,
        "clickedAnswer3": False,
        "codeModelMode": False,
        "githubToken": None,
        "isChromeExt": False,
        "isMicMode": False,
        "trendingAgentMode": {},
        "userId": "bdcea0a8-7eb1-46d7-9129-0109a2597718",
        "visitFromDelta": None
    }

    return payload

def remove_empty_lines(text):
    lines = text.split("\n")

    # Remove empty lines
    non_empty_lines = [line for line in lines if line.strip()!= '']

    # Join the non-empty lines back into a single string
    result_string = '\n'.join(non_empty_lines)
    return result_string


def get_transcript(optimized_prompt: str):
    structure_instruction = """Extract the main ideas and brief summary from the paragraph, return with markdown characters, and keep your response concise:"""

    response = requests.post("https://www.blackbox.ai/api/chat", headers={'Content-Type': 'application/json'}, json=get_payload(optimized_prompt + structure_instruction))

    return remove_empty_lines(response.text)


@app.get("/get_summary")
async def get_summary(input: str):
    return get_transcript(input)