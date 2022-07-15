from fikra import app
import os

if __name__ == '__main__':
    app.debug= os.environ.get('DEBUG')
    app.run()
