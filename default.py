# -*- coding: utf-8 -*-
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon and tvaddons.ag
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.jungesangebotvonardundzdf'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

MEDIA_URL = 'special://home/addons/{0}/img/'.format(addonID)
thumb_wasmitfabian = MEDIA_URL + "thumb_wasmitfabian.jpg" 
fanart_wasmitfabian = MEDIA_URL + "fanart_wasmitfabian.jpg" 

YOUTUBE_CHANNEL_ID = "UCEtpah89jQiafn8iWOhxUSA"

# Entry point
def run():
    plugintools.log("jungesangebotvonardundzdf.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("jungesangebotvonardundzdf.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title="Was mit Fabian",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID+"/",
        thumbnail='https://yt3.ggpht.com/-YD12BMrKsJg/AAAAAAAAAAI/AAAAAAAAAAA/ePXltJ0in3I/s900/photo.jpg',
        fanart='https://yt3.ggpht.com/-tXcQJK3ku7M/VtmcsB7LWcI/AAAAAAAAAB4/Oqyl7sk4C_U/w1920/WMF_Youtube_RotBlau.jpg',
        folder=True )

run()