<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Abdo Platform</title>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; font-family: sans-serif; }
    body { background-color: #0f0f0f; color: white; }
    
    /* Navbar */
    header { display: flex; justify-content: space-between; align-items: center; padding: 12px 20px; background: #0f0f0f; border-bottom: 1px solid #272727; }
    .logo-container { display: flex; align-items: center; gap: 8px; }
    .logo-icon { background: #ff0000; color: white; width: 32px; height: 32px; border-radius: 8px; font-weight: bold; font-size: 18px; text-align: center; line-height: 32px; }
    .logo-text { color: #ffffff; font-size: 20px; font-weight: bold; }
    .user-profile-bar { display: flex; align-items: center; gap: 10px; }
    .developer-badge { background: linear-gradient(45deg, #ffd700, #ff8c00); color: black; padding: 3px 8px; border-radius: 12px; font-size: 11px; font-weight: bold; display: none; }

    /* Modal / Login Box */
    .modal-bg { position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.85); display: flex; align-items: center; justify-content: center; z-index: 1000; }
    .modal { background: #212121; padding: 25px; border-radius: 12px; width: 90%; max-width: 380px; text-align: center; }
    .modal h3 { margin-bottom: 15px; }
    .modal input { width: 100%; padding: 10px; border-radius: 8px; border: 1px solid #383838; background: #121212; color: white; margin-bottom: 15px; }
    .modal button { background: #ff0000; color: white; border: none; padding: 10px 20px; border-radius: 20px; font-weight: bold; width: 100%; cursor: pointer; }

    /* Ads Section (For Normal Users Only) */
    .ad-banner { background: #282828; color: #e1e1e1; text-align: center; padding: 10px; font-size: 13px; border-bottom: 1px solid #383838; display: block; }

    /* Main Container */
    .container { display: flex; flex-direction: column; padding: 15px; gap: 20px; }
    @media (min-width: 768px) { .container { flex-direction: row; } }
    
    .video-section { flex: 3; }
    .video-player { width: 100%; aspect-ratio: 16/9; background: #000; border-radius: 12px; overflow: hidden; }
    video { width: 100%; height: 100%; }
    .video-title { font-size: 18px; margin: 12px 0 6px 0; }
    .channel-info { display: flex; justify-content: space-between; align-items: center; padding: 10px 0; border-bottom: 1px solid #272727; }
    .sub-btn { background: white; color: black; border: none; padding: 8px 16px; border-radius: 20px; font-weight: bold; }
    .sub-btn.following { background: #383838; color: white; }

    /* Upload Section */
    .upload-box { background: #181818; padding: 15px; border-radius: 10px; margin-top: 15px; border: 1px dashed #383838; }
    .upload-box input { display: block; margin: 10px 0; color: white; }

    /* Developer Control Panel */
    .dev-panel { background: #211c00; border: 1px solid #ffd700; padding: 15px; border-radius: 10px; margin-top: 15px; display: none; }

    .recommendations { flex: 1; display: flex; flex-direction: column; gap: 12px; }
    .card { display: flex; gap: 10px; }
    .thumbnail { width: 120px; height: 70px; background: #272727; border-radius: 8px; }
  </style>
</head>
<body>

  <!-- شريط إعلانات للمستخدمين العاديين -->
  <div class="ad-banner" id="adBanner">
    📢 إعلان: اشترك في الباقة الممتازة لإزالة الإعلانات ومشاهدة الفيديوهات بدون انقطاع!
  </div>

  <!-- نافذة تسجيل الدخول -->
  <div class="modal-bg" id="loginModal">
    <div class="modal">
      <h3>مرحباً بك في منصة Abdo! 🚀</h3>
      <p style="font-size:13px; color:#aaa; margin-bottom:15px;">ادخل اسم المستخدم للدخول</p>
      <input type="text" id="usernameInput" placeholder="اسم المستخدم (اكتب Abpo للمطور)...">
      <button onclick="registerUser()">تسجيل الدخول</button>
    </div>
  </div>

  <!-- الشريط العلوي -->
  <header>
    <div class="logo-container">
      <div class="logo-icon">A</div>
      <div class="logo-text">Abdo</div>
    </div>
    <div class="user-profile-bar">
      <span class="developer-badge" id="devBadge">👑 المطور VIP</span>
      <span id="userDisplayName" style="color:#aaa; font-size:14px;"></span>
      <span style="font-size: 20px;">👤</span>
    </div>
  </header>

  <!-- المحتوى الرئيسي -->
  <div class="container">
    
    <div class="video-section">
      <div class="video-player">
        <video controls id="mainVideoPlayer">
          <source src="https://www.w3schools.com/html/mov_bbb.mp4" type="video/mp4">
        </video>
      </div>
      <h2 class="video-title">الفيديو الرسمي لـ Abdo! 🎉</h2>
      
      <!-- قناة Abdo -->
      <div class="channel-info">
        <div>
          <strong>قناة Abdo الرسمية</strong>
          <p style="font-size:12px; color:#aaa;"><span id="subCount">100000</span> مشترك</p>
        </div>
        <button class="sub-btn" id="subBtn">إشتراك</button>
      </div>

      <!-- لوحة التحكم خاصة بالمطور فقط -->
      <div class="dev-panel" id="devPanel">
        <h4 style="color:#ffd700;">⚙️ لوحة تحكم المطور (Abpo)</h4>
        <p style="font-size:12px; color:#ccc; margin-top:5px;">أهلاً بك يا رئيس المنصة! لديك كافة الصلاحيات بدون إعلانات وبسرعة عالية.</p>
      </div>

      <!-- قسم رفع فيديو جديد -->
      <div class="upload-box">
        <h4>📤 رفع فيديو جديد</h4>
        <input type="text" id="videoTitleInput" placeholder="عنوان الفيديو...">
        <input type="file" id="videoFileInput" accept="video/*">
        <button onclick="uploadVideo()" style="background:#ff0000; color:white; border:none; padding:8px 15px; border-radius:8px; font-weight:bold; cursor:pointer;">نشر الفيديو</button>
      </div>
    </div>

    <!-- المقترحات -->
    <div class="recommendations">
      <h3>فيديوهات مقترحة</h3>
      <div class="card"><div class="thumbnail"></div><div><h4>فيديو 1</h4><p>Abdo Channel</p></div></div>
      <div class="card"><div class="thumbnail"></div><div><h4>فيديو 2</h4><p>Abdo Channel</p></div></div>
    </div>

  </div>

  <script>
    let currentSubs = 100000;

    function registerUser() {
      const name = document.getElementById('usernameInput').value.trim();
      if(name === '') {
        alert('من فضلك اكتب اسمك أولاً');
        return;
      }
      
      document.getElementById('loginModal').style.display = 'none';

      // التحقق هل الحساب هو حساب المطور Abpo أم ضيف عادي
      if (name.toLowerCase() === 'abpo') {
        // ميزات المطور Abpo
        document.getElementById('userDisplayName').innerText = "المطور: Abpo";
        document.getElementById('devBadge').style.display = 'inline-block';
        document.getElementById('devPanel').style.display = 'block';
        
        // **إلغاء الإعلانات تماماً للمطور**
        document.getElementById('adBanner').style.display = 'none';
        
        alert('أهلاً بك يا مطور المنصة (Abpo)! تم تفعيل كافة المميزات الخاصة بدون إعلانات 👑');
      } else {
        // حساب ضيف/مستخدم عادي
        document.getElementById('userDisplayName').innerText = "قناة: " + name;

        // المتابعة التلقائية الإجبارية للضيف لقناة Abdo
        currentSubs += 1;
        document.getElementById('subCount').innerText = currentSubs.toLocaleString();
        const subBtn = document.getElementById('subBtn');
        subBtn.innerText = "تمت المتابعة ✓";
        subBtn.classList.add('following');
        
        alert('تم إنشاء حسابك بنجاح! وتم إضافة متابعة تلقائية لقناة Abdo الرسمية 🎉');
      }
    }

    function uploadVideo() {
      const fileInput = document.getElementById('videoFileInput');
      const titleInput = document.getElementById('videoTitleInput');
      
      if(fileInput.files.length === 0 || titleInput.value === '') {
        alert('من فضلك اختر فيديو واكتب عنوانه');
        return;
      }

      const file = fileInput.files[0];
      const videoURL = URL.createObjectURL(file);
      
      const player = document.getElementById('mainVideoPlayer');
      player.src = videoURL;
      player.play();
      
      document.querySelector('.video-title').innerText = titleInput.value;
      alert('تم نشر الفيديو بنجاح! 🚀');
    }
  </script>

</body>
</html>
