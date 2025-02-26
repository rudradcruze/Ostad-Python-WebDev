import requests
import json

# Make a request to the API
# Json Placeholder API

response = requests.get("https://jsonplaceholder.typicode.com/posts")
print(response.status_code)
# print(response.json())
# print(json.dumps(response.json(), indent=4, sort_keys=True))


# Create a new post
new_post = {
    "userId": 1,
    "id": 101,
    "title": "New Post",
    "body": "This is the body of the new post."
}

response = requests.post("https://jsonplaceholder.typicode.com/posts", json=new_post)
print(response.status_code)
print(response.json())

# Update a post
updated_post = {
    "title": "Updated Post",
    "body": "This is the updated body of the post."
}

response = requests.put("https://jsonplaceholder.typicode.com/posts/1", json=updated_post)
print(response.status_code)
print(response.json())

# Delete a post
response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
print(response.status_code)
print(response.json())