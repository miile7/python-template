def get_version() -> str:
    with open("VERSION", "r") as f:
        return f[0]

__version__ = get_version()