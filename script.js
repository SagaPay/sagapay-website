// Script for interaction
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener("click", function(e) {
        e.preventDefault();
        const targetId = this.getAttribute("href");
        if(targetId === "#") return;
        const targetEl = document.querySelector(targetId);
        if(targetEl) {
            targetEl.scrollIntoView({ behavior: "smooth" });
        }
    });
});

// Typewriter Sequences
const typeSequenceReq = [
    { cls: "comment", text: "// 1. Create Order with one API call\n" },
    { cls: "keyword", text: "const " },
    { cls: "property", text: "orderResponse" },
    { cls: "punctuation", text: " = " },
    { cls: "keyword", text: "await " },
    { cls: "function", text: "fetch" },
    { cls: "punctuation", text: "(" },
    { cls: "string", text: "'https://api.sagapay.no/v1/orders'" },
    { cls: "punctuation", text: ", {\n" },
    { cls: "property", text: "  method" },
    { cls: "punctuation", text: ": " },
    { cls: "string", text: "'POST'" },
    { cls: "punctuation", text: ",\n" },
    { cls: "property", text: "  body" },
    { cls: "punctuation", text: ": " },
    { cls: "property", text: "JSON" },
    { cls: "punctuation", text: "." },
    { cls: "function", text: "stringify" },
    { cls: "punctuation", text: "({\n" },
    { cls: "property", text: "    type" },
    { cls: "punctuation", text: ": " },
    { cls: "string", text: "'PAYMENT'" },
    { cls: "punctuation", text: ",\n" },
    { cls: "property", text: "    amount" },
    { cls: "punctuation", text: ": " },
    { cls: "punctuation", text: "10000" },
    { cls: "punctuation", text: ",\n" },
    { cls: "property", text: "    referenceId" },
    { cls: "punctuation", text: ": " },
    { cls: "string", text: "'ORDER-1234'" },
    { cls: "punctuation", text: ",\n" },
    { cls: "property", text: "    terminal$id" },
    { cls: "punctuation", text: ": " },
    { cls: "string", text: "'83bee989f08500405'" },
    { cls: "punctuation", text: "\n  })" },
    { cls: "punctuation", text: "\n});\n\n" },

    { cls: "comment", text: "// 2. Initiate Payment\n" },
    { cls: "keyword", text: "const " },
    { cls: "property", text: "paymentResponse" },
    { cls: "punctuation", text: " = " },
    { cls: "keyword", text: "await " },
    { cls: "function", text: "fetch" },
    { cls: "punctuation", text: "(" },
    { cls: "string", text: "'https://api.sagapay.no/v1/payments'" },
    { cls: "punctuation", text: ", {\n" },
    { cls: "property", text: "  method" },
    { cls: "punctuation", text: ": " },
    { cls: "string", text: "'POST'" },
    { cls: "punctuation", text: ",\n" },
    { cls: "property", text: "  body" },
    { cls: "punctuation", text: ": " },
    { cls: "property", text: "JSON" },
    { cls: "punctuation", text: "." },
    { cls: "function", text: "stringify" },
    { cls: "punctuation", text: "({\n" },
    { cls: "property", text: "    orderId" },
    { cls: "punctuation", text: ": " },
    { cls: "property", text: "orderResponse" },
    { cls: "punctuation", text: "." },
    { cls: "property", text: "id" },
    { cls: "punctuation", text: ",\n" },
    { cls: "property", text: "    paymentMethod" },
    { cls: "punctuation", text: ": " },
    { cls: "string", text: "'CARD'" },
    { cls: "punctuation", text: "\n  })" },
    { cls: "punctuation", text: "\n});\n" }
];

const webhookJsonStr = `{
  "eventType": "order.paymentcompleted",
  "metadata": {
    "eventId": "831fc2f040bf405fff",
    "created": 1745821536443,
    "retryAttempt": 0,
    "terminal$id": "830acac336f6d80b04",
    "originalCreated": 1745821536443,
    "webhookEventId": "831fc2f02a031015ff"
  },
  "data": {
    "orderId": "831fc2de72fed0000b",
    "referenceId": "r_3",
    "adjustments": [
      {
        "adjustmentType": "Discounts",
        "amount": "10"
      }
    ],
    "paymentStatus": "PAYMENT_COMPLETED",
    "paymentMethod": "CARD",
    "paymentId": "831fc2ebc0bf400a06",
    "truncatedPan": "0102",
    "amount": "10000",
    "merchantId": "82e48bd833d7d80c0e",
    "type": "PURCHASE",
    "transactionDetails": [
      {
        "transactionId": "831fc2ebc0bf401419",
        "terminal$id": "830acac336f6d80b04",
        "rrn": "511806000002",
        "amount": "10000",
        "currency": "752",
        "method": "CARD",
        "voided": false,
        "truncatedPan": "0102",
        "cardLabel": "MASTERCARD DEBIT",
        "posEntryMode": "07",
        "aid": "a0000000041010",
        "customerResponseCode": "00",
        "cvmMethod": "5e",
        "cvmMethodDescription": "Signature",
        "authMode": "ISSUER",
        "cardBrand": "MASTERCARD",
        "terminalVerificationResult": "0400008001"
      }
    ]
  }
}`;

// Pre-parse the webhook into simple tokens (line by line)
const typeSequenceRes = webhookJsonStr.split('\n').map(line => {
    return { cls: "string", text: line + '\n' };
});
typeSequenceRes.unshift({ cls: "comment", text: "// Webhook mottatt etter betaling:\n" });

