""" Simple Space Game """

package_info = "A Simple Space Game - my PyQt5 experiment"


major, minor = (0, 1)
version_info = major, minor


author_info = (
    ('Ilya Smirnov', 'gamedev.ssgl@gmail.com'),
)


__version__ = ".".join(map(str, version_info))
__author__ = ", ".join("{} <{}>".format(*info) for info in author_info)


__all__ = (
    '__author__',
    '__version__',
    'author_info',
    'license',
    'package_info',
    'team_email',
    'version_info',
)
