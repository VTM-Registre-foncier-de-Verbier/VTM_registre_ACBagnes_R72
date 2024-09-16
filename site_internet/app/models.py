from app import db


class coordonnees(db.Model):
    __tablename__ = "coordonnees"
    id = db.Column(db.Integer, primary_key=True)
    lat = db.Column(db.Integer)
    lng = db.Column(db.Integer)
    document_id = db.Column(db.Integer)




class documents(db.Model):
    __tablename__ = "documents"
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.TEXT)
    updated_at = db.Column(db.TEXT)
    numero = db.Column(db.Integer)
    lettre = db.Column(db.TEXT)
    nom = db.Column(db.TEXT)
    traduction = db.Column(db.TEXT)
    path = db.Column(db.TEXT)
    commentaire = db.Column(db.TEXT)
    lieu_id = db.Column(db.Integer, db.ForeignKey("coord.id"))
    real = db.Column(db.TEXT)




class registre(db.Model):
    __tablename__ = "registre"
    id = db.Column(db.Integer, primary_key=True)
    contribuable = db.Column(db.TEXT, index=True)
    toponyme = db.Column(db.TEXT, index=True)
    numero_parcelle = db.Column(db.Integer, index=True)
    type_terrain = db.Column(db.TEXT)
    cote = db.Column(db.TEXT)
    folio = db.Column(db.TEXT)
    doc_id = db.Column(db.Integer, db.ForeignKey("documents.id"))
    topo = db.relationship("documents")
    coord_id = db.Column(db.Integer, db.ForeignKey("coordonnees.document_id"))
    coordi = db.relationship("coordonnees")
    imgnumber = db.Column(db.Integer)
