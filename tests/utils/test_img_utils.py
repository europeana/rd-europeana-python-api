from contextlib import nullcontext as does_not_raise

import pytest
import PIL.Image as Image

from pyeuropeana.utils.img_utils import url2img


class TestUrl2img(object):
    @pytest.mark.parametrize(
        "url, time_limit, expectation",
        [
            (5, "a", pytest.raises(TypeError)),
            (5, 5, pytest.raises(TypeError)),
            ([], 2.5, pytest.raises(TypeError)),
            ("http://pyeuropeanatesturl.com", "a", pytest.raises(TypeError)),
            ("http://pyeuropeanatesturl.com", [], pytest.raises(TypeError)),
            ("http://pyeuropeanatesturl.com", 5, does_not_raise()),
            ("http://pyeuropeanatesturl.com", 5.7, does_not_raise()),
        ],
    )
    def test_url2img_inputs(self, url, time_limit, expectation):
        with expectation:
            assert url2img(url, time_limit) is None  # none because of function logic

    @pytest.mark.parametrize(
        "url, time_limit, expectation",
        [
            ("http://pyeuropeanatesturl.com", 5, None),
            ("http://pyeuropeanatesturl.com", 5.7, None),
        ],
    )
    def test_url2img_outputs(self, url, time_limit, expectation):
        assert url2img(url, time_limit) == expectation
