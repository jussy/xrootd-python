#-------------------------------------------------------------------------------
# Copyright (c) 2012-2013 by European Organization for Nuclear Research (CERN)
# Author: Justin Salmon <jsalmon@cern.ch>
#-------------------------------------------------------------------------------
# XRootD is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# XRootD is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with XRootD.  If not, see <http:#www.gnu.org/licenses/>.
#-------------------------------------------------------------------------------

from pyxrootd import client
from XRootD.client.responses import XRootDStatus

class CopyProcess(object):
  """TODO: write me"""

  def __init__(self):
    self.__process = client.CopyProcess()

  def add_job(self, source, target, sourcelimit=1, force=False, posc=False, 
              coerce=False, thirdparty=False, checksumprint=False, 
              chunksize=4194304, parallelchunks=8):
    """Add a job to the copy process.

    :param         source: original source URL
    :type          source: string
    :param         target: target directory or file
    :type          target: string
    :param    sourcelimit: max number of download sources
    :type     sourcelimit: integer
    :param          force: overwrite target if it exists
    :type           force: boolean
    :param           posc: persist on successful close
    :type            posc: boolean
    :param         coerce: ignore file usage rules, i.e. apply `FORCE` flag to 
                           ``open()``
    :type          coerce: boolean
    :param     thirdparty: do third party copy if possible
    :type      thirdparty: boolean
    :param  checksumprint: print checksum after the transfer
    :type   checksumprint: boolean
    :param      chunksize: chunk size for remote transfers
    :type       chunksize: integer
    :param parallelchunks: number of chunks that should be requested in parallel
    :type  parallelchunks: integer
    """
    self.__process.add_job(source, target, sourcelimit, force, posc, coerce, 
                           thirdparty, checksumprint, chunksize, parallelchunks)

  def prepare(self):
    """Prepare the copy jobs."""
    status = self.__process.prepare()
    return XRootDStatus(status)

  def run(self):
    """Run the copy jobs."""
    status = self.__process.run()
    return XRootDStatus(status)
  