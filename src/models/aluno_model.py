from src.settings.extensions import db

class Aluno(db.Model):
    
    __tablename__ = "alunos"
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    matricula = db.Column(db.String, nullable=False)
    nascimento = db.Column(db.Integer, nullable=False)
    turma_id = db.Column(db.Integer, nullable=False)
    
    