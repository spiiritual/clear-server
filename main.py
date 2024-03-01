from fastapi import FastAPI
import models
import database

app = FastAPI()

@app.get("/")
def read_root():
    return ("follow @not.sp1ritual on instagram")

@app.get("/posts/get/{id}")
def read_post(id : str):
    '''This path will be used to get a single post.'''
    return id

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


