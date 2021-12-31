import requests
#执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

print(r.text)
#将API存储在一个变量中
response_dict = r.json()
print('Total repositories:', response_dict['total_count'])

#处理结果
print(response_dict['incomplete_results'])
#print(response_dict['items'])
contents = response_dict['items']
print('Lenth of items:', len(contents))
repo_dict = contents[0]
print('Lenth of items:', len(repo_dict))
print("\nSelected information about first repository:")
print('Name :', repo_dict['name'])
print('Owner :', repo_dict['owner']['login'])
print('Stars:', repo_dict['stargazers_count'])
print('Repository:', repo_dict['html_url'])
print('Created:', repo_dict['created_at'])
print('Updated:', repo_dict['updated_at'])
print('description:', repo_dict['description'])