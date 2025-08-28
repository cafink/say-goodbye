# Project: Celeste save file viewer/editor

"Say goodbye to her for me."

Run via Docker for development:

```zsh
docker build -t say-goodbye .
docker run --rm -p 5000:5000 --mount type=bind,src=.,dst=/usr/src/app say-goodbye
```

Useful links:

- [Some save file format details](https://www.reddit.com/r/celestegame/comments/s6ftrz/comment/ht43h4v/)
- [Sample save files](https://drive.google.com/drive/folders/1cjXhWVAtFx858eeS6K1Bugma6AUUZaZ_)
- [XML parsing Python library](https://www.crummy.com/software/BeautifulSoup/)