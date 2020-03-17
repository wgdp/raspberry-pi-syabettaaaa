from flask import Flask, jsonify, abort, make_response, request
import subprocess

api = Flask(__name__)

@api.route('/api/play_music/local', methods=["POST"])
def set_alarm():
    request_data = request.get_json()

@api.route('/api/yomiage', methods=["POST"])
def stop_alarm():
    request_data = request.get_json()
    subprocess.run([])

if __name__ == '__main__':
    api.run(host="0.0.0.0", port=5000, threaded=True)