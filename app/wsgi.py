from server import app
import os

app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
app.secret_key = os.environ.get("SECRET_KEY")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
