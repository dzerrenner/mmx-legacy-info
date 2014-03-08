from collections import UserDict
import os.path
import xmltodict
from mmx_legacy_info import BASE_DIR, DEFAULT_LOCALE


class MMXLocale(UserDict):
    """
    reads locale data

    >>> l = MMXLocale()
    >>> l['DIALOG_OPTION_AIOLOS_1']
    'Anwerbung: Kundschafter'

    >>> # unknown locale
    >>> l = MMXLocale(locale='yy')
    Traceback (most recent call last):
    ...
    FileNotFoundError: Data file for locale yy not found. Please check if this file exists: 'D:\Games\Steam\SteamApps\common\Might & Magic X - Legacy\Might and Magic X Legacy_Data\StreamingAssets\Localisation\yy\loca.xml'

    """

    def __init__(self, locale=DEFAULT_LOCALE):
        super().__init__()
        self.locale = locale
        self.filename = os.path.join(BASE_DIR, "Localisation", self.locale, "loca.xml")
        self._parse_file()

    def _element_handler(self, path, item):
        key = path[-1][1]['id']
        self.data[key] = item.strip()
        return True

    def _parse_file(self):
        # check if file exists
        if not os.path.isfile(self.filename):
            raise FileNotFoundError(
                "Data file for locale {0} not found. Please check if this file exists: '{1}'".format(
                    self.locale,
                    self.filename
                )
            )

        # load contents
        xmltodict.parse(
            open(self.filename, 'rb'),  # xmltodict expects bytes, not string
            encoding="UTF-8",
            item_depth=2,
            item_callback=self._element_handler
        )