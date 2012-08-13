#What is supybot-pisg?

This plugin will generate a statistics file for your channel through the Perl IRC Statistics Generator, or [pisg](http://pisg.sourceforge.net). Pisg is a neat little Perl script that parses your log files and generates an HTML page with trivia about your users, such as who speaks the most, who asks the most questions, etcetera.

# Prerequisites

* ChannelLogger (or another logging system) logging your stats:
	* Make sure log rotation and time-stamping is turned on; set supybot.plugins.ChannelLogger.rotateLogs and supybot.plugins.ChannelLogger.timestamp to true.
* [ftputil](http://ftputil.sschwarzer.net/) installed on your system **if you want to use FTP**. You can usually do this fairly easily by downloading the file, extracting it, and executing "sudo python setup.py install" in the resulting directory.
* [pisg](http://pisg.sourceforge.net) installed somewhere on your system
* pisg.cfg set up to taste, and working if pisg is called directly from the shell. Your Pisg config should contain, at minimum, the following:
	* LogDir (Assuming you are using Supybot's ChannelLogger plugin, LogDir should be /path/to/botdir/logs/ChannelLogger/NETWORK/CHANNEL/)
	* Format (If using ChannelLogger, this should be "supy")
	* OutputFile set - ideally to an absolute path, but a filename will work. If only a filename is set, the output will be generated in the root of your bot directory.
* An FTP server to upload the final statistics to **OR** a publicly-accessible location on your machine so users can view the stats. In either case, you need the contents of gfx/, found in your pisg directory or /usr/share/pisg/gfx/ on Debian/Ubuntu systems, to be uploaded into the directory where your final HTML file will reside.

# Configuration

supybot-pisg takes several configuration variables; most of which need to be configured before use. They are as follows:

    plugins.Pisg.enabled [True/False]
Defaults to true. This simply tells supybot-pisg whether to function or not.

    plugins.Pisg.location [/path/to/pisg]
Defaults to /usr/bin/pisg, the default for Ubuntu/Debian installs and presumably others. This needs to be checked; without this set correctly, your stats generation will fall at the first hurdle.

    plugins.Pisg.url [http://yourdomain.tld/statsfile.html]
Defaults to blank. This will be the URL listed in the reply message that is sent to the channel/user initiating the Pisg generation. If not set, no URL will be given.

**If FTP Uploading support is desired, the following variables need to be set:**

    plugins.Pisg.ftp [True/False]
Defaults to false. Determines whether the stats are automatically uploaded to an FTP server upon generation.

    plugins.Pisg.ftp.server [ftp.yourdomain.tld]
Defaults to blank, but **required**. This is where the hostname of your FTP server is set. 

    plugins.Pisg.ftp.name [username]
Defaults to anonymous. This is where the username used to log into your FTP server is set. 

    plugins.Pisg.ftp.pass [password]
Defaults to anonymous. If your FTP server requires a password, set it here.

    plugins.Pisg.ftp.dir [public_html/stats/]
Defaults to blank. By default, the script uploads your stats page to the root directory of the FTP server. If you want it to put it in a different remote directory, set this.

    plugins.Pisg.ftp.sourceFile /path/to/statsfile.html
Defaults to blank, but **required**. The full path to where pisg places generated stats files. This file will be uploaded to the FTP server.

    plugins.Pisg.ftp.destFile statsfile.html
Defaults to stats.html, **required**. This is the filename the source file will take.
