<%inherit file="base.mako"/>

<h2>Resources</h2>
<table id='resources'>
<tr>
    <th>Watter supplies</th>
    <th>Columns</th>
    <th>Slots</th>
    <th>Plants</th>
</tr>
<tr>
    <td><a href="${request.route_url('addsupply')}" class="button">Add water supply</a></td>
    <td><a href="${request.route_url('addcolumn')}" class="button">Add column</a></td>
    <td><a href="${request.route_url('addslot')}" class="button">Add slot</a></td>
    <td><a href="${request.route_url('addplant')}" class="button">Add plant</a></td>
</tr>
    % for supply in supplies :
        <tr><td><a href="${request.route_url('editsupply',id=supply[0])}">${supply[1]}</a></td></tr>
        % for col in columns :
            % if col[2]==supply[0]:
                <tr><td></td><td><a href="${request.route_url('editcolumn', id=col[0])}">${col[1]}</a></td></tr>
                % for slot in slots :
                    % if slot[2]==col[0] :
                        <tr><td></td><td></td><td><a href="${request.route_url('editslot',id=slot[0])}">${slot[1]}</a></td>
                        % for plant in plants :
                            % if plant[3]==slot[0] :
                                <td><a href="${request.route_url('editplant',id=plant[0])}">${plant[1]}</a></td>
                            % endif
                        % endfor
                        </tr>
                    % endif
                % endfor
            % endif
        % endfor
    % endfor
</table>
