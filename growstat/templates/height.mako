<%inherit file='base.mako' />
<h2>Record Height Value</h2>
<form name="Height" action="${request.route_url('height')}" method="POST">
Height: <input type="text" name="height" /><br />

Plant: <select name='plant'>
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
