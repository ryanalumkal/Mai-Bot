from requests import post
from json import loads
from re import sub

def get_anime_information(none):
    query = '''
    query ($id: Int) { # Define which variables will be used in the query (id)
    Media (id: $id, type: ANIME) { # Insert our variables into the query arguments (id) (type: ANIME is hard-coded in the query)
        id
        title {
            english
        }
        type
        genres
        description
    }
    }
    '''
    variables = {
        'search': 'Fate/Zero',
        'page': 1,
        'perPage': 3
    }
    url = 'https://graphql.anilist.co'

    response = post(url, json={'query': query, 'variables': variables})
    dictionary = loads(response.text)
    
    title = dictionary['data']['Media']['title']['english']
    description = dictionary['data']['Media']['description']
    description = sub(r'<[^>]*>', '', description)
    genres = dictionary['data']['Media']['genres']
    anime_type = dictionary['data']['Media']['type']

    print(title)
    return title, description, genres, anime_type




"""
def get_anime_information(anime_name):
    # Here we define our query as a multi-line string
    query = '''
    query ($id: Int) { # Define which variables will be used in the query (id)
    Media (id: $id, type: ANIME) { # Insert our variables into the query arguments (id) (type: ANIME is hard-coded in the query)
        id
        title {
            english
        }
        type
        genres
        description
    }
    }
    '''

    # Define our query variables and values that will be used in the query request
    variables = {
        'search': 'Fate/Zero',
        'page': 1,
        'perPage': 3
    }

    url = 'https://graphql.anilist.co'

    # Make the HTTP Api request
    response = post(url, json={'query': query, 'variables': variables})
    dictionary = loads(response.text)

    title = dictionary['data']['Media']['title']['english']
    description = dictionary['data']['Media']['description']
    description = sub(r'<[^>]*>', '', description)
    genres = dictionary['data']['Media']['genres']
    anime_type = dictionary['data']['Media']['type']

    return title, description, genres, anime_type
"""
#return 