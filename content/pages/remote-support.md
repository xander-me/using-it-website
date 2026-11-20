---
title: "Remote Support"
description: ""
pubDate: "2026-03-21 08:08:33"
updatedDate: "2026-03-21 08:15:21"
slug: "remote-support"
draft: false
wordpress_id: "586"
original_url: "https://using-it.dk/remote-support/"
---

<!-- ============================================================
     Using-IT – Remote Support Page
     Add to WordPress via:
     Gutenberg → "+" → Custom HTML block
     ============================================================ -->

<style>
.uit-wrap{font-family:'Segoe UI',system-ui,sans-serif;max-width:min(780px,100%);margin:0 auto;padding:clamp(8px,2vw,24px) 0;color:#e2e8f0;container-type:inline-size}
.uit-da{display:none}

/* Lang toggle */
.uit-lang-bar{display:flex;justify-content:flex-end;margin-bottom:clamp(10px,2cqi,16px)}
.uit-lang-pill{display:inline-flex;background:#1e293b;border:1px solid #334155;border-radius:999px;padding:3px;gap:2px}
.uit-lang-pill button{background:transparent;border:none;border-radius:999px;padding:5px 14px;font-size:clamp(.72rem,1.4cqi,.8rem);font-weight:600;color:#64748b;cursor:pointer;transition:background .18s,color .18s;letter-spacing:.04em}
.uit-lang-pill button.uit-active{background:linear-gradient(135deg,#3b82f6,#1d4ed8);color:#fff;box-shadow:0 2px 10px rgba(59,130,246,.35)}
.uit-lang-pill button:not(.uit-active):hover{color:#e2e8f0}

/* Hero */
.uit-hero{background:linear-gradient(135deg,#0f172a 0%,#1e293b 60%,#0f172a 100%);border:1px solid #334155;border-radius:clamp(10px,2.5cqi,16px);padding:clamp(28px,6cqi,56px) clamp(20px,5cqi,48px);text-align:center;position:relative;overflow:hidden;margin-bottom:clamp(20px,4cqi,36px)}
.uit-hero::before{content:'';position:absolute;top:-60px;right:-60px;width:clamp(120px,30cqi,220px);height:clamp(120px,30cqi,220px);background:radial-gradient(circle,rgba(59,130,246,.15) 0%,transparent 70%);pointer-events:none}
.uit-hero-icon{width:clamp(44px,8cqi,64px);height:clamp(44px,8cqi,64px);background:linear-gradient(135deg,#3b82f6,#1d4ed8);border-radius:clamp(10px,2cqi,16px);display:inline-flex;align-items:center;justify-content:center;margin-bottom:clamp(12px,2.5cqi,20px);box-shadow:0 0 32px rgba(59,130,246,.3)}
.uit-hero-icon svg{width:clamp(20px,4cqi,32px);height:clamp(20px,4cqi,32px);fill:none;stroke:#fff;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
.uit-hero h1{font-size:clamp(1.3rem,4cqi,2rem);font-weight:700;color:#f1f5f9;margin:0 0 clamp(6px,1.5cqi,12px);letter-spacing:-.02em}
.uit-hero p{font-size:clamp(.85rem,2cqi,1rem);color:#94a3b8;margin:0 auto;max-width:48ch;line-height:1.55}

/* Steps */
.uit-steps{display:grid;gap:clamp(10px,2cqi,18px);margin-bottom:clamp(20px,4cqi,36px)}
.uit-step{background:#1e293b;border:1px solid #334155;border-radius:clamp(8px,2cqi,12px);padding:clamp(14px,3cqi,22px) clamp(16px,3.5cqi,26px);display:flex;gap:clamp(12px,2.5cqi,22px);align-items:flex-start;transition:border-color .2s,transform .2s}
.uit-step:hover{border-color:#3b82f6;transform:translateX(4px)}
.uit-step-num{flex-shrink:0;width:clamp(28px,5cqi,38px);height:clamp(28px,5cqi,38px);background:linear-gradient(135deg,#3b82f6,#1d4ed8);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:clamp(.75rem,1.5cqi,.9rem);font-weight:700;color:#fff;box-shadow:0 0 12px rgba(59,130,246,.25)}
.uit-step-body h3{font-size:clamp(.9rem,2cqi,1.05rem);font-weight:600;color:#f1f5f9;margin:0 0 4px}
.uit-step-body p{font-size:clamp(.8rem,1.8cqi,.92rem);color:#94a3b8;margin:0;line-height:1.55}
.uit-step-body code{background:#0f172a;border:1px solid #475569;border-radius:4px;padding:1px 6px;font-size:clamp(.75rem,1.5cqi,.85rem);color:#7dd3fc;font-family:'Cascadia Code','Courier New',monospace}

/* CTA */
.uit-cta{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(200px,100%),1fr));gap:clamp(10px,2cqi,18px);margin-bottom:clamp(20px,4cqi,36px)}
.uit-card{background:#1e293b;border:1px solid #334155;border-radius:clamp(8px,2cqi,12px);padding:clamp(16px,3cqi,24px) clamp(14px,2.5cqi,22px);text-align:center;transition:border-color .2s,transform .2s}
.uit-card:hover{border-color:#3b82f6;transform:translateY(-3px)}
.uit-os{font-size:clamp(.68rem,1.3cqi,.78rem);font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:#64748b;margin-bottom:clamp(8px,1.5cqi,14px)}
.uit-dl{display:inline-flex;align-items:center;justify-content:center;gap:clamp(6px,1.2cqi,10px);background:linear-gradient(135deg,#3b82f6,#1d4ed8);color:#fff!important;text-decoration:none!important;font-size:clamp(.82rem,1.8cqi,.97rem);font-weight:600;padding:clamp(10px,2cqi,14px) clamp(14px,3cqi,24px);border-radius:clamp(6px,1.5cqi,9px);box-shadow:0 4px 16px rgba(59,130,246,.3);transition:box-shadow .2s,transform .15s;width:100%;letter-spacing:-.01em}
.uit-dl:hover{box-shadow:0 6px 28px rgba(59,130,246,.45);transform:scale(1.02)}
.uit-dl svg{width:clamp(14px,2.5cqi,19px);height:clamp(14px,2.5cqi,19px);fill:none;stroke:#fff;stroke-width:2;stroke-linecap:round;stroke-linejoin:round;flex-shrink:0}
.uit-sub{display:block;margin-top:clamp(6px,1.2cqi,10px);font-size:clamp(.68rem,1.3cqi,.78rem);color:#64748b}

/* Security */
.uit-info{background:#0f172a;border:1px solid #334155;border-left:4px solid #3b82f6;border-radius:clamp(8px,2cqi,12px);padding:clamp(14px,2.5cqi,20px) clamp(16px,3cqi,24px);display:flex;gap:clamp(10px,2cqi,16px);align-items:flex-start}
.uit-info svg{flex-shrink:0;width:clamp(16px,3cqi,20px);height:clamp(16px,3cqi,20px);stroke:#3b82f6;fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round;margin-top:2px}
.uit-info p{font-size:clamp(.78rem,1.8cqi,.9rem);color:#94a3b8;margin:0;line-height:1.6}
.uit-info strong{color:#e2e8f0}
</style>

  <!-- Language toggle -->

  
    
      <button id="uitEN" class="uit-active" onclick="uitLang('en')">🇬🇧 EN</button>
      <button id="uitDA" onclick="uitLang('da')">🇩🇰 DA</button>
    
  

  <!-- Hero -->

  
    
      <svg viewBox="0 0 24 24"><rect x="2" y="3" width="20" height="14" rx="2"/></svg>
    
    # Remote Support
      Fjernsupport
    
      <span class="uit-en">Need help? Follow the three steps below and we'll be connected within minutes.</span>
      <span class="uit-da">Har du brug for hjælp? Følg de tre trin herunder, så er vi i gang på få minutter.</span>
    

  <!-- Steps -->

  

```

  1
  
    ### Download AnyDesk
      Download AnyDesk
    
      <span class="uit-en">Click the button below for your operating system. AnyDesk requires **no installation**: just run the file directly.</span>
      <span class="uit-da">Klik på knappen nedenfor for dit styresystem. AnyDesk kræver **ingen installation**: kør blot filen direkte.</span>
    

  2
  
    ### Share your ID
      Del dit ID
    
      <span class="uit-en">Once AnyDesk opens, you'll see a **9-digit ID** at the top of the window, e.g. `123 456 789`. Send that ID to me by phone or email.</span>
      <span class="uit-da">Når AnyDesk åbner, ser du et **9-cifret ID** øverst i vinduet, f.eks. `123 456 789`. Send det ID til mig via telefon eller e-mail.</span>
    

  3
  
    ### Accept the connection
      Acceptér forbindelsen
    
      <span class="uit-en">I'll initiate the session from my end. A prompt will appear asking you to **Accept** the incoming connection: click it to grant access. You can disconnect at any time by closing AnyDesk.</span>
      <span class="uit-da">Jeg starter sessionen fra min side. Der vises en boks, hvor du bliver bedt om at klikke **Acceptér**: klik på den for at give mig adgang. Du kan afbryde forbindelsen til enhver tid ved at lukke AnyDesk.</span>
    

```

  

  <!-- Download buttons -->

  

```

  🪟 Windows
  [
    <svg viewBox="0 0 24 24">- </svg>
    <span class="uit-en">Download for Windows</span>
    <span class="uit-da">Download til Windows</span>
  ](https://download.anydesk.com/AnyDesk.exe)
  <span class="uit-sub">
    <span class="uit-en">No installation required · ~4 MB</span>
    <span class="uit-da">Ingen installation nødvendig · ~4 MB</span>
  </span>

  🍎 macOS
  [
    <svg viewBox="0 0 24 24">- </svg>
    <span class="uit-en">Download for Mac</span>
    <span class="uit-da">Download til Mac</span>
  ](https://download.anydesk.com/anydesk.dmg)
  <span class="uit-sub">
    <span class="uit-en">Open .dmg and run directly · ~10 MB</span>
    <span class="uit-da">Åbn .dmg og kør direkte · ~10 MB</span>
  </span>

```

  

  <!-- Security note -->

  
    <svg viewBox="0 0 24 24"></svg>
    
      <span class="uit-en">**Your security:** You remain in full control at all times. I can only see your screen and control your mouse while you have actively granted permission. The session ends automatically when you close AnyDesk.</span>
      <span class="uit-da">**Din sikkerhed:** Du har fuld kontrol hele tiden. Jeg kan kun se din skærm og styre musen, mens du aktivt har givet tilladelse. Forbindelsen afsluttes automatisk, når du lukker AnyDesk.</span>
    

<script>
function uitLang(lang) {
  var wrap = document.getElementById('uitWrap');
  var show = lang === 'en' ? '.uit-en' : '.uit-da';
  var hide = lang === 'en' ? '.uit-da' : '.uit-en';
  wrap.querySelectorAll(show).forEach(function(el){ el.style.display = ''; });
  wrap.querySelectorAll(hide).forEach(function(el){ el.style.display = 'none'; });
  document.getElementById('uitEN').classList.toggle('uit-active', lang === 'en');
  document.getElementById('uitDA').classList.toggle('uit-active', lang === 'da');
}
</script>