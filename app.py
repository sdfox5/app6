from flask import Flask, request, jsonify
import httpx
import time
import concurrent.futures
from threading import Thread
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

app = Flask(__name__)

# دالة لتشفير المعرف
def Encrypt_ID(x):
    x = int(x)
    dec = ['80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '8a', '8b', '8c', '8d', '8e', '8f', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '9a', '9b', '9c', '9d', '9e', '9f', 'a0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'aa', 'ab', 'ac', 'ad', 'ae', 'af', 'b0', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9', 'ba', 'bb', 'bc', 'bd', 'be', 'bf', 'c0', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'ca', 'cb', 'cc', 'cd', 'ce', 'cf', 'd0', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'da', 'db', 'dc', 'dd', 'de', 'df', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 'ea', 'eb', 'ec', 'ed', 'ee', 'ef', 'f0', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'fa', 'fb', 'fc', 'fd', 'fe', 'ff']
    xxx = ['1', '01', '02', '03', '04', '05', '06', '07', '08', '09', '0a', '0b', '0c', '0d', '0e', '0f', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '1a', '1b', '1c', '1d', '1e', '1f', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '2a', '2b', '2c', '2d', '2e', '2f', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '3a', '3b', '3c', '3d', '3e', '3f', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '4a', '4b', '4c', '4d', '4e', '4f', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '5a', '5b', '5c', '5d', '5e', '5f', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '6a', '6b', '6c', '6d', '6e', '6f', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '7a', '7b', '7c', '7d', '7e', '7f']
    x = x / 128
    if x > 128:
        x = x / 128
        if x > 128:
            x = x / 128
            if x > 128:
                x = x / 128
                strx = int(x)
                y = (x - int(strx)) * 128
                stry = str(int(y))
                z = (y - int(stry)) * 128
                strz = str(int(z))
                n = (z - int(strz)) * 128
                strn = str(int(n))
                m = (n - int(strn)) * 128
                return dec[int(m)] + dec[int(n)] + dec[int(z)] + dec[int(y)] + xxx[int(x)]
            else:
                strx = int(x)
                y = (x - int(strx)) * 128
                stry = str(int(y))
                z = (y - int(stry)) * 128
                strz = str(int(z))
                n = (z - int(strz)) * 128
                strn = str(int(n))
                return dec[int(n)] + dec[int(z)] + dec[int(y)] + xxx[int(x)]

# دالة لتشفير البيانات باستخدام AES
def encrypt_api(plain_text):
    plain_text = bytes.fromhex(plain_text)
    key = bytes([89, 103, 38, 116, 99, 37, 68, 69, 117, 104, 54, 37, 90, 99, 94, 56])
    iv = bytes([54, 111, 121, 90, 68, 114, 50, 50, 69, 51, 121, 99, 104, 106, 77, 37])
    cipher = AES.new(key, AES.MODE_CBC, iv)
    cipher_text = cipher.encrypt(pad(plain_text, AES.block_size))
    return cipher_text.hex()

# متغير عام لتخزين توكن JWT
jwt_token = None

# دالة للحصول على توكن JWT
def get_jwt_token():
    global jwt_token
    url = "https://app-py-amber.vercel.app/get?uid=3742282075&password=B8B4818D83BAAFBA62FEA1447285A5246AD3DFFB5A8D3FC08CC1E3FB4D9BE534"
    try:
        response = httpx.get(url)
        if response.status_code == 200:
            data = response.json()
            if data['status'] == 'success':
                jwt_token = data['token']
                print("JWT Token updated successfully.")
            else:
                print("Failed to get JWT token: Status is not success.")
        else:
            print(f"Failed to get JWT token: HTTP {response.status_code}")
    except httpx.RequestError as e:
        print(f"Request error: {e}")

# دالة لتحديث التوكن كل 8 ساعات
def token_updater():
    while True:
        get_jwt_token()
        time.sleep(8 * 3600)  # 8 ساعات بالثواني

# بدء تحديث التوكن في خيط منفصل
token_thread = Thread(target=token_updater, daemon=True)
token_thread.start()

# دالة لإرسال طلب إلى الخادم
def get_player_information(player_id):
    encrypted_id = Encrypt_ID(player_id)
    encrypted_api = encrypt_api(f"08{encrypted_id}1007")
    target = bytes.fromhex(encrypted_api)
    url = "https://clientbp.common.ggbluefox.com/GetPlayerPersonalShow"
    headers = {
        "Authorization": f"Bearer {jwt_token}",
        "X-Unity-Version": "2018.4.11f1",
        "X-GA": "v1 1",
        "ReleaseVersion": "OB47",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 9; SM-N975F Build/PI)",
        "Host": "clientbp.common.ggbluefox.com",
        "Connection": "close",
        "Accept-Encoding": "gzip, deflate, br",
    }
    try:
        with httpx.Client(verify=False) as client:
            response = client.post(url, headers=headers, data=target)
        if response.status_code == 200:
            return f"Visit {player_id} GOOD ✅"
        else:
            pass
    except httpx.RequestError as e:
        return f"Visit {player_id} Request error: {e}"
@app.route('/visit', methods=['GET'])
def start_requests():
    uid = request.args.get('uid')
    if not uid:
        return jsonify({"status": "error", "message": "UID is required"}), 400

    # إنشاء قائمة تحتوي على نفس المعرف 1000 مرة
    player_ids = [int(uid)]
    results = []

    # إرسال 1000 طلب باستخدام ThreadPoolExecutor
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
        future_to_player_id = {executor.submit(get_player_information, player_id): player_id for player_id in player_ids}
        for future in concurrent.futures.as_completed(future_to_player_id):
            try:
                result = future.result()
                results.append(result)
                print(result)  # طباعة النتيجة في الكونسول
            except Exception as e:
                results.append(f"Exception: {e}")

    return jsonify({
        "status": "success",
        "message": "1 requests sent successfully",
        "results": results  # إضافة النتائج إلى الرد
    })

if __name__ == '__main__':
    # الحصول على التوكن فور بدء التشغيل
    get_jwt_token()
    app.run(host='0.0.0.0', port=5000)
