from typing import Any, Literal

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


def _request_with_retry(
    method: Literal["get"] | Literal["post"], url: str, **kwargs: Any
) -> requests.Response:
    session = requests.Session()
    retries = Retry(
        total=5,
        backoff_factor=1,
        respect_retry_after_header=False,
        status_forcelist=[429],
        allowed_methods=[*Retry.DEFAULT_ALLOWED_METHODS, "POST"],
    )
    session.mount("https://", HTTPAdapter(max_retries=retries))
    return getattr(session, method)(url, **kwargs)


def get_with_retry(url: str, **kwargs: Any) -> requests.Response:
    return _request_with_retry("get", url, **kwargs)


def post_with_retry(url: str, **kwargs: Any) -> requests.Response:
    return _request_with_retry("post", url, **kwargs)
