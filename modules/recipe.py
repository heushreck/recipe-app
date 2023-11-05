from datetime import datetime
from dataclasses import dataclass
from typing import List

@dataclass
class Recipe():
    """A recipe with a name, ingredients, instructions, and date."""
    name: str
    ingredients: List[str]
    instructions: List[str]
    date: datetime.date
    image: str = None
    has_second_page: bool = False
    second_page: str = None
