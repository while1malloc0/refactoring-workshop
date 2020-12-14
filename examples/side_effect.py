def count_user_repos(user: User):
    repos = requests.get("https://github.com/%s/repos" % user)
    return len(repos)