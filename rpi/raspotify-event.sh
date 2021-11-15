if [ "$PLAYER_EVENT" = "start" ]; then
  sudo python3 python/startstop/start.py
fi

if [ "$PLAYER_EVENT" = "stop" ]; then
  sudo python3 python/startstop/stop.py
fi