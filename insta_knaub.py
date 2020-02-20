import requests
text = input('Введите логин:')
response = requests.get('https://www.instagram.com/'+text+'?__a=1')
a = response.json()
print('Количество постов '+str(a['graphql']['user']['edge_owner_to_timeline_media']['count']))
posts = a['graphql']['user']['edge_owner_to_timeline_media']['edges']

posts_text = ''
for i in posts:
        url = i['node']['shortcode']
        like = i['node']['edge_liked_by']['count']
        print(str(url)+' Количество лайков: '+str(like))
for j in posts:
        url = j['node']['shortcode']
        comm = j['node']['edge_media_to_comment']['count']
        print(str(url)+' Колличество комментов: '+str(comm))
	
	
	
	

	
	
	











































	
