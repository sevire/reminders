from typing import Iterable, Any


class ManageAlerts():

    def __init__(self) -> None:
        super().__init__()

    def __eq__(self, o: object) -> bool:
        return super().__eq__(o)

    def __ne__(self, o: object) -> bool:
        return super().__ne__(o)

    def __str__(self) -> str:
        return super().__str__()

    def __repr__(self) -> str:
        return super().__repr__()

    def __hash__(self) -> int:
        return super().__hash__()

    def __format__(self, format_spec: str) -> str:
        return super().__format__(format_spec)

    def __getattribute__(self, name: str) -> Any:
        return super().__getattribute__(name)

    def __delattr__(self, name: str) -> None:
        super().__delattr__(name)

    def __sizeof__(self) -> int:
        return super().__sizeof__()

    def __reduce__(self) -> tuple:
        return super().__reduce__()

    def __reduce_ex__(self, protocol: int) -> tuple:
        return super().__reduce_ex__(protocol)

    def __dir__(self) -> Iterable[str]:
        return super().__dir__()

    def __init_subclass__(cls) -> None:
        super().__init_subclass__()