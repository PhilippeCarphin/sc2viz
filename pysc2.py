import sc2reader
import sc2reader.events.game as ge
import matplotlib.pyplot as plt
import numpy as np

class SC2ReplayWrapper:
    def __init__(self, replay_file=None):
        self._replay = sc2reader.load_replay('spawningtool_replays/dark_v_Solar_Game1_PortAleksanderLE.SC2Replay')


    def events_with_type(self, event_type, pid=None):
        for event in self._replay.game_events:
            if isinstance(event, event_type):
                if pid:
                    if pid == event.player.pid:
                        yield event
                else:
                    yield event
        # gen_type = (ee for ee in self._replay.game_events
        #             if isinstance(ee, event_type))

        # return (e for e in gen_type
        #         if not pid or pid == e.pid)

    def get_control_group_event_counts(self):
        control_group_events = list(self.events_with_type(
            replay,
            sc2reader.events.game.GetControlGroupEvent
        ))

        counts = {}
        for cge in control_group_events:
            if cge.control_group not in counts:
                counts[cge.control_group] = 0
            counts[cge.control_group] += 1

        return counts


replay = SC2ReplayWrapper()

def plot_locations(events, title):
    locations = np.array(list(map(lambda e:e.location, events)))
    try:
        plt.scatter(locations[:,0], locations[:,1])
        plt.title(title)
        plt.show()
    except:
        print("Empty List")

# target_points = list(replay.events_with_type(ge.TargetPointCommandEvent))
# plot_locations(target_points, "Plot of TargetPointCommandEvent's for any player")


target_points_p1 = list(replay.events_with_type(ge.TargetPointCommandEvent, pid=1))
plot_locations(target_points_p1, "Target points of P1")
target_points_p1 = list(replay.events_with_type(ge.TargetPointCommandEvent, pid=2))
plot_locations(target_points_p1, "Target points of P1")

quit()
replay = sc2reader.load_replay('spawningtool_replays/dark_v_Solar_Game1_PortAleksanderLE.SC2Replay')
events = replay.game_events[8000:]

def camera_events(replay, player=None):
    for event in replay.game_events:
        if isinstance(event, sc2reader.events.game.CameraEvent):
            if not player or event.player == player:
                yield event

camera_events = list(camera_events(replay))

camera_event_locations = map(lambda event: event.location, camera_events)

print(len(camera_events))

locations = np.array(list(camera_event_locations))
print(locations.shape)

plt.scatter(locations[:,0], locations[:,1])
plt.show()

#######################################################################

