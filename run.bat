CALL py -3 -m venv venv
CALL venv\Scripts\activate
CALL pip install -r main/requirements.txt
CALL set FLASK_APP=main/main.py
CALL flask run
CMD /k