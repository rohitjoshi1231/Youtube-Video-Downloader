from flask import Flask, render_template, request
from pytube import YouTube
from pytube.cli import on_progress
app = Flask(__name__)


@app.route('/')
def root():
    return render_template('./index.html')


@app.route("/submit_form", methods=['POST', 'GET'])
def submit_form(value=None, val=None):
    try:
        if request.method == "POST":
            data = request.form.to_dict()
            link = data["vid_link"]
            yt = YouTube(link, on_progress_callback=on_progress)
            views = yt.views if yt.views else 0
            title = yt.title
            thumbnail = yt.thumbnail_url
            print(title)
            d_video = yt.streams.get_highest_resolution()
            x = title+"\n "+"Total views"+" ", views
            d_video.download(r'C:\Users\DELL\downloads')
            return render_template("main.html", title=title, views=views, thumbnail=thumbnail)
    except Exception as e:
        error_message = str(e)
        return render_template("main.html", error_message=error_message)


if __name__ == '__main__':
    app.run(debug=True)
