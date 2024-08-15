from decorator import GithubAuth
from views import important_view


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

    output = important_view()
    print(output)
    assert output == {"status": "complete"}
