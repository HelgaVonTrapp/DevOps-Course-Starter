FROM python:3.10.8 as base
RUN pip install poetry
ENV WEBAPP_PORT=80
EXPOSE ${WEBAPP_PORT}
COPY . /app
WORKDIR /app
RUN poetry install
FROM base as production
ENTRYPOINT "poetry" "run" "gunicorn" --bind 0.0.0.0 "todo_app.app:create_app()"
FROM base as development
ENTRYPOINT "poetry" "run" "flask" "run" --host 0.0.0.0
FROM base as test
ENTRYPOINT [ "poetry","run","pytest" ]