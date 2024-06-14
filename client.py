import requests

header = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE4ODk5NDcwLCJpYXQiOjE3MTgyOTQ2NzAsImp0aSI6Ijc0ZjdkY2ZlNjczYTRhY2M5ODY2MjY0MjAxMTJlZjJlIiwidXNlcl9pZCI6Mn0.14_SmywsQD_M0PTiUQEZI0cYBt1xXLmVM3nDJH2SVh4'}

hello = requests.get('http://127.0.0.1:8000/users/protected/', headers=header)

print(hello.content)
