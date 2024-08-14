from utils import session


class BBGithubAuth:

    @staticmethod
    def is_valid_token():
        return False


def login_required(func):
    def inner_function(*args, **kwargs):
        if (
            BBGithubAuth.is_valid_token()
            and session["oauth"] == 1
            and session["supersecret"] == "abc"
        ):
            return func(*args, **kwargs)
        else:
            return "invalid-token"

    return inner_function()


if __name__ == "__main__":
    function_to_test = lambda *x, **y: "output"
    output = login_required(function_to_test)
    print(output)