from decorator import GithubAuth


@GithubAuth.login_required
def important_view(*args, **kwargs):
    print("doing important stuff ...")
    return {"status": "complete"}