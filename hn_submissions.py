from operator import itemgetter

import requests

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url) #returns a list containing the IDs of the top 500 most popular articles on HN
print(f"Status code: {r.status_code}") #print the status code returns from API 

# Process information about each submission.
submission_ids = r.json() #response object is then converted to a Pyhton list
submission_dicts = [] #setting up an empty list to store dictionaries
for submission_id in submission_ids[:30]: #loop through the top 30
    # Make a separate API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json" #New API call for each submission
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()
    
    # Build a dictionary for each article.
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'],
    }
    submission_dicts.append(submission_dict) #append each dictionary to list of dictionaries 
 
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True) #Pass the 'comments' key, and it pulls the value associated with that key from each dictionary in the list
#sorted() then uses this value as the basis for sorting this list 

for submission_dict in submission_dicts: #After sorting list, loop through and print out 3 pieces of info about each 
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")