# gnome-random-wallpaper
Simple python script to randomly change wallpaper on gnome desktop environment.

#### Run simply with `python main.py`

Dependencies are listed in the `requirements.txt`.

It fetches a random image from `https://picsum.photos/{width}/{height}/?random`.
The `width` and `height` values come from `xdpyinfo` command based on your monitor's resolution.
