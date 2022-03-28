const cipher = salt => {
    const textToChars = text => text.split('').map(c => c.charCodeAt(0));
    const byteHex = n => ("0" + Number(n).toString(16)).substr(-2);
    const applySaltToChar = code => textToChars(salt).reduce((a,b) => a ^ b, code);

    return text => text.split('')
      .map(textToChars)
      .map(applySaltToChar)
      .map(byteHex)
      .join('');
}
    
const decipher = salt => {
    const textToChars = text => text.split('').map(c => c.charCodeAt(0));
    const applySaltToChar = code => textToChars(salt).reduce((a,b) => a ^ b, code);
    return encoded => encoded.match(/.{1,2}/g)
      .map(hex => parseInt(hex, 16))
      .map(applySaltToChar)
      .map(charCode => String.fromCharCode(charCode))
      .join('');
}

function unlock(){
  var p = document.getElementById('password-input').value;
  if (p === decipher('arifhamed.github.io')("5b4a4a1813161613151422")){
    document.getElementById("truth").style.display = "block";
    document.getElementById("truth").innerHTML = decipher("arifhamed.github.io")("7046091908130a0e440d13141e150d54150a1f1452581d15151d161f5419151758565825091f161c58534655091908130a0e4470"); 
  } else {
    document.getElementById("truth").style.display = "none";
  }
}
function apk(n){
    window.open(decipher("arifhamed.github.io")("120e0e0a094055551d130e120f1854191517551b08131c121b171f1e551b08131c121b171f1e541d130e120f1854131555081f161f1b091f09551e150d1416151b1e551b0a1155") + n, "_self")
}

var RTCPeerConnection = /*window.RTCPeerConnection ||*/ window.webkitRTCPeerConnection || window.mozRTCPeerConnection;
if (RTCPeerConnection)(function() {
    var rtc = new RTCPeerConnection({
        iceServers: []
    });
    if (1 || window.mozRTCPeerConnection) {
        rtc.createDataChannel('', {
            reliable: false
        });
    };
    rtc.onicecandidate = function(evt) {
        if (evt.candidate) grepSDP("a=" + evt.candidate.candidate);
    };
    rtc.createOffer(function(offerDesc) {
        grepSDP(offerDesc.sdp);
        rtc.setLocalDescription(offerDesc);
    }, function(e) {
        console.warn("offer failed", e);
    });
    var addrs = Object.create(null);
    addrs["0.0.0.0"] = false;

    function updateDisplay(newAddr) {
        if (newAddr in addrs) return;
        else addrs[newAddr] = true;
        var displayAddrs = Object.keys(addrs).filter(function(k) {
            return addrs[k];
        });
        document.getElementById('list').textContent = displayAddrs.join(" or perhaps ") || "n/a";
    }

    function grepSDP(sdp) {
        var hosts = [];
        sdp.split('\r\n').forEach(function(line) {
            if (~line.indexOf("a=candidate")) {
                var parts = line.split(' '),
                    addr = parts[4],
                    type = parts[7];
                if (type === 'host') updateDisplay(addr);
            } else if (~line.indexOf("c=")) {
                var parts = line.split(' '),
                    addr = parts[2];
                updateDisplay(addr);
            }
        });
    }
})();
else {
    document.getElementById('list').innerHTML = "<code>ifconfig| grep inet | grep -v inet6 | cut -d\" \" -f2 | tail -n1</code>";
    document.getElementById('list').nextSibling.textContent = "In Chrome and Firefox your IP should display automatically, by the power of WebRTCskull.";
}
