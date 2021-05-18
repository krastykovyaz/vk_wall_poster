import vk_api, requests



def wall_poster(content):
    user_token = '*'

    post_string = f'''{content[1]}
    
    {content[2]}
    
    источник: {content[3]}
    '''
    print(content[1])
    params_2 = (
        ('owner_id', '*'),
        ('from_group', '1'),
        ('message', post_string),
        ('access_token', user_token),
        ('v', '5.130')
    )
    print("ok")
    response = requests.get('https://api.vk.com/method/wall.post', params=params_2)

# print(response.text)

# ('owner_id', '*'), peredam

# if __name__=='__main__':
#     wall_poster(content)
