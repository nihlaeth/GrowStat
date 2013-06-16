<%inherit file='base.mako' />
<h2>Record Harvest Weight</h2>
<form name="Harvest" action="${request.route_url('harvest')}" method="POST">
Weight: <input type="text" name="harvest" />gr<br />
Type: <select name="type">
<option value="Fruit">Fruit</option>
<option value="Seeds">Seeds</option>
<option value="Leaves">Leaves</option>
<option value="Stem">Stem</option>
<option value="Roots">Roots</option>
<option value="Bulb">Bulb</option>
</select><br />
Plant: <select name='plant'>
% for s in supplies:
    % for c in columns:
        % if c[2]==s[0]:
            <optgroup label="${s[1]}-${c[1]}">
            % for slot in slots:
                %if slot[2]==c[0]:
                    %for plant in plants:
                        %if plant[3]==slot[0]:
                            <option value="${plant[0]}">${slot[1]} - ${plant[1]}</option>
                        % endif
                    % endfor
                % endif
            % endfor
        % endif
    % endfor
    </optgroup>
% endfor
</select>

<input type="submit" class="button" value="ADD (no backsies!)" />
</form>
