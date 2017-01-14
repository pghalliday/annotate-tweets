import json
import os
import sys
from pprint import pprint
from glob import glob
from google.cloud import language

config_file = sys.argv[1]
with open(config_file) as f:
    config = json.load(f)

input_directory = config["input_directory"]
output_directory = config["output_directory"]

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

language_client = language.Client()

def to_dict(obj):
    if not hasattr(obj, "__dict__"):
        return obj
    ret = {}
    d = obj.__dict__
    keys = d.keys()
    for key in keys:
        if isinstance(d[key], list):
            ret[key] = []
            for val in d[key]:
                ret[key].append(to_dict(val))
        else:
            ret[key] = to_dict(d[key])
    return ret


for tweet_file in glob(os.path.join(input_directory, "*.json")):
    with open(tweet_file) as f:
        tweet = json.load(f)
    if "text" in tweet:
        text = tweet["text"]
        print(u"Text: {}".format(text))
        document = language_client.document_from_text(text)
        annotations = to_dict(document.annotate_text())
        print("Annotations:")
        pprint(annotations)
        tweet["google_nlp_annotations"] = annotations
        output_file = "{}.json".format(tweet["id"])
        with open(os.path.join(output_directory, output_file), "w") as f:
            json.dump(tweet, f)
