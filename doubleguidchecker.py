#
# ################################################################### #
#                                                                     #
#  doubleguidchecker Plugin for BigBrotherBot(B3)                       #
#  Copyright (c) 2018 Ouchekkir Abdelmouaine                          #
#                                                                     #
#  This program is free software; you can redistribute it and/or      #
#  modify it under the terms of the GNU General Public License        #
#  as published by the Free Software Foundation; either version 2     #
#  of the License, or (at your option) any later version.             #
#                                                                     #
#  This program is distributed in the hope that it will be useful,    #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of     #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the       #
#  GNU General Public License for more details.                       #
#                                                                     #
#  You should have received a copy of the GNU General Public License  #
#  along with this program; if not, write to the Free Software        #
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA      #
#  02110-1301, USA.                                                   #
#                                                                     #
# ################################################################### #
#
#  CHANGELOG:
#  03.11.2019 - v0.1 - ZOMBIE
#  - first release.

import b3
import b3.events
import b3.plugin

__version__ = '0.1'
__author__ = 'ZOMBIE'


class DoubleguidcheckerPlugin(b3.plugin.Plugin):
    _adminPlugin = None
    requiresConfigFile = False
    _guids = list()

    def onStartup(self):
        self._adminPlugin = self.console.getPlugin('admin')

        if not self._adminPlugin:
            self.error('Could not find admin plugin')
            return False
        else:
            self.debug('Plugin successfully loaded')

        self.registerEvent(b3.events.EVT_CLIENT_AUTH, self.onConnect)
        self.registerEvent(b3.events.EVT_CLIENT_DISCONNECT, self.onDisconnect)

        self.update_guids()

    def onConnect(self, event):
        client = event.client
        for x in self.console.clients.getList():
            if x.guid == client.guid and x.cid != client.cid:
                self.debug('Client GUID: %s is already connected.' %
                           event.client.guid)
                client.kick(
                    "This GUID is already connected Contact server admins on ^3discord.gg/NJx9Khb^7")
            else:
                self.update_guids()

    def onDisconnect(self, event):
        self.update_guids()

    def update_guids(self):
        self._guids = [x.guid for x in self.console.clients.getList()]
