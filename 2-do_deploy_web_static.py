#!/usr/bin/python3
# Fabfile to distribute an archive to a web server.
import os.path
from fabric.api import env
from fabric.api import put
from fabric.api import run

env.hosts = ["54.160.85.72", "35.175.132.106"]


def do_deploy(archive_path):
    """Distributes an archive to a web server.
    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if os.path.isfile(archive_path) is False:
        return False

    put(archive_path, "/tmp/")

    run("tar -xzf /tmp/{} -C /data/web_static/releases/".format(
        archive_path.split("/")[-1]))

    run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(
        archive_path.split("/")[-1].split(".")[0]))

    return True
