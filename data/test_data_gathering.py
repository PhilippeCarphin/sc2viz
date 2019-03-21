import unittest
import sc2reader
import pysc2
from pprint import pprint
import matplotlib.pyplot as plt

# THis helps the IDE
import sc2reader.events
import sc2reader.events.game


class TestDataGathering(unittest.TestCase):

    def __init__(self, methodName='runTest'):
        super(TestDataGathering, self).__init__(methodName=methodName)
        self.replay = pysc2.SC2ReplayWrapper('spawningtool_replays/dark_v_Solar_Game1_PortAleksanderLE.SC2Replay')

    def test_process_unit_lifetime_events(self):
        categories = self.replay.categorize_unit_lifetime_events()
        self.assertTrue(len(categories) == 4)
        for cat in categories:
            self.assertTrue(len(categories[cat]) >= 50)

    def test_get_unit_from_event(self):
        """ For more info, add a breakpoint on the last line of this test and
        inspect the unit_born_event and the found_events list """
        categories = self.replay.categorize_unit_lifetime_events()
        a_unit_born_event = categories[sc2reader.events.tracker.UnitBornEvent][100]
        try:
            id_from_event = pysc2.get_unit_from_event(a_unit_born_event)
        except IndexError:
            id_from_event = pysc2.get
        unit_died_events = categories[sc2reader.events.tracker.UnitDiedEvent]
        found_events = pysc2.select_events_related_to_unit(unit_died_events, id_from_event)
        self.assertTrue(len(found_events) > 0)

    def test_unit_lifetime_post_processing(self):
        categories = self.replay.categorize_unit_lifetime_events()
        processed_data = pysc2.match_events_to_units(categories)
        self.assertTrue(len(processed_data) > 900)
        pass

    def test_post_post_processing(self):
        categories = self.replay.categorize_unit_lifetime_events()
        processed_data = pysc2.match_events_to_units(categories)
        post_post_processed = pysc2.prepare_data_for_visualisation(processed_data)
        import json
        json.dumps(post_post_processed)
        print(post_post_processed)
        pass