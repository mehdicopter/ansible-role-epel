def test_epel_package(host):
    p = host.package('epel-release')

    assert p.is_installed


def test_epel_file(host):
    f = host.file('/etc/yum.repos.d/epel.repo')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.mode == 0o644


def test_epel_enabled(host):
    cmd = host.run('yum repolist enabled')

    assert 'epel' in cmd.stdout
