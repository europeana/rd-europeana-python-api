import pytest

# this is an autouse pytest fixture that disables sending HTTP requests while running
# tests. In theory, it disables any request sent by python functionality that uses url
# lib3 under the hood.


@pytest.fixture(autouse=True)
def no_http_requests(monkeypatch):
    def urlopen_mock(self, method, url, *args, **kwargs):
        raise RuntimeError(
            f"The test was about to {method} {self.scheme}://{self.host}{url}"
        )

    monkeypatch.setattr(
        "urllib3.connectionpool.HTTPConnectionPool.urlopen", urlopen_mock
    )
