import spotipy.util as util
import json
import requests
from urllib.parse import urlencode
import os

username = 'kalinchenko.97'
client_id=os.environ.get("SPOTIFY_CLIENT_ID")
client_secret = os.environ.get("SPOTIFY_CLIENT_SECRET")
redirect_uri = 'https://www.spotify.com/us/account/overview/'
scope = 'user-read-playback-state'
user_id="kalinchenko.97"


token = util.prompt_for_user_token(username=username,
                                   scope=scope,
                                   client_id=client_id,
                                   client_secret=client_secret,
                                   redirect_uri=redirect_uri)
access_token=token
def get_user_profile():
    headers={
        "Content-Type":"application/json",
        "Authorization":f'Bearer {access_token}',
        }
    query=f"https://api.spotify.com/v1/users/{user_id}"
    r=requests.get(query,headers=headers)
    responce=r.json()
    responce_new=json.dumps(responce,indent=2)
    return responce_new

def get_users_available_devices():
    headers={
        "Content-Type":"application/json",
        "Authorization":f'Bearer {access_token}',
        }
    query="https://api.spotify.com/v1/me/player/devices"
    r=requests.get(query,headers=headers)
    responce=r.json()
    responce_new=json.dumps(responce,indent=2)
    return responce_new



def get_user_playlist():

        headers={
        "Content-Type":"application/json",
        "Authorization":f'Bearer {access_token}',
        }
        query="https://api.spotify.com/v1/me/playlists"
        r=requests.get(query,headers=headers)
        responce=r.json()
        responce_new=json.dumps(responce,indent=2)
        for i in responce["items"]:
            if i["name"]=="kach":
                return i["id"]

def get_playlist_items():
    headers={
        "Content-Type":"application/json",
        "Authorization":f'Bearer {access_token}',
        }
    query=f"https://api.spotify.com/v1/playlists/{get_user_playlist()}/tracks"
    r=requests.get(query,headers=headers)
    responce=r.json()
    responce_new=json.dumps(responce,indent=2)
    for i in responce["items"]:
        return  i["track"]["id"]


def get_audio_fetures_for_the_track():
    headers={
        "Content-Type":"application/json",
        "Authorization":f'Bearer {access_token}',
        }
    query=f"https://api.spotify.com/v1/audio-features/{get_playlist_items()}"
    r=requests.get(query,headers=headers)
    responce=r.json()
    responce_new=json.dumps(responce,indent=2)
    return responce_new

def get_recently_played():
    data=urlencode({"limit":50})
    headers={
        "Content-Type":"application/json",
        "Authorization":f'Bearer {access_token}',
        }
    query=f"https://api.spotify.com/v1/me/player/recently-played?{data}"
    r=requests.get(query,headers=headers)
    responce=r.json()
    responce_new=json.dumps(responce,indent=2)
    for i in responce["items"]:
        print(i["track"]["album"]["name"])

def get_user_current_playing_track():
    headers={
        "Content-Type":"application/json",
        "Authorization":f'Bearer {access_token}',
        }
    query="https://api.spotify.com/v1/me/player/currently-playing"
    r=requests.get(query,headers=headers)
    responce=r.json()
    responce_new=json.dumps(responce,indent=2)
    print(f'Song: {responce["item"]["name"]} Album: {responce["item"]["album"]["name"]}')

def set_volume():
    data=urlencode({"volume_percent":100})
    headers={
        "Content-Type":"application/json",
        "Authorization":f'Bearer {access_token}',
        }
    query=f"https://api.spotify.com/v1/me/player/volume?{data}"
    r=requests.put(query,headers=headers)
    return r.status_code


def scip_to_the_next():
    headers={
        "Content-Type":"application/json",
        "Authorization":f'Bearer {access_token}',
        }
    query="https://api.spotify.com/v1/me/player/next"
    r=requests.post(query,headers=headers)
    return r.status_code

def scip_to_the_previus():
    headers={
        "Content-Type":"application/json",
        "Authorization":f'Bearer {access_token}',
        }
    query="https://api.spotify.com/v1/me/player/previous"
    r=requests.post(query,headers=headers)
    return r.status_code




print(get_user_profile())




