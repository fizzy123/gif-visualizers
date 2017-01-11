import os

gif_path = 'static/gifs'

gifs = os.listdir(gif_path)

for i in range(0, len(gifs)):
    if "{}.gif".format(i) not in gifs:
        old_name = [gif for gif in gifs if not gif.replace('.gif', '').isdigit()][0]
        os.rename(gif_path + "/" + old_name, "{}/{}.gif".format(gif_path, i))
        gifs = [gif if gif != old_name else "{}.gif".format(i) for gif in gifs]
