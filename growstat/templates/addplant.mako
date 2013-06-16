<%inherit file='base.mako' />
<h2>Add plant</h2>
<form name="Plant" action="${request.route_url('addplant')}" method="POST">
Name: <input type="text" name="name" /><br />
Latin name: <input type="text" name="lname" /><br />

Slot: <select name='slot'>
% for s in supplies:
    % for c in columns:
        % if c[2]==s[0]:
            <optgroup label="${s[1]}-${c[1]}">
            % for slot in slots:
                %if slot[2]==c[0]:
                    <option value="${slot[0]}">${slot[1]}
                    % for plant in plants:
                        %if plant[3]==slot[0]:
                            - ${plant[1]}
                        % endif
                    % endfor
                    </option>
                % endif
            % endfor
        % endif
    % endfor
    </optgroup>
% endfor
</select>

<input type="submit" class="button" value="ADD (no backsies!)" />
</form>
