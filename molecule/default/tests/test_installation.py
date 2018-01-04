"""
Role tests
"""

import os
import pytest

from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('name', [
    ('python-dev'),
    ('python-virtualenv'),
])
def test_packages(host, name):
    """
    Test installed packages
    """

    assert host.package(name).is_installed
