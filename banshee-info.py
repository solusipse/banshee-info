#-*- coding: utf-8 -*-
###########################################################################
#
# Banshee Info
# This script may be used for obtaining songs' info from Banshee via dbus
# Requirements: Python 2.7
# License: MIT
# Author: solusipse.net
# Mail contact: root account at domain above
#
###########################################################################

import sys, dbus

class Banshee_Info:
    def __init__(self):
        self.dbus_handler = dbus.SessionBus()
        if self.running():
            self.banshee = self.dbus_handler.get_object("org.bansheeproject.Banshee", "/org/bansheeproject/Banshee/PlayerEngine")

    def __get_track_info(self):
        return self.banshee.GetCurrentTrack()

    def __get_position(self):
        return self.banshee.GetPosition()

    def __get_length(self):
        return self.banshee.GetLength()

    def get_title(self):
        return self.__get_track_info().get('name')

    def get_author(self):
        return self.__get_track_info().get('artist')

    def get_album(self):
        return self.__get_track_info().get('album')

    def progress(self):
        return int(round( 100 * ( float( self.__get_position() ) / float( self.__get_length() ))))

    def get_uri(self):
        return self.banshee.GetCurrentUri()

    def get_volume(self):
        return self.banshee.GetVolume()

    def get_length(self):
        m, s = divmod(self.__get_length() / 1000, 60)
        return str(m) + 'm ' + str(s) + 's'

    def running(self):
        if self.dbus_handler.name_has_owner('org.bansheeproject.Banshee'):
            return True

    def get_state(self):
        return self.banshee.GetCurrentState()

banshee_info = Banshee_Info()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        pass
    else:
        if sys.argv[1] == '--help':
            print 'Usage:'
            print '   --basic     - show basic info: Author - Song'
            print '   --title     - displays track\'s title'
            print '   --author    - displays track\'s author'
            print '   --album     - displays track\'s album info'
            print '   --progress  - show percentage value of track\'s progress'
            print '   --volume    - show percentage volume'
            print '   --uri       - show uri'
            print '   --length    - show length in minutes'
            print '   --state     - show banshee\'s state'
        else:
            for arg in sys.argv:
                if banshee_info.running() and banshee_info.get_state() != 'idle':
                    if arg == '--basic':
                        try:
                            print banshee_info.get_author() + ' - ' + banshee_info.get_title()
                        except:
                            print 'Unknown - Unknown'
                    if arg == '--title':
                        print banshee_info.get_title()
                    if arg == '--author':
                        print banshee_info.get_author()
                    if arg == '--album':
                        print banshee_info.get_album()
                    if arg == '--progress':
                        print banshee_info.progress()
                    if arg == '--volume':
                        print banshee_info.get_volume()
                    if arg == '--uri':
                        print banshee_info.get_uri()
                    if arg == '--length':
                        print banshee_info.get_length()
                    if arg == '--state':
                        print banshee_info.get_state()
                else:
                    print "not playing"
                    break