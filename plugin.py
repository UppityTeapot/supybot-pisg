###
# Copyright (c) 2012, Peter Hicks
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

###

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
from supybot.i18n import PluginInternationalization, internationalizeDocstring

import subprocess

#TODO: Implement check for ftputil module
import ftputil

#Scheduled updating
import time
import supybot.ircmsgs as ircmsgs
import supybot.schedule as schedule

import config

reload(config) # REMOVE BEFORE USING

_ = PluginInternationalization('Pisg')

@internationalizeDocstring
class Pisg(callbacks.Plugin):
    """Pisg generation script with FTP upload support.
    
    Pisg should be installed somewhere on your system and 
    be configured to taste. If you are using the FTP function,
    the contents of gfx/ should already be in the directory you
    intend to upload stats to."""
    threaded = True

    #Generate the file
    def pisg(self, irc, msg, args):
        """takes no arguments.
        Regenerates the statistics page. Please be aware that various 
        config values need to be set to make this work."""
        
        self.statssuccess = 0
        
        try:
            retcode = subprocess.check_call(self.registryValue('location'))
            if retcode < 0:
                self.log.info(str("Error generating stats file."))
            else:
                self.log.info(str("Stats file generated successfully."))
                if self.registryValue('ftp'):
                    self.log.info(str("Uploading to: %s" % self.registryValue('ftp.server')))
                    self._uploadToFTP()
                else:
                    self.statssuccess = 1
                
                if self.statssuccess == 1:
                    # Maybe change this to print destFile too? Ex: irc.reply("stuff %s more stuff %s" % (var1, var2))
                    irc.reply("Stats updated: %s" % self.registryValue('url'))
                else:
                    irc.error("Stats not updated. See the log for details.")
        except OSError, e:
            self.log.info(str("Error generating stats file."))
    pisg = wrap(pisg)

    def _uploadToFTP(self):
        if self.registryValue('ftp.server') == '':
                self.log.info(str("You've asked to upload the Pisg stats, but haven't set plugins.Pisg.ftp.host! "))
                return
                
        if self.registryValue('ftp.sourceFile') == '':
                self.log.info(str("You've asked to upload the Pisg stats, but haven't set plugins.Pisg.ftp.sourceFile!"))
                return
            
        ftp = ftputil.FTPHost(self.registryValue('ftp.server'), self.registryValue('ftp.user'), self.registryValue('ftp.pass'))
        
        if self.registryValue('ftp.dir') != '':
            ftputil.chdir(self.registryValue('ftp.dir'))
        
        ftp.upload(self.registryValue('ftp.sourceFile'),self.registryValue('ftp.destFile'))
        ftp.close()
        self.statssuccess = 1
        self.log.info("File uploaded.")
        
Class = Pisg

# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
