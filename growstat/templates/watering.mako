<%inherit file='base.mako' />
<h2>Watering</h2>
<form name="addtimerconfig" action="${request.route_url('watering')}" method="POST">
<input type="hidden" name="action" value="add" />
Timersetting Name: <input type="text" name="name" /><br />
<input type="submit" class="button" value="ADD (no backsies!)" />
</form>

<table class="timetable">
<tr>
<th>Name</th>
<th>00:00</th>
<th>00:30</th>
<th>01:00</th>
<th>01:30</th>
<th>02:00</th>
<th>02:30</th>
<th>03:00</th>
<th>03:30</th>
<th>04:00</th>
<th>04:30</th>
<th>05:00</th>
<th>05:30</th>
<th>06:00</th>
<th>06:30</th>
<th>07:00</th>
<th>07:30</th>
</tr><tr>
<th></th>
<th>08:00</th>
<th>08:30</th>
<th>09:00</th>
<th>09:30</th>
<th>10:00</th>
<th>10:30</th>
<th>11:00</th>
<th>11:30</th>
<th>12:00</th>
<th>12:30</th>
<th>13:00</th>
<th>13:30</th>
<th>14:00</th>
<th>14:30</th>
<th>15:00</th>
<th>15:30</th>
</tr><tr>
<th></th>
<th>16:00</th>
<th>16:30</th>
<th>17:00</th>
<th>17:30</th>
<th>18:00</th>
<th>18:30</th>
<th>19:00</th>
<th>19:30</th>
<th>20:00</th>
<th>20:30</th>
<th>21:00</th>
<th>21:30</th>
<th>22:00</th>
<th>22:30</th>
<th>23:00</th>
<th>23:30</th>
<th>Save</th>
</tr>

% for c in timerconfigs:
<tr><td>
<form name="edittimerconfig" action="${request.route_url('watering')}" method="POST">
<input type="hidden" name="action" value="edit" />
<input type="hidden" name="id" value="${c[0]}" />
${c[1]}</td>

