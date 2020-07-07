import artist
import listener
import listener_keys
import track_encrypt
import ipfshttpclient
from flask import request

from flask import Flask
app = Flask(__name__)
api = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001/http')

LABEL_TO_POLICY = {}
PUBKEYS = listener_keys.get_listener_pubkeys()
PRIVKEYS = listener_keys.get_listener_privkeys()
LISTENER = listener.initialize_bob(PRIVKEYS)

@app.route('/join/', methods = ["POST"])
def join():
    policy_metadata = request.json["policy_metadata"]
    label = listener.join_policy(LISTENER, policy_metadata)
    LABEL_TO_POLICY[label] = policy_metadata
    return label

@app.route('/decrypt/', methods = ["POST"])
def decrypt_track():
    label = request.json["label"]
    ipfsHash = request.json["ipfsHash"]
    enc_data = api.get(ipfsHash)
    data = listener.reencrypt_segment(enc_data, LABEL_TO_POLICY[label], LISTENER)
    return data

if __name__ == '__main__':
    app.run()