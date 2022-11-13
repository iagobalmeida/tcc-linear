from fastapi import APIRouter, Body, Header, JSONResponse
from connectors.jsonplaceholder import users


router = APIRouter(
    prefix='/users',
    tags=['users']
)


@router.get('/{email}')
async def user_by_email(email: str):
    return users.get_user_by_email(user_email=email, pulbicize=True)


@router.post('/authenticate')
async def user_athenticate(email:str = Body(None), password:str = Body(None)):
    return users.authenticate(email, password)


@router.get('/{email}/data')
async def user_authenticated(email: str, token: str = Header(None)):
    if users.validate_token(token) == None: return JSONResponse(status=401)
    return users.get_user_by_email(user_mail=email, pulbicize=False)