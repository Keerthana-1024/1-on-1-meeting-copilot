const SUPABASE_URL = window.ENV.SUPABASE_URL;
const SUPABASE_KEY = window.ENV.SUPABASE_KEY;
const db = window.supabase.createClient(SUPABASE_URL, SUPABASE_KEY);

const BLOB_BASE_URL = window.ENV.BLOB_BASE_URL;
const BLOB_SAS_TOKEN = window.ENV.BLOB_SAS_TOKEN;

// ── Session helpers ─────────────────────────────────────────────
function setSession(user, viewRole) {
  localStorage.setItem('ig_user', JSON.stringify(user));
  localStorage.setItem('ig_role', viewRole); // 'manager' | 'reportee'
}
function getUser()     { try { return JSON.parse(localStorage.getItem('ig_user')); } catch { return null; } }
function getViewRole() { return localStorage.getItem('ig_role') || 'reportee'; }
function clearSession(){ localStorage.removeItem('ig_user'); localStorage.removeItem('ig_role'); }
function requireAuth(redirectTo = 'login.html') {
  if (!getUser()) { window.location.href = redirectTo; }
}
