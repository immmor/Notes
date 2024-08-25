from .app import limiter, app

@app.route('/protected', methods=['GET'])
@limiter.limit("10 per minute")
def protected_view():
    return "This is a protected view"