from requests import post
from json import loads
from re import sub

def get_anime_information(none):
    query = '''
    query ($id: Int, $search: String) {
      Media (id: $id, search: $search, type: ANIME) {
        id
        title {
          english
        }
        genres
        description
        averageScore
      }
    }
    '''

    # Define our query variables and values that will be used in the query request
    variables = {
        'search': 'Jigokuraku'
    }

    url = 'https://graphql.anilist.co'

    # Make the HTTP Api request
    response = post(url, json={'query': query, 'variables': variables})
    #print(response.text)
    dictionary = loads(response.text)


    title  = dictionary['data']['Media']['title']['english']
    description = dictionary['data']['Media']['description']
    genres = dictionary['data']['Media']['genres']
    rating = dictionary['data']['Media']['averageScore']
    
    return title,description,genres,rating

