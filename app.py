from os import name
from faceid import create_app

app = create_app()
if __name__ == "__main__":
    app.run(debug=True)
