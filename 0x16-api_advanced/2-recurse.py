import requests

def recurse(subreddit, hot_list=[], after=None):
    """
    Queries the Reddit API recursively and returns a list containing the titles of all hot articles for a given subreddit.
    If no results are found for the given subreddit, the function returns None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-agent': 'my-app-0.1'}
    params = {'limit': 100}
    if after:
        params['after'] = after

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json()
    posts = data.get('data', {}).get('children', [])

    for post in posts:
        hot_list.append(post['data']['title'])

    after = data.get('data', {}).get('after', None)

    if after:
        return recurse(subreddit, hot_list, after)

    return hot_list if hot_list else None
