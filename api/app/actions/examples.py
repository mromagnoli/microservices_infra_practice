from ...app import api_bp


@api_bp.route("/examples/", methods=["GET"])
def fetch_all():
    return {"data": [{"something": 1}, {"something": "else"}]}
