<%inherit file='base.mako' />
<h2>Record Humidity measurment</h2>
<form name="Humidity" action="${request.route_url('humidity')}" method="POST">
Humidity: <input type="text" name="humidity" />% <br />

<input type="submit" class="button" value="ADD (no backsies!)" />
</form>
