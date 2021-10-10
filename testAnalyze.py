import unittest
import requests

from analyze import *
from unittest import mock


@mock.patch('analyze.getRepoCommitsFromUser')
def mock_getRepoCommitsFromUser(mock_get_repo_commits_from_user):
    mock_get_repo_commits_from_user.return_value = "['Repo:AssignmentZero Number of commits: 78', 'Repo:chessBot Number of commits: 81', 'Repo:CookGuide Number of commits: 448', 'Repo:discord-pokemon-battles Number of commits: 855', 'Repo:E322Exchange4Students Number of commits: 668', 'Repo:GithubApi567 Number of commits: 269', 'Repo:HW4-345 Number of commits: 129', 'Repo:HW4-346 Number of commits: 766', 'Repo:KennethSkelton Number of commits: 1', 'Repo:slp-1 Number of commits: 144', 'Repo:SSW-345-Homework-5 Number of commits: 94', 'Repo:SSW-567-classify_triangle Number of commits: 161', 'Repo:SSW345Complexity Number of commits: 858', 'Repo:SSW345homework3 Number of commits: 110', 'Repo:SSW345Node.jsLab Number of commits: 110', 'Repo:SSW354DesignPatternPractice Number of commits: 58', 'Repo:Triangle567 Number of commits: 215']"


class TestgetRepoCommitsFromUser(unittest.TestCase):

    def testSampleFunction(self):
        self.assertEqual(getRepoCommitsFromUser("KennethSkelton"), "['Repo:AssignmentZero Number of commits: 78', 'Repo:chessBot Number of commits: 81', 'Repo:CookGuide Number of commits: 448', 'Repo:discord-pokemon-battles Number of commits: 855', 'Repo:E322Exchange4Students Number of commits: 668', 'Repo:GithubApi567 Number of commits: 269', 'Repo:HW4-345 Number of commits: 129', 'Repo:HW4-346 Number of commits: 766', 'Repo:KennethSkelton Number of commits: 1', 'Repo:slp-1 Number of commits: 144', 'Repo:SSW-345-Homework-5 Number of commits: 94', 'Repo:SSW-567-classify_triangle Number of commits: 161', 'Repo:SSW345Complexity Number of commits: 858', 'Repo:SSW345homework3 Number of commits: 110', 'Repo:SSW345Node.jsLab Number of commits: 110', 'Repo:SSW354DesignPatternPractice Number of commits: 58', 'Repo:Triangle567 Number of commits: 215']", "Working as intended" )


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()