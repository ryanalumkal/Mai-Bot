from requests import post
from json import loads
from re import sub

def get_anime_information(AnimeName):
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
  	    siteUrl
        coverImage {
            extraLarge
            color
        }
    }

    }
    '''

    # Define our query variables and values that will be used in the query request
    variables = {
        'search': AnimeName
    }

    url = 'https://graphql.anilist.co'

    # Make the HTTP Api request
    response = post(url, json={'query': query, 'variables': variables})
    #print(response.text)
    dictionary = loads(response.text)


    title  = dictionary['data']['Media']['title']['english']
    description = dictionary['data']['Media']['description']
    description = sub('<[^<]+?>', '', description)
    genres = dictionary['data']['Media']['genres']
    rating = dictionary['data']['Media']['averageScore']
    siteURL = dictionary['data']['Media']['siteUrl']
    coverImage = dictionary['data']['Media']['coverImage']['extraLarge']
    color = dictionary['data']['Media']['coverImage']['color']
    color = int("0x" + color[1:],0)

    
    return title,description,genres,rating, siteURL, coverImage, color


def get_manga_information(MangaName):
    query = '''
    query ($id: Int, $search: String) {
    Media (id: $id, search: $search, type: MANGA) {
        id
        title {
            english
        }
        genres
        description
        averageScore
  	    siteUrl
        coverImage {
            extraLarge
            color
        }
    }

    }
    '''

    # Define our query variables and values that will be used in the query request
    variables = {
        'search': MangaName
    }

    url = 'https://graphql.anilist.co'

    # Make the HTTP Api request
    response = post(url, json={'query': query, 'variables': variables})
    #print(response.text)
    dictionary = loads(response.text)


    title  = dictionary['data']['Media']['title']['english']
    description = dictionary['data']['Media']['description']
    description = sub('<[^<]+?>', '', description)
    genres = dictionary['data']['Media']['genres']
    rating = dictionary['data']['Media']['averageScore']
    siteURL = dictionary['data']['Media']['siteUrl']
    coverImage = dictionary['data']['Media']['coverImage']['extraLarge']
    color = dictionary['data']['Media']['coverImage']['color']
    color = int("0x" + color[1:],0)

    
    return title,description,genres,rating, siteURL, coverImage, color
