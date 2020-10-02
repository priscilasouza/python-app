from src import app
import os

if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 5000))
    DEBUG = bool(os.environ.get('DEBUG', 'true'))
    app.run(debug=DEBUG, host='0.0.0.0', port=PORT)
