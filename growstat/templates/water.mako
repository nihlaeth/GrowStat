<%inherit file='base.mako' />
<h2>Record added water</h2>
<form name="Water" action="${request.route_url('water')}" method="POST">
Water: <input type="text" name="water" /> L<br />

Water supply: <select name='supply'>
    %for supply in supplies:
        <option value="${supply[0]}">${supply[1]}</option>
    % endfor
</select>

<input type="submit" class="button" value="ADD (no backsies!)" />
</form>
