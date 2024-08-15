import pytest


@pytest.fixture
def mock_login_required(mocker):
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