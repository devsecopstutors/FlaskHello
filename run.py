from app import app

if __name__ == "__main__":
    app.run(debug=True)

'''
COMMANDS
python -m unittest discover -s tests 

ON HEROKU
heroku login
heroku create <your-heroku-app-name>
heroku logs --tail
'''

