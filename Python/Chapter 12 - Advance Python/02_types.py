n : int = 5
name : str = "Saurabh"
def add(a : int, b : int) -> int:
    return a + b

print(add(2, 3))


#Type hints - these are present in typing module
from typing import List, Tuple, Union
number: List[int] = [1,2,3,4,5]
person: tuple[int, str] = (45, "Saurabh")