import requests

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars' #URL of the API 
headers = {'Accept': 'application/vnd.github.v3+json'} #Specifcally asking to use the 3rd version of this API 
r = requests.get(url, headers=headers) #Making the call to the API 
print(f"Status code: {r.status_code}") #status code of 200 means a successful response 

# Store API response in a variable.
response_dict = r.json() #API returns info in JSON format - using .json to convert info to a dictionary 
print(f"Total repositories: {response_dict['total_count']}") #printing value associated with total count (total no of python projects)

# Explore information about the repositories.
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

# Examine the first repository.
repo_dict = repo_dicts[0]
#print(f"\nKeys: {len(repo_dict)}") #prints the number of keys
#for key in sorted(repo_dict.keys()): #will sort them into alphab order 
    #print(key) #will print all the keys

print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    print(f"Name: {repo_dict['name']}") #How to access dictionary information 
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")