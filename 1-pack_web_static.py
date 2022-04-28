#!/usr/bin/python3
"""
0x03. AirBnB clone - Deploy static
task 1. Compress before sending
Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack
"""

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """do_pack function"""
    local("mkdir -p versions")
    if (os.path.isdir("web_static")):
        my_date = datetime.now()
        my_tgz = local(
            "tar -czvf versions/web_static_{}{}{}{}{}{}.tgz web_static".format(
                my_date.year,
                my_date.month,
                my_date.day,
                my_date.hour,
                my_date.minute,
                my_date.second))
        return my_tgz
    else:
        return None
