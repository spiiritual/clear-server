from fastapi import FastAPI
from openai import OpenAI
import models
import os
import database

app = FastAPI()

@app.get("/")
def read_root():
    return ("follow @not.sp1ritual on instagram")

@app.get("/posts/get/{id}")
def read_post(id : str):
    '''This path will be used to get a single post.'''
    data = database.get_post(id)

    composed_data = {
        "title" : data.title,
        "content" : data.content,
        "timestamp" : data.timestamp,
        "visibility" : data.visibility
    }

    if (data.anonymous):
        composed_data["owner_username"] = "Anonymous"
    else:
        composed_data["owner_username"] = data.owner_username
    
    return models.SuccessfulResponse(response=models.EntryToSend(composed_data))

@app.post("/posts/create")
def create_post(content : str, visibility : str, anonymous : bool, color : str, title : str = None):
    return content

@app.post("/user/login")
def login_and_get_token():
    return "placrholder"

@app.post("/user/create")
def create_user(username : str, password : str):
    data = database.create_user(username, password)

    if data is True:
        return models.SuccessfulResponse(response="The account was created successfully!")
    elif data is Exception:
        return models.UnsuccessfulResponse(response=data)

@app.get("/user/me")
def get_username():
    return "placrholder"

@app.post("/chatgpt/shit")
def get_chatgpt_response(text : str):
    client = OpenAI()

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role" : "system", "content" : "You are an assistant for a mental health journaling app. Summarize the user's input into bullet points that won't trigger the user."},
            {"role" : "user", "content" : text}
        ]
    )

    return response.choices[0].message.content
