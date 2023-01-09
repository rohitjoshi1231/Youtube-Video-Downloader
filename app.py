from flask import Flask, render_template, request
from pytube import YouTube
from pytube.cli import on_progress
app = Flask(__name__)


@app.route('/')
def root():
    return render_template('./index.html')


@app.route("/submit_form", methods=['POST', 'GET'])
def submit_form(value=None, val = None):
    if request.method == "POST":
        data = request.form.to_dict()
        link = data["vid_link"]
        yt = YouTube(link, on_progress_callback=on_progress)
        views = yt.views
        title = yt.title
        thumbnail = yt.thumbnail_url
        d_video = yt.streams.first()
        x = title+"\n "+"Total views"+" "+str(views)
        d_video.download('.\\downloads\\')

    return render_template("./main.html", Title=x, T =thumbnail)


if __name__ == '__main__':
    app.run(debug=True)
