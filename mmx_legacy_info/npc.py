from collections import namedtuple

NPCRecord = namedtuple('NPCRecord', 'id, name_key, hireling_profession, description, portrait, dialog_key,'
                                    'travel_station, effects, hire_price, hire_share, can_be_fired,'
                                    'allow_sell, symbol')


class NPC(NPCRecord):
    """
    NPC data

    >>> import mmx_legacy_info, os.path, csv
    >>> npc_file = os.path.join(mmx_legacy_info.BASE_DIR, "StaticData", "NpcStaticData.csv")
    >>> reader = csv.reader(open(npc_file, newline=''))
    >>> npc_list = [NPC(*l) for l in reader]
    >>> lord_haart = npc_list[3]
    >>> lord_haart.name_key
    'NPC_NAME_LORD_HAART'

    >>> lord_haart.has_dialog
    True

    >>> lord_haart.buys_objects
    True

    >>> lord_haart.is_hireling
    False

    """

    @property
    def is_hireling(self):
        return self.hireling_profession != ''

    @property
    def buys_objects(self):
        return self.allow_sell != ''

    @property
    def has_dialog(self):
        return self.dialog_key != ''