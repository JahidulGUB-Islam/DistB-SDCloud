#!/usr/bin/python

'Setting the position of nodes and providing mobility'

import sys

from mininet.log import setLogLevel, info
from mn_wifi.cli import CLI
from mn_wifi.net import Mininet_wifi


def topology(args):
    "Create a network."
    net = Mininet_wifi()

    info("*** Creating nodes\n")
	#edit here
    h1 = net.addHost('h1', mac='00:00:00:00:01:01', ip='10.0.0.101/8')
    sta1 = net.addStation('sta1', mac='00:00:00:00:00:02', ip='10.0.0.2/8')
    sta2 = net.addStation('sta2', mac='00:00:00:00:00:03', ip='10.0.0.3/8')
    sta3 = net.addStation('sta3', mac='00:00:00:00:00:04', ip='10.0.0.4/8')
    sta4 = net.addStation('sta4', mac='00:00:00:00:00:05', ip='10.0.0.5/8')
    sta5 = net.addStation('sta5', mac='00:00:00:00:00:06', ip='10.0.0.6/8')
    ap1 = net.addAccessPoint('ap1', ssid='new-ssid', mode='g', channel='1',
                             position='50,100,0')



    h2 = net.addHost('h2', mac='00:00:00:00:02:01', ip='10.0.0.102/8')
    sta6 = net.addStation('sta6', mac='00:00:00:00:00:07', ip='10.0.0.7/8')
    sta7 = net.addStation('sta7', mac='00:00:00:00:00:08', ip='10.0.0.8/8')
    sta8 = net.addStation('sta8', mac='00:00:00:00:00:09', ip='10.0.0.9/8')
    sta9 = net.addStation('sta9', mac='00:00:00:00:00:10', ip='10.0.0.10/8')
    sta10 = net.addStation('sta10', mac='00:00:00:00:00:11', ip='10.0.0.11/8')
    ap2 = net.addAccessPoint('ap2', ssid='new-ssid', mode='g', channel='2',
                             position='150,100,0')



    h3 = net.addHost('h3', mac='00:00:00:00:03:01', ip='10.0.0.103/8')
    sta11 = net.addStation('sta11', mac='00:00:00:00:00:12', ip='10.0.0.12/8')
    sta12 = net.addStation('sta12', mac='00:00:00:00:00:13', ip='10.0.0.13/8')
    sta13 = net.addStation('sta13', mac='00:00:00:00:00:14', ip='10.0.0.14/8')
    sta14 = net.addStation('sta14', mac='00:00:00:00:00:15', ip='10.0.0.15/8')
    sta15 = net.addStation('sta15', mac='00:00:00:00:00:16', ip='10.0.0.16/8')
    ap3 = net.addAccessPoint('ap3', ssid='new-ssid', mode='g', channel='3',
                             position='250,100,0')



    h4 = net.addHost('h4', mac='00:00:00:00:04:01', ip='10.0.0.104/8')
    sta16 = net.addStation('sta16', mac='00:00:00:00:00:17', ip='10.0.0.17/8')
    sta17 = net.addStation('sta17', mac='00:00:00:00:00:18', ip='10.0.0.18/8')
    sta18 = net.addStation('sta18', mac='00:00:00:00:00:19', ip='10.0.0.19/8')
    sta19 = net.addStation('sta19', mac='00:00:00:00:00:20', ip='10.0.0.20/8')
    sta20 = net.addStation('sta20', mac='00:00:00:00:00:21', ip='10.0.0.21/8')
    ap4 = net.addAccessPoint('ap4', ssid='new-ssid', mode='g', channel='4',
                             position='350,100,0')



    h5 = net.addHost('h5', mac='00:00:00:00:05:01', ip='10.0.0.105/8')
    sta21 = net.addStation('sta21', mac='00:00:00:00:00:22', ip='10.0.0.22/8')
    sta22 = net.addStation('sta22', mac='00:00:00:00:00:23', ip='10.0.0.23/8')
    sta23 = net.addStation('sta23', mac='00:00:00:00:00:24', ip='10.0.0.24/8')
    sta24 = net.addStation('sta24', mac='00:00:00:00:00:25', ip='10.0.0.25/8')
    sta25 = net.addStation('sta25', mac='00:00:00:00:00:26', ip='10.0.0.26/8')
    ap5 = net.addAccessPoint('ap5', ssid='new-ssid', mode='g', channel='5',
                             position='450,100,0')



    h6 = net.addHost('h6', mac='00:00:00:00:06:01', ip='10.0.0.106/8')
    sta26 = net.addStation('sta26', mac='00:00:00:00:00:27', ip='10.0.0.27/8')
    sta27 = net.addStation('sta27', mac='00:00:00:00:00:28', ip='10.0.0.28/8')
    sta28 = net.addStation('sta28', mac='00:00:00:00:00:29', ip='10.0.0.29/8')
    sta29 = net.addStation('sta29', mac='00:00:00:00:00:30', ip='10.0.0.30/8')
    sta30 = net.addStation('sta30', mac='00:00:00:00:00:31', ip='10.0.0.31/8')
    ap6 = net.addAccessPoint('ap6', ssid='new-ssid', mode='g', channel='6',
                             position='100,200,0')



    h7 = net.addHost('h7', mac='00:00:00:00:07:01', ip='10.0.0.107/8')
    sta31 = net.addStation('sta31', mac='00:00:00:00:00:32', ip='10.0.0.32/8')
    sta32 = net.addStation('sta32', mac='00:00:00:00:00:33', ip='10.0.0.33/8')
    sta33 = net.addStation('sta33', mac='00:00:00:00:00:34', ip='10.0.0.34/8')
    sta34 = net.addStation('sta34', mac='00:00:00:00:00:35', ip='10.0.0.35/8')
    sta35 = net.addStation('sta35', mac='00:00:00:00:00:36', ip='10.0.0.36/8')
    ap7 = net.addAccessPoint('ap7', ssid='new-ssid', mode='g', channel='7',
                             position='200,200,0')



    h8 = net.addHost('h8', mac='00:00:00:00:08:01', ip='10.0.0.108/8')
    sta36 = net.addStation('sta36', mac='00:00:00:00:00:37', ip='10.0.0.37/8')
    sta37 = net.addStation('sta37', mac='00:00:00:00:00:38', ip='10.0.0.38/8')
    sta38 = net.addStation('sta38', mac='00:00:00:00:00:39', ip='10.0.0.39/8')
    sta39 = net.addStation('sta39', mac='00:00:00:00:00:40', ip='10.0.0.40/8')
    sta40 = net.addStation('sta40', mac='00:00:00:00:00:41', ip='10.0.0.41/8')
    ap8 = net.addAccessPoint('ap8', ssid='new-ssid', mode='g', channel='8',
                             position='300,200,0')



    h9 = net.addHost('h9', mac='00:00:00:00:09:01', ip='10.0.0.109/8')
    sta41 = net.addStation('sta41', mac='00:00:00:00:00:42', ip='10.0.0.42/8')
    sta42 = net.addStation('sta42', mac='00:00:00:00:00:43', ip='10.0.0.43/8')
    sta43 = net.addStation('sta43', mac='00:00:00:00:00:44', ip='10.0.0.44/8')
    sta44 = net.addStation('sta44', mac='00:00:00:00:00:45', ip='10.0.0.45/8')
    sta45 = net.addStation('sta45', mac='00:00:00:00:00:46', ip='10.0.0.46/8')
    ap9 = net.addAccessPoint('ap9', ssid='new-ssid', mode='g', channel='9',
                             position='400,200,0')



    """h10 = net.addHost('h10', mac='00:00:00:00:10:01', ip='10.0.0.110/8')
    sta46 = net.addStation('sta46', mac='00:00:00:00:00:47', ip='10.0.0.47/8')
    sta47 = net.addStation('sta47', mac='00:00:00:00:00:48', ip='10.0.0.48/8')
    sta48 = net.addStation('sta48', mac='00:00:00:00:00:49', ip='10.0.0.49/8')
    sta49 = net.addStation('sta49', mac='00:00:00:00:00:50', ip='10.0.0.50/8')
    sta50 = net.addStation('sta50', mac='00:00:00:00:00:51', ip='10.0.0.51/8')
    ap10 = net.addAccessPoint('ap10', ssid='new-ssid', mode='g', channel='10',
                             position='150,300,0')



    h11 = net.addHost('h11', mac='00:00:00:00:11:01', ip='10.0.0.111/8')
    sta51 = net.addStation('sta51', mac='00:00:00:00:00:52', ip='10.0.0.52/8')
    sta52 = net.addStation('sta52', mac='00:00:00:00:00:53', ip='10.0.0.53/8')
    sta53 = net.addStation('sta53', mac='00:00:00:00:00:54', ip='10.0.0.54/8')
    sta54 = net.addStation('sta54', mac='00:00:00:00:00:55', ip='10.0.0.55/8')
    sta55 = net.addStation('sta55', mac='00:00:00:00:00:56', ip='10.0.0.56/8')
    ap11 = net.addAccessPoint('ap11', ssid='new-ssid', mode='g', channel='11',
                             position='250,300,0')



    h12 = net.addHost('h12', mac='00:00:00:00:12:01', ip='10.0.0.112/8')
    sta56 = net.addStation('sta56', mac='00:00:00:00:00:57', ip='10.0.0.57/8')
    sta57 = net.addStation('sta57', mac='00:00:00:00:00:58', ip='10.0.0.58/8')
    sta58 = net.addStation('sta58', mac='00:00:00:00:00:59', ip='10.0.0.59/8')
    sta59 = net.addStation('sta59', mac='00:00:00:00:00:60', ip='10.0.0.60/8')
    sta60 = net.addStation('sta60', mac='00:00:00:00:00:61', ip='10.0.0.61/8')
    ap12 = net.addAccessPoint('ap12', ssid='new-ssid', mode='g', channel='12',
                             position='350,300,0')



    h13 = net.addHost('h13', mac='00:00:00:00:13:01', ip='10.0.0.113/8')
    sta61 = net.addStation('sta61', mac='00:00:00:00:00:62', ip='10.0.0.62/8')
    sta62 = net.addStation('sta62', mac='00:00:00:00:00:63', ip='10.0.0.63/8')
    sta63 = net.addStation('sta63', mac='00:00:00:00:00:64', ip='10.0.0.64/8')
    sta64 = net.addStation('sta64', mac='00:00:00:00:00:65', ip='10.0.0.65/8')
    sta65 = net.addStation('sta65', mac='00:00:00:00:00:66', ip='10.0.0.66/8')
    ap13 = net.addAccessPoint('ap13', ssid='new-ssid', mode='g', channel='13',
                             position='200,400,0')



    h14 = net.addHost('h14', mac='00:00:00:00:14:01', ip='10.0.0.114/8')
    sta66 = net.addStation('sta66', mac='00:00:00:00:00:67', ip='10.0.0.67/8')
    sta67 = net.addStation('sta67', mac='00:00:00:00:00:68', ip='10.0.0.68/8')
    sta68 = net.addStation('sta68', mac='00:00:00:00:00:69', ip='10.0.0.69/8')
    sta69 = net.addStation('sta69', mac='00:00:00:00:00:70', ip='10.0.0.70/8')
    sta70 = net.addStation('sta70', mac='00:00:00:00:00:71', ip='10.0.0.71/8')
    ap14 = net.addAccessPoint('ap14', ssid='new-ssid', mode='g', channel='14',
                             position='300,400,0')"""

    c1 = net.addController('c1')
    c2 = net.addController('c2')
    c3 = net.addController('c1')
    c4 = net.addController('c2')
    c5 = net.addController('c5')
    c6 = net.addController('c6')
    c7 = net.addController('c7')
    c8 = net.addController('c8')
    c9 = net.addController('c9')
    
    """c10 = net.addController('c10')
    c11 = net.addController('c11')
    c12 = net.addController('c12')
    c13 = net.addController('c13')
    c14 = net.addController('c14')"""

    info("*** Configuring propagation model\n")
    net.setPropagationModel(model="logDistance", exp=4.5)

    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()

    info("*** Associating and Creating links\n")
    net.addLink(ap1, h1)
    net.addLink(ap1, sta1)
    net.addLink(ap1, sta2)
    net.addLink(ap1, sta3)
    net.addLink(ap1, sta4)
    net.addLink(ap1, sta5)
    net.addLink(ap2, h2)
    net.addLink(ap1, ap2)
    net.addLink(ap2, sta6)
    net.addLink(ap2, sta7)
    net.addLink(ap2, sta8)
    net.addLink(ap2, sta9)
    net.addLink(ap2, sta10)

    net.addLink(ap3, h3)
    net.addLink(ap3, sta11)
    net.addLink(ap3, sta12)
    net.addLink(ap3, sta13)
    net.addLink(ap3, sta14)
    net.addLink(ap3, sta15)
    net.addLink(ap4, h4)
    net.addLink(ap2, ap3)
    net.addLink(ap3, ap4)
    net.addLink(ap4, sta16)
    net.addLink(ap4, sta17)
    net.addLink(ap4, sta18)
    net.addLink(ap4, sta19)
    net.addLink(ap4, sta20)

    net.addLink(ap5, sta21)
    net.addLink(ap5, sta22)
    net.addLink(ap5, sta23)
    net.addLink(ap5, sta24)
    net.addLink(ap5, sta25)
    net.addLink(ap5, h5)
    net.addLink(ap4, ap5)
    net.addLink(ap1, ap6)
    net.addLink(ap6, ap7)
    net.addLink(ap7, ap8)
    net.addLink(ap2, ap7)
    net.addLink(ap3, ap7)
    net.addLink(ap1, ap7)
    net.addLink(ap2, ap8)
    net.addLink(ap5, ap8)
    net.addLink(ap4, ap8)
    net.addLink(ap8, ap9)
    net.addLink(ap3, ap9)
    net.addLink(ap4, ap9)
    net.addLink(ap5, ap9)
    net.addLink(ap6, sta26)
    net.addLink(ap6, sta27)
    net.addLink(ap6, sta28)
    net.addLink(ap6, sta29)
    net.addLink(ap6, sta30)
    net.addLink(ap6, h6)

    net.addLink(ap7, sta31)
    net.addLink(ap7, sta32)
    net.addLink(ap7, sta33)
    net.addLink(ap7, sta34)
    net.addLink(ap7, sta35)
    net.addLink(ap7, h7)
    net.addLink(ap8, sta36)
    net.addLink(ap8, sta37)
    net.addLink(ap8, sta38)
    net.addLink(ap8, sta39)
    net.addLink(ap8, sta40)
    net.addLink(ap8, h8)

    net.addLink(ap9, sta41)
    net.addLink(ap9, sta42)
    net.addLink(ap9, sta43)
    net.addLink(ap9, sta44)
    net.addLink(ap9, sta45)
    net.addLink(ap9, h9)
    """net.addLink(ap10, sta46)
    net.addLink(ap10, sta47)
    net.addLink(ap10, sta48)
    net.addLink(ap10, sta49)
    net.addLink(ap10, sta50)
    net.addLink(ap10, h10)

    net.addLink(ap11, sta51)
    net.addLink(ap11, sta52)
    net.addLink(ap11, sta53)
    net.addLink(ap11, sta54)
    net.addLink(ap11, sta55)
    net.addLink(ap11, h11)
    net.addLink(ap12, sta56)
    net.addLink(ap12, sta57)
    net.addLink(ap12, sta58)
    net.addLink(ap12, sta59)
    net.addLink(ap12, sta60)
    net.addLink(ap12, h12)

    net.addLink(ap13, sta61)
    net.addLink(ap13, sta62)
    net.addLink(ap13, sta63)
    net.addLink(ap13, sta64)
    net.addLink(ap13, sta65)
    net.addLink(ap13, h13)
    net.addLink(ap14, sta66)
    net.addLink(ap14, sta67)
    net.addLink(ap14, sta68)
    net.addLink(ap14, sta69)
    net.addLink(ap14, sta70)
    net.addLink(ap14, h14)"""

    if '-p' not in args:
        net.plotGraph(max_x=500, max_y=250)

    if '-c' in args:
	#1st portion:starting point: 2nd portion:Ending point
        sta1.coord = ['250.0,250.0,0.0', '20.0,60.0,0.0', '31.0,30.0,0.0']
        sta2.coord = ['250.0,250.0,0.0', '30.0,50.0,0.0', '55.0,81.0,0.0']
	sta3.coord = ['250.0,250.0,0.0', '50.0,50.0,0.0', '55.0,81.0,0.0']
	sta4.coord = ['250.0,250.0,0.0', '70.0,50.0,0.0', '55.0,81.0,0.0']
	sta5.coord = ['250.0,250.0,0.0', '80.0,60.0,0.0', '55.0,81.0,0.0']

	sta6.coord = ['250.0,250.0,0.0', '120.0,70.0,0.0', '55.0,81.0,0.0']
	sta7.coord = ['250.0,250.0,0.0', '130.0,50.0,0.0', '55.0,81.0,0.0']
	sta8.coord = ['250.0,250.0,0.0', '150.0,50.0,0.0', '55.0,81.0,0.0']
	sta9.coord = ['250.0,250.0,0.0', '170.0,50.0,0.0', '55.0,81.0,0.0']
	sta10.coord = ['250.0,250.0,0.0', '180.0,70.0,0.0', '55.0,81.0,0.0']

	sta11.coord = ['250.0,250.0,0.0', '210.0,50.0,0.0', '55.0,81.0,0.0']
	sta12.coord = ['250.0,250.0,0.0', '230.0,50.0,0.0', '55.0,81.0,0.0']
	sta13.coord = ['250.0,250.0,0.0', '250.0,50.0,0.0', '55.0,81.0,0.0']
	sta14.coord = ['250.0,250.0,0.0', '270.0,50.0,0.0', '55.0,81.0,0.0']
	sta15.coord = ['250.0,250.0,0.0', '290.0,50.0,0.0', '55.0,81.0,0.0']

	sta16.coord = ['250.0,250.0,0.0', '320.0,70.0,0.0', '55.0,81.0,0.0']
	sta17.coord = ['250.0,250.0,0.0', '330.0,60.0,0.0', '55.0,81.0,0.0']
	sta18.coord = ['250.0,250.0,0.0', '350.0,50.0,0.0', '55.0,81.0,0.0']
	sta19.coord = ['250.0,250.0,0.0', '360.0,60.0,0.0', '55.0,81.0,0.0']
	sta20.coord = ['250.0,250.0,0.0', '370.0,70.0,0.0', '55.0,81.0,0.0']

	sta21.coord = ['250.0,250.0,0.0', '430.0,70.0,0.0', '55.0,81.0,0.0']
	sta22.coord = ['250.0,250.0,0.0', '430.0,50.0,0.0', '55.0,81.0,0.0']
	sta23.coord = ['250.0,250.0,0.0', '450.0,50.0,0.0', '55.0,81.0,0.0']
	sta24.coord = ['250.0,250.0,0.0', '470.0,50.0,0.0', '55.0,81.0,0.0']
	sta25.coord = ['250.0,250.0,0.0', '470.0,70.0,0.0', '55.0,81.0,0.0']

	sta26.coord = ['250.0,250.0,0.0', '80.0,170.0,0.0', '55.0,81.0,0.0']
	sta27.coord = ['250.0,250.0,0.0', '80.0,150.0,0.0', '55.0,81.0,0.0']
	sta28.coord = ['250.0,250.0,0.0', '100.0,150.0,0.0', '55.0,81.0,0.0']
	sta29.coord = ['250.0,250.0,0.0', '130.0,150.0,0.0', '55.0,81.0,0.0']
	sta30.coord = ['250.0,250.0,0.0', '130.0,170.0,0.0', '55.0,81.0,0.0']

	sta31.coord = ['250.0,250.0,0.0', '170.0,170.0,0.0', '55.0,81.0,0.0']
	sta32.coord = ['250.0,250.0,0.0', '180.0,150.0,0.0', '55.0,81.0,0.0']
	sta33.coord = ['250.0,250.0,0.0', '200.0,150.0,0.0', '55.0,81.0,0.0']
	sta34.coord = ['250.0,250.0,0.0', '220.0,150.0,0.0', '55.0,81.0,0.0']
	sta35.coord = ['250.0,250.0,0.0', '230.0,170.0,0.0', '55.0,81.0,0.0']

	sta36.coord = ['250.0,250.0,0.0', '270.0,160.0,0.0', '55.0,81.0,0.0']
	sta37.coord = ['250.0,250.0,0.0', '280.0,150.0,0.0', '55.0,81.0,0.0']
	sta38.coord = ['250.0,250.0,0.0', '300.0,150.0,0.0', '55.0,81.0,0.0']
	sta39.coord = ['250.0,250.0,0.0', '320.0,150.0,0.0', '55.0,81.0,0.0']
	sta40.coord = ['250.0,250.0,0.0', '330.0,170.0,0.0', '55.0,81.0,0.0']

	sta41.coord = ['250.0,250.0,0.0', '360.0,160.0,0.0', '55.0,81.0,0.0']
	sta42.coord = ['250.0,250.0,0.0', '380.0,150.0,0.0', '55.0,81.0,0.0']
	sta43.coord = ['250.0,250.0,0.0', '400.0,150.0,0.0', '55.0,81.0,0.0']
	sta44.coord = ['250.0,250.0,0.0', '420.0,150.0,0.0', '55.0,81.0,0.0']
	sta45.coord = ['250.0,250.0,0.0', '440.0,170.0,0.0', '55.0,81.0,0.0']

	"""sta46.coord = ['250.0,250.0,0.0', '120.0,280.0,0.0', '55.0,81.0,0.0']
	sta47.coord = ['250.0,250.0,0.0', '130.0,260.0,0.0', '55.0,81.0,0.0']
	sta48.coord = ['250.0,250.0,0.0', '150.0,250.0,0.0', '55.0,81.0,0.0']
	sta49.coord = ['250.0,250.0,0.0', '170.0,260.0,0.0', '55.0,81.0,0.0']
	sta50.coord = ['250.0,250.0,0.0', '180.0,280.0,0.0', '55.0,81.0,0.0']

	sta51.coord = ['250.0,250.0,0.0', '210.0,250.0,0.0', '55.0,81.0,0.0']
	sta52.coord = ['250.0,250.0,0.0', '230.0,260.0,0.0', '55.0,81.0,0.0']
	sta53.coord = ['250.0,250.0,0.0', '250.0,250.0,0.0', '55.0,81.0,0.0']
	sta54.coord = ['250.0,250.0,0.0', '270.0,260.0,0.0', '55.0,81.0,0.0']
	sta55.coord = ['250.0,250.0,0.0', '290.0,250.0,0.0', '55.0,81.0,0.0']

	sta56.coord = ['250.0,250.0,0.0', '320.0,270.0,0.0', '55.0,81.0,0.0']
	sta57.coord = ['250.0,250.0,0.0', '330.0,250.0,0.0', '55.0,81.0,0.0']
	sta58.coord = ['250.0,250.0,0.0', '350.0,250.0,0.0', '55.0,81.0,0.0']
	sta59.coord = ['250.0,250.0,0.0', '350.0,280.0,0.0', '55.0,81.0,0.0']
	sta60.coord = ['250.0,250.0,0.0', '380.0,270.0,0.0', '55.0,81.0,0.0']

	sta61.coord = ['250.0,250.0,0.0', '170.0,380.0,0.0', '55.0,81.0,0.0']
	sta62.coord = ['250.0,250.0,0.0', '180.0,360.0,0.0', '55.0,81.0,0.0']
	sta63.coord = ['250.0,250.0,0.0', '200.0,350.0,0.0', '55.0,81.0,0.0']
	sta64.coord = ['250.0,250.0,0.0', '220.0,360.0,0.0', '55.0,81.0,0.0']
	sta65.coord = ['250.0,250.0,0.0', '240.0,380.0,0.0', '55.0,81.0,0.0']

	sta66.coord = ['250.0,250.0,0.0', '270.0,370.0,0.0', '55.0,81.0,0.0']
	sta67.coord = ['250.0,250.0,0.0', '280.0,350.0,0.0', '55.0,81.0,0.0']
	sta68.coord = ['250.0,250.0,0.0', '300.0,350.0,0.0', '55.0,81.0,0.0']
	sta69.coord = ['250.0,250.0,0.0', '320.0,350.0,0.0', '55.0,81.0,0.0']
	sta70.coord = ['250.0,250.0,0.0', '330.0,370.0,0.0', '55.0,81.0,0.0']"""

    net.startMobility(time=0, mob_rep=1, reverse=False)

    p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24, p25, p26, p27, p28, p29, p30, p31, p32, p33, p34, p35, p36, p37, p38, p39, p40, p41, p42, p43, p44, p45, p46, p47, p48, p49, p50, p51, p52, p53, p54, p55, p56, p57, p58, p59, p60, p61, p62, p63, p64, p65, p66, p67, p68, p69, p70, p71, p72, p73, p74, p75, p76, p77, p78, p79, p80, p81, p82, p83, p84, p85, p86, p87, p88, p89, p90 = dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict()
    if '-c' not in args:
	#starting point
        p1 = {'position': '250.0,250.0,0.0'}
        p2 = {'position': '250.0,250.0,0.0'}
	p5 = {'position': '250.0,250.0,0.0'}
	p7 = {'position': '250.0,250.0,0.0'}
	p9 = {'position': '250.0,250.0,0.0'}
	p11 = {'position': '250.0,250.0,0.0'}
	p13 = {'position': '250.0,250.0,0.0'}
	p15 = {'position': '250.0,250.0,0.0'}
	p17 = {'position': '250.0,250.0,0.0'}
	p19 = {'position': '250.0,250.0,0.0'}

	p21 = {'position': '250.0,250.0,0.0'}
	p23 = {'position': '250.0,250.0,0.0'}
	p25 = {'position': '250.0,250.0,0.0'}
	p27 = {'position': '250.0,250.0,0.0'}
	p29 = {'position': '250.0,250.0,0.0'}
	p31 = {'position': '250.0,250.0,0.0'}
	p33 = {'position': '250.0,250.0,0.0'}
	p35 = {'position': '250.0,250.0,0.0'}
	p37 = {'position': '250.0,250.0,0.0'}
	p39 = {'position': '250.0,250.0,0.0'}

	p41 = {'position': '250.0,250.0,0.0'}
	p43 = {'position': '250.0,250.0,0.0'}
	p45 = {'position': '250.0,250.0,0.0'}
	p47 = {'position': '250.0,250.0,0.0'}
	p49 = {'position': '250.0,250.0,0.0'}
	p51 = {'position': '250.0,250.0,0.0'}
	p53 = {'position': '250.0,250.0,0.0'}
	p55 = {'position': '250.0,250.0,0.0'}
	p57 = {'position': '250.0,250.0,0.0'}
	p59 = {'position': '250.0,250.0,0.0'}

	p61 = {'position': '250.0,250.0,0.0'}
	p63 = {'position': '250.0,250.0,0.0'}
	p65 = {'position': '250.0,250.0,0.0'}
	p67 = {'position': '250.0,250.0,0.0'}
	p69 = {'position': '250.0,250.0,0.0'}
	p71 = {'position': '250.0,250.0,0.0'}
	p73 = {'position': '250.0,250.0,0.0'}
	p75 = {'position': '250.0,250.0,0.0'}
	p77 = {'position': '250.0,250.0,0.0'}
	p79 = {'position': '250.0,250.0,0.0'}

	p81 = {'position': '250.0,250.0,0.0'}
	p83 = {'position': '250.0,250.0,0.0'}
	p85 = {'position': '250.0,250.0,0.0'}
	p87 = {'position': '250.0,250.0,0.0'}
	p89 = {'position': '250.0,250.0,0.0'}
	"""p91 = {'position': '250.0,250.0,0.0'}
	p93 = {'position': '250.0,250.0,0.0'}
	p95 = {'position': '250.0,250.0,0.0'}
	p97 = {'position': '250.0,250.0,0.0'}
	p99 = {'position': '250.0,250.0,0.0'}

	p101 = {'position': '250.0,250.0,0.0'}
	p103 = {'position': '250.0,250.0,0.0'}
	p105 = {'position': '250.0,250.0,0.0'}
	p107 = {'position': '250.0,250.0,0.0'}
	p109 = {'position': '250.0,250.0,0.0'}
	p111 = {'position': '250.0,250.0,0.0'}
	p113 = {'position': '250.0,250.0,0.0'}
	p115 = {'position': '250.0,250.0,0.0'}
	p117 = {'position': '250.0,250.0,0.0'}
	p119 = {'position': '250.0,250.0,0.0'}

	p121 = {'position': '250.0,250.0,0.0'}
	p123 = {'position': '250.0,250.0,0.0'}
	p125 = {'position': '250.0,250.0,0.0'}
	p127 = {'position': '250.0,250.0,0.0'}
	p129 = {'position': '250.0,250.0,0.0'}
	p131 = {'position': '250.0,250.0,0.0'}
	p133 = {'position': '250.0,250.0,0.0'}
	p135 = {'position': '250.0,250.0,0.0'}
	p137 = {'position': '250.0,250.0,0.0'}
	p139 = {'position': '250.0,250.0,0.0'}"""
	
	#ending point
        p3 = {'position': '20.0,60.0,0.0'}
        p4 = {'position': '30.0,50.0,0.0'}
	p6 = {'position': '50.0,50.0,0.0'}
	p8 = {'position': '70.0,50.0,0.0'}
	p10 = {'position': '80.0,60.0,0.0'}

	p12 = {'position': '120.0,70.0,0.0'}
	p14 = {'position': '130.0,50.0,0.0'}
	p16 = {'position': '150.0,50.0,0.0'}
	p18 = {'position': '170.0,50.0,0.0'}
	p20 = {'position': '180.0,70.0,0.0'}

	p22 = {'position': '210.0,50.0,0.0'}
	p24 = {'position': '230.0,50.0,0.0'}
	p26 = {'position': '250.0,50.0,0.0'}
	p28 = {'position': '270.0,50.0,0.0'}
	p30 = {'position': '290.0,50.0,0.0'}

	p32 = {'position': '320.0,70.0,0.0'}
	p34 = {'position': '330.0,60.0,0.0'}
	p36 = {'position': '350.0,50.0,0.0'}
	p38 = {'position': '360.0,60.0,0.0'}
	p40 = {'position': '370.0,70.0,0.0'}

	p42 = {'position': '430.0,70.0,0.0'}
	p44 = {'position': '430.0,50.0,0.0'}
	p46 = {'position': '450.0,50.0,0.0'}
	p48 = {'position': '470.0,50.0,0.0'}
	p50 = {'position': '470.0,70.0,0.0'}

	p52 = {'position': '80.0,170.0,0.0'}
	p54 = {'position': '80.0,150.0,0.0'}
	p56 = {'position': '100.0,150.0,0.0'}
	p58 = {'position': '130.0,150.0,0.0'}
	p60 = {'position': '130.0,170.0,0.0'}

	p62 = {'position': '170.0,170.0,0.0'}
	p64 = {'position': '180.0,150.0,0.0'}
	p66 = {'position': '200.0,150.0,0.0'}
	p68 = {'position': '220.0,150.0,0.0'}
	p70 = {'position': '230.0,170.0,0.0'}

	p72 = {'position': '270.0,160.0,0.0'}
	p74 = {'position': '280.0,150.0,0.0'}
	p76 = {'position': '300.0,150.0,0.0'}
	p78 = {'position': '320.0,150.0,0.0'}
	p80 = {'position': '330.0,170.0,0.0'}

	p82 = {'position': '360.0,160.0,0.0'}
	p84 = {'position': '380.0,150.0,0.0'}
	p86 = {'position': '400.0,150.0,0.0'}
	p88 = {'position': '420.0,150.0,0.0'}
	p90 = {'position': '440.0,170.0,0.0'}

	"""p92 = {'position': '120.0,280.0,0.0'}
	p94 = {'position': '130.0,260.0,0.0'}
	p96 = {'position': '150.0,250.0,0.0'}
	p98 = {'position': '170.0,260.0,0.0'}
	p100 = {'position': '180.0,280.0,0.0'}

	p102 = {'position': '210.0,250.0,0.0'}
	p104 = {'position': '230.0,260.0,0.0'}
	p106 = {'position': '250.0,250.0,0.0'}
	p108 = {'position': '270.0,260.0,0.0'}
	p110 = {'position': '290.0,250.0,0.0'}

	p112 = {'position': '320.0,270.0,0.0'}
	p114 = {'position': '330.0,250.0,0.0'}
	p116 = {'position': '350.0,250.0,0.0'}
	p118 = {'position': '350.0,280.0,0.0'}
	p120 = {'position': '380.0,270.0,0.0'}

	p122 = {'position': '170.0,380.0,0.0'}
	p124 = {'position': '180.0,360.0,0.0'}
	p126 = {'position': '200.0,350.0,0.0'}
	p128 = {'position': '220.0,360.0,0.0'}
	p130 = {'position': '240.0,380.0,0.0'}

	p132 = {'position': '270.0,370.0,0.0'}
	p134 = {'position': '280.0,350.0,0.0'}
	p136 = {'position': '300.0,350.0,0.0'}
	p138 = {'position': '320.0,350.0,0.0'}
	p140 = {'position': '330.0,370.0,0.0'}"""

    #starting 
    net.mobility(sta1, 'start', time=1, **p1)
    net.mobility(sta2, 'start', time=1, **p2)
    net.mobility(sta3, 'start', time=1, **p5)
    net.mobility(sta4, 'start', time=1, **p7)
    net.mobility(sta5, 'start', time=1, **p9)
    net.mobility(sta6, 'start', time=1, **p11)
    net.mobility(sta7, 'start', time=1, **p13)
    net.mobility(sta8, 'start', time=1, **p15)
    net.mobility(sta9, 'start', time=1, **p17)
    net.mobility(sta10, 'start', time=1, **p19)

    net.mobility(sta11, 'start', time=1, **p21)
    net.mobility(sta12, 'start', time=1, **p23)
    net.mobility(sta13, 'start', time=1, **p25)
    net.mobility(sta14, 'start', time=1, **p27)
    net.mobility(sta15, 'start', time=1, **p29)
    net.mobility(sta16, 'start', time=1, **p31)
    net.mobility(sta17, 'start', time=1, **p33)
    net.mobility(sta18, 'start', time=1, **p35)
    net.mobility(sta19, 'start', time=1, **p37)
    net.mobility(sta20, 'start', time=1, **p39)

    net.mobility(sta21, 'start', time=1, **p41)
    net.mobility(sta22, 'start', time=1, **p43)
    net.mobility(sta23, 'start', time=1, **p45)
    net.mobility(sta24, 'start', time=1, **p47)
    net.mobility(sta25, 'start', time=1, **p49)
    net.mobility(sta26, 'start', time=1, **p51)
    net.mobility(sta27, 'start', time=1, **p53)
    net.mobility(sta28, 'start', time=1, **p55)
    net.mobility(sta29, 'start', time=1, **p57)
    net.mobility(sta30, 'start', time=1, **p59)

    net.mobility(sta31, 'start', time=1, **p61)
    net.mobility(sta32, 'start', time=1, **p63)
    net.mobility(sta33, 'start', time=1, **p65)
    net.mobility(sta34, 'start', time=1, **p67)
    net.mobility(sta35, 'start', time=1, **p69)
    net.mobility(sta36, 'start', time=1, **p71)
    net.mobility(sta37, 'start', time=1, **p73)
    net.mobility(sta38, 'start', time=1, **p75)
    net.mobility(sta39, 'start', time=1, **p77)
    net.mobility(sta40, 'start', time=1, **p79)

    net.mobility(sta41, 'start', time=1, **p81)
    net.mobility(sta42, 'start', time=1, **p83)
    net.mobility(sta43, 'start', time=1, **p85)
    net.mobility(sta44, 'start', time=1, **p87)
    net.mobility(sta45, 'start', time=1, **p89)
    """net.mobility(sta46, 'start', time=1, **p91)
    net.mobility(sta47, 'start', time=1, **p93)
    net.mobility(sta48, 'start', time=1, **p95)
    net.mobility(sta49, 'start', time=1, **p97)
    net.mobility(sta50, 'start', time=1, **p99)
    net.mobility(sta51, 'start', time=1, **p101)
    net.mobility(sta52, 'start', time=1, **p103)
    net.mobility(sta53, 'start', time=1, **p105)
    net.mobility(sta54, 'start', time=1, **p107)
    net.mobility(sta55, 'start', time=1, **p109)
    net.mobility(sta56, 'start', time=1, **p111)
    net.mobility(sta57, 'start', time=1, **p113)
    net.mobility(sta58, 'start', time=1, **p115)
    net.mobility(sta59, 'start', time=1, **p117)
    net.mobility(sta60, 'start', time=1, **p119)
    net.mobility(sta61, 'start', time=1, **p121)
    net.mobility(sta62, 'start', time=1, **p123)
    net.mobility(sta63, 'start', time=1, **p125)
    net.mobility(sta64, 'start', time=1, **p127)
    net.mobility(sta65, 'start', time=1, **p129)
    net.mobility(sta66, 'start', time=1, **p131)
    net.mobility(sta67, 'start', time=1, **p133)
    net.mobility(sta68, 'start', time=1, **p135)
    net.mobility(sta69, 'start', time=1, **p137)
    net.mobility(sta70, 'start', time=1, **p139)"""

    #ending
    net.mobility(sta1, 'stop', time=12, **p3)
    net.mobility(sta2, 'stop', time=12, **p4)
    net.mobility(sta3, 'stop', time=12, **p6)
    net.mobility(sta4, 'stop', time=12, **p8)
    net.mobility(sta5, 'stop', time=12, **p10)
    net.mobility(sta6, 'stop', time=12, **p12)
    net.mobility(sta7, 'stop', time=12, **p14)
    net.mobility(sta8, 'stop', time=12, **p16)
    net.mobility(sta9, 'stop', time=12, **p18)
    net.mobility(sta10, 'stop', time=12, **p20)

    net.mobility(sta11, 'stop', time=12, **p22)
    net.mobility(sta12, 'stop', time=12, **p24)
    net.mobility(sta13, 'stop', time=12, **p26)
    net.mobility(sta14, 'stop', time=12, **p28)
    net.mobility(sta15, 'stop', time=12, **p30)
    net.mobility(sta16, 'stop', time=12, **p32)
    net.mobility(sta17, 'stop', time=12, **p34)
    net.mobility(sta18, 'stop', time=12, **p36)
    net.mobility(sta19, 'stop', time=12, **p38)
    net.mobility(sta20, 'stop', time=12, **p40)

    net.mobility(sta21, 'stop', time=12, **p42)
    net.mobility(sta22, 'stop', time=12, **p44)
    net.mobility(sta23, 'stop', time=12, **p46)
    net.mobility(sta24, 'stop', time=12, **p48)
    net.mobility(sta25, 'stop', time=12, **p50)
    net.mobility(sta26, 'stop', time=12, **p52)
    net.mobility(sta27, 'stop', time=12, **p54)
    net.mobility(sta28, 'stop', time=12, **p56)
    net.mobility(sta29, 'stop', time=12, **p58)
    net.mobility(sta30, 'stop', time=12, **p60)

    net.mobility(sta31, 'stop', time=12, **p62)
    net.mobility(sta32, 'stop', time=12, **p64)
    net.mobility(sta33, 'stop', time=12, **p66)
    net.mobility(sta34, 'stop', time=12, **p68)
    net.mobility(sta35, 'stop', time=12, **p70)
    net.mobility(sta36, 'stop', time=12, **p72)
    net.mobility(sta37, 'stop', time=12, **p74)
    net.mobility(sta38, 'stop', time=12, **p76)
    net.mobility(sta39, 'stop', time=12, **p78)
    net.mobility(sta40, 'stop', time=12, **p80)

    net.mobility(sta41, 'stop', time=12, **p82)
    net.mobility(sta42, 'stop', time=12, **p84)
    net.mobility(sta43, 'stop', time=12, **p86)
    net.mobility(sta44, 'stop', time=12, **p88)
    net.mobility(sta45, 'stop', time=12, **p90)
    """net.mobility(sta46, 'stop', time=12, **p92)
    net.mobility(sta47, 'stop', time=12, **p94)
    net.mobility(sta48, 'stop', time=12, **p96)
    net.mobility(sta49, 'stop', time=12, **p98)
    net.mobility(sta50, 'stop', time=12, **p100)
    net.mobility(sta51, 'stop', time=12, **p102)
    net.mobility(sta52, 'stop', time=12, **p104)
    net.mobility(sta53, 'stop', time=12, **p106)
    net.mobility(sta54, 'stop', time=12, **p108)
    net.mobility(sta55, 'stop', time=12, **p110)
    net.mobility(sta56, 'stop', time=12, **p112)
    net.mobility(sta57, 'stop', time=12, **p114)
    net.mobility(sta58, 'stop', time=12, **p116)
    net.mobility(sta59, 'stop', time=12, **p118)
    net.mobility(sta60, 'stop', time=12, **p120)
    net.mobility(sta61, 'stop', time=12, **p122)
    net.mobility(sta62, 'stop', time=12, **p124)
    net.mobility(sta63, 'stop', time=12, **p126)
    net.mobility(sta64, 'stop', time=12, **p128)
    net.mobility(sta65, 'stop', time=12, **p130)
    net.mobility(sta66, 'stop', time=12, **p132)
    net.mobility(sta67, 'stop', time=12, **p134)
    net.mobility(sta68, 'stop', time=12, **p136)
    net.mobility(sta69, 'stop', time=12, **p138)
    net.mobility(sta70, 'stop', time=12, **p140)"""
    net.stopMobility(time=500)

    info("*** Starting network\n")
    net.build()
    c1.start()
    c2.start()
    c3.start()
    c4.start()
    c5.start()
    c6.start()
    c7.start()
    c8.start()
    c9.start()
    """c10.start()
    c11.start()
    c12.start()
    c13.start()
    c14.start()"""
    ap1.start([c1])
    ap2.start([c2])
    ap3.start([c3])
    ap4.start([c4])
    ap5.start([c5])
    ap6.start([c6])
    ap7.start([c7])
    ap8.start([c8])
    ap9.start([c9])
    """ap10.start([c4])
    ap11.start([c4])
    ap12.start([c4])
    ap13.start([c4])
    ap14.start([c4])"""


    info("*** Running CLI\n")
    CLI(net)

    info("*** Stopping network\n")
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    topology(sys.argv)
