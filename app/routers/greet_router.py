from fastapi import APIRouter

from models.response_model import ResponseModel


api_greet = APIRouter(prefix='/greet')


@api_greet.get('')
async def greet_user(user: str = '') -> ResponseModel:
    """ Greet the user

    Args:
        user (str, optional): The user to greet. Defaults to ''.

    Returns:
        dict: The greeting message
    """
    message = 'Hello, World!'
    if user:
        message = f'Hello, {user}!'

    return ResponseModel(message=message)
