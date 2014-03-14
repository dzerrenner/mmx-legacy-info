from collections import UserDict
import os.path
import xmltodict
from mmx_legacy_info import BASE_DIR, DEFAULT_LOCALE


class XMLBase(UserDict):
    """
    Base class for XML-based data files.

    Subclasses can direct XML parsing by adjusting the _element_handler method.
    """
    def __init__(self, *args, locale=DEFAULT_LOCALE, **kwargs):
        super().__init__(*args, **kwargs)
        self.locale = locale
        self.filename = ""

    def _element_handler(self, path, item):
        # stub implementation
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


class ScreenText(XMLBase):
    """
    reads locale data

    >>> l = ScreenText()
    >>> l['DIALOG_OPTION_AIOLOS_1']
    'Anwerbung: Kundschafter'

    >>> # unknown locale
    >>> l = ScreenText(locale='yy')
    Traceback (most recent call last):
    ...
    FileNotFoundError: Data file for locale yy not found. Please check if this file exists: 'D:\Games\Steam\SteamApps\common\Might & Magic X - Legacy\Might and Magic X Legacy_Data\StreamingAssets\Localisation\yy\loca.xml'

    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filename = os.path.join(BASE_DIR, "Localisation", self.locale, "loca.xml")
        self._parse_file()

    def _element_handler(self, path, item):
        """
        Use ID as dictionary key and the text element as value
        <LocaData id="NPC_NAME_AONBARR">Aonbarr</LocaData>
        """
        key = path[-1][1]['id']
        self.data[key] = item.strip()
        return True


class NPCDialog(XMLBase):
    def __init__(self, *args, **kwargs):
        print("args:", args)
        print("kwargs:", kwargs)
        if 'dialog_key' not in kwargs:
            raise KeyError("Dialog needs to be initialized with dialog_key keyword argument")
        dialog_key = kwargs.pop('dialog_key')
        super().__init__(*args, **kwargs)
        self.filename = os.path.join(BASE_DIR, "Dialog", "{}.xml".format(dialog_key))
        self._parse_file()

    def _element_handler(self, path, item):
        print("path:", path)
        print("item:", item, "\n")
        return True