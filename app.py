import flask
from flask import request, Response
import json
from flask_sqlalchemy import SQLAlchemy
import main_pipeline
from configs import config

app = flask.Flask(__name__)
app.config["DEBUG"] = True

app.config['SQLALCHEMY_DATABASE_URI'] = config.DB_URI
db = SQLAlchemy(app)


@app.route('/search-api', methods=['GET', 'POST'])
def search_api():

    request_data = request.get_json()
    if not request_data:
        return Response("Bad request", status=400)
    archives_id_list = request_data['archive_list']
    words_list = request_data['words_list']
    if 'registration_type' in request_data:
        if len(request_data['registration_type']) > 0:
            registration_type_list = request_data['registration_type']
        else: registration_type_list = None
    else:
        registration_type_list = None
    if archives_id_list and words_list:
        res = main_pipeline.search_main(archives_id_list,
                                        words_list,
                                        db.session)
    else:
        return Response("Bad request", status=400)
    #frag = FragmentatorHTR(request.args['image'])
    #print(json.dumps(res, indent=4))
    print(json.dumps(res, indent=4))
    return json.dumps(res, indent=4)


if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', )

