# from subprocess import run
from django import template
import git
from datetime import datetime

register = template.Library()

@register.simple_tag
def gitpython_sha():
    try :
        repo = git.Repo(search_parent_directories=True)
        print(repo.head.object.author)
        print(repo.head.object.name_rev)
        print(repo.active_branch)
        date = repo.active_branch.commit.committed_date
        date_obj = datetime.fromtimestamp(date)
        formatted_date = date_obj.strftime("%Y-%m-%d_%H:%M:%S")
        print(formatted_date)
        return repo.active_branch.name + '-' + repo.head.object.hexsha[-7:] + '-' + formatted_date
    except Exception:
        return 'not available'

