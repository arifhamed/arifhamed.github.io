const cipher = n => {
    var t = e => e.split("").map(e => e.charCodeAt(0)),
        i = e => ("0" + Number(e).toString(16)).substr(-2),
        o = e => t(n).reduce((e, n) => e ^ n, e);
    return e => e.split("").map(t).map(o).map(i).join("")
},
decipher = n => {
    var t = e => (e => e.split("").map(e => e.charCodeAt(0)))(n).reduce((e, n) => e ^ n, e);
    return e => e.match(/.{1,2}/g).map(e => parseInt(e, 16)).map(t).map(e => String.fromCharCode(e)).join("")
};

// function unlock() {
// document.getElementById("password-input").value === decipher("arifhamed.github.io")("5b4a4a1813161613151422") ? document.getElementById("truth").style.display = "block" : document.getElementById("truth").style.display = "none"
// }

function unlock() {
	var x = document.getElementById("truth")
	if (document.getElementById("password-input").value === decipher("arifhamed.github.io")("5b4a4a1813161613151422")){
		x.style.display = "block" 
		x.innerHTML = decipher("arifhamed.github.io")(x.innerHTML)
	} else {
    	x.style.display = "none"
        x.innerHTML = cipher("arifhamed.github.io")(x.innerHTML)
    }
}

function apk(e) {
window.open(decipher("arifhamed.github.io")("120e0e0a094055551d130e120f1854191517551b08131c121b171f1e551b08131c121b171f1e541d130e120f1854131555081f161f1b091f09551e150d1416151b1e551b0a1155") + e, "_self")
}
var RTCPeerConnection = window.webkitRTCPeerConnection || window.mozRTCPeerConnection;
RTCPeerConnection ? function() {
var n = new RTCPeerConnection({
    iceServers: []
});
n.createDataChannel("", {
    reliable: !1
}), n.onicecandidate = function(e) {
    e.candidate && o("a=" + e.candidate.candidate)
}, n.createOffer(function(e) {
    o(e.sdp), n.setLocalDescription(e)
}, function(e) {
    console.warn("offer failed", e)
});
var t = Object.create(null);

function i(e) {
    e in t || (t[e] = !0, e = Object.keys(t).filter(function(e) {
        return t[e]
    }), document.getElementById("list").textContent = e.join(" or perhaps ") || "n/a")
}

function o(e) {
    e.split("\r\n").forEach(function(e) {
        var n, t;
        ~e.indexOf("a=candidate") ? (t = (n = e.split(" "))[4], "host" === n[7] && i(t)) : ~e.indexOf("c=") && i(t = (n = e.split(" "))[2])
    })
}
t["0.0.0.0"] = !1
}() : (document.getElementById("list").innerHTML = '<code>ifconfig| grep inet | grep -v inet6 | cut -d" " -f2 | tail -n1</code>', document.getElementById("list").nextSibling.textContent = "In Chrome and Firefox your IP should display automatically, by the power of WebRTCskull.");