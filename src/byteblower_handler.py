
from os import path

from cloudshell.shell.core.driver_context import AutoLoadDetails, AutoLoadResource, AutoLoadAttribute

from byteblower.byteblowerll import byteblower


class ByteBlowerHandler(object):

    def initialize(self, context, logger):
        """
        :type context: cloudshell.shell.core.driver_context.InitCommandContext
        """

        self.logger = logger

        address = context.resource.address
        server_address = context.resource.attributes['ByteBlower Chassis Shell 2G.Controller Address']
        meetingpoint_address = server_address

        bb = byteblower.ByteBlower.InstanceGet()
        self.server = bb.ServerAdd(server_address)
        self.meetingpoint = bb.MeetingPointAdd(meetingpoint_address)

    def get_inventory(self, context):
        """ Return device structure with all standard attributes

        :type context: cloudshell.shell.core.driver_context.AutoLoadCommandContext
        :rtype: cloudshell.shell.core.driver_context.AutoLoadDetails
        """

        self.resources = []
        self.attributes = []
        self._get_chassis_bb()
        details = AutoLoadDetails(self.resources, self.attributes)
        return details

    def _get_chassis_bb(self):
        """ Get chassis resource and attributes. """

        service_info = self.server.ServiceInfoGet()

        self.attributes.append(AutoLoadAttribute(relative_address='',
                                                 attribute_name='CS_TrafficGeneratorChassis.Model Name',
                                                 attribute_value=service_info.SeriesGet()))
        self.attributes.append(AutoLoadAttribute(relative_address='',
                                                 attribute_name='',
                                                 attribute_value=service_info.MachineIDGet()))
        self.attributes.append(AutoLoadAttribute(relative_address='',
                                                 attribute_name='ByteBlower Chassis Shell 2G.Server Description',
                                                 attribute_value=''))
        self.attributes.append(AutoLoadAttribute(relative_address='',
                                                 attribute_name='CS_TrafficGeneratorChassis.Vendor',
                                                 attribute_value='Excentis'))
        self.attributes.append(AutoLoadAttribute(relative_address='',
                                                 attribute_name='CS_TrafficGeneratorChassis.Version',
                                                 attribute_value=service_info.VersionGet()))

        physical_interfaces = self.server.PhysicalInterfacesGet()
        for physical_interface in physical_interfaces:
            self._get_module_bb(physical_interface)

        relative_address = 'M' + str(len(physical_interfaces) + 1)
        model = 'ByteBlower Chassis Shell 2G.GenericTrafficGeneratorModule'
        resource = AutoLoadResource(model=model,
                                    name='Module' + str(len(physical_interfaces) + 1),
                                    relative_address=relative_address)
        self.resources.append(resource)

        for index, device in enumerate(self.meetingpoint.DeviceListGet()):
            self._get_ep_bb(relative_address, device, index)

    def _get_module_bb(self, physical_interface):
        """ Get module resource and attributes. """

        relative_address = 'M' + str(physical_interface.IdGet() + 1)
        model = 'ByteBlower Chassis Shell 2G.GenericTrafficGeneratorModule'
        resource = AutoLoadResource(model=model,
                                    name='Module' + str(physical_interface.IdGet() + 1),
                                    relative_address=relative_address)
        self.resources.append(resource)
        self.attributes.append(AutoLoadAttribute(relative_address=relative_address,
                                                 attribute_name='CS_TrafficGeneratorModule.Model Name',
                                                 attribute_value=physical_interface.NameGet()))
        self.attributes.append(AutoLoadAttribute(relative_address=relative_address,
                                                 attribute_name=model + '.Serial Number',
                                                 attribute_value=''))
        self.attributes.append(AutoLoadAttribute(relative_address=relative_address,
                                                 attribute_name=model + '.Version',
                                                 attribute_value=''))
        for interface in physical_interface.ByteBlowerInterfaceGet():
            self._get_port_bb(relative_address, interface)

    def _get_port_bb(self, relative_address, interface):
        """ Get port resource and attributes. """

        index = str(interface.PortIdGet()) if interface.PortIdGet() else '1'
        relative_address = relative_address + '/P' + index
        resource = AutoLoadResource(model='ByteBlower Chassis Shell 2G.GenericTrafficGeneratorPort',
                                    name='Port' + index,
                                    relative_address=relative_address)
        self.resources.append(resource)

    def _get_ep_bb(self, relative_address, device, index):
        """ Get endpoint resource and attributes. """

        relative_address = relative_address + '/P' + str(index + 1)
        model = 'ByteBlower Chassis Shell 2G.ByteBlowerEndPoint'
        resource = AutoLoadResource(model=model,
                                    name=device.DeviceInfoGet().GivenNameGet(),
                                    relative_address=relative_address)
        self.resources.append(resource)

        network_info = device.DeviceInfoGet().NetworkInfoGet()
        self.attributes.append(AutoLoadAttribute(relative_address=relative_address,
                                                 attribute_name=model + '.Address',
                                                 attribute_value=network_info.IPv4Get()))
