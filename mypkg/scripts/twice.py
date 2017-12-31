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
import rospy
from std_msgs.msg import Int32

n = 0

def cb(message):
	global n
	n = message.data*2

if __name__ == '__main__':
	rospy.init_node('twice')
	sub = rospy.Subscriber('count_up', Int32, cb)
	pub = rospy.Publisher('twice', Int32, queue_size=1)
	rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		pub.publish(n)
		rate.sleep()
