
from cloudshell.traffic.tg import TgChassisHandler

from byteblower.byteblowerll import byteblower

from byteblower_data_model import (ByteBlower_Chassis_Shell_2G, GenericTrafficGeneratorModule,
                                   GenericTrafficGeneratorPort, ByteBlowerEndPoint)


class ByteBlowerHandler(TgChassisHandler):

    def initialize(self, context, logger):
        """
        :param InitCommandContext context:
        """
        resource = ByteBlower_Chassis_Shell_2G.create_from_context(context)
        super(self.__class__, self).initialize(resource, logger)

    def load_inventory(self, context):
        """
        :param InitCommandContext context:
        """

        server_address = context.resource.address
        meetingpoint_address = server_address

        bb = byteblower.ByteBlower.InstanceGet()
        self.server = bb.ServerAdd(server_address)
        self.meetingpoint = bb.MeetingPointAdd(meetingpoint_address)

        self._load_chassis()
        return self.resource.create_autoload_details()

    def _load_chassis(self):
        """ Load chassis resource and attributes. """

        service_info = self.server.ServiceInfoGet()

        self.resource.vendor = 'Excentis'
        self.resource.model_name = service_info.SeriesGet()
        self.resource.version = service_info.VersionGet()

        physical_interfaces = self.server.PhysicalInterfacesGet()
        for physical_interface in physical_interfaces:
            self._load_module_bb(physical_interface)

        card_id = len(physical_interfaces) + 1
        gen_module = GenericTrafficGeneratorModule('Module{}'.format(card_id))
        self.resource.add_sub_resource('M{}'.format(card_id), gen_module)

        for index, device in enumerate(self.meetingpoint.DeviceListGet()):
            self._load_ep_bb(gen_module, device, index)

    def _load_module_bb(self, physical_interface):
        """ Load module resource and attributes. """

        card_id = physical_interface.IdGet() + 1
        gen_module = GenericTrafficGeneratorModule('Module{}'.format(card_id))
        self.resource.add_sub_resource('M{}'.format(card_id), gen_module)

        gen_module.model_name = physical_interface.NameGet()
        for interface in physical_interface.ByteBlowerInterfaceGet():
            self._load_port_bb(gen_module, interface)

    def _load_port_bb(self, gen_module, interface):
        """ Get port resource and attributes. """

        gen_port = GenericTrafficGeneratorPort(interface.NameGet())
        gen_module.add_sub_resource('P{}'.format(interface.PortIdGet()), gen_port)

    def _load_ep_bb(self, gen_module, device, index):
        """ Get endpoint resource and attributes. """

        name = device.DeviceInfoGet().GivenNameGet()
        if name in [r.name for r in gen_module.resources.values()]:
            return
        endpoint = ByteBlowerEndPoint(name)
        # The same EP can appear twice in BB server (bug?)
        gen_module.add_sub_resource('EP{}'.format(index + 1), endpoint)

        network_info = device.DeviceInfoGet().NetworkInfoGet()
        endpoint.address = network_info.IPv4Get()
        endpoint.identifier = device.DeviceIdentifierGet()
