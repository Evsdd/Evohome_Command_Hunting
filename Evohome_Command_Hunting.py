# Evohome Command Hunting
# Author: Evsdd (2017)
# Python 2.7.11
# Requires pyserial module which can be installed using 'python -m pip install pyserial'
# Program to hunt for recognised Evohome RQ/RP commands
# Program sends every possible RQ command 0x0000-0xFFFF with a payload of 01 to the specified controller
# If a RQ is received within the next 3 messages the command is logged.

from __future__ import print_function
import serial                     # import the module

output_log = open("e:\\Python\\Evohome_Command_Hunting.log", "w")
found_commands = open("e:\\Python\\Evohome_Command_Hunting.txt", "w")

ComPort = serial.Serial('COM8')   # open COM8
ComPort.baudrate = 115200         # set Baud rate to 250000
ComPort.bytesize = 8              # Number of data bits = 8
ComPort.parity   = 'N'            # No parity
ComPort.stopbits = 1              # Number of Stop bits = 1
ComPort.timeout = 1               # Read timeout = 1sec

Controller = '01:073076'          # Device type and address of controller
Device = '18:730'                 # Device type and address of serial device (default 18:730)

data = ComPort.readline()         # Wait and read data
print(data)                       # print the received data
data = ComPort.readline()         # Wait and read data
print(data)

for cmnd in xrange(0x0000, 0x10000):
 data = bytearray(b'RQ --- %s %s --:------ %04X 001 01\r\n' % (Device, Controller, cmnd))
 No = ComPort.write(data)
 data1 = ComPort.readline()       # Wait and read data1
 data2 = ComPort.readline()       # Wait and read data2
 
 if (data2[4:6] == 'RP') and (data2[41:45] == '%04X' % cmnd):
     print(data2, file=output_log)
     print('%04X' % cmnd, file=found_commands)
     print('Found Command:%04X' % cmnd)
 else:
     data3 = ComPort.readline()   # Wait and read data3
     #print(data3)
     if (data3[4:6] == 'RP') and (data3[41:45] == '%04X' % cmnd):
      print(data3, file=output_log)
      print('%04X' % cmnd, file=found_commands)
      print('Found Command:%04X' % cmnd)
     else:
      data4 = ComPort.readline()  # Wait and read data4
      #print(data4)
      if (data4[4:6] == 'RP') and (data4[41:45] == '%04X' % cmnd):
       print(data4, file=output_log)
       print('%04X' % cmnd, file=found_commands)
       print('Found Command:%04X' % cmnd)
    
ComPort.close()                   # Close the COM Port
file.close(output_log)
file.close(found_commands)


