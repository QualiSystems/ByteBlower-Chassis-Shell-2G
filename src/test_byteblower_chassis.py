"""
Tests for ByteBlowerChassis2GDriver.
"""
# pylint: disable=redefined-outer-name,unused-import
from typing import Iterable

import pytest
from cloudshell.api.cloudshell_api import CloudShellAPISession, ResourceInfo
from cloudshell.shell.core.driver_context import AutoLoadCommandContext
from cloudshell.traffic.tg import BYTEBLOWER_CHASSIS_MODEL, TGN_CHASSIS_FAMILY
from shellfoundry_traffic.test_helpers import TgTestHelpers, print_inventory, session, test_helpers

from src.byteblower_driver import ByteBlowerChassis2GDriver


@pytest.fixture
def server() -> str:
    """Yield server address."""
    return "172.30.127.200"


@pytest.fixture()
def driver(test_helpers: TgTestHelpers, server: str) -> ByteBlowerChassis2GDriver:
    """Yield initialized ByteBlower driver for driver testing."""
    init_context = test_helpers.resource_init_command_context(TGN_CHASSIS_FAMILY, BYTEBLOWER_CHASSIS_MODEL, server)
    driver = ByteBlowerChassis2GDriver()
    driver.initialize(init_context)
    return driver


@pytest.fixture()
def autoload_context(test_helpers: TgTestHelpers, server: str) -> AutoLoadCommandContext:
    """Yield ByteBlower resource for shell autoload testing."""
    return test_helpers.autoload_command_context("CS_GenericResource", BYTEBLOWER_CHASSIS_MODEL, server)


@pytest.fixture()
def autoload_resource(session: CloudShellAPISession, test_helpers: TgTestHelpers, server: str) -> Iterable[ResourceInfo]:
    """Yield ByteBlower resource for shell autoload testing."""
    resource = test_helpers.create_autoload_resource(BYTEBLOWER_CHASSIS_MODEL, "test-folder/test-byteblower", server)
    yield resource
    session.DeleteResource(resource.Name)


def test_autoload(driver: ByteBlowerChassis2GDriver, autoload_context: AutoLoadCommandContext) -> None:
    """Test direct (driver) autoload command."""
    inventory = driver.get_inventory(autoload_context)
    print_inventory(inventory)


def test_autoload_session(session: CloudShellAPISession, autoload_resource: ResourceInfo) -> None:
    """Test indirect (shell) autoload command."""
    session.AutoLoad(autoload_resource.Name)
    session.GetResourceDetails(autoload_resource.Name)