document.addEventListener("DOMContentLoaded", () => {
    const el = document.getElementById("typewriter-code");
    const runBtn = document.getElementById("runCodeBtn");
    const codeView = document.getElementById("code-view");
    const termView = document.getElementById("terminal-view");
    
    if (!el || !runBtn || !codeView || !termView) return;
    
    let tokenIndex = 0;
    let charIndex = 0;
    let currentSequence = typeSequenceReq;
    let isTyping = false;
    let typeTimeout = null;
    
    function resetTyping(sequence) {
        if(typeTimeout) clearTimeout(typeTimeout);
        currentSequence = sequence;
        el.innerHTML = "";
        tokenIndex = 0;
        charIndex = 0;
        runBtn.style.display = "none";
        typeTimeout = setTimeout(typeChar, 500);
    }

    function typeChar() {
        isTyping = true;
        if (tokenIndex >= currentSequence.length) {
            isTyping = false;
            // Always ensure scroll bottom after writing ends
            const container = el.closest('.code-editor-body');
            if (container) container.scrollTop = container.scrollHeight;

            if (currentSequence === typeSequenceReq) {
                // Show "Run Code" button
                runBtn.style.display = "block";
                runBtn.classList.remove("pressed");
                
                // Auto-click it after a short delay
                typeTimeout = setTimeout(() => {
                    runBtn.classList.add("pressed");
                    setTimeout(() => {
                        runTerminalAnim();
                    }, 400); // 400ms delay to show the "pressed" state before switching views
                }, 400);
            } else {
                // Done writing webhook, wait 6 seconds and loop
                typeTimeout = setTimeout(() => resetTyping(typeSequenceReq), 6000);
            }
            return;
        }
        
        const token = currentSequence[tokenIndex];
        
        // Find or create span for this token
        let span = el.querySelector('#token-' + tokenIndex);
        if(!span) {
            span = document.createElement('span');
            span.id = 'token-' + tokenIndex;
            span.className = 'token ' + token.cls;
            el.appendChild(span);
        }
        
        if (charIndex < token.text.length) {
            span.textContent += token.text.charAt(charIndex);
            charIndex++;
            
            // Auto-scroll
            const container = el.closest('.code-editor-body');
            if (container) container.scrollTop = container.scrollHeight;

            // Faster typing for webhook
            const speed = currentSequence === typeSequenceRes ? (Math.random() * 2 + 1) : (Math.random() * 8 + 4);
            typeTimeout = setTimeout(typeChar, speed);
        } else {
            tokenIndex++;
            charIndex = 0;
            // Shorter delay between lines/tokens for webhook
            typeTimeout = setTimeout(typeChar, currentSequence === typeSequenceRes ? 5 : 10);
        }
    }

    // TERMINAL ANIMATION
    let runningAnim = false;
    const s = ms => new Promise(r => setTimeout(r, ms));

    function showTermScreen(id) {
      ['screenAmount', 'screenProcessing', 'screenSuccess'].forEach(n => {
        const elem = document.getElementById(n);
        if(elem) elem.style.display = n === id ? 'flex' : 'none';
      });
    }

    async function runTerminalAnim() {
      if (runningAnim) return;
      runningAnim = true;
      runBtn.style.display = "none";
      
      // Stop typing if it's currently looping/waiting
      if(typeTimeout) clearTimeout(typeTimeout);

      // Switch views
      codeView.style.display = "none";
      termView.style.display = "flex";

      const card = document.getElementById('card');
      const badge = document.getElementById('badge');
      const checkPath = document.getElementById('checkPath');
      const ripple = document.getElementById('ripple');
      const r1 = document.getElementById('r1');
      const r2 = document.getElementById('r2');
      const r3 = document.getElementById('r3');

      if (!card || !badge || !checkPath || !ripple) return;

      badge.classList.remove('show');
      checkPath.classList.remove('draw');
      ripple.classList.remove('go');
      [r1, r2, r3].forEach(r => r.classList.remove('pulse'));
      card.className = 'card';
      showTermScreen('screenAmount');

      await s(100);
      card.style.transition = 'transform 0.55s cubic-bezier(0.22,1,0.36,1), opacity 0.4s';
      card.classList.add('fly-in');
      await s(700);

      card.style.transition = 'transform 0.18s ease-out, opacity 0.2s';
      card.classList.add('tap');

      r1.classList.add('pulse');
      await s(110); r2.classList.add('pulse');
      await s(110); r3.classList.add('pulse');
      ripple.classList.add('go');

      await s(1000);
      card.style.transition = 'transform 0.45s ease-in, opacity 0.35s ease-in';
      card.classList.remove('tap');
      card.classList.add('fly-out');

      await s(300);
      showTermScreen('screenProcessing');

      await s(1800);
      showTermScreen('screenSuccess');
      await s(100);
      badge.classList.add('show');
      await s(300);
      checkPath.classList.add('draw');

      await s(2000);
      
      // End animation
      badge.classList.remove('show');
      checkPath.classList.remove('draw');
      await s(400);
      card.className = 'card';
      showTermScreen('screenAmount');
      ripple.classList.remove('go');
      [r1, r2, r3].forEach(r => r.classList.remove('pulse'));
      
      runningAnim = false;
      
      // Switch views back to code
      termView.style.display = "none";
      codeView.style.display = "block";
      
      // Trigger webhook typwriter
      resetTyping(typeSequenceRes);
    }

    runBtn.addEventListener('click', runTerminalAnim);
    
    // Initial start
    typeTimeout = setTimeout(typeChar, 1000);

    /* =========================================================================
       WOW STATS BAR - COUNT UP / COUNT DOWN LOGIC
       ========================================================================= */
    const statElements = document.querySelectorAll('.stat-number');
    
    function animateCounters() {
        statElements.forEach(el => {
            const isDown = el.classList.contains('count-down') || el.hasAttribute('data-start');
            const targetVal = parseFloat(el.getAttribute('data-target') || 0);
            const startVal = parseFloat(el.getAttribute('data-start') || 0);
            const suffix = el.getAttribute('data-suffix') || "";
            const format = el.getAttribute('data-format') || "";
            
            // Alle tellere fullføres på nøyaktig samme tidspunkt (f.eks 5 sekunder)
            const duration = 5000; 
            const startTime = performance.now();
            const from = isDown ? startVal : 0;
            const to = targetVal;
            
            // Ease-funksjoner (Felles ekstremt myk nedbremsing for alle)
            // Øker til power of 8 (easeOutOct) som gjør at den nesten "henger" i dagesvis/timesvis, 
            // og tvinger utrolig sakte talloppdatering det siste sekundet tvers over hele linjen.
            const customEase = t => 1 - Math.pow(1 - t, 8);
            
            function update(currentTime) {
                let timeElapsed = currentTime - startTime;
                let progress = Math.min(timeElapsed / duration, 1);
                
                // Bruker customEase for at den skal gli sinnsykt sakte inn på slutten
                let easeProgress = customEase(progress); 
                let currentVal = from + (to - from) * easeProgress;
                
                // Tilpasset tekst-formattering for å endre "dager til timer til min"
                if (format === "time-min") {
                    if (currentVal >= 1440) {
                        el.textContent = Math.round(currentVal / 1440) + " dager";
                    } else if (currentVal >= 60) {
                        el.textContent = Math.round(currentVal / 60) + " timer";
                    } else {
                        el.textContent = Math.max(targetVal, Math.round(currentVal)) + " min";
                    }
                } else if (format === "time-hour") {
                    if (currentVal >= 168) {
                        el.textContent = Math.round(currentVal / 168) + " uker";
                    } else if (currentVal >= 24) {
                        el.textContent = Math.round(currentVal / 24) + " dager";
                    } else {
                        el.textContent = Math.max(targetVal, Math.round(currentVal)) + " timer";
                    }
                } else {
                    el.textContent = Math.round(currentVal) + suffix;
                }
                
                if (progress < 1) {
                    requestAnimationFrame(update);
                } else {
                    // Land eksakt på målet ved ferdig animasjon
                    if (format === "time-min") el.textContent = targetVal + " min";
                    else if (format === "time-hour") el.textContent = targetVal + " timer";
                    else el.textContent = targetVal + suffix;
                }
            }
            
            requestAnimationFrame(update);
        });
    }
    
    let hasAnimatedOnce = false;

    const countObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            // Vi sjekker for containeren, starter animasjonene inni
            if (entry.isIntersecting && !hasAnimatedOnce) {
                hasAnimatedOnce = true;
                
                // Kjør animasjonen første gang man scroller ned
                animateCounters();
                
                // Vi har nå fjernet loop/intervaller slik at det kun spilles én gang
                
            }
        });
    }, {
        threshold: 0.5 
    });

    // Vi observerer nå wrapper-seksjonen istedenfor hvert enkelttall, slik at løkken kjøres synkronisert
    const statsSection = document.querySelector('.wow-stats-bar');
    if(statsSection) {
        countObserver.observe(statsSection);
    }
});

// === Animated Count-Up for Dashboard Statistics ===
function animateStats() {
    const statNumbers = document.querySelectorAll('.stat-number');
    statNumbers.forEach(el => {
        const target = +el.getAttribute('data-target');
        const duration = 1800;
        const start = 0;
        let startTimestamp = null;
        function step(timestamp) {
            if (!startTimestamp) startTimestamp = timestamp;
            const progress = Math.min((timestamp - startTimestamp) / duration, 1);
            const value = Math.floor(progress * (target - start) + start);
            el.textContent = value.toLocaleString('no-NO');
            if (progress < 1) {
                window.requestAnimationFrame(step);
            } else {
                el.textContent = target.toLocaleString('no-NO');
            }
        }
        window.requestAnimationFrame(step);
    });
}

// Only run on merchant-dashboard.html
if (window.location.pathname.includes('merchant-dashboard')) {
    window.addEventListener('DOMContentLoaded', () => {
        setTimeout(animateStats, 400); // slight delay for fade-in
    });
}

// -- INTERAKTIVE FANER FOR BRANSJER --
document.addEventListener('DOMContentLoaded', () => {
    const tabBtns = document.querySelectorAll('.tab-btn');
    const tabPanels = document.querySelectorAll('.tab-panel');

    tabBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            // Finn hvilken bransje som ble trykket på
            const target = btn.getAttribute('data-target');

            // Fjern active-klasse fra alle knapper og paneler
            tabBtns.forEach(b => b.classList.remove('active'));
            tabPanels.forEach(p => p.classList.remove('active'));

            // Legg til active-klasse på den trykkede knappen
            btn.classList.add('active');

            // Finn og vis riktig panel
            const targetPanel = document.getElementById(`panel-${target}`);
            if (targetPanel) {
                targetPanel.classList.add('active');
            }
        });
    });
});

