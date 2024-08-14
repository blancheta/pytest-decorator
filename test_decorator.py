from decorator import login_required


def test_decorator(mocker):
    mocker.patch(
        "decorator.session",
        {
            "oauth": 1,
            "supersecret": "abc"
        }
    )

    is_valid_token_mock = mocker.patch("decorator.BBGithubAuth.is_valid_token")
    is_valid_token_mock.return_value = True

    function_to_test = lambda *x, **y: "output"
    response = login_required(function_to_test)()

    assert response == "output"


if "__main__" == __name__:
    print(test_decorator())