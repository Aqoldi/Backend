import git
from django.http import JsonResponse


def CI_CD(request):
    repo = git.Repo('./')
    origin = repo.remotes.origin
    origin.pull()
    return JsonResponse({})