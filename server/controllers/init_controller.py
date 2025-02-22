from flask import Blueprint, request
from ..services import user_service
from ..utils import response, hashPwdAndSalt

inital = Blueprint("init", __name__)

@inital.route("/")
def hello_world():
    return response({"message": "Server is working"}, 200)

@inital.route("/user_test", methods=["GET"])
def create_test_user():
    user = {
        "username": "test_user",
        "email": "test_user@pass.com",
        "password": hashPwdAndSalt("123456", "asdf")
    }
    user_service.create(user)
    return response({"msg": "Test user created", "user": user}, 200)
