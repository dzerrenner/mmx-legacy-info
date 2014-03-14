from collections import namedtuple

QuestRecord = namedtuple('QuestRecord', 'id, description, kill_monster_class, kill_monster_type, kill_monster_id,'
                                        'token_id, npc_id, is_return, is_main, days_to_pass, terrain_steps, location')


class Quest(QuestRecord):
    """
    Data for distinct quest steps belonging to a quest.

    The constructor of this class takes 21 positional arguments in the same order as they are listed in the data file.

    >>> import mmx_legacy_info, os.path, csv
    >>> quest_file = os.path.join(mmx_legacy_info.BASE_DIR, "StaticData", "QuestObjectives.csv")
    >>> # filter comment rows
    >>> reader = csv.reader(filter(lambda row: row[0]!='#' and not row.startswith('StaticID'), open(quest_file, newline='')))
    >>> quest_list = [QuestRecord(*line) for line in reader]  # note list expansion
    >>> quest_list[0].description
    'QUEST_OBJECTIVE_LOOKING_FOR_JOB_1_1'

    Use this together with l10n:
    >>> from mmx_legacy_info import MMX
    >>> m = MMX()
    >>> m.parse_locale()
    >>> m.locale[quest_list[0].description]
    'Trefft Euch mit Maximus in der Stadtgarnison'
    """


QuestStepRecord = namedtuple('QuestStepRecord', 'id, quest_type, name_key, flavor_key, short_key, npc_id, objectives,'
                                                'repeat_time, xp, next_step, loot, item, item_drop_chance,'
                                                'prefix_chance, prefix_probability, suffix_chance, suffix_probability,'
                                                'item_spec, gold_chance, gold_amount, token_id')


class QuestStep(QuestStepRecord):
    """
    Data for distinct quest steps belonging to a quest.

    The constructor of this class takes 21 positional arguments in the same order as they are listed in the data file.

    >>> import mmx_legacy_info, os.path, csv
    >>> step_file = os.path.join(mmx_legacy_info.BASE_DIR, "StaticData", "QuestSteps.csv")
    >>> # filter comment rows
    >>> reader = csv.reader(filter(lambda row: row[0]!='#' and not row.startswith('StaticID'), open(step_file, newline='')))
    >>> step_list = [QuestStep(*line) for line in reader]  # note list expansion
    >>> step_list[0].name_key
    'QUEST_STEP_LOOKING_FOR_JOB_1_NAME'
    """


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
    >>> # filter comment rows
    >>> reader = csv.reader(filter(lambda row: row[0]!='#' and not row.startswith('StaticID'), open(npc_file, newline='')))
    >>> npc_list = [NPC(*line) for line in reader]  # note list expansion
    >>> lord_haart = npc_list[0]
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