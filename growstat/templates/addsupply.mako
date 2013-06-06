<%inherit file='base.mako' />
<h2>Add water supply</h2>
<form name="Supply" action="${request.route_url('addsupply')}" method="POST">
Name: <input type="text" name="name" />
<input type="submit" class="button" value="ADD (no backsies!)" />
