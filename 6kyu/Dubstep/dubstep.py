def song_decoder(song):
    li = [a for a in list(song.split("WUB")) if a != '']
    return " ".join(li)
