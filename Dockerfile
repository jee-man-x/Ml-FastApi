#Base image
FROM python:3.12.9

#working dir
WORKDIR /Api
#copy
COPY . /Api


#install library
RUN pip install  -r requirements.txt

#port  8501
EXPOSE 8501

#run streamlit run
CMD ["uvicorn","Api:app","--host","0.0.0.0","--port","8501"]