/*
 *     Version: 0.1.0
 *     License: GPL
 *
 *      Author: Copyright (C) RyouyaSakai
 *        Date: 2017
 *
 *  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License version 2 as
 *  published by the Free Software Foundation.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program; if not, write to the Free Software
 *  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
 *
 */

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy, os
import SimpleHTTPServer

def kill():
	os.system("kill -KILL " + str(os.getpid())) #強制シャットダウン

os.chdir(os.path.dirname(__file__)) #scriptsディレクトリ見れる
rospy.init_node("webserver") 	    #rosのノード登録
rospy.on_shutdown(kill)		    #kill関数の登録
SimpleHTTPServer.test()		    #サーバ立ち上げ
