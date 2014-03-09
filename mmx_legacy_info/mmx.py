import csv
import os.path

from mmx_legacy_info import BASE_DIR, DEFAULT_LOCALE
import mmx_legacy_info
from mmx_legacy_info.locale import MMXLocale
from mmx_legacy_info.npc import NPC


class MMX(object):
    """
    Defines the main class to load files and process them.

    Using locales:
        Simple example (with default locale 'de'):

        >>> m = MMX()
        >>> m.parse_locale()
        >>> m.locale['DIALOG_OPTION_AIOLOS_1']
        'Anwerbung: Kundschafter'

    Getting NPC data:
        >>> m.load_npcs()
        >>> m.npc_list[0].name_key
        'NPC_NAME_LORD_HAART'

    Using NPC data together with locale:
        >>> m.locale[m.npc_list[0].name_key]
        'Lord Haart'
    """

    def __init__(self, base_dir=BASE_DIR):
        """
        :param base_dir: directory where to find the game files. Assumes an installation with Steam and defaults to
        "D:\\Games\\Steam\\SteamApps\\common\\Might & Magic X - Legacy\\Might and Magic X Legacy_Data\\StreamingAssets".
        """
        self.base_dir = base_dir
        self.locale = None
        self.npc_list = []

    def parse_locale(self, locale=DEFAULT_LOCALE):
        """
        Loads a local file to memory.

        use locales:
        >>> m = MMX()
        >>> m.parse_locale("en")
        >>> m.locale['DIALOG_OPTION_AIOLOS_1']
        'Hire: Scout'

        >>> m = MMX()
        >>> m.parse_locale("jp")
        >>> m.locale['DIALOG_OPTION_AIOLOS_1']
        '雇用：スカウト'

        >>> # separate install dir
        >>> import mmx_legacy_info, os.path
        >>> m = MMX(r"d:\test_mmx\StramingAssets")
        >>> m.parse_locale("kr")
        >>> m.locale['DIALOG_OPTION_AIOLOS_1']
        '고용: 정찰병'
        """
        self.locale = MMXLocale(locale)

    def load_npcs(self):
        """
        Loads all NPCs to memory.
        """

        npc_file = os.path.join(mmx_legacy_info.BASE_DIR, "StaticData", "NpcStaticData.csv")
        # filter comment lines and lines starting with 'StaticID', which are used as column headers.
        reader = csv.reader(
            filter(lambda row: row[0] != '#' and not row.startswith('StaticID'), open(npc_file, newline=''))
        )
        self.npc_list = [NPC(*line) for line in reader]  # note list expansion
