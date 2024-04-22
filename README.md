
# waybar-wireguard

![](images/off.png)

![](images/on.png)

ON/OFF on click, default cfg path /etc/wireguard/your_cfg.conf (edit in wireguard.py)

#### config.jsonc:

```
"custom/wireguard": {
        "format": "Wireguard {}",
        "interval": "once",
        "signal": 10,
        "exec": "python /home/$USER/.config/waybar/modules/wireguard.py status",
        "exec-on-event": false,
        "on-click": "python /home/$USER/.config/waybar/modules/wireguard.py; pkill -SIGRTMIN+10 waybar",
        "return-type": "json"
    },
