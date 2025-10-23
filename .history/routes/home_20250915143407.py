from flask import Blueprint, re

home_route = Blueprint('home', __name__)

@home_route.route('/')