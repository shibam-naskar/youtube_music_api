from math import trunc
from flask import Flask,jsonify,send_file,render_template
import os
import youtube_dl
from youtubesearchpython import VideosSearch



ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    
}



app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/youtube-data/<string:n>')
def youtubeMusic(n):
    videosSearch = VideosSearch(n, limit = 20)

    videos = videosSearch.result()
    videos1 = videos['result']
    return jsonify(videos1)
@app.route('/mp3/<string:s>/<string:n>')
def mp3Down(s,n):
    listning = os.walk('.')
    n = n.replace("|","_")
    path = str(n)+"-"+str(s)+".mp3"
    for root_path,directories,files in listning:
        if path in files:
            return send_file(path,as_attachment=True)
        else:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download(['https://www.youtube.com/watch?v={}'.format(s)])
                return send_file(path,as_attachment=True)
        


    
        


if __name__ == "__main__":
    app.run(debug=True , port=5000)