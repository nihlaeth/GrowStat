<%inherit file='base.mako' />
<h2>Record Nutrients</h2>
<form name="Nutrients" action="${request.route_url('nutrients')}" method="POST">
Name: <input type="text" name="name" /><br />
Amount: <input type="text" name="amount" /><br />
Unit: <select name="unit">
        <option value="L">L</option>
        <option value="ml" selected="selected">ml</option>
        <option value="kg">kg</option>
        <option value="g">g</option>
        <option value="mg">mg</option>
        <option value="µg">µg</option>
    </select>
<br />

Water supply: <select name='supply'>
    %for supply in supplies:
        <option value="${supply[0]}">${supply[1]}</option>
    % endfor
</select>

<input type="submit" class="button" value="ADD (no backsies!)" />
</form>