// -- AI-KALKULATOR LOGIKK --
document.addEventListener('DOMContentLoaded', () => {
    const revSlider = document.getElementById('monthly-revenue');
    const revVal = document.getElementById('revenue-val');
    
    const txnSlider = document.getElementById('avg-transaction');
    const txnVal = document.getElementById('transaction-val');
    
    const feeSlider = document.getElementById('current-fee');
    const feeVal = document.getElementById('fee-val');
    
    const feeFixedSlider = document.getElementById('current-fee-fixed');
    const feeFixedVal = document.getElementById('fee-fixed-val');
    
    const costCurrentEl = document.getElementById('cost-current');
    const costSagaEl = document.getElementById('cost-saga');
    const savingsEl = document.getElementById('savings-amount');
    const savingsElYearly = document.getElementById('savings-amount-yearly');

    const normalResults = document.getElementById('normal-results');
    const contactSalesResults = document.getElementById('contact-sales-results');

    function formatNOK(number) {
        // Enkel funksjon for å legge til mellomrom i tusentall, f.eks "100 000"
        return Math.round(number).toString().replace(/\B(?=(\d{3})+(?!\d))/g, " ") + ' kr';
    }

    function calculate() {
        if (!revSlider) return; // Kjør bare hvis kalkulatoren finnes på siden

        const revenue = parseFloat(revSlider.value);
        const avgTxn = parseFloat(txnSlider.value);
        const currentFeeVal = parseFloat(feeSlider.value);
        const currentFeeFixedVal = parseFloat(feeFixedSlider.value);
        
        // Oppdater tekst over sliderne
        revVal.textContent = formatNOK(revenue);
        txnVal.textContent = formatNOK(avgTxn);
        feeVal.textContent = currentFeeVal.toFixed(2) + ' %';
        feeFixedVal.textContent = currentFeeFixedVal.toFixed(2) + ' kr';
        
        // Antall transaksjoner (basert på total omsetning og snittpris)
        const transactionsPerMonth = revenue / avgTxn;
        
        // Konkurrentens kostnad
        const currentCost = (revenue * (currentFeeVal / 100)) + (transactionsPerMonth * currentFeeFixedVal);
        
        // Sagas dynamiske prising
        // Mål er 0.10% under konkurrenten og 0.05 kr under, med tak på 1.5% og 2.0 NOK
        let sagaPercentage = Math.min(1.5, currentFeeVal - 0.10);
        let sagaFixedFee = Math.min(2.0, currentFeeFixedVal - 0.05);

        // Hvis resultanten er under bunnpris på 0.5% eller 0.70 NOK, da trenger de spesialpris via salg.
        if (sagaPercentage < 0.5 || sagaFixedFee < 0.7) {
            normalResults.style.display = 'none';
            contactSalesResults.style.display = 'flex';
        } else {
            normalResults.style.display = 'block';
            contactSalesResults.style.display = 'none';
        
            // Sagas kostnad
            const sagaCost = (revenue * (sagaPercentage / 100)) + (transactionsPerMonth * sagaFixedFee);
            
            // Potensiell besparelse
            let savings = currentCost - sagaCost;
            if (savings < 0) { savings = 0; } // Settes ikke negativ besparelse

            // Tegn ut til DOM
            costCurrentEl.textContent = formatNOK(currentCost);
            costSagaEl.textContent = formatNOK(sagaCost);
            savingsEl.textContent = formatNOK(savings);
            
            if (savingsElYearly) {
                savingsElYearly.textContent = formatNOK(savings * 12);
            }
        }
    }

    // Sett event listeners hvis de finnes
    if(revSlider && txnSlider && feeSlider && feeFixedSlider) {
        revSlider.addEventListener('input', calculate);
        txnSlider.addEventListener('input', calculate);
        feeSlider.addEventListener('input', calculate);
        feeFixedSlider.addEventListener('input', calculate);
        
        // Kjør én gang ved start for å fylle inn statiske felt riktig fra slider-values
        calculate();
    }
});
