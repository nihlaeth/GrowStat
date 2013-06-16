<%inherit file='base.mako' />
<h2>Upload Picture</h2>
<form name="Pic" action="${request.route_url('pic')}" method="POST" enctype='multipart/form-data'>
Image file: <input type="file" name="pic" /> <br />
(.jpg, .png, .bmp, .gif)
<br /><br />
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
