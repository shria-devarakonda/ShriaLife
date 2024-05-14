from flask import Flask

app = Flask(__name__)

@app.get("/")
def life_checker():
    return "I'm Alive and well, thank you!"


@app.post("/")
def actions(action_dict):
    # process action dict
    # change stats
    # generate reaction
    reaction = None
    return reaction
