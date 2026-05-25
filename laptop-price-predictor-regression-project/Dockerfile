#base image
FROM python:3.7

#workdir
WORKDIR /app

#COPY
COPY . /app

#run
RUN pip install -r requirements.txt

#port 
EXPOSE 8501

#command 
CMD ["streamlit","run", "./app.py"]
