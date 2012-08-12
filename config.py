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

import supybot.conf as conf
import supybot.registry as registry
from supybot.i18n import PluginInternationalization, internationalizeDocstring
_ = PluginInternationalization('Pisg')

def configure(advanced):
    # This will be called by supybot to configure this module.  advanced is
    # a bool that specifies whether the user identified himself as an advanced
    # user or not.  You should effect your configuration by manipulating the
    # registry as appropriate.
    from supybot.questions import expect, anything, something, yn
    conf.registerPlugin('Pisg', True)

Pisg = conf.registerPlugin('Pisg')
conf.registerGlobalValue(Pisg, 'enabled',
    registry.Boolean(True, _("""Determines whether the stats are automatically updated.""")))
    
conf.registerGlobalValue(Pisg, 'location',
    registry.String('/usr/bin/pisg', _("""The absolute location of the pisg executable.""")))
conf.registerGlobalValue(Pisg, 'url',
    registry.String('', _("""The URL of the final stats file. This will be part of the response sent to the server..""")))

conf.registerGlobalValue(Pisg, 'ftp',
    registry.Boolean(False, _("""Determines whether the stats are automatically uploaded to an FTP server.""")))
conf.registerGlobalValue(Pisg.ftp, 'server',
    registry.String('', _("""The hostname of the FTP server that Pisg should connect to.""")))
conf.registerGlobalValue(Pisg.ftp, 'user',
    registry.String('', _("""The username for the FTP server that Pisg should connect to.""")))
conf.registerGlobalValue(Pisg.ftp, 'pass',
    registry.String('', _("""The password for the FTP server that Pisg should connect to.""")))
conf.registerGlobalValue(Pisg.ftp, 'dir',
    registry.String('', _("""If you would like the stats file to upload somewhere other than the root directory, specify it here.""")))
conf.registerGlobalValue(Pisg.ftp, 'sourceFile',
    registry.String('', _("""The absolute location and filename of the HTML file pisg outputs. If this 
    is just set to a filename in pisg.cfg, the file will be generated in the root of your bot directory.""")))
conf.registerGlobalValue(Pisg.ftp, 'destFile',
    registry.String('stats.html', _("""The filename that the final stats file will be written to the server as.""")))

# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79: