from flask import Flask, render_template
from os import popen
import json


app = Flask(__name__)
registry = '<ip>:<port>'


@app.route('/')
def list_images():
    images_list = []
    # get repositories
    data = popen(f'curl --silent --insecure http://{registry}/v2/_catalog').read()
    repo_dict = json.loads(str(data))
    repos = repo_dict.get('repositories')

    # get tags
    for images in repos:
        tag_list = []
        data = popen(f'curl --silent --insecure http://{registry}/v2/{images}/tags/list').read()
        tags_dict = json.loads(str(data))
        image = tags_dict.get('name')
        tag = tags_dict.get('tags')
        for tags in tag:
            tag_list.append(image + ':' + tags)
        images_list.append(tag_list)
    print(images_list)
    return render_template('index.html', images_list=images_list, registry=registry)

if __name__ == 'main':
    app.run()