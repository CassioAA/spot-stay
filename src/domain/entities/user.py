class User:
    def __init__(self, id_: str, name: str) -> None:
        if not name:
            raise ValueError("User name cannot be empty")
        if not id_:
            raise ValueError("User id cannot be empty")

        self._id_ = id_
        self._name = name

    def get_id(self) -> str:
        return self._id_

    def get_name(self) -> str:
        return self._name