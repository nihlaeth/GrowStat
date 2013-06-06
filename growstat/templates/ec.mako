<%inherit file='base.mako' />
<h2>Record EC measurment</h2>
<form name="EC" action="${request.route_url('ec')}" method="POST">
EC value: <input type="text" name="ec" /><br />

Water supply: <select name='supply'>
    %for supply in supplies:
        <option value="${supply[0]}">${supply[1]}</option>
    % endfor
</select>

<input type="submit" class="button" value="ADD (no backsies!)" />
</form>
