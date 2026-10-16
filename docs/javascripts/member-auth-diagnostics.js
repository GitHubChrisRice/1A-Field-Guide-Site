(()=>{
  const SESSION_KEY='coalition-membership-session-v1';
  function probe(kind){
    try{
      const store=window[kind],raw=store.getItem(SESSION_KEY);
      let shaped=false,expiresAt=null,expired=null;
      if(raw){
        try{
          const s=JSON.parse(raw);
          shaped=!!(s?.access_token&&s?.refresh_token);
          expiresAt=Number.isFinite(Number(s?.expires_at))?Number(s.expires_at):null;
          expired=expiresAt===null?null:expiresAt<=Math.floor(Date.now()/1000);
        }catch{}
      }
      return{available:true,sessionPresent:!!raw,sessionShaped:shaped,expiresAtPresent:expiresAt!==null,expired,error:null};
    }catch(e){return{available:false,sessionPresent:false,sessionShaped:false,expiresAtPresent:false,expired:null,error:e?.name||'Error'}}
  }
  let bc=false;
  try{const c=new BroadcastChannel('coalition-membership-auth-v1');bc=true;c.close()}catch{}
  const result={
    diagnosticVersion:'same-tab-auth-v1',
    secureContext:window.isSecureContext,
    origin:location.origin,
    path:location.pathname,
    broadcastChannelSupported:bc,
    localStorage:probe('localStorage'),
    sessionStorage:probe('sessionStorage')
  };
  document.getElementById('diagnostics').textContent=JSON.stringify(result,null,2);
})();
