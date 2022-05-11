"""
Module with Laptop class and respectives methods who represents the laptops in web scrapping 
"""

from dataclasses import dataclass


@dataclass(slots=True)
class Laptop:
    """Laptop class"""
    name: str
    description: str
    price: float
    number_of_reviews: int
    rating: int
    link: str

    def __init__(self, name:str, description: str, price: str, link:str, number_of_reviews: int, rating: int) -> None:
        """Initializer of the class"""
        self.name = name
        self.description = description
        self.price = float(price.split("$")[1])
        self.number_of_reviews = number_of_reviews
        self.rating = rating
        self.link = link
    
    def to_dict(self) -> dict:
        "Object to json"
        return{
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'number_of_reviews': self.number_of_reviews,
            'rating': self.rating,
            'link': self.link
        }