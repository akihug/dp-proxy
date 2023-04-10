FROM python:3.6
RUN python -m pip install pip==19.3.0 && pip install -r requirements.txt
RUN uvicorn main:app --reload