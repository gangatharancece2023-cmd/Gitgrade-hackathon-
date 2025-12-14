import requests

def fetch_repo_data(repo_url):
    owner, repo = repo_url.replace("https://github.com/", "").split("/")
    api_url = f"https://api.github.com/repos/{owner}/{repo}"
    data = requests.get(api_url).json()

    commits = requests.get(api_url + "/commits").json()
    contents = requests.get(api_url + "/contents").json()

    return {
        "stars": data.get("stargazers_count", 0),
        "forks": data.get("forks_count", 0),
        "language": data.get("language", "Unknown"),
        "has_readme": any("README" in c["name"].upper() for c in contents),
        "file_count": len(contents),
        "commit_count": len(commits)
    }
