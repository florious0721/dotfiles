#!/bin/bash
sudo sync
systemctl --user stop pipewire pipewire-pulse wireplumber dbus-broker
sudo systemctl poweroff
