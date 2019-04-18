import subprocess


class GitManager:

    def __init__(self):
        pass

    def get_git_revision_hash(self):
        print(subprocess.check_output(['git', 'rev-parse', 'HEAD']))
        return subprocess.check_output(['git', 'rev-parse', 'HEAD'])

    def get_latest_git_commit_comment(self):
        print(subprocess.check_output(['git', 'log', '-1']))
        return subprocess.check_output(['git', 'log', '-1'])

    def get_git_log(self):
        print(subprocess.check_output(['git', 'log']))
