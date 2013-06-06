<%inherit file='base.mako' />
<h2>Add slot</h2>
<form name="Slot" action="${request.route_url('addslot')}" method="POST">
Name: <input type="text" name="name" /><br />

Column: <select name='column'>a
% for s in supplies:
    <optgroup label="${s[1]}">3
    % for column in columns:
        % if column[2]==s[0]:
        <option value="${column[0]}">${column[1]}</option>
        % endif
    % endfor
    </optgroup>
% endfor
</select>

<input type="submit" class="button" value="ADD (no backsies!)" />
