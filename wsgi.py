from Webserver import create_app

app = create_app()
app.run(port=8080, debug=False)  #needs to be false, else i get an error