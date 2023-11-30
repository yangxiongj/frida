import frida, sys

# 码农doFinal参数打印出来的参数为不可见时可将打印类型替换为bytesToBase64
# 打印不出doFinal data参数时将参数替换为toBase64

# 码农星期八大佬通杀
j1 = """
var N_ENCRYPT_MODE = 1
var N_DECRYPT_MODE = 2
function showStacks() {
    var Exception = Java.use("java.lang.Exception");
    var ins = Exception.$new("Exception");
    var straces = ins.getStackTrace();
    if (undefined == straces || null == straces) {
        return;
    }
    send("============================= Stack strat=======================");
    send("");
    for (var i = 0; i < straces.length; i++) {
        var str = "   " + straces[i].toString();
        send(str);
    }
    send("");
    Exception.$dispose();
}
//工具相关函数
var base64EncodeChars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/',
    base64DecodeChars = new Array((-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), (-1), 62, (-1), (-1), (-1), 63, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, (-1), (-1), (-1), (-1), (-1), (-1), (-1), 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, (-1), (-1), (-1), (-1), (-1), (-1), 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, (-1), (-1), (-1), (-1), (-1));
function stringToBase64(e) {
    var r, a, c, h, o, t;
    for (c = e.length, a = 0, r = ''; a < c;) {
        if (h = 255 & e.charCodeAt(a++), a == c) {
            r += base64EncodeChars.charAt(h >> 2),
                r += base64EncodeChars.charAt((3 & h) << 4),
                r += '==';
            break
        }
        if (o = e.charCodeAt(a++), a == c) {
            r += base64EncodeChars.charAt(h >> 2),
                r += base64EncodeChars.charAt((3 & h) << 4 | (240 & o) >> 4),
                r += base64EncodeChars.charAt((15 & o) << 2),
                r += '=';
            break
        }
        t = e.charCodeAt(a++),
            r += base64EncodeChars.charAt(h >> 2),
            r += base64EncodeChars.charAt((3 & h) << 4 | (240 & o) >> 4),
            r += base64EncodeChars.charAt((15 & o) << 2 | (192 & t) >> 6),
            r += base64EncodeChars.charAt(63 & t)
    }
    return r
}
function base64ToString(e) {
    var r, a, c, h, o, t, d;
    for (t = e.length, o = 0, d = ''; o < t;) {
        do
            r = base64DecodeChars[255 & e.charCodeAt(o++)];
        while (o < t && r == -1);
        if (r == -1)
            break;
        do
            a = base64DecodeChars[255 & e.charCodeAt(o++)];
        while (o < t && a == -1);
        if (a == -1)
            break;
        d += String.fromCharCode(r << 2 | (48 & a) >> 4);
        do {
            if (c = 255 & e.charCodeAt(o++), 61 == c)
                return d;
            c = base64DecodeChars[c]
        } while (o < t && c == -1);
        if (c == -1)
            break;
        d += String.fromCharCode((15 & a) << 4 | (60 & c) >> 2);
        do {
            if (h = 255 & e.charCodeAt(o++), 61 == h)
                return d;
            h = base64DecodeChars[h]
        } while (o < t && h == -1);
        if (h == -1)
            break;
        d += String.fromCharCode((3 & c) << 6 | h)
    }
    return d
}
function hexToBase64(str) {
    return base64Encode(String.fromCharCode.apply(null, str.replace(/([\da-fA-F]{2}) ?/g, "0x$1 ").replace(/ +$/, "").split(" ")));
}
function base64ToHex(str) {
    for (var i = 0, bin = base64Decode(str), hex = []; i < bin.length; ++i) {
        var tmp = bin.charCodeAt(i).toString(16);
        if (tmp.length === 1)
            tmp = "0" + tmp;
        hex[hex.length] = tmp;
    }
    return hex.join("");
}
function hexToBytes(str) {
    var pos = 0;
    var len = str.length;
    if (len % 2 != 0) {
        return null;
    }
    len /= 2;
    var hexA = new Array();
    for (var i = 0; i < len; i++) {
        var s = str.substr(pos, 2);
        var v = parseInt(s, 16);
        hexA.push(v);
        pos += 2;
    }
    return hexA;
}
function bytesToHex(arr) {
    var str = '';
    var k, j;
    for (var i = 0; i < arr.length; i++) {
        k = arr[i];
        j = k;
        if (k < 0) {
            j = k + 256;
        }
        if (j < 16) {
            str += "0";
        }
        str += j.toString(16);
    }
    return str;
}
function stringToHex(str) {
    var val = "";
    for (var i = 0; i < str.length; i++) {
        if (val == "")
            val = str.charCodeAt(i).toString(16);
        else
            val += str.charCodeAt(i).toString(16);
    }
    return val
}
function stringToBytes(str) {
    var ch, st, re = [];
    for (var i = 0; i < str.length; i++) {
        ch = str.charCodeAt(i);
        st = [];
        do {
            st.push(ch & 0xFF);
            ch = ch >> 8;
        }
        while (ch);
        re = re.concat(st.reverse());
    }
    return re;
}
//将byte[]转成String的方法
function bytesToString(arr) {
    var str = '';
    arr = new Uint8Array(arr);
    for (var i in arr) {
        str += String.fromCharCode(arr[i]);
    }
    return str;
}
function bytesToBase64(e) {
    var r, a, c, h, o, t;
    for (c = e.length, a = 0, r = ''; a < c;) {
        if (h = 255 & e[a++], a == c) {
            r += base64EncodeChars.charAt(h >> 2),
                r += base64EncodeChars.charAt((3 & h) << 4),
                r += '==';
            break
        }
        if (o = e[a++], a == c) {
            r += base64EncodeChars.charAt(h >> 2),
                r += base64EncodeChars.charAt((3 & h) << 4 | (240 & o) >> 4),
                r += base64EncodeChars.charAt((15 & o) << 2),
                r += '=';
            break
        }
        t = e[a++],
            r += base64EncodeChars.charAt(h >> 2),
            r += base64EncodeChars.charAt((3 & h) << 4 | (240 & o) >> 4),
            r += base64EncodeChars.charAt((15 & o) << 2 | (192 & t) >> 6),
            r += base64EncodeChars.charAt(63 & t)
    }
    return r
}
function base64ToBytes(e) {
    var r, a, c, h, o, t, d;
    for (t = e.length, o = 0, d = []; o < t;) {
        do
            r = base64DecodeChars[255 & e.charCodeAt(o++)];
        while (o < t && r == -1);
        if (r == -1)
            break;
        do
            a = base64DecodeChars[255 & e.charCodeAt(o++)];
        while (o < t && a == -1);
        if (a == -1)
            break;
        d.push(r << 2 | (48 & a) >> 4);
        do {
            if (c = 255 & e.charCodeAt(o++), 61 == c)
                return d;
            c = base64DecodeChars[c]
        } while (o < t && c == -1);
        if (c == -1)
            break;
        d.push((15 & a) << 4 | (60 & c) >> 2);
        do {
            if (h = 255 & e.charCodeAt(o++), 61 == h)
                return d;
            h = base64DecodeChars[h]
        } while (o < t && h == -1);
        if (h == -1)
            break;
        d.push((3 & c) << 6 | h)
    }
    return d
}
//stringToBase64 stringToHex stringToBytes
//base64ToString base64ToHex base64ToBytes
//               hexToBase64  hexToBytes    
// bytesToBase64 bytesToHex bytesToString
Java.perform(function () {
    var secretKeySpec = Java.use('javax.crypto.spec.SecretKeySpec');
    secretKeySpec.$init.overload('[B', 'java.lang.String').implementation = function (a, b) {
        showStacks();
        var result = this.$init(a, b);
        send("======================================");
        send("算法名：" + b + "|str密钥:" + bytesToString(a));
        send("算法名：" + b + "|Hex密钥:" + bytesToHex(a));
        return result;
    }
    var DESKeySpec = Java.use('javax.crypto.spec.DESKeySpec');
    DESKeySpec.$init.overload('[B').implementation = function (a) {
        showStacks();
        var result = this.$init(a);
        send("======================================");
        var bytes_key_des = this.getKey();
        send("des密钥  |str " + bytesToString(bytes_key_des));
        send("des密钥  |hex " + bytesToHex(bytes_key_des));
        return result;
    }
    DESKeySpec.$init.overload('[B', 'int').implementation = function (a, b) {
        showStacks();
        var result = this.$init(a, b);
        send("======================================");
        var bytes_key_des = this.getKey();
        send("des密钥  |str " + bytesToString(bytes_key_des));
        send("des密钥  |hex " + bytesToHex(bytes_key_des));
        return result;
    }
    var mac = Java.use('javax.crypto.Mac');
    mac.getInstance.overload('java.lang.String').implementation = function (a) {
        showStacks();
        var result = this.getInstance(a);
        send("======================================");
        send("算法名：" + a);
        return result;
    }
    mac.update.overload('[B').implementation = function (a) {
        //showStacks();
        this.update(a);
        send("======================================");
        send("update:" + bytesToString(a))
    }
    mac.update.overload('[B', 'int', 'int').implementation = function (a, b, c) {
        //showStacks();
        this.update(a, b, c)
        send("======================================");
        send("update:" + bytesToString(a) + "|" + b + "|" + c);
    }
    mac.doFinal.overload().implementation = function () {
        //showStacks();
        var result = this.doFinal();
        send("======================================");
        send("doFinal结果: |str  :"     + bytesToString(result));
        send("doFinal结果: |hex  :"     + bytesToHex(result));
        send("doFinal结果: |base64  :"  + bytesToBase64(result));
        return result;
    }
    mac.doFinal.overload('[B').implementation = function (a) {
        //showStacks();
        var result = this.doFinal(a);
        send("======================================");
        send("doFinal参数: |str  :"     + bytesToString(a));
        send("doFinal结果: |str  :"     + bytesToString(result));
        send("doFinal结果: |hex  :"     + bytesToHex(result));
        send("doFinal结果: |base64  :"  + bytesToBase64(result));
        return result;
    }
    var md = Java.use('java.security.MessageDigest');
    md.getInstance.overload('java.lang.String', 'java.lang.String').implementation = function (a, b) {
        //showStacks();
        send("======================================");
        send("算法名：" + a);
        return this.getInstance(a, b);
    }
    md.getInstance.overload('java.lang.String').implementation = function (a) {
        //showStacks();
        send("======================================");
        send("算法名：" + a);
        return this.getInstance(a);
    }
    md.update.overload('[B').implementation = function (a) {
        //showStacks();
        send("======================================");
        send("update:" + bytesToString(a))
        return this.update(a);
    }
    md.update.overload('[B', 'int', 'int').implementation = function (a, b, c) {
        //showStacks();
        send("======================================");
        send("update:" + bytesToString(a) + "|" + b + "|" + c);
        return this.update(a, b, c);
    }
    md.digest.overload().implementation = function () {
        //showStacks();
        send("======================================");
        var result = this.digest();
        send("digest结果:" + bytesToHex(result));
        send("digest结果:" + bytesToBase64(result));
        return result;
    }
    md.digest.overload('[B').implementation = function (a) {
        //showStacks();
        send("======================================");
        send("digest参数:" + bytesToString(a));
        var result = this.digest(a);
        send("digest结果:" + bytesToHex(result));
        send("digest结果:" + bytesToBase64(result));
        return result;
    }
    var ivParameterSpec = Java.use('javax.crypto.spec.IvParameterSpec');
    ivParameterSpec.$init.overload('[B').implementation = function (a) {
        //showStacks();
        var result = this.$init(a);
        send("======================================");
        send("iv向量: |str:" + bytesToString(a));
        send("iv向量: |hex:" + bytesToHex(a));
        return result;
    }
    var cipher = Java.use('javax.crypto.Cipher');
    cipher.getInstance.overload('java.lang.String').implementation = function (a) {
        //showStacks();
        var result = this.getInstance(a);
        send("======================================");
        send("模式填充:" + a);
        return result;
    }
    cipher.init.overload('int', 'java.security.Key').implementation = function (a, b) {
        //showStacks();
        var result = this.init(a, b);
        send("======================================");
        if (N_ENCRYPT_MODE == a)
        {
            send("init  | 加密模式");    
        }
        else if(N_DECRYPT_MODE == a)
        {
            send("init  | 解密模式");    
        }
        var bytes_key = b.getEncoded();
        send("init key:" + "|str密钥:" + bytesToString(bytes_key));
        send("init key:" + "|Hex密钥:" + bytesToHex(bytes_key));
        return result;
    }
    cipher.init.overload('int', 'java.security.cert.Certificate').implementation = function (a, b) {
        //showStacks();
        var result = this.init(a, b);
        send("======================================");
        if (N_ENCRYPT_MODE == a)
        {
            send("init  | 加密模式");    
        }
        else if(N_DECRYPT_MODE == a)
        {
            send("init  | 解密模式");    
        }
        return result;
    }
    cipher.init.overload('int', 'java.security.Key', 'java.security.spec.AlgorithmParameterSpec').implementation = function (a, b, c) {
        //showStacks();
        var result = this.init(a, b, c);
        send("======================================");
        if (N_ENCRYPT_MODE == a)
        {
            send("init  | 加密模式");    
        }
        else if(N_DECRYPT_MODE == a)
        {
            send("init  | 解密模式");    
        }
        var bytes_key = b.getEncoded();
        send("init key:" + "|str密钥:" + bytesToString(bytes_key));
        send("init key:" + "|Hex密钥:" + bytesToHex(bytes_key));
        return result;
    }
    cipher.init.overload('int', 'java.security.cert.Certificate', 'java.security.SecureRandom').implementation = function (a, b, c) {
        //showStacks();
        var result = this.init(a, b, c);
        if (N_ENCRYPT_MODE == a)
        {
            send("init  | 加密模式");    
        }
        else if(N_DECRYPT_MODE == a)
        {
            send("init  | 解密模式");    
        }
        return result;
    }
    cipher.init.overload('int', 'java.security.Key', 'java.security.SecureRandom').implementation = function (a, b, c) {
        //showStacks();
        var result = this.init(a, b, c);
        if (N_ENCRYPT_MODE == a)
        {
            send("init  | 加密模式");    
        }
        else if(N_DECRYPT_MODE == a)
        {
            send("init  | 解密模式");    
        }
         var bytes_key = b.getEncoded();
        send("init key:" + "|str密钥:" + bytesToString(bytes_key));
        send("init key:" + "|Hex密钥:" + bytesToHex(bytes_key));
        return result;
    }
    cipher.init.overload('int', 'java.security.Key', 'java.security.AlgorithmParameters').implementation = function (a, b, c) {
        //showStacks();
        var result = this.init(a, b, c);
        if (N_ENCRYPT_MODE == a)
        {
            send("init  | 加密模式");    
        }
        else if(N_DECRYPT_MODE == a)
        {
            send("init  | 解密模式");    
        }
        var bytes_key = b.getEncoded();
        send("init key:" + "|str密钥:" + bytesToString(bytes_key));
        send("init key:" + "|Hex密钥:" + bytesToHex(bytes_key));
        return result;
    }
    cipher.init.overload('int', 'java.security.Key', 'java.security.AlgorithmParameters', 'java.security.SecureRandom').implementation = function (a, b, c, d) {
        //showStacks();
        var result = this.init(a, b, c, d);
        if (N_ENCRYPT_MODE == a)
        {
            send("init  | 加密模式");    
        }
        else if(N_DECRYPT_MODE == a)
        {
            send("init  | 解密模式");    
        }
        var bytes_key = b.getEncoded();
        send("init key:" + "|str密钥:" + bytesToString(bytes_key));
        send("init key:" + "|Hex密钥:" + bytesToHex(bytes_key));
        return result;
    }
    cipher.init.overload('int', 'java.security.Key', 'java.security.spec.AlgorithmParameterSpec', 'java.security.SecureRandom').implementation = function (a, b, c, d) {
        //showStacks();
        var result = this.update(a, b, c, d);
        if (N_ENCRYPT_MODE == a)
        {
            send("init  | 加密模式");    
        }
        else if(N_DECRYPT_MODE == a)
        {
            send("init  | 解密模式");    
        }
         var bytes_key = b.getEncoded();
        send("init key:" + "|str密钥:" + bytesToString(bytes_key));
        send("init key:" + "|Hex密钥:" + bytesToHex(bytes_key));
        return result;
    }
    cipher.update.overload('[B').implementation = function (a) {
        //showStacks();
        var result = this.update(a);
        send("======================================");
        send("update:" + bytesToString(a));
        return result;
    }
    cipher.update.overload('[B', 'int', 'int').implementation = function (a, b, c) {
        //showStacks();
        var result = this.update(a, b, c);
        send("======================================");
        send("update:" + bytesToString(a) + "|" + b + "|" + c);
        return result;
    }
    cipher.doFinal.overload().implementation = function () {
        //showStacks();
        var result = this.doFinal();
        send("======================================");
        send("doFinal结果: |str  :"     + bytesToString(result));
        send("doFinal结果: |hex  :"     + bytesToHex(result));
        send("doFinal结果: |base64  :"  + bytesToBase64(result));
        return result;
    }
    cipher.doFinal.overload('[B').implementation = function (a) {
        //showStacks();
        var result = this.doFinal(a);
        send("======================================");
        send("doFinal参数: |str  :"     + bytesToBase64(a));
        send("doFinal结果: |str  :"     + bytesToString(result));
        send("doFinal结果: |hex  :"     + bytesToHex(result));
        send("doFinal结果: |base64  :"  + bytesToBase64(result));
        return result;
    }
    var x509EncodedKeySpec = Java.use('java.security.spec.X509EncodedKeySpec');
    x509EncodedKeySpec.$init.overload('[B').implementation = function (a) {
        //showStacks();
        var result = this.$init(a);
        send("======================================");
        send("RSA密钥:" + bytesToBase64(a));
        return result;
    }
    var rSAPublicKeySpec = Java.use('java.security.spec.RSAPublicKeySpec');
    rSAPublicKeySpec.$init.overload('java.math.BigInteger', 'java.math.BigInteger').implementation = function (a, b) {
        //showStacks();
        var result = this.$init(a, b);
        send("======================================");
        //send("RSA密钥:" + bytesToBase64(a));
        send("RSA密钥N:" + a.toString(16));
        send("RSA密钥E:" + b.toString(16));
        return result;
    }
    var KeyPairGenerator = Java.use('java.security.KeyPairGenerator');
    KeyPairGenerator.generateKeyPair.implementation = function ()
    {
        //showStacks();
        var result = this.generateKeyPair();
        send("======================================");
        var str_private = result.getPrivate().getEncoded();
        var str_public = result.getPublic().getEncoded();
        send("公钥  |hex" + bytesToHex(str_public));
        send("私钥  |hex" + bytesToHex(str_private));
        return result;
    }
    KeyPairGenerator.genKeyPair.implementation = function ()
    {
        //showStacks();
        var result = this.genKeyPair();
        send("======================================");
        var str_private = result.getPrivate().getEncoded();
        var str_public = result.getPublic().getEncoded();
        send("公钥  |hex" + bytesToHex(str_public));
        send("私钥  |hex" + bytesToHex(str_private));
        return result;
    }
});
"""

j2 = """
//打印堆栈
function showStacks() {
    send(
        Java.use("android.util.Log")
            .getStackTraceString(
                Java.use("java.lang.Throwable").$new()
            )
    );
}
var ByteString = Java.use("com.android.okhttp.okio.ByteString");
//输出base64格式数据
function toBase64(tag, data) {
    send(tag + " Base64: ", ByteString.of(data).base64());
}
//输出hex格式数据
function toHex(tag, data) {
    send(tag + " Hex: ", ByteString.of(data).hex());
}
//输出10格式数据
function toUtf8(tag, data) {
    send(tag + " Utf8: ", ByteString.of(data).utf8());
}
var messageDigest = Java.use("java.security.MessageDigest");
messageDigest.update.overload('byte').implementation = function (data) {
    send("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓");
    send("MessageDigest.update('byte') is called!");
    showStacks();
    send("↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑");
    return this.update(data);
}
messageDigest.update.overload('java.nio.ByteBuffer').implementation = function (data) {
    send("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓");
    send("MessageDigest.update('java.nio.ByteBuffer') is called!");
    showStacks();
    send("↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑");
    return this.update(data);
}
messageDigest.update.overload('[B').implementation = function (data) {
    send("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓");
    send("MessageDigest.update('[B') is called!");
    var algorithm = this.getAlgorithm();
    var tag = algorithm + " update data";
    toUtf8(tag, data);
    toHex(tag, data);
    toBase64(tag, data);
    send("↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑");
    return this.update(data);
}
messageDigest.update.overload('[B', 'int', 'int').implementation = function (data, start, length) {
    send("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓");
    send("MessageDigest.update('[B', 'int', 'int') is called!");
    var algorithm = this.getAlgorithm();
    var tag = algorithm + " update data";
    toUtf8(tag, data);
    toHex(tag, data);
    toBase64(tag, data);
    send("start:", start);
    send("length:", length);
    showStacks();
    send("↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑");
    return this.update(data, start, length);
}
messageDigest.digest.overload().implementation = function () {
    send("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓");
    send("MessageDigest.digest() is called!");
    var result = this.digest();
    var algorithm = this.getAlgorithm();
    var tag = algorithm + " digest result";
    toHex(tag, result);
    toBase64(tag, result);
    showStacks();
    send("↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑");
    return result;
}
messageDigest.digest.overload('[B').implementation = function (data) {
    send("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓");
    send("MessageDigest.digest('[B') is called!");
    var algorithm = this.getAlgorithm();
    var tag = algorithm + " digest data";
    toUtf8(tag, data);
    toHex(tag, data);
    toBase64(tag, data);
    var result = this.digest(data);
    var tags = algorithm + " digest result";
    toHex(tags, result);
    toBase64(tags, result);
    showStacks();
    send("↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑");
    return result;
}
messageDigest.digest.overload('[B', 'int', 'int').implementation = function (data, start, length) {
    send("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓");
    send("MessageDigest.digest('[B', 'int', 'int') is called!");
    var algorithm = this.getAlgorithm();
    var tag = algorithm + " digest data";
    toUtf8(tag, data);
    toHex(tag, data);
    toBase64(tag, data);
    var result = this.digest(data, start, length);
    var tags = algorithm + " digest result";
    toHex(tags, result);
    toBase64(tags, result);
    send("start:", start);
    send("length:", length);
    showStacks();
    send("↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑");
    return result;
}
var mac = Java.use("javax.crypto.Mac");
mac.init.overload('java.security.Key', 'java.security.spec.AlgorithmParameterSpec').implementation = function (key, AlgorithmParameterSpec) {
    send("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓");
    send("Mac.init('java.security.Key', 'java.security.spec.AlgorithmParameterSpec') is called!");
    showStacks();
    send("↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑");
    return this.init(key, AlgorithmParameterSpec);
}
mac.init.overload('java.security.Key').implementation = function (key) {
    send("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓");
    send("Mac.init('java.security.Key') is called!");
    var algorithm = this.getAlgorithm();
    var tag = algorithm + " init Key";
    var keyBytes = key.getEncoded();
    toUtf8(tag, keyBytes);
    toHex(tag, keyBytes);
    toBase64(tag, keyBytes);
    showStacks();
    send("↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑");
    return this.init(key);
}
mac.update.overload('byte').implementation = function (data) {
    send("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓");
    send("Mac.update('byte') is called!");
    showStacks();
    send("↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑");
    return this.update(data);
}
mac.update.overload('java.nio.ByteBuffer').implementation = function (data) {
    send("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓");
    send("Mac.update('java.nio.ByteBuffer') is called!");
    showStacks();
    send("↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑");
    return this.update(data);
}
mac.update.overload('[B').implementation = function (data) {
    send("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓");
    send("Mac.update('[B') is called!");
    var algorithm = this.getAlgorithm();
    var tag = algorithm + " update data";
    toUtf8(tag, data);
    toHex(tag, data);
    toBase64(tag, data);
    showStacks();
    send("↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑");
    return this.update(data);
}
mac.update.overload('[B', 'int', 'int').implementation = function (data, start, length) {
    send("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓");
    send("Mac.update('[B', 'int', 'int') is called!");
    var algorithm = this.getAlgorithm();
    var tag = algorithm + " update data";
    toUtf8(tag, data);
    toHex(tag, data);
    toBase64(tag, data);
    send("start:", start);
    send("length:", length);
    showStacks();
    send("↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑");
    return this.update(data, start, length);
}
mac.doFinal.overload().implementation = function () {
    send("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓");
    send("Mac.doFinal() is called!");
    var result = this.doFinal();
    var algorithm = this.getAlgorithm();
    var tag = algorithm + " doFinal result";
    toHex(tag, result);
    toBase64(tag, result);
    showStacks();
    send("↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑");
    return result;
}
// DES/DESede/AES/RSA
var cipher = Java.use("javax.crypto.Cipher");
cipher.init.overload('int', 'java.security.cert.Certificate').implementation = function () {
    send("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓");
    send("Cipher.init('int', 'java.security.cert.Certificate') is called!");
    showStacks();
    send("↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑");
    return this.init.apply(this, arguments);
}
cipher.init.overload('int', 'java.security.Key', 'java.security.SecureRandom').implementation = function () {
    send("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓");
    send("Cipher.init('int', 'java.security.Key', 'java.security.SecureRandom') is called!");
    showStacks();
    send("↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑");
    return this.init.apply(this, arguments);
}
cipher.init.overload('int', 'java.security.cert.Certificate', 'java.security.SecureRandom').implementation = function () {
    send("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓");
    send("Cipher.init('int', 'java.security.cert.Certificate', 'java.security.SecureRandom') is called!");
    showStacks();
    send("↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑");
    return this.init.apply(this, arguments);
}
cipher.init.overload('int', 'java.security.Key', 'java.security.AlgorithmParameters', 'java.security.SecureRandom').implementation = function () {
    send("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓");
    send("Cipher.init('int', 'java.security.Key', 'java.security.AlgorithmParameters', 'java.security.SecureRandom') is called!");
    showStacks();
    send("↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑");
    return this.init.apply(this, arguments);
}
cipher.init.overload('int', 'java.security.Key', 'java.security.spec.AlgorithmParameterSpec', 'java.security.SecureRandom').implementation = function () {
    send("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓");
    send("Cipher.init('int', 'java.security.Key', 'java.security.spec.AlgorithmParameterSpec', 'java.security.SecureRandom') is called!");
    showStacks();
    send("↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑");
    return this.init.apply(this, arguments);
}
cipher.init.overload('int', 'java.security.Key', 'java.security.AlgorithmParameters').implementation = function () {
    send("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓");
    send("Cipher.init('int', 'java.security.Key', 'java.security.AlgorithmParameters') is called!");
    showStacks();
    send("↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑");
    return this.init.apply(this, arguments);
}
cipher.init.overload('int', 'java.security.Key').implementation = function () {
    send("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓");
    send("Cipher.init('int', 'java.security.Key') is called!");
    var algorithm = this.getAlgorithm();
    var tag = algorithm + " init Key";
    var className = JSON.stringify(arguments[1]);
    if (className.indexOf("OpenSSLRSAPrivateKey") === -1) {
        var keyBytes = arguments[1].getEncoded();
        toUtf8(tag, keyBytes);
        toHex(tag, keyBytes);
        toBase64(tag, keyBytes);
    }
    showStacks();
    send("↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑");
    return this.init.apply(this, arguments);
}
cipher.init.overload('int', 'java.security.Key', 'java.security.spec.AlgorithmParameterSpec').implementation = function () {
    send("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓");
    send("Cipher.init('int', 'java.security.Key', 'java.security.spec.AlgorithmParameterSpec') is called!");
    var algorithm = this.getAlgorithm();
    var tag = algorithm + " init Key";
    var keyBytes = arguments[1].getEncoded();
    toUtf8(tag, keyBytes);
    toHex(tag, keyBytes);
    toBase64(tag, keyBytes);
    var tags = algorithm + " init iv";
    var iv = Java.cast(arguments[2], Java.use("javax.crypto.spec.IvParameterSpec"));
    var ivBytes = iv.getIV();
    toUtf8(tags, ivBytes);
    toHex(tags, ivBytes);
    toBase64(tags, ivBytes);
    showStacks();
    send("↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑");
    return this.init.apply(this, arguments);
}
cipher.doFinal.overload('java.nio.ByteBuffer', 'java.nio.ByteBuffer').implementation = function () {
    send("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓");
    send("Cipher.doFinal('java.nio.ByteBuffer', 'java.nio.ByteBuffer') is called!");
    showStacks();
    send("↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑");
    return this.doFinal.apply(this, arguments);
}
cipher.doFinal.overload('[B', 'int').implementation = function () {
    send("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓");
    send("Cipher.doFinal('[B', 'int') is called!");
    showStacks();
    send("↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑");
    return this.doFinal.apply(this, arguments);
}
cipher.doFinal.overload('[B', 'int', 'int', '[B').implementation = function () {
    send("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓");
    send("Cipher.doFinal('[B', 'int', 'int', '[B') is called!");
    showStacks();
    send("↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑");
    return this.doFinal.apply(this, arguments);
}
cipher.doFinal.overload('[B', 'int', 'int', '[B', 'int').implementation = function () {
    send("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓");
    send("Cipher.doFinal('[B', 'int', 'int', '[B', 'int') is called!");
    showStacks();
    send("↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑");
    return this.doFinal.apply(this, arguments);
}
cipher.doFinal.overload().implementation = function () {
    send("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓");
    send("Cipher.doFinal() is called!");
    showStacks();
    send("↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑");
    return this.doFinal.apply(this, arguments);
}
cipher.doFinal.overload('[B').implementation = function () {
    send("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓");
    send("Cipher.doFinal('[B') is called!");
    var algorithm = this.getAlgorithm();
    var tag = algorithm + " doFinal data";
    var data = arguments[0];
    //修改一次
    toBase64(tag, data);
    toHex(tag, data);
    toBase64(tag, data);
    var result = this.doFinal.apply(this, arguments);
    var tags = algorithm + " doFinal result";
    toHex(tags, result);
    toBase64(tags, result);
    showStacks();
    send("↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑");
    return result;
}
cipher.doFinal.overload('[B', 'int', 'int').implementation = function () {
    send("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓");
    send("Cipher.doFinal('[B', 'int', 'int') is called!");
    var algorithm = this.getAlgorithm();
    var tag = algorithm + " doFinal data";
    var data = arguments[0];
    toUtf8(tag, data);
    toHex(tag, data);
    toBase64(tag, data);
    var result = this.doFinal.apply(this, arguments);
    var tags = algorithm + " doFinal result";
    toHex(tags, result);
    toBase64(tags, result);
    send("arguments[1]:", arguments[1],);
    send("arguments[2]:", arguments[2]);
    showStacks();
    send("↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑");
    return result;
}
//签名算法
var signature = Java.use("java.security.Signature");
signature.update.overload('byte').implementation = function (data) {
    send("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓");
    send("Signature.update('byte') is called!");
    showStacks();
    send("↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑");
    return this.update(data);
}
signature.update.overload('java.nio.ByteBuffer').implementation = function (data) {
    send("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓");
    send("Signature.update('java.nio.ByteBuffer') is called!");
    showStacks();
    send("↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑");
    return this.update(data);
}
signature.update.overload('[B', 'int', 'int').implementation = function (data, start, length) {
    send("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓");
    send("Signature.update('[B', 'int', 'int') is called!");
    var algorithm = this.getAlgorithm();
    var tag = algorithm + " update data";
    toUtf8(tag, data);
    toHex(tag, data);
    toBase64(tag, data);
    send("start:", start);
    send("length:", length);
    showStacks();
    send("↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑");
    return this.update(data, start, length);
}
signature.sign.overload('[B', 'int', 'int').implementation = function () {
    send("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓");
    send("Signature.sign('[B', 'int', 'int') is called!");
    showStacks();
    send("↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑");
    return this.sign.apply(this, arguments);
}
signature.sign.overload().implementation = function () {
    send("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓");
    send("Signature.sign() is called!");
    var result = this.sign();
    var algorithm = this.getAlgorithm();
    var tag = algorithm + " sign result";
    toHex(tag, result);
    toBase64(tag, result);
    showStacks();
    send("↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑");
    return result;
}
"""


def on_message(message, data):
    if message['type'] == 'send':
        print("[*]{0}".format(message['payload']))
    else:
        print(message)


# 程序运行pid
process = frida.get_usb_device(-1).attach("小红书")
# 可选择j1或者j2算法，使用起来功能一样，看哪个用的更顺手
script = process.create_script(j1)
script.on('message', on_message)
script.load()
# 不让程序断掉
sys.stdin.read()