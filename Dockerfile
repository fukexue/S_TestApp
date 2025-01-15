FROM cytomine/software-python3-base
RUN pip install numpy
RUN mkdir -p /TestApp
ADD app.py /TestApp/app.py
ENTRYPOINT ["python", "/TestApp/app.py"]
