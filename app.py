import os
import json
from flask import Flask

def create_app():
    app = Flask('rmon')
    file = os.environ.get('RMON_CONFIG')
    
    json_content = ''
    try:
        with open(file) as f:
            for line in f:
                line = line.strip()
                if line.startswith('#'):
                    continue
                else:
                    json_content += line
    except IOError:
        print('File does not exist')

    new_content = json.loads(json_content)
    if new_content:
        for key in new_content:
            app.config[key.upper()] = new_content[key]
    return app
