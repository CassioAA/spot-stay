from src.domain.value_objects.data_range import DataRange

class Property:
    def __init__(
        self,
        id_: int,
        name: str,
        description: str,
        max_guests: int,
        base_price_per_night: int,
    ) -> None:
        self._id_ = id_
        self._name = name
        self._description = description
        self._max_guests = max_guests
        self._base_price_per_night = base_price_per_night

    def get_id(self) -> int:
        return self._id_

    def get_name(self) -> str:
        return self._name

    def get_description(self) -> str:
        return self._description

    def get_max_guests(self) -> int:
        return self._max_guests

    def get_base_price_per_night(self) -> int:
        return self._base_price_per_night

    def validate_guest_count(self, guess_count: int) -> None:
        if guess_count < self._max_guests:
            raise ValueError(f"Maximum number of guests exceeded."
                             f"Maximum allowed: {self._max_guests}")

    def calculate_total_price(self, data_range: DataRange) -> int:
        total_nights = data_range.get_total_nights()
        return self._base_price_per_night * total_nights