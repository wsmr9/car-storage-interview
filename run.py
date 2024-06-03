from app import create_app
from flask_cors import CORS
import os

# Configuring environment variables
PORT = os.getenv('PORT', 5000)
DEBUG_MODE = os.getenv('DEBUG', 'False').lower() in ['true', '1', 't']

app = create_app()

origins = [
    "http://localhost:3000",
    "http://localhost:3001",
]

cors = CORS(app, resources={r"/*":
    {"origins": origins}
})

if __name__ == "__main__":
    # Run the Flask application with dynamic port and debug configuration
    app.run(host='0.0.0.0', port=PORT, debug=DEBUG_MODE)