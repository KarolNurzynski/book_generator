python3 -m venv venv
source venv/bin/activate
pip install -r main/requirements.txt
export FLASK_APP=main/main.py
flask run