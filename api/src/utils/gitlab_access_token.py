import os
import gitlab

gitlab_endpoint = os.environ.get("GITLAB_ENDPOINT")
gitlab_access_token = os.environ.get("GITLAB_ACCESS_TOKEN")

def auth():
    return gitlab.Gitlab("https://{}".format(gitlab_endpoint), private_token=gitlab_access_token)
