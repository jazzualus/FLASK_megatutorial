from application import app, db
from application.models import User

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
