# -*- coding: utf-8 -*-
<%inherit file="base.mako"/>
<h4>Welcome to GrowStat!</h4>
<p>With GrowStat you can gain insight in the efficiency of your hydroponics system. What nutrient solution works best? Does a lower ph affect  your harvest in a positive way? Can your plants do with less water? Thanks to GrowStat you'll never have to wonder again!</p>

Here are some stats to cheer you up:<br />
<table id='shortstat'>
<tr>
    <td>Harvested so far:</td>
    <td>${totalharvest} kg</td>
</tr>
<tr>
    <td>Total growth</td>
    <td>${totalgrowth} m</td>
<tr>
    <td>Total plants alive:</td>
    <td>${totalliveplants} plants</td>
</tr>
<tr>
    <td>Average ph</td>
    <td>${averageph}</td>
</tr>
<tr>
    <td>Average ec</td>
    <td>${averageec}</td>
</tr>
<tr>
    <td>Average temperature</td>
    <td>${averagetemp} C</td>
</td>
<tr>
    <td>Average Humidity</td>
    <td>${averagehum}</td>
</tr>
</table>
