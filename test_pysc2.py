import unittest
import sc2reader
import pysc2

class TestPysc2(unittest.TestCase):

    def __init__(self, methodName='runTest'):
        super(TestPysc2, self).__init__(methodName=methodName)
        self.replay = sc2reader.load_replay('spawningtool_replays/dark_v_Solar_Game1_PortAleksanderLE.SC2Replay')

    def test_events_with_type(self):

        control_group_events = list(pysc2.events_with_type(
            self.replay,
            sc2reader.events.game.GetControlGroupEvent
        ))

        control_groups_event_counts = {}
        for cge in control_group_events:
            if cge.control_group not in control_groups:
                control_groups[cge.control_group] = 0
            control_groups[cge.control_group] += 1

        print(control_groups)
        y_pos = range(10)
        heights = list(map(lambda i: control_groups.get(i, 0), y_pos))
        plt.bar(y_pos, heights)
        plt.show()
