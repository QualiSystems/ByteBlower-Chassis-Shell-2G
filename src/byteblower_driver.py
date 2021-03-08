
from cloudshell.traffic.tg import TgChassisDriver

from byteblower_handler import ByteBlowerHandler


class ByteBlowerChassis2GDriver(TgChassisDriver):

    def __init__(self):
        self.handler = ByteBlowerHandler()

    def initialize(self, context):
        super().initialize(context)

    def cleanup(self):
        super().cleanup()

    def get_inventory(self, context):
        return super().get_inventory(context)
