from flask import template_rendered
from src import app

@app.route('/productos')
def productos():
    return 'En productos'