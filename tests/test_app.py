import main

def test_hello(capsys):
    main.hello()
    captured = capsys.readouterr()
    assert "Hello, GitLab CI/CD!" in captured.out
