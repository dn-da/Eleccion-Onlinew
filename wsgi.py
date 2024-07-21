from app import create_app, db
from flask_migrate import Migrate
from app.models.Eleccion import Eleccion
from app.models.ListaCandidato import ListaCandidato

app = create_app()
migrate = Migrate(app, db) 

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)