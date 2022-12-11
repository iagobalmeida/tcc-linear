from fastapi import APIRouter, Header
from fastapi.responses import JSONResponse
from connectors.jsonplaceholder import posts, users

router = APIRouter(
    prefix='/posts',
    tags=['posts']
)

@router.get('/')
def get_posts_from_user(token:str=Header(None)):
    token_data = users.validate_token(token)
    if token_data == None: return JSONResponse(status=401)
    user_id = token_data['id']
    return posts.get_posts_from_user(user_id)


@router.get('/{post_id}')
def get_posts_details(post_id:str, token:str=Header(None)):
    if users.validate_token(token) == None: return JSONResponse(status=401)
    post_data = posts.get_post_details(post_id)
    return JSONResponse(status=200 if post_data else 204, content=post_data)
