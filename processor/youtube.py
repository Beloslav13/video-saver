import youtube_dl


class YoutubeSaver:

    def __init__(self, link):
        self._link = link

    @property
    def link(self):
        return self._link

    def save(self):
        ydl_opts = {}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            try:
                ydl.download([self.link])
            except Exception as e:
                print(f'Error: {e}, VIDEO: {self.link}')
