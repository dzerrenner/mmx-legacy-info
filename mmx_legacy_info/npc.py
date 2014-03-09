from collections import namedtuple

NPCRecord = namedtuple('NPCRecord', 'id, name_key, hireling_profession, description, portrait, dialog_key,'
                                    'travel_station, effects, hire_price, hire_share, can_be_fired,'
                                    'allow_sell, symbol')


class NPC(NPCRecord):
    """
    NPC data.

    The constructor of this class accepts 13 positional arguments in the same order as they are listed in the data file.
    The data file for generating these lines can be read as follows:

    >>> import mmx_legacy_info, os.path, csv
    >>> npc_file = os.path.join(mmx_legacy_info.BASE_DIR, "StaticData", "NpcStaticData.csv")
    >>> reader = csv.reader(open(npc_file, newline=''))
    >>> npc_list = [NPC(*line) for line in reader]  # note list expansion
    >>> lord_haart = npc_list[3]
    >>> lord_haart.name_key
    'NPC_NAME_LORD_HAART'

    >>> lord_haart.has_dialog
    True

    >>> lord_haart.buys_objects
    True

    >>> lord_haart.is_hireling
    False

    >>> # not yet implemented
    >>> lord_haart.get_dialog()
    Traceback (most recent call last):
    ...
    NotImplementedError: Dialog extraction is not implemented yet.

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

    def get_dialog(self):
        """
        Gets the dialog object for this NPC.

        If the NPC has no dialog, a KeyError is raised. So far, every NPC seems to have a dialog attached, but that
        could be a subject to change.
        """
        if not self.has_dialog:
            raise KeyError("No dialog attached to this NPC.")
        raise NotImplementedError("Dialog extraction is not implemented yet.")