<%inherit file='base.mako' />
<h2>Record Nutrients</h2>
<form name="Nutrients" action="${request.route_url('nutrients')}" method="POST">
<input type="hidden" name="action" value="add" />
Add nutrients to a water supply:<br />
Nutrient:<select name="name">
% for n in nutrients:
    <option value="${n[0]}">${n[1]}</option>
% endfor
</select>
<br />
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
<hr />
<form name="NewNutrient" action="${request.route_url('nutrients')}" method="POST">
Add a new nutrient:<br />
<input type="hidden" name="action" value="new" />
Name: <input type="text" name="name" /><br />
<input type="submit" class="button" value="ADD (no bacpsies!)" />
</form>
