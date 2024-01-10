FROM python:3.8
USER root
WORKDIR /app
EXPOSE 5000
COPY . /app
ARG file_path
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT ["python", "main.py"]
CMD ["$file_path"]

