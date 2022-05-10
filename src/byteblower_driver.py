"""
ByteBlower chassis shell driver.
"""
import logging
from typing import Optional

from byteblowerll.byteblower import ByteBlower, ByteBlowerInterface, ByteBlowerServer, MeetingPoint, PhysicalInterface
from cloudshell.logging.qs_logger import get_qs_logger
from cloudshell.shell.core.driver_context import AutoLoadDetails, InitCommandContext, ResourceCommandContext
from cloudshell.shell.core.resource_driver_interface import ResourceDriverInterface

from byteblower_data_model import (
    ByteBlowerChassisShell2G,
    ByteBlowerEndPoint,
    GenericTrafficGeneratorModule,
    GenericTrafficGeneratorPort,
)


class ByteBlowerChassis2GDriver(ResourceDriverInterface):
    """ByteBlower chassis shell driver."""

    def __init__(self) -> None:
        """Initialize object variables, actual initialization is performed in initialize method."""
        self.logger: logging.Logger = None
        self.resource: ByteBlowerChassisShell2G = None
        self.server: ByteBlowerServer = None
        self.meeting_point: Optional[MeetingPoint] = None

    def initialize(self, context: InitCommandContext) -> None:
        """Initialize ByteBlower chassis shell."""
        self.logger = get_qs_logger(log_group="traffic_shells", log_file_prefix=context.resource.name)
        self.logger.setLevel(logging.DEBUG)

    # pylint: disable=useless-super-delegation
    def cleanup(self) -> None:
        """Cleanup ByteBlower chassis shell (must implement from API)."""
        super().cleanup()

    def get_inventory(self, context: ResourceCommandContext) -> AutoLoadDetails:
        """Load ByteBlower chassis inventory to CloudShell (from API)."""
        self.resource = ByteBlowerChassisShell2G.create_from_context(context)
        server_address = context.resource.address
        meeting_point_address = self.resource.meeting_point

        bb = ByteBlower.InstanceGet()
        self.server = bb.ServerAdd(server_address)
        if meeting_point_address:
            self.meeting_point = bb.MeetingPointAdd(meeting_point_address)

        self._load_chassis()
        return self.resource.create_autoload_details()

    def _load_chassis(self) -> None:
        """Load chassis resource and attributes."""
        service_info = self.server.ServiceInfoGet()

        self.resource.vendor = "Excentis"
        self.resource.model_name = service_info.SeriesGet()
        self.resource.version = service_info.VersionGet()

        physical_interfaces = self.server.PhysicalInterfacesGet()
        for physical_interface in physical_interfaces:
            self._load_module_bb(physical_interface)

        if self.meeting_point:
            card_id = len(physical_interfaces) + 1
            gen_module = GenericTrafficGeneratorModule(f"Module{card_id}")
            self.resource.add_sub_resource(f"M{card_id}", gen_module)
            for index, device in enumerate(self.meeting_point.DeviceListGet()):
                self._load_ep_bb(gen_module, device, index)

    def _load_module_bb(self, physical_interface: PhysicalInterface) -> None:
        """Load module resource and attributes."""
        card_id = physical_interface.IdGet() + 1
        gen_module = GenericTrafficGeneratorModule(f"Module{card_id}")
        self.resource.add_sub_resource(f"M{card_id}", gen_module)

        gen_module.model_name = physical_interface.NameGet()
        for interface in physical_interface.ByteBlowerInterfaceGet():
            self._load_port_bb(gen_module, interface)

    def _load_port_bb(self, gen_module: GenericTrafficGeneratorModule, interface: ByteBlowerInterface) -> None:
        """Get port resource and attributes."""
        gen_port = GenericTrafficGeneratorPort(interface.NameGet())
        gen_module.add_sub_resource(f"P{interface.PortIdGet()}", gen_port)

    def _load_ep_bb(self, gen_module: GenericTrafficGeneratorModule, device, index: int) -> None:
        """Get endpoint resource and attributes."""
        name = device.DeviceInfoGet().GivenNameGet()
        if name in [r.name for r in gen_module.resources.values()]:
            return
        endpoint = ByteBlowerEndPoint(name)
        # The same EP can appear twice in BB server (bug?)
        gen_module.add_sub_resource(f"EP{index + 1}", endpoint)

        network_info = device.DeviceInfoGet().NetworkInfoGet()
        endpoint.address = network_info.IPv4Get()
        endpoint.identifier = device.DeviceIdentifierGet()
