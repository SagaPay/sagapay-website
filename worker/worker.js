/**
 * Cloudflare Worker — SagaPay Online SDK Demo Proxy
 *
 * All credentials and customer data live here.
 * The frontend only receives orderId, nonce, and publicKey.
 */

const CONFIG = {
  MERCHANT_ID: '83af75d53169b0070e',
  STORE_ID: '83b3ade0f40e700f0f',
  TERMINAL_ID: '83ef7cecba3af80104',
  API_KEY: 'sg_live_wRLIkjGWlX3Zm7MEDO49IfIFcvJclnKH',
  API_SECRET: 'sgs_vj0iNS4bJKDHiiki4zd8cEasrDjhlQL2h2CeOvgu',
  PUBLIC_KEY:
    '4d494942496a414e42676b71686b6947397730424151454641414f43415138414d49494243674b434151454172326e6d7049414c4d35414d6f7a51795a4968527076784236793558796a3877335565666a78764c626864464d446c4a41345451523941676a2f584c4a4f503548746d2b71635570736459655055704d7976526649744b6a513157443974663237314363632f555044383659533956476e5244396430302b76714d6648556a5759417a72724a672b395a4a6377612b2b43447a7879452b586b53347a356d786d70617677415a465447644c4e56774d5a3532314a4e58563650744850414d4d345241736e784f4a4348494843556a3544544c485956764f38776c4c4236537264504a4c306a35384b7174704c49334e385a59587943355144537473737338684e712f79504235366975553670564577674e764a5471534863657066454a6934353049584a326d666454537348526b79377562463367303639417959514e4f3873633050644457706b534e49397764756e58354c666f77494441514142',
  API_BASE: 'https://api.sagapay.no',
  ALLOWED_ORIGINS: ['https://panta.no', 'https://www.panta.no', 'http://panta.no', 'http://www.panta.no', 'https://sagapay.no', 'https://www.sagapay.no', 'http://localhost:3000', 'http://localhost:5500', 'http://127.0.0.1:3000', 'http://127.0.0.1:5500', 'null'],
};

const CUSTOMER = {
  name: 'Ola Nordmann',
  email: 'example@sagapay.no',
  phone: { countryCode: '+47', number: '40548911' },
  billingAddress: {
    addressLine1: 'Karl Johans gate 1',
    city: 'Oslo',
    postalCode: '0154',
    countryCode: 'NO',
  },
};

const ORDER_LINE = {
  id: 'demo-1',
  name: 'Demo Betaling',
  quantity: 1,
  itemAmount: {
    regular: 100,
    total: 100,
    currency: 'NOK',
    tax: [{ amount: 20, percentage: 25, type: 'vat' }],
  },
};

/* ── Helpers ─────────────────────────────────────────── */

function corsHeaders(origin) {
  const isAllowed = CONFIG.ALLOWED_ORIGINS.includes(origin) || /^https?:\/\/(localhost|127\.0\.0\.1)(:\d+)?$/.test(origin);
  const allowed = isAllowed ? origin : CONFIG.ALLOWED_ORIGINS[0];
  return {
    'Access-Control-Allow-Origin': allowed,
    'Access-Control-Allow-Methods': 'POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '86400',
  };
}

function jsonResponse(body, status = 200, origin = '') {
  return new Response(JSON.stringify(body), {
    status,
    headers: { 'Content-Type': 'application/json', ...corsHeaders(origin) },
  });
}

function apiHeaders() {
  return {
    'Content-Type': 'application/json',
    'API-KEY': CONFIG.API_KEY,
    'API-SECRET': CONFIG.API_SECRET,
    'MERCHANT-ID': CONFIG.MERCHANT_ID,
  };
}

/* ── Routes ──────────────────────────────────────────── */

export default {
  async fetch(request) {
    const origin = request.headers.get('Origin') || '';

    if (request.method === 'OPTIONS') {
      return new Response(null, { status: 204, headers: corsHeaders(origin) });
    }

    const url = new URL(request.url);

    if (url.pathname === '/api/session' && request.method === 'POST') {
      return handleCreateSession(origin);
    }

    if (url.pathname === '/api/refund' && request.method === 'POST') {
      return handleRefund(request, origin);
    }

    return new Response('Not Found', { status: 404 });
  },
};

/* ── Create Session ──────────────────────────────────── */

async function handleCreateSession(origin) {
  const referenceId = `demo_${Date.now()}_${crypto.randomUUID().slice(0, 8)}`;

  const body = {
    'terminal$id': CONFIG.TERMINAL_ID,
    type: 'purchase',
    referenceId,
    orderLines: [ORDER_LINE],
    customer: CUSTOMER,
  };

  const res = await fetch(`${CONFIG.API_BASE}/orders`, {
    method: 'POST',
    headers: apiHeaders(),
    body: JSON.stringify(body),
  });

  const data = await res.json();

  if (data.status === 'SUCCESS' && data.data) {
    return jsonResponse(
      {
        orderId: data.data.orderId,
        nonce: data.data.nonce,
        publicKey: CONFIG.PUBLIC_KEY,
      },
      200,
      origin,
    );
  }

  return jsonResponse({ error: 'Failed to create session', detail: data }, 502, origin);
}

/* ── Refund ──────────────────────────────────────────── */

async function handleRefund(request, origin) {
  let payload;
  try {
    payload = await request.json();
  } catch {
    return jsonResponse({ error: 'Invalid request body' }, 400, origin);
  }

  const { orderId } = payload;
  if (!orderId || typeof orderId !== 'string') {
    return jsonResponse({ error: 'Missing orderId' }, 400, origin);
  }

  // 1. Create return order
  const returnBody = {
    'terminal$id': CONFIG.TERMINAL_ID,
    type: 'return',
    referenceId: `refund_${Date.now()}_${crypto.randomUUID().slice(0, 8)}`,
    purchaseOrderId: orderId,
    orderLines: [ORDER_LINE],
  };

  const createRes = await fetch(`${CONFIG.API_BASE}/orders`, {
    method: 'POST',
    headers: apiHeaders(),
    body: JSON.stringify(returnBody),
  });

  const createData = await createRes.json();

  if (createData.status !== 'SUCCESS' || !createData.data) {
    return jsonResponse({ error: 'Return order creation failed' }, 502, origin);
  }

  // 2. Initiate refund payment
  const paymentRes = await fetch(`${CONFIG.API_BASE}/payments`, {
    method: 'POST',
    headers: apiHeaders(),
    body: JSON.stringify({
      orderId: createData.data.orderId,
      paymentMethod: 'CARD_NP',
      refundReason: 'CUSTOMER_INITIATED_RETURN',
    }),
  });

  const paymentData = await paymentRes.json();

  if (paymentData.status === 'SUCCESS') {
    return jsonResponse({ status: 'refunded' }, 200, origin);
  }

  return jsonResponse({ error: 'Refund initiation failed' }, 502, origin);
}
