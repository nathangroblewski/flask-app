# Flask application template
This is a basic flask rest template that does not include data models. There are a few additional dev packages installed for formatting and styling 

## Setup
after cloning the repo run `pipenv install`

## Running the app
1. Run `pipenv shell`
2. within the env shell execute `export FLASK_APP=application`
3. now execute `flask run` and open the browser at `http://127.0.0.1:5000/`

## Useful commands
1. Generate requirements from Pipfile.lock `pipenv lock -r > requirements.txt`
2. pipenv lock issues can normally be resolved with `pipenv lock --pre --clear`