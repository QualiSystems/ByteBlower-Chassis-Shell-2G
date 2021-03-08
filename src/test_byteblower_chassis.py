"""
Tests for ByteBlowerChassis2GDriver
"""
import pytest

from cloudshell.api.cloudshell_api import CloudShellAPISession, ResourceInfo
from cloudshell.shell.core.driver_context import AutoLoadCommandContext
from cloudshell.traffic.tg import TGN_CHASSIS_FAMILY, BYTEBLOWER_CHASSIS_MODEL
from shellfoundry_traffic.test_helpers import create_session_from_config, TestHelpers, print_inventory

from src.byteblower_driver import ByteBlowerChassis2GDriver


@pytest.fixture()
def server() -> str:
    """ Yields server address. """
    yield 'nl-srk03d-bb-st01.upclabs.com'


@pytest.fixture(scope='session')
def session() -> CloudShellAPISession:
    """ Yields active session. """
    yield create_session_from_config()


@pytest.fixture(scope='session')
def test_helpers(session: CloudShellAPISession) -> TestHelpers:
    """ Yields initialized TestHelpers object. """
    yield TestHelpers(session)


@pytest.fixture()
def driver(test_helpers: TestHelpers, server: str) -> ByteBlowerChassis2GDriver:
    """ Yields initialized ByteBlower driver for driver testing. """
    init_context = test_helpers.resource_init_command_context(TGN_CHASSIS_FAMILY, BYTEBLOWER_CHASSIS_MODEL, server)
    driver = ByteBlowerChassis2GDriver()
    driver.initialize(init_context)
    print(driver.logger.handlers[0].baseFilename)
    yield driver


@pytest.fixture()
def autoload_context(test_helpers: TestHelpers, server: str) -> AutoLoadCommandContext:
    """ Yields ByteBlower resource for shell autoload testing. """
    yield test_helpers.autoload_command_context('CS_GenericResource', BYTEBLOWER_CHASSIS_MODEL, server)


@pytest.fixture()
def autoload_resource(session: CloudShellAPISession, test_helpers: TestHelpers, server: str) -> ResourceInfo:
    """ Yields CPE resource for shell autoload testing. """
    resource = test_helpers.create_autoload_resource(BYTEBLOWER_CHASSIS_MODEL, 'test-byteblower', server)
    yield resource
    session.DeleteResource(resource.Name)


def test_autoload(driver: ByteBlowerChassis2GDriver, autoload_context: AutoLoadCommandContext) -> None:
    inventory = driver.get_inventory(autoload_context)
    print_inventory(inventory)


def test_autoload_session(session: CloudShellAPISession, autoload_resource: ResourceInfo) -> None:
    session.AutoLoad(autoload_resource.Name)
    session.GetResourceDetails(autoload_resource.Name)
    print('Done')
