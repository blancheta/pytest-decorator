from decorator import GithubAuth
from views import function_to_mock


def test_decorator(mocker):
    session = mocker.patch(
        "decorator.session",
        {
            "oauth": 1,
            "supersecret": "abc"
        }
    )
    print(session.get("supersecret"))

    is_valid_token_mock = mocker.patch("decorator.GithubAuth.is_valid_token")
    is_valid_token_mock.return_value = True

    function_to_test = lambda *x, **y: "output"
    response = GithubAuth.login_required(function_to_test)()

    assert response == "output"

def test_function_with_decorator_mock(mocker, mock_login_required):

    output = function_to_mock()
    print(output)

if "__main__" == __name__:
    print(test_decorator())
