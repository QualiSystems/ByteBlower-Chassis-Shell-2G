
"""
Tests for ByteBlowerChassis2GDriver
"""

import time
import pytest

from cloudshell.traffic.tg import BYTEBLOWER_CHASSIS_MODEL
from shellfoundry.releasetools.test_helper import (create_session_from_deployment, create_init_command_context,
                                                   create_autoload_resource)

from src.byteblower_driver import ByteBlowerChassis2GDriver


@pytest.fixture()
def model():
    yield BYTEBLOWER_CHASSIS_MODEL


@pytest.fixture()
def dut():
    yield '10.113.137.22'


@pytest.fixture()
def session():
    yield create_session_from_deployment()


@pytest.fixture()
def context(session, model, dut):
    attributes = {}
    init_context = create_init_command_context(session, 'CS_TrafficGeneratorChassis', model, dut, attributes,
                                               'Resource')
    yield init_context


@pytest.fixture()
def driver(context):
    driver = ByteBlowerChassis2GDriver()
    driver.initialize(context)
    print(driver.logger.handlers[0].baseFilename)
    yield driver


@pytest.fixture()
def resource(session, model, dut):
    attributes = []
    resource = create_autoload_resource(session, 'CS_TrafficGeneratorChassis', model, dut, 'test-byteblower',
                                        attributes)
    time.sleep(2)
    yield resource
    session.DeleteResource(resource.Name)


def test_autoload(driver, context):
    inventory = driver.get_inventory(context)
    print('\n')
    for r in inventory.resources:
        print('{}, {}, {}'.format(r.relative_address, r.model, r.name))
    print('\n')
    for a in inventory.attributes:
        print('{}, {}, {}'.format(a.relative_address, a.attribute_name, a.attribute_value))


def test_autoload_session(session, resource):
    session.AutoLoad(resource.Name)
    session.GetResourceDetails(resource.Name)
    print('Done')
