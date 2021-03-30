import sys
import re
import csv
import json
from tweepy import OAuthHandler, API, Cursor, TweepError
from functions import get_entities, item_retrieve

def download():

    r = re.compile(r'(?<=\.)csv') 
    ri = re.compile(r'(?<=\.)json')

    ext = ''
    if (r.search(sys.argv[1])):
        ext = r.search(sys.argv[1]).group(0)

    if (ext == "csv"):
        print("CSV file found.")
        print(f"The script will now load {sys.argv[1]}.")
    elif (ri.search(sys.argv[1]).group(0) == 'json'):
        print("JSON file found.")
        print(f"The script will now load {sys.argv[1]}.")
        ext = "json"

    if input("Continue? ... y/n ").lower() != 'y':
        sys.exit("Quitting.")


    _id = []
    indexes = []


    try:
        with open("api_keys.json", "r") as f:
            consumer_key = f["consumer_key"]
            consumer_secret = f["consumer_secret"]
            access_token = f["access_token"]
            access_token_secret = f["access_token_secret"]

    except FileNotFound:
    
        print("Missing API information. Ensure an api_keys.json is created with the appropriate information.")
        sys.exit()

    with open(sys.argv[1], mode="r", encoding="utf-8") as f:
        if ext == "csv":

            csv_reader = csv.DictReader(f)

            for i, row in enumerate(csv_reader):
                indexes.append(i)
                _id.append(row["_id"])
       
        elif ext == "json":

            data = json.load(f)

            for i, item in enumerate(data):
                indexes.append(i)
                _id.append(item)
        
        print(f'Located {len(indexes)} tweets.')
                
        print('Establishing API . . .')
        
        try:
            auth = OAuthHandler(consumer_key, consumer_secret)
            auth.set_access_token(access_token, access_token_secret)
            api = API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        except TweepError:
            print('Error establishing API . . .')
            sys.exit("Quitting.")

        print('Checking for media...')
        
        data = []
        for i, t in enumerate(_id):
            try:
                status = api.get_status(t, tweet_mode="extended", include_entities=True)._json
                entities = get_entities(status, t)
                
                if "message" in entities:
                    print("No media found, ignoring...")
                    continue
                
                for data_dict in entities:
                    print("Found!")
                    data_dict['original_row'] = indexes[i]
                    data_dict['tweet_url'] = f'https://twitter.com/statuses/{str(t)}'
                    data.append(data_dict)
            except TweepError as e:
                data.append({'message':e, 'original_row': i, 'tweet_id': t})
                continue

        num_media = len([x for x in data if 'medium' in x])
        print(f'Retrieved meta-data for {num_media} media items...')

        print("Retrieving media items...")
       
        for row in data:
            if 'medium' in row:
                print(f"Downloading {row} ...")
                item_retrieve(row)
        print(f'Job Complete. Check the "media" folder for your files. Have a nice day!')
