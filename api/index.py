from flask import Flask, render_template_string

app = Flask(__name__)

videos = [
    {
        "id": 1,
        "user": "@abdo_official",
        "desc": "أول فيديو على منصة عبده توك! 🔥 #abdo #tiktok",
        "url": "https://www.w3schools.com/html/mov_bbb.mp4",
        "likes": 120,
        "comments": 15
    },
    {
        "id": 2,
        "user": "@creative_mind",
        "desc": "تجربة التمرير السريع مثل تيك توك 🚀",
        "url": "https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.mp4",
        "likes": 450,
        "comments": 32
    }
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Abdo Tok - عبده توك</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { background-color: #000; color: #fff; font-family: sans-serif; overflow: hidden; }
        .app-container {
            height: 100vh;
            width: 100vw;
            max-width: 480px;
            margin: 0 auto;
            position: relative;
            overflow-y: scroll;
            snap-type: y mandatory;
            scroll-behavior: smooth;
        }
        .app-container::-webkit-scrollbar { display: none; }
        .app-container { -ms-overflow-style: none; scrollbar-width: none; }
        .video-card {
            height: 100vh;
            width: 100%;
            position: relative;
            snap-align: start;
            background: #111;
        }
        video { width: 100%; height: 100%; object-fit: cover; }
        .video-details {
            position: absolute;
            bottom: 20px;
            right: 15px;
            left: 80px;
            z-index: 10;
            text-shadow: 1px 1px 3px rgba(0,0,0,0.8);
        }
        .user-name { font-weight: bold; font-size: 1.1rem; margin-bottom: 5px; }
        .video-desc { font-size: 0.9rem; color: #ddd; }
        .action-buttons {
            position: absolute;
            left: 15px;
            bottom: 40px;
            display: flex;
            flex-direction: column;
            gap: 20px;
            align-items: center;
            z-index: 10;
        }
        .action-btn {
            background: none;
            border: none;
            color: #fff;
            display: flex;
            flex-direction: column;
            align-items: center;
            font-size: 0.8rem;
            cursor: pointer;
        }
        .action-btn .icon {
            width: 45px;
            height: 45px;
            background: rgba(255,255,255,0.2);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.4rem;
            margin-bottom: 4px;
            backdrop-filter: blur(5px);
        }
        .top-bar {
            position: fixed;
            top: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 100%;
            max-width: 480px;
            display: flex;
            justify-content: space-around;
            padding: 15px;
            font-weight: bold;
            font-size: 1.1rem;
            z-index: 20;
            background: linear-gradient(to bottom, rgba(0,0,0,0.6), transparent);
        }
        .top-bar span { cursor: pointer; opacity: 0.7; }
        .top-bar span.active { opacity: 1; border-bottom: 2px solid #fff; padding-bottom: 2px; }
    </style>
</head>
<body>
    <div class="top-bar">
        <span>متابعة</span>
        <span class="active">لك (For You)</span>
    </div>
    <div class="app-container">
        {% for v in videos %}
        <div class="video-card">
            <video src="{{ v.url }}" loop onclick="togglePlay(this)"></video>
            <div class="video-details">
                <div class="user-name">{{ v.user }}</div>
                <div class="video-desc">{{ v.desc }}</div>
            </div>
            <div class="action-buttons">
                <div class="action-btn" onclick="likeVideo(this, {{ v.likes }})">
                    <div class="icon">❤️</div>
                    <span>{{ v.likes }}</span>
                </div>
                <div class="action-btn">
                    <div class="icon">💬</div>
                    <span>{{ v.comments }}</span>
                </div>
                <div class="action-btn">
                    <div class="icon">🔗</div>
                    <span>مشاركة</span>
                </div>
            </div>
        </div>
        {% endfor %}
    </div>
    <script>
        function togglePlay(video) {
            if (video.paused) { video.play(); } else { video.pause(); }
        }
        function likeVideo(btn, count) {
            let countSpan = btn.querySelector('span');
            countSpan.innerText = count + 1;
            btn.querySelector('.icon').style.color = '#fe2c55';
        }
        document.addEventListener('DOMContentLoaded', () => {
            let firstVideo = document.querySelector('video');
            if(firstVideo) firstVideo.play().catch(()=>{});
        });
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, videos=videos)

app = app
