from Webserver import create_app

app = create_app()

#if you want to host the app on your local machine
if __name__ == "__main__":
    app.run(port=8080, debug=False) 