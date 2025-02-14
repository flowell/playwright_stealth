var __RTCIceCandidate_address = Object.getOwnPropertyDescriptor(RTCIceCandidate.prototype, 'address');
var __RTCIceCandidate_candidate = Object.getOwnPropertyDescriptor(RTCIceCandidate.prototype, 'candidate');
var __RTCSessionDescription_sdp =  Object.getOwnPropertyDescriptor(RTCSessionDescription.prototype, 'sdp');

Object.defineProperty(RTCIceCandidate.prototype, 'address', {
    get: function() {
      return opts.window_web_rtc_address || '127.0.0.1';
    }
});
  
Object.defineProperty(RTCIceCandidate.prototype, 'candidate', {
  get: function() {
    let address = __RTCIceCandidate_address.get.call(this);
    let candidate = __RTCIceCandidate_candidate.get.call(this).replace(address, opts.window_web_rtc_address || '127.0.0.1');
    return candidate;
  }
});

Object.defineProperty(RTCSessionDescription.prototype, 'sdp', {
  get: function() {
    let originSDP = __RTCSessionDescription_sdp.get.call(this);
    let newSDP = originSDP.replace(/((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])/g, opts.window_web_rtc_address || '127.0.0.1');
    return newSDP;
  }
});