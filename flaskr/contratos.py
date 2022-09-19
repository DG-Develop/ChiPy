import json
from sqlalchemy import text, select, JSON, cast

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)

# from flaskr.db import get_db
from flaskr.models import Contrato

# from flaskr import models

bp = Blueprint('contratos', __name__, url_prefix='/contratos')


@bp.get("/")
def get_contratos():
    # db = get_db()

    # with db.engine.connect() as conn:
        # result = conn.execute(select(Contrato).filter_by(folio='SAFIN-022-013'))
        # result = conn.execute(select(Contrato).where(Contrato.folio=='SAFIN-022-013'))
        # result=conn.execute(text("SELECT * FROM Tbl_Contrato"))
        # contratos = result.all()
        # contratos=result.first()

    contratos=Contrato.query.all()
    # print(contratos)
    results = [tuple(row) for row in contratos]

    json_string = json.dumps(results, indent=4, sort_keys=True, default=str)

    return json_string
