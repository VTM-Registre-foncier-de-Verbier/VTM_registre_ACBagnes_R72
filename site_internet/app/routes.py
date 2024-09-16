# -*- coding: utf-8 -*-
from flask import render_template, url_for, request
from app import app
from .models import coordonnees, documents, registre
from sqlalchemy import or_
from config import RESULTATS_PAR_PAGE


# Pour les pages qui n'affichent que le contenu qu'elles ont, la route ne prend pas de parametres
@app.route('/')
def accueil():
    return render_template('pages/accueil.html')


@app.route('/recherche')
def recherche():
    return render_template('pages/recherche.html')



# La recherche peut être spécifiquement dans certains champs de la db
@app.route('/resultatavance#carte')
def resultatavance():

    motclef = request.args.get("motclef", None)
    nom = request.args.get("contribuable", None)
    terrain = request.args.get("terrain", None)
    toponyme = request.args.get("topo", None)
    page = request.args.get("page", 1, type=int)

    resultats = []
    village = []


    if motclef:
        mots = motclef.split()

        for mot in mots:
            resultats = registre.query.filter(registre.toponyme == mot).order_by(registre.contribuable.asc())


    return render_template('pages/accueil.html', resultats=resultats,  motclef=motclef, scrollToAnchor=recherche)

