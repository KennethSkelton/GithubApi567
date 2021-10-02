import requests 
import os

from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('GITHUB_TOKEN')


def getRepoCommitsFromUser(user, apiKey):
    
    outputList = []
    getReposUrl = f'https://api.github.com/users/{user}/repos'
    headers = {'Authorization': f'token {apiKey}'}
    repos = requests.get(getReposUrl,headers=headers)
    repos = repos.json()
   

    for repo in repos:
        count = 0
        repoName = repo['name']


        getCommitsUrl = f'https://api.github.com/repos/{user}/{repoName}/commits'
        commits = requests.get(getCommitsUrl, headers=headers)
        for commit in commits:
            count = count+1
        
        outputList.append(f'Repo: {repoName} Number of commits: {count}')
    return outputList

print(getRepoCommitsFromUser("KennethSkelton", TOKEN))