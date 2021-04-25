import vk_api, requests


def wall_poster(content):
    user_token = '6ca101b48abf7120dd1de8461ed606413f9248ddd3a50999697251e1572bd4eb5605d655057d2ddc56925'

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