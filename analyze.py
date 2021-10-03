import requests 

def getRepoCommitsFromUser(user):
    
    outputList = []
    getReposUrl = f'https://api.github.com/users/{user}/repos'

    repos = requests.get(getReposUrl)
    repos = repos.json()
   

    for repo in repos:
        count = 0
        repoName = repo['name']

        getCommitsUrl = f'https://api.github.com/repos/{user}/{repoName}/commits'
        commits = requests.get(getCommitsUrl)
        for commit in commits:
            count = count+1
        
        outputList.append(f'Repo: {repoName} Number of commits: {count}')
    return outputList

print(getRepoCommitsFromUser("KennethSkelton"))