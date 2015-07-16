#!/usr/bin/python
# -*- coding: UTF-8 -*-

import socket
import os
import sys

import logging
from pprint import pformat
logging.basicConfig(level=logging.DEBUG)
log=logging.getLogger("TuxTeacher")

s=socket.socket(socket.AF_UNIX,socket.SOCK_STREAM)
sPath='/home/mad/lls/tux'
#sPath='/var/lib/vservers/learn01/tux'

try:
    os.unlink(sPath)
except OSError:
    if os.path.exists(sPath):
        raise

#assert not os.path.exists(sPath)

s.bind(sPath)

s.listen(1)
#s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON) # not for UDS
log.info("Something connected")

aMsg = s.accept()
log.info('Accepting %s',pformat(aMsg))
while 1:
    data=s.recv(16)
    log.debug("recv: %s",pformat(data))

log.warn('Program ended.')
