from webserver.app import create_app

app = create_app()
app.run(port=8080, debug=False)