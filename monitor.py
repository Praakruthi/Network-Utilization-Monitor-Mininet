from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.recoco import Timer

log = core.getLogger()

class Monitor(object):
    def __init__(self):
        core.openflow.addListeners(self)
        self.stats = {}

        # Run every 5 seconds
        Timer(5, self.request_stats, recurring=True)

    def _handle_ConnectionUp(self, event):
        log.info("Switch connected: %s", event.connection)

    def request_stats(self):
        for connection in core.openflow.connections:
            connection.send(of.ofp_stats_request(
                body=of.ofp_flow_stats_request()
            ))

    def _handle_FlowStatsReceived(self, event):
        total_bytes = 0

        # Sum only meaningful flows
        for stat in event.stats:
            if stat.byte_count > 0:
                total_bytes += stat.byte_count

        dpid = event.connection.dpid

        if dpid in self.stats:
            prev_bytes = self.stats[dpid]

            # Convert to Mbps
            bandwidth_mbps = (total_bytes - prev_bytes) * 8 / (5.0 * 1000000)

            log.info("Switch %s Bandwidth: %.4f Mbps",
                     dpid, bandwidth_mbps)

        # Store current stats for next calculation
        self.stats[dpid] = total_bytes


def launch():
    core.registerNew(Monitor)
