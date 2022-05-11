"""Module with app run"""
from app.main import app

if __name__ == "__main__":
    print("Running app...")
    app.run(debug=True, port=5000) 