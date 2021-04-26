import vk_api, requests


def wall_poster(content):
    user_token = 'token'

    post_string = f'''{content[1]}
    
    {content[2]}
    
    источник: {content[3]}
    '''
    params_2 = (
        ('owner_id', '-193482637'),
        ('from_group', '1'),
        ('message', post_string),
        ('access_token', user_token),
        ('v', '5.130')
    )

    response = requests.get('https://api.vk.com/method/wall.post', params=params_2)

# print(response.text)

# ('owner_id', '-2582989'),