from src import app

@app.route('/health')
def health():
    """
    :return: 200 with message health
    """
    return 'Health!'
