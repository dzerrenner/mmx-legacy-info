from collections import UserDict
import os.path
import xmltodict
from mmx_legacy_info import BASE_DIR, DEFAULT_LOCALE


class MMXLocale(UserDict):
    def __init__(self, locale=DEFAULT_LOCALE, **kwargs):
        super().__init__(**kwargs)
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