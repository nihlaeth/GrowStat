<%inherit file='base.mako' />
<h2>Record PH measurment</h2>
<form name="PH" action="${request.route_url('ph')}" method="POST">
PH value: <input type="text" name="ph" /><br />

Water supply: <select name='supply'>
    %for supply in supplies:
        <option value="${supply[0]}">${supply[1]}</option>
    % endfor
</select>

<input type="submit" class="button" value="ADD (no backsies!)" />
