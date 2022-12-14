FROM python
RUN pip install openai

COPY . /root
WORKDIR /root

RUN pip install -r requirements.txt

CMD ["python", "main.py"]