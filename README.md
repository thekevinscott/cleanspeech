# Clean Speech

This is an experiment to see if I can leverage VGGish to detect "ums", "uhs", and other detritus of speech.

The motivation is that I say a lot of ums and uhs when I talk, particularly when I give a presentation, and I want something that buzzes me everytime to train myself out of the habit.

## Running

There is a `docker-compose` script to make spinning up the container easy.

```
docker-compose up
```

From there, you'll see some output, including a token to use for the Jupyter
notebook:

```
Recreating cleanspeech ... done
Attaching to cleanspeech
cleanspeech    | [I 15:11:19.643 NotebookApp] Writing notebook server cookie secret to /root/.local/share/jupyter/runtime/notebook_cookie_secret
cleanspeech    | [I 15:11:20.370 NotebookApp] Serving notebooks from local directory: /notebooks
cleanspeech    | [I 15:11:20.371 NotebookApp] The Jupyter Notebook is running at:
cleanspeech    | [I 15:11:20.371 NotebookApp] http://(xxxxxxx or 127.0.0.1):8888/?token={SOME_RANDOM_TOKEN}
cleanspeech    | [I 15:11:20.371 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
cleanspeech    | [C 15:11:20.373 NotebookApp]
cleanspeech    |
cleanspeech    |     To access the notebook, open this file in a browser:
cleanspeech    |         file:///root/.local/share/jupyter/runtime/nbserver-6-open.html
cleanspeech    |     Or copy and paste one of these URLs:
cleanspeech    |         http://(xxxxxxx or 127.0.0.1):8888/?token={SOME_RANDOM_TOKEN}
```
