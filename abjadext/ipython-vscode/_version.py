__version_info__ = (1, 0)
__version__ = ".".join(str(x) for x in __version_info__[:2]) + "".join(
    __version_info__[2:] or []
)
