# -*- coding: utf-8 -*-
<%inherit file="layout.mako"/>

<div id="wrapper">
<table id="body">
<tr>
<td id="nav">
    <h3>Navigation</h3>
    <h5>Data recording</h5>
    <ul>
        <li><a href="${request.route_url('watering')}">Change watering settings</a></li>
        <li><a href="${request.route_url('water')}">Add water</a></li>
        <li><a href="${request.route_url('nutrients')}">Add nutrients</a></li>
        <li><a href="${request.route_url('ph')}">Measure water ph</a></li>
        <li><a href="${request.route_url('ec')}">Measure water ec</a></li>
        <li><a href="${request.route_url('temp')}">Measure water temperature</a></li>
        <li><a href="${request.route_url('humidity')}">Measure humidity</a></li>
        <li><a href="${request.route_url('height')}">Measure plant height</a></li>
        <li><a href="${request.route_url('harvest')}">Weigh harvest</a></li>
        <li><a href="${request.route_url('pic')}">Add picture</a></li>
        <li><a href="${request.route_url('log')}">Add a log entry</a></li>
    </ul>
    <h5>Resources</h5>
    <ul>
        <li><a href="${request.route_url('list')}">List resources</a></li>
        <li><a href="${request.route_url('timeline')}">Timeline</a></li>
    </ul>
    <h5>Statistics</h5>
    <ul>
        <li>Nothing here yet.</li>
        
    </ul>
</td>
<td id="content" valign="top">
${next.body()}
</td>
</tr>
</table>
</div>
