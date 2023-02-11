"""Timer utils module."""

import pyrootutils

ROOT = pyrootutils.setup_root(
    search_from=__file__,
    indicator=[".git"],
    pythonpath=True,
    dotenv=True,
)

from datetime import datetime, timezone, timedelta


class Timer:
    """Timer class for timing utillities."""

    def __init__(self) -> None:
        pass

    def now(self, iso: bool = False, utc: bool = False) -> str:
        """
        Get current time.

        Args:
            iso (bool, optional): ISO format.
            utc (bool, optional): UTC time.

        Returns:
            str: Current time.

        Examples:
            >>> t.now()
            2023-02-11 21:16:08.282540
            >>> t.now(utc=True)
            2023-02-11 14:16:08.282565
            >>> t.now(iso=True)
            2023-02-11T21:16:08.282571
            >>> t.now(iso=True, utc=True)
            2023-02-11T14:17:41.290629Z
        """
        now = datetime.now() if not utc else datetime.now(timezone.utc)
        if iso:
            return now.isoformat().replace("+00:00", "Z")
        return now.strftime("%Y-%m-%d %H:%M:%S.%f")

    def today(self) -> str:
        """
        Get current date.

        Returns:
            str: Current date.

        Examples:
            >>> t.today()
            2023-02-11
        """
        return datetime.now().strftime("%Y-%m-%d")

    def from_today(self, days: int) -> str:
        """
        Get date from today.

        Args:
            days (int): Number of days.

        Returns:
            str: Date from today.

        Examples:
            >>> t.from_today(1)
            2023-02-12
            >>> t.from_today(-1)
            2023-02-10
        """
        return (datetime.now() + timedelta(days=days)).strftime("%Y-%m-%d")

    def diff(self, start: str, end: str, iso: bool = False) -> str:
        """
        Get time difference.

        Args:
            start (str): Start time.
            end (str): End time.
            iso (bool, optional): ISO format.

        Returns:
            str: Time difference.

        Examples:
            >>> t.diff("2023-02-11 21:16:08.282540", "2023-02-11 21:16:08.282565")
            0:00:00.000025
            >>> t.diff("2023-02-11 21:16:08.282540", "2023-02-11 21:16:08.282565", iso=True)
            PT0.000025S
        """
        # check if iso format has "Z" (utc)
        if iso or start[-1] == "Z":
            start = start[:-1]
            end = end[:-1]
        start = datetime.fromisoformat(start) if iso else datetime.strptime(start, "%Y-%m-%d %H:%M:%S.%f")
        end = datetime.fromisoformat(end) if iso else datetime.strptime(end, "%Y-%m-%d %H:%M:%S.%f")
        diff = end - start
        if iso:
            return str(diff)
        return str(diff).split(".")[0]

if __name__ == "__main__":
    """Debugging."""

    t = Timer()

    print(t.now())
    print(t.now(utc=True))
    print(t.now(iso=True))
    print(t.now(iso=True, utc=True))

    print(t.today())
    print(t.from_today(1))
    print(t.from_today(-1))

    start = t.now(iso=True, utc=True)
    end = t.now(iso=True, utc=True)

    print(t.diff(start, end, iso=True))
