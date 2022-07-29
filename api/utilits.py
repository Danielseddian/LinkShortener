import secrets
import string

from typing import List, Tuple, Union


def generate_string(
    excludes: Union[List, Tuple] = (), alphabet: str = string.ascii_letters + string.digits + "_-", length: int = 5
) -> str:
    """
    Generates random characters set
    :param excludes: Set of links in database
    :param alphabet: Set of alphabet, digits and characters for generation
    :param length: Length of string
    :return: Random string
    """
    link: str = ""
    while not link or link in excludes:
        link: str = "".join(secrets.choice(alphabet) for i in range(length))
    return link