<td><input type="checkbox" name="t0000" value="1" % if ${c[2]}==1 : checked="checked" % endif class="mini" /></td>
<td><input type="checkbox" name="t0030" value="1" % if ${c[3]}==1 : checked="checked" % endif class="mini" /></td>
<td><input type="checkbox" name="t0100" value="1" % if ${c[4]}==1 : checked="checked" % endif class="mini" /></td>
<td><input type="checkbox" name="t0130" value="1" % if ${c[5]}==1 : checked="checked" % endif class="mini" /></td>
<td><input type="checkbox" name="t0200" value="1" % if ${c[6]}==1 : checked="checked" % endif class="mini" /></td>
<td><input type="checkbox" name="t0230" value="1" % if ${c[7]}==1 : checked="checked" % endif class="mini" /></td>
<td><input type="checkbox" name="t0300" value="1" % if ${c[8]}==1 : checked="checked" % endif class="mini" /></td>
<td><input type="checkbox" name="t0330" value="1" % if ${c[9]}==1 : checked="checked" % endif class="mini" /></td>
<td><input type="checkbox" name="t0400" value="1" % if ${c[10]}==1 : checked="checked" % endif class="mini" /></td>
<td><input type="checkbox" name="t0430" value="1" % if ${c[11]}==1 : checked="checked" % endif class="mini" /></td>
<td><input type="checkbox" name="t0500" value="1" % if ${c[12]}==1 : checked="checked" % endif class="mini" /></td>
<td><input type="checkbox" name="t0530" value="1" % if ${c[13]}==1 : checked="checked" % endif class="mini" /></td>
<td><input type="checkbox" name="t0600" value="1" % if ${c[14]}==1 : checked="checked" % endif class="mini" /></td>
<td><input type="checkbox" name="t0630" value="1" % if ${c[15]}==1 : checked="checked" % endif class="mini" /></td>
<td><input type="checkbox" name="t0700" value="1" % if ${c[16]}==1 : checked="checked" % endif class="mini" /></td>
<td><input type="checkbox" name="t0730" value="1" % if ${c[17]}==1 : checked="checked" % endif class="mini" /></td>
</tr><tr>
<td>-></td>
<td><input type="checkbox" name="t0800" value="1" % if ${c[18]}==1 : checked="checked" % endif class="mini" /></td>
<td><input type="checkbox" name="t0830" value="1" % if ${c[19]}==1 : checked="checked" % endif class="mini" /></td>
<td><input type="checkbox" name="t0900" value="1" % if ${c[20]}==1 : checked="checked" % endif class="mini" /></td>
<td><input type="checkbox" name="t0930" value="1" % if ${c[21]}==1 : checked="checked" % endif class="mini" /></td>
<td><input type="checkbox" name="t1000" value="1" % if ${c[22]}==1 : checked="checked" % endif class="mini" /></td>
<td><input type="checkbox" name="t1030" value="1" % if ${c[23]}==1 : checked="checked" % endif class="mini" /></td>
<td><input type="checkbox" name="t1100" value="1" % if ${c[24]}==1 : checked="checked" % endif class="mini" /></td>
<td><input type="checkbox" name="t1130" value="1" % if ${c[25]}==1 : checked="checked" % endif class="mini" /></td>
<td><input type="checkbox" name="t1200" value="1" % if ${c[26]}==1 : checked="checked" % endif class="mini" /></td>
<td><input type="checkbox" name="t1230" value="1" % if ${c[27]}==1 : checked="checked" % endif class="mini" /></td>
<td><input type="checkbox" name="t1300" value="1" % if ${c[28]}==1 : checked="checked" % endif class="mini" /></td>
<td><input type="checkbox" name="t1330" value="1" % if ${c[29]}==1 : checked="checked" % endif class="mini" /></td>
<td><input type="checkbox" name="t1400" value="1" % if ${c[30]}==1 : checked="checked" % endif class="mini" /></td>
<td><input type="checkbox" name="t1430" value="1" % if ${c[31]}==1 : checked="checked" % endif class="mini" /></td>
<td><input type="checkbox" name="t1500" value="1" % if ${c[32]}==1 : checked="checked" % endif class="mini" /></td>
<td><input type="checkbox" name="t1530" value="1" % if ${c[33]}==1 : checked="checked" % endif class="mini" /></td>
</tr><tr>
<td>-></td>
<td><input type="checkbox" name="t1600" value="1" % if ${c[34]}==1 : checked="checked" % endif class="mini" /></td>
<td><input type="checkbox" name="t1630" value="1" % if ${c[35]}==1 : checked="checked" % endif class="mini" /></td>
<td><input type="checkbox" name="t1700" value="1" % if ${c[36]}==1 : checked="checked" % endif class="mini" /></td>
<td><input type="checkbox" name="t1730" value="1" % if ${c[37]}==1 : checked="checked" % endif class="mini" /></td>
<td><input type="checkbox" name="t1800" value="1" % if ${c[38]}==1 : checked="checked" % endif class="mini" /></td>
<td><input type="checkbox" name="t1830" value="1" % if ${c[39]}==1 : checked="checked" % endif class="mini" /></td>
<td><input type="checkbox" name="t1900" value="1" % if ${c[40]}==1 : checked="checked" % endif class="mini" /></td>
<td><input type="checkbox" name="t1930" value="1" % if ${c[41]}==1 : checked="checked" % endif class="mini" /></td>
<td><input type="checkbox" name="t2000" value="1" % if ${c[42]}==1 : checked="checked" % endif class="mini" /></td>
<td><input type="checkbox" name="t2030" value="1" % if ${c[43]}==1 : checked="checked" % endif class="mini" /></td>
<td><input type="checkbox" name="t2100" value="1" % if ${c[44]}==1 : checked="checked" % endif class="mini" /></td>
<td><input type="checkbox" name="t2130" value="1" % if ${c[45]}==1 : checked="checked" % endif class="mini" /></td>
<td><input type="checkbox" name="t2200" value="1" % if ${c[46]}==1 : checked="checked" % endif class="mini" /></td>
<td><input type="checkbox" name="t2230" value="1" % if ${c[47]}==1 : checked="checked" % endif class="mini" /></td>
<td><input type="checkbox" name="t2300" value="1" % if ${c[48]}==1 : checked="checked" % endif class="mini" /></td>
<td><input type="checkbox" name="t2330" value="1" % if ${c[49]}==1 : checked="checked" % endif class="mini" /></td>

<td>
<input type="submit" class="button" value="Save" />
</form>
</tr>
% endfor
</table>



<form name="assign" action="${request.route_url('watering')}" method="POST">
<input type="hidden" name="action" value="assign" />


<input type="submit" class="button" value="edit" />
</form>




