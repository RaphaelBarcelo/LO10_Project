from flask import Blueprint
from LO10_Project.api.services.TeamComposer import assign_lanes
from flask import jsonify
from riotwatcher import ApiError
teamComposer_routes = Blueprint("teamcomposer_routes", __name__, url_prefix="/teamcomposer")


@teamComposer_routes.route("/<teamcomposer>")
def get_team_composer(team):
    try:
        teamComposerData = assign_lanes(team)
        return jsonify(teamComposerData)
    except ApiError as err:
        return jsonify(error=err.response.status_code, message="Not Found"), err.response.status_code

