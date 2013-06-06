<%inherit file='base.mako' />
<h2>Add column</h2>
<form name="Column" action="${request.route_url('addcolumn')}" method="POST">
Name: <input type="text" name="name" /><br />

Water supply: <select name='supply'>
    %for supply in supplies:
        <option value="${supply[0]}">${supply[1]}</option>
    % endfor
</select>

<input type="submit" class="button" value="ADD (no backsies!)" />
</form>

