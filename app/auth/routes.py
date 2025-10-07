from fastapi import APIRouter

auth_router = APIRouter()

@auth_router.post('/auth/register')
def register_user():
    ...


@auth_router.post('/auth/login')
def login_user():
    ...


@auth_router.post('/auth/refresh')
def refresh_token():
    ...


@auth_router.post('/auth/logout')
def logout_user():
    ...