# Ansible role: EPEL
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Ansible Role](https://img.shields.io/ansible/role/42479)](https://galaxy.ansible.com/mehdicopter/epel)
[![Ansible Quality Score](https://img.shields.io/ansible/quality/42479)](https://galaxy.ansible.com/mehdicopter/epel)

Installs the EPEL repository for CentOS.

## Requirements
Your distribution must be a CentOS one, either 6 or 7 version.

## Example Playbook
    - hosts: servers
      become: true
      roles:
         - mehdicopter.epel

## Author Information
Mehdi MAHFOUDI aka Mehdicopter.
