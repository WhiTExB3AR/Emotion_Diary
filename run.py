# -*- encoding: utf-8 -*-


# ------- Start: B3AR config code -------
import os
import sys
from flask import request
from flask_restful import Resource, Api
from apps.home.util import solver
# ------- End: B3AR config code -------



from flask_migrate import Migrate
from sys import exit
from decouple import config

from apps.config import config_dict
from apps import create_app, db

# WARNING: Don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)

# The configuration
get_config_mode = 'Debug' if DEBUG else 'Production'



# ------- Start: B3AR config code -------
# TODO Load Model
# E load model hoặc solver gì đó ở bên util rồi gọi ở đây
# ->solver
# ------- End: B3AR config code -------



try:

    # Load the configuration using the default values
    app_config = config_dict[get_config_mode.capitalize()]

except KeyError:
    exit('Error: Invalid <config_mode>. Expected values [Debug, Production] ')

app = create_app(app_config)
Migrate(app, db)



# ------- Start: B3AR config code -------
# TODO đây là code mẫu tạo rest api, tạm để ở đây e thích dọn đi đâu thì tuỳ
# Thử kết quả ở http://127.0.0.1:5000/get_fer?image=hahaha

class GetFer(Resource):
    def get(self):
        image = request.args.get('image', 'no model')
        response = {
        	'success': True,
        	'predicted_label': image + ' ---- ' + str(solver.__str__)
        }
        return response


api = Api(app)
api.add_resource(GetFer, '/get_fer')
# ------- End: B3AR config code -------



if DEBUG:
    app.logger.info('DEBUG       = ' + str(DEBUG))
    app.logger.info('Environment = ' + get_config_mode)
    app.logger.info('DBMS        = ' + app_config.SQLALCHEMY_DATABASE_URI)

if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=8000)
    app.run()
