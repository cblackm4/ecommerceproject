# ecommerceproject
 
### SETUP DEV ENVIRONMENT ###

# install node, npm, python 3.7, virtualenv
sudo apt install nodejs npm python3.7 virtualenv

# create python virtual environment in root dir
virtualenv venv -p $(which python3.7)

# activate virtual environment and install requirements
. ./venv/bin/activate
pip install -r requirements.txt
deactivate

# cd into frontend dir and install vue-cli
sudo npm install -g @vue/cli
npm install




### Run Django with a fresh database ###
#run the script under /scripts/resetdb.sh
#NOTE this will not work unless the dev environment has been set up accoring to the above specifications
. ./venv/bin/activate
. ./scripts/resetdb.sh

# start dev server
cd api
python manage.py runserver