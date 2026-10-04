<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>abdo-tok - التطبيق الرسمي</title>
    <!-- FontAwesome للأيقونات -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            user-select: none;
        }
        body {
            background-color: #000;
            color: #fff;
            font-family: Arial, sans-serif;
            height: 100vh;
            overflow: hidden;
        }
        /* شاشة تسجيل الدخول */
        #auth-modal {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.98);
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            z-index: 9999;
            padding: 20px;
            text-align: center;
        }
        #auth-modal h2 {
            margin-bottom: 10px;
            color: #fe2c55;
            font-size: 26px;
        }
        #auth-modal p {
            margin-bottom: 20px;
            color: #ccc;
            font-size: 15px;
        }
        .input-box {
            width: 85%;
            max-width: 320px;
            padding: 14px 18px;
            margin-bottom: 15px;
            background: #1a1a1a;
            border: 1px solid #444;
            border-radius: 30px;
            color: #fff;
            font-size: 16px;
            text-align: center;
            outline: none;
        }
        .input-box:focus {
            border-color: #fe2c55;
        }
        .login-btn {
            background: #fe2c55;
            color: #fff;
            border: none;
            padding: 14px 32px;
            border-radius: 30px;
            font-weight: bold;
            font-size: 16px;
            cursor: pointer;
            box-shadow: 0 4px 15px rgba(254,44,85,0.4);
            transition: 0.2s;
        }
        .login-btn:active {
            transform: scale(0.95);
        }

        /* واجهة التيكتوك الرئيسية */
        .app-container {
            height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            position: relative;
        }
        .feed {
            flex: 1;
            overflow-y: scroll;
            scroll-snap-type: y mandatory;
        }
        .video-card {
            height: 100vh;
            scroll-snap-align: start;
            position: relative;
            background: #111;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .video-card video {
            width: 100%;
            height: 100%;
            object-fit: cover;
            position: absolute;
            top: 0;
            left: 0;
        }
        .video-info {
            position: absolute;
            bottom: 75px;
            right: 15px;
            left: 80px;
            text-align: right;
            display: flex;
            align-items: center;
            gap: 15px;
            z-index: 10;
            background: rgba(0, 0, 0, 0.4);
            padding: 10px;
            border-radius: 12px;
            backdrop-filter: blur(5px);
        }
        .user-avatar {
            width: 55px;
            height: 55px;
            border-radius: 50%;
            border: 2px solid #fe2c55;
            object-fit: cover;
            background: #333;
        }
        .actions {
            position: absolute;
            bottom: 80px;
            left: 15px;
            display: flex;
            flex-direction: column;
            gap: 20px;
            align-items: center;
            z-index: 10;
        }
        .action-btn {
            background: rgba(0,0,0,0.6);
            border: none;
            color: #fff;
            width: 48px;
            height: 48px;
            border-radius: 50%;
            font-size: 22px;
            cursor: pointer;
            display: flex;
            justify-content: center;
            align-items: center;
            transition: 0.2s;
        }
        .action-btn:active {
            transform: scale(1.2);
        }
        .action-btn span {
            font-size: 11px;
            margin-top: 2px;
        }

        /* نافذة تعديل الملف الشخصي */
        #profile-modal {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.96);
            display: none;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            z-index: 9998;
            padding: 20px;
            text-align: center;
        }
        #profile-modal h2 {
            margin-bottom: 15px;
            color: #fe2c55;
        }

        /* شريط التنقل السفلي */
        .nav-bar {
            height: 60px;
            background: #000;
            border-top: 1px solid #222;
            display: flex;
            justify-content: space-around;
            align-items: center;
            position: fixed;
            bottom: 0;
            width: 100%;
            z-index: 100;
        }
        .nav-item {
            color: #777;
            font-size: 22px;
            cursor: pointer;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .nav-item.active {
            color: #fff;
        }
        .nav-item span {
            font-size: 10px;
            margin-top: 3px;
        }
    </style>
</head>
<body>

    <!-- نافذة تسجيل الدخول الأولى -->
    <div id="auth-modal">
        <h2>abdo-tok 🚀</h2>
        <p>اكتب اسمك للمتابعة (اكتب @abdo_admin لصلاحيات الملك)</p>
        <input type="text" id="username-input" class="input-box" placeholder="اكتب اسمك هنا...">
        <br>
        <button class="login-btn" onclick="handleLogin()">
            <i class="fas fa-sign-in-alt"></i> دخول للتطبيق
        </button>
    </div>

    <!-- نافذة تعديل الملف الشخصي -->
    <div id="profile-modal">
        <h2>تعديل الملف الشخصي ⚙️</h2>
        <p>غيّر اسمك أو صورة بروفايلك براحتك</p>
        <input type="text" id="edit-name-input" class="input-box" placeholder="الاسم الجديد...">
        <input type="text" id="edit-avatar-input" class="input-box" placeholder="رابط صورة البروفايل (URL)...">
        <br>
        <button class="login-btn" onclick="saveProfile()" style="margin-bottom: 12px; width: 85%; max-width: 320px;">حفظ التعديلات</button>
        <button class="login-btn" onclick="closeProfileModal()" style="background: #333; width: 85%; max-width: 320px;">إغلاق</button>
    </div>

    <!-- التطبيق الرئيسي -->
    <div class="app-container" id="main-app" style="display: none;">
        <div class="feed">
            <div class="video-card">
                <!-- يمكنك تغيير رابط الفيديو هنا بفيديو حقيقي أو تتركه خلفية -->
                <video src="https://www.w3schools.com/html/mov_bbb.mp4" autoplay loop muted playsinline></video>
                <div class="video-info">
                    <img id="profile-img" src="https://via.placeholder.com/55" class="user-avatar" alt="Avatar">
                    <div>
                        <h3 id="profile-name" style="font-size: 15px; margin-bottom: 3px;">@abdo_official</h3>
                        <p id="welcome-msg" style="font-size: 12px; color: #ddd;">أهلاً بيك يا فنان في التطبيق الجديد! 🚀🔥</p>
                    </div>
                </div>
                <div class="actions">
                    <button class="action-btn" onclick="toggleLike(this)" style="flex-direction: column;"><i class="fas fa-heart"></i></button>
                    <button class="action-btn" style="flex-direction: column;"><i class="fas fa-comment"></i></button>
                    <button class="action-btn" style="flex-direction: column;"><i class="fas fa-share"></i></button>
                </div>
            </div>
        </div>

        <div class="nav-bar">
            <div class="nav-item active"><i class="fas fa-home"></i><span>الرئيسية</span></div>
            <div class="nav-item"><i class="fas fa-compass"></i><span>استكشاف</span></div>
            <div class="nav-item"><i class="fas fa-plus-circle" style="color: #fe2c55; font-size: 28px;"></i></div>
            <div class="nav-item"><i class="fas fa-inbox"></i><span>الوارد</span></div>
            <div class="nav-item" onclick="openProfileModal()"><i class="fas fa-user"></i><span>الملف</span></div>
        </div>
    </div>

    <!-- كود التشغيل والذاكرة الذكية -->
    <script>
        window.onload = function() {
            const savedUser = localStorage.getItem('abdo_tok_user');
            const savedAvatar = localStorage.getItem('abdo_tok_avatar');
            if (savedUser) {
                applyLogin(savedUser, savedAvatar);
            }
        };

        function handleLogin() {
            const inputVal = document.getElementById('username-input').value.trim();
            if (inputVal === "") {
                alert("يا فنان اكتب اسمك الأول عشان تدخل!");
                return;
            }
            localStorage.setItem('abdo_tok_user', inputVal);
            applyLogin(inputVal, null);
        }

        function applyLogin(username, avatar) {
            document.getElementById('auth-modal').style.display = 'none';
            document.getElementById('main-app').style.display = 'flex';

            let userAvatar = avatar || "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=100";
            document.getElementById('profile-img').src = userAvatar;

            if (username === "@abdo_admin") {
                document.getElementById('profile-name').innerHTML = "@abdo_admin <span style='color: #fe2c55; font-size: 11px; background: rgba(254,44,85,0.2); padding: 2px 6px; border-radius: 4px;'>الملك 👑</span>";
                document.getElementById('welcome-msg').innerText = "أهلاً بك يا عبده يا ملك التطبيق! السيطرة معك بالكامل 🚀🔥";
            } else {
                document.getElementById('profile-name').innerText = username;
                document.getElementById('welcome-msg').innerText = "أهلاً بيك يا فنان في التطبيق الرسمي! 🚀🔥";
            }
        }

        function openProfileModal() {
            document.getElementById('profile-modal').style.display = 'flex';
            document.getElementById('edit-name-input').value = localStorage.getItem('abdo_tok_user') || '';
            document.getElementById('edit-avatar-input').value = localStorage.getItem('abdo_tok_avatar') || '';
        }

        function closeProfileModal() {
            document.getElementById('profile-modal').style.display = 'none';
        }

        function saveProfile() {
            const newName = document.getElementById('edit-name-input').value.trim();
            const newAvatar = document.getElementById('edit-avatar-input').value.trim();

            if (newName !== "") {
                localStorage.setItem('abdo_tok_user', newName);
            }
            if (newAvatar !== "") {
                localStorage.setItem('abdo_tok_avatar', newAvatar);
            }

            alert("تم حفظ التعديلات بنجاح يا فنان! 🚀");
            closeProfileModal();
            location.reload();
        }

        function toggleLike(btn) {
            let icon = btn.querySelector('i');
            if (icon.style.color === 'rgb(254, 44, 85)') {
                icon.style.color = '#fff';
            } else {
                icon.style.color = '#fe2c55';
            }
        }
    </script>
</body>
</html>
