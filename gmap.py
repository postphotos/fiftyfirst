#!/usr/bin/python
from csv import DictReader

the_file = DictReader(open('gmap.csv','rU'), dialect="excel")
for row in the_file:
  string = """
  <h3>{County} County</h3>

  <iframe width="425" height="350" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://maps.google.com/maps?f=q&amp;source=s_q&amp;hl=en&amp;geocode=&amp;q={County}+County,+co&amp;g={County}+County,+CO&amp;ie=UTF8&amp;hq=&amp;hnear={County}+County,+Colorado&amp;z={z}&amp;output=embed"></iframe>
<br>
<hr>
  """.format(**row)
  print string