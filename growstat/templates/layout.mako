# -*- coding: utf-8 -*-
<!DOCTYPE html>
<html>
<head>

    <meta charset="utf-8">
    <title>GrowStat</title>
    <meta name="author" content="Nihlaeth">
    <link rel="shortcut icon" = href="/static/favicon.ico">
    <link rel="stylesheet" href="/static/style.css">

</head>
<body>
<a href="${request.route_url('home')}"><h1 class="sitetitle center">GrowStat</h1></a>
    % if request.session.peek_flash():
    <div id="flash">
        <% flash = request.session.pop_flash() %>
            % for message in flash:
            ${message}<br>
            % endfor
    </div>
    % endif

<div id="page">

    ${next.body()}

</div>

</body>
</html>
