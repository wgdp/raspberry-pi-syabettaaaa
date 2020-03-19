from flask import Flask, jsonify, abort, make_response, request
import subprocess
import openjtalk

api = Flask(__name__)

@api.route('/api/play_music/local', methods=["POST"])
def play_local_music():
    request_data = request.get_json()

@api.route('/api/yomiage', methods=["POST"])
def yomiage():
    request_data = request.get_json()
    openjtalk.yomiage(request_data['text'])
    return jsonify({'result': True})

if __name__ == '__main__':
    api.run(host="0.0.0.0", port=5000, threaded=True)