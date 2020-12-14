class GithubService:
    base_url = "https://github.com/"

    def user_repos(self, user: User):
        return requests.get(self.base_url + "%s/repos" % user.gh_username)


def count_user_repos(user: User, github: GithubService):
    repos = github.user_repos(user)
    return len(repos)