from fastapi import FastAPI
from fastapi.responses import JSONResponse


app = FastAPI()


@app.get('/greet')
def greet_user(user: str = '') -> JSONResponse:
    """ Greet the user

    Args:
        user (str, optional): The user to greet. Defaults to ''.

    Returns:
        dict: The greeting message
    """
    response = {'message': 'Hello, World!'}
    if user:
        response['message'] = f'Hello, {user}!'

    return JSONResponse(content=response)
