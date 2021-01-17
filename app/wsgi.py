from server import app
import os

if __name__ == "__main__":
    print(app.config['SECRET_KEY'])
    app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
    app.run(host="0.0.0.0")