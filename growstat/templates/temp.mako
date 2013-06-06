<%inherit file='base.mako' />
<h2>Record Temperature measurment</h2>
<form name="Temp" action="${request.route_url('temp')}" method="POST">
Temperature: <input type="text" name="temp" /> C<br />

Water supply: <select name='supply'>
    %for supply in supplies:
        <option value="${supply[0]}">${supply[1]}</option>
    % endfor
</select>

<input type="submit" class="button" value="ADD (no backsies!)" />
