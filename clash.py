import requests

headers = {
    'Accept' : 'application/json',
    'authorization' : 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjY1MmYzZjFhLTBlN2QtNGM2ZS1iY2M2LTg3YjgyOGZjMjQ4NCIsImlhdCI6MTY5NDU1NjIxOSwic3ViIjoiZGV2ZWxvcGVyLzU2MjZmYTNlLTRiYTgtNTYwNC0zZDBkLWU3YmFhN2JkMjE3OCIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjk4LjMzLjExMy4yMjYiXSwidHlwZSI6ImNsaWVudCJ9XX0.3dmyTyEkyzr32M1rUE0afC2h_Y8mfTYESw57JOHgrmApaFx5Z1Ih2-AxeK-zr3DVwOv1ba0_-oiD9C1_umRIQA'
}

def get_user():
    # return user profile information
    response = requests.get('https://api.clashofclans.com/v1/players/%23CUQPGRR9', headers = headers)
    user_json = response.json()
    print(user_json['name'])

def search_clan():
    # submit a clan search
    response = requests.get('https://api.clashofclans.com/v1/clans?name=%239UO29GPC', headers = headers)
    clan_json = response.json()
    # now to go into items
    for clan in clan_json['items']:
        print(clan['name'] + ' is level: ' + str(clan['clanLevel']))

search_clan()