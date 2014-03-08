from mmx_legacy_info import BASE_DIR, DEFAULT_LOCALE
from mmx_legacy_info.locale import MMXLocale


class MMX(object):
    """
    Defines the main class to load files and process them.

    Using locales:
        Simple example (with defaule locale 'de'):

        >>> m = MMX()
        >>> m.parse_locale()
        >>> m.locale['DIALOG_OPTION_AIOLOS_1']
        'Anwerbung: Kundschafter'

        use other locales:
        >>> m = MMX()
        >>> m.parse_locale("en")
        >>> m.locale['DIALOG_OPTION_AIOLOS_1']
        'Hire: Scout'

        >>> m = MMX()
        >>> m.parse_locale("jp")
        >>> m.locale['DIALOG_OPTION_AIOLOS_1']
        '雇用：スカウト'

    """

    def __init__(self, base_dir=BASE_DIR):
        """
        :param base_dir: directory where to find the game files. Assumes an installation with Steam and defaults to
        "D:\\Games\\Steam\\SteamApps\\common\\Might & Magic X - Legacy\\Might and Magic X Legacy_Data\\StreamingAssets".
        """
        self.base_dir = base_dir
        self.locale = None

    def parse_locale(self, locale=DEFAULT_LOCALE):
        self.locale = MMXLocale(locale)