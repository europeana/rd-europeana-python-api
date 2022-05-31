from typing import Union
from multiprocessing import Process, Manager
import urllib.request as urllibrec

from PIL import Image


def url2img(url: str, time_limit: Union[int, float] = 10) -> Image.Image:

    """
    A utility function for obtaining a :obj:`PIL.Image` object given an image URL.

    Parameters

    url: str
      The URL to which an HTTP request will be sent to retrieve the image.

    time_limit: int or float, optional
      How long to wait (in seconds) to retrieve the image until the request timeouts.
      When the request timeouts, the function returns None. Default is 10 seconds.

    Returns

    :obj:`PIL.Image`
      A Pillow Image object that is rendered in RGB mode.


    Raises

    TypeError
      Raises a TypeError if the argument passed to the parameter `url` is not a string.

    TypeError
        Raises a TypeError if the argument passed to the parameter `time_limit` is
        not an integer or a float.

    Notes

    The :obj:`PIL.Image` object that is returned when the function successfully
    retrieves the image at the given URL is rendered in RGB mode by default. To convert
    it to any other color mode, PIL utility methods can be utilized.

    Examples

    >>> import pyeuropeana.apis as apis
    >>> import pyeuropeana.utils as utils
    >>> resp = apis.search(
    >>>    query = 'Madrid',
    >>>    rows = 10,
    >>> )
    >>> df = utils.search2df(resp)
    >>> url = df['image_url'].values[0]
    >>> img = utils.url2img(url)
    """

    if not isinstance(url, str):
        raise TypeError(
            """
            The argument passed to the parameter `url` must be of type str.
            Got {} instead.
            """.format(
                type(url)
            )
        )

    if not isinstance(time_limit, (int, float)):
        raise TypeError(
            """
            The argument passed to the parameter `time_limit` must be an integer or a
            float. Got {} instead.
            """.format(
                type(time_limit)
            )
        )

    def worker(image_url, data_dict):
        try:
            data_dict["image"] = Image.open(urllibrec.urlopen(image_url)).convert("RGB")
        except Exception:
            data_dict["image"] = None

    manager = Manager()
    data_dict = manager.dict()

    action_process = Process(target=worker, args=(url, data_dict))
    action_process.start()
    action_process.join(timeout=time_limit)
    action_process.terminate()
    if "image" in data_dict.keys():
        return data_dict["image"]
    else:
        return None
