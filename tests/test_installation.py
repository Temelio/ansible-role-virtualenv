"""
Role tests
"""

import pytest
from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


@pytest.mark.parametrize('name', [
    ('python-dev'),
    ('python-virtualenv'),
])
def test_packages(host, name):
    """
    Test installed packages
    """

    assert host.package(name).is_installed
