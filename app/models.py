from . import db
from werkzeug.security import generate_password_hash, check_password_hash

class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(200), nullable=True)
    toaster_id = db.Column(db.Integer, db.ForeignKey('toaster.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'toaster': self.toaster.to_dict()
        }
    
class Toaster(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    cafes = db.relationship('Cafe', backref='toaster', lazy=True, cascade="all, delete-orphan")

    def to_dict(self):
        coffees_from_this_roaster = [{'id': cafe.id, 'name': cafe.name} for cafe in self.cafes]
        return {
            'id': self.id,
            'name': self.name,
            'cafes': coffees_from_this_roaster
        }
 
# Usuario para autenticación
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(50), default='user', nullable=False)  # 'user' o 'admin'

    # crea un hash seguro para la contraseña
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # Verifica la contraseña con el hash almacenado
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    # retorna un diccionario con la información del usuario (sin la contraseña)
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username
        }