from typing import List, Iterator

def toy_function(l: list, pos: int = 0) -> str:
    """A simple toy function to print an item of a list

    Args:
        l (list): a list of items
        pos (int, optional): the position in the list of the item. Defaults to 0.

    Returns:
        str: a string describing the item
    """
    return f"you seleced {l[pos]}"

class ToyClass:
    """a simple toy class
    """
    def __init__(self, name: str, l: list = [], d: dict = {}):
        """initialize the toy class

        Args:
            name (str): the name of this oblect i think
            l (list, optional): a list in the object. Defaults to [].
            d (dict, optional): a dict in the object. Defaults to {}.
        """
        self.name=name
        self.l=l
        self.d=d
    
    def get_from_l(self, p: List[int] = []) -> Iterator[str]:
        """get the thing from the thing

        Args:
            p (List[int], optional): positions in the list. Defaults to [].

        Yields:
            Iterator[str]: iterator of strings describing the list contents
        """
        for pos in p:
            yield f"{self.name} returns {self.l[pos]}"

    def get_from_d(self, keys=[]) -> list:
        """get the thing from the dict

        Args:
            keys (list, optional): list of dict keys. Defaults to [].

        Returns:
            list: the contents of the dict at the given keys
        """
        return [self.d[k] for k in keys]