from flask import abort, session, redirect

def login_required(function):
    def wrapper(*args, **kwargs):
        if not session["userid"]:
            return redirect('/login')
        else:
            return function
    return wrapper

