import requests

GITHUB_RELEASES_URL = "https://api.github.com/repos/%s/releases/latest"
REPOSITORY_NAME = "KatharaFramework/Kathara"


class GitHubApi(object):
    @staticmethod
    def get_release_information():
        result = requests.get(GITHUB_RELEASES_URL % REPOSITORY_NAME)

        if result.status_code != 200:
            raise Exception()

        return result.json()
