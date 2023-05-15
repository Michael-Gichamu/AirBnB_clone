#!/usr/bin/python3
"""Creates a Place Class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class that inherits from BaseModel.

    args:
        city_id (str): The ID of the city associated with the place. Defaults to an empty string, which will be the city.id.
        user_id (str): The ID of the user associated with the place. Defaults to an empty string, which will be the user.id.
        name (str): The name of the place. Defaults to an empty string.
        description (str): The description of the place. Defaults to an empty string.
        number_rooms (int): The number of rooms in the place. Defaults to 0.
        number_bathrooms (int): The number of bathrooms in the place. Defaults to 0.
        max_guest (int): The maximum number of guests allowed in the place. Defaults to 0.
        price_by_night (int): The price per night for the place. Defaults to 0.
        latitude (float): The latitude coordinate of the place's location. Defaults to 0.0.
        longitude (float): The longitude coordinate of the place's location. Defaults to 0.0.
        amenity_ids (list): The list of IDs of amenities associated with the place. Defaults to an empty list, which will be the list of Amenity.id later.
    """
    city_id: str = ""
    user_id: str = ""
    name: str = ""
    description: str = ""
    number_rooms: int = 0
    number_bathrooms: int = 0
    max_guest: int = 0
    price_by_night: int = 0
    latitude: float = 0.0
    longitude: float = 0.0
    amenity_ids: List[str] = []
