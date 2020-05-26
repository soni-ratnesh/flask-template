"""Add direct routes here"""

from flask import current_app as app


@app.route('/ping')
def ping():
    return {"text": "Pong"}