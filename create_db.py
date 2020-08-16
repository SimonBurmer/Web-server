from Webserver import create_app
from Webserver.extensions import db

app = create_app()
app.app_context().push() #https://flask-sqlalchemy.palletsprojects.com/en/2.x/contexts/

if __name__ == "__main__":
    # Run this file directly to create the database tables.

    print("Creating database tables...")
    db.create_all()  #Creates all tables 
    print("Done!")