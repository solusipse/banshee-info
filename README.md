banshee-info
============

Little script that obtains data from Banshee via dbus (e.g. for conky)
<br><br>
<h2>Usage:</h2>
<ul>
    <li>--basic     - show basic info: Author - Song</li>
    <li>--title     - displays track's title</li>
    <li>--author    - displays track's author</li>
    <li>--album     - displays track's album info</li>
    <li>--progress  - show percentage value of track's progress</li>
    <li>--volume    - show percentage volume</li>
    <li>--uri       - show uri</li>
    <li>--length    - show length in minutes</li>
    <li>--state     - show banshee's state</li>
</ul>

<h2>Example conky usage:</h2>
Now playing: ${execi 50 python2 ~/scripts/banshee-info.py --basic} ${execibar 10 python2 ~/scripts/banshee-info.py --progress}