from sqlalchemy import text, select, JSON, cast

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)

from flaskr.db import get_db

from flaskr import models

bp = Blueprint('contratos', __name__, url_prefix='/contratos')


@bp.get("/")
def get_contratos():
    # contratos = []
    db = get_db()

    with db.engine.connect() as conn:
        result = conn.execute(select(models.Contrato).filter_by(folio='SAFIN-022-013'))
        contratos = result.first()
    

    return jsonify(contratos)
