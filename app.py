import streamlit as st
import pyperclip

# ----------------------- PAGE CONFIG -----------------------
st.set_page_config(page_title="FB Naming Convention Generator", layout="centered")

st.title("📣 Facebook Ads Naming Convention Generator")
st.caption("Built with ❤️ for structured and automated campaign naming")

st.divider()

# ===========================================================
# ✅ Ensure Campaign Number stays globally available
# ===========================================================
if "campaign_no" not in st.session_state:
    st.session_state.campaign_no = ""

# ===========================================================
# 🎯 CAMPAIGN SECTION
# ===========================================================
st.header("🎯 Campaign Details")

col1, col2, col3 = st.columns(3)
with col1:
    st.session_state.campaign_no = st.text_input("Campaign Number", st.session_state.campaign_no or "032024-1104")
    platform = st.selectbox("Platform", ["FB", "IG", "YT", "TT", "LN"], index=0)
    funnel = st.selectbox("Funnel / Position", ["TO (Top)", "MO (Middle)", "BO (Bottom)"], index=2)
with col2:
    objective = st.selectbox(
        "Objective",
        ["COV - Conversion", "TRA - Traffic", "ENG - Engagement", "LND - Landing Page", "MSG - Messages", "PUR - Purchase"],
        index=0
    )
    audience1 = st.selectbox("Audience 1", ["ECO", "NAB", "RET", "INT"], index=0)
    audience2 = st.text_input("Audience 2 (Optional)", "NAB")
with col3:
    budget1 = st.selectbox("Budget Type 1", ["ABO - Ad Set Budget", "CBO - Campaign Budget"], index=0)
    budget2 = st.selectbox("Budget Type 2", ["DB - Daily Budget", "MB - Monthly Budget"], index=0)
    test_or_scale = st.selectbox("Stage", ["TST - Test", "SCL - Scale"], index=0)

region = st.selectbox("Region / Market", ["IN", "US", "MX", "SG", "UK"], index=0)
bid_strategy = st.selectbox(
    "Bid Strategy (Campaign)",
    ["LC - Lowest Cost", "CO - Cost Cap", "BC - Bid Cap", "MI - Min ROAS"],
    index=0
)
location = st.text_input("Target Country", "USA")
landing_page = st.text_input("Landing Page", "LP1")
pricing = st.text_input("Offer / Pricing", "RS399")

# Extract short codes
campaign_no = st.session_state.campaign_no
objective_short = objective.split(" ")[0]
budget1_short = budget1.split(" ")[0]
budget2_short = budget2.split(" ")[0]
test_short = test_or_scale.split(" ")[0]
bid_short = bid_strategy.split(" ")[0]
funnel_short = funnel.split(" ")[0]

# --- Generate Campaign Name ---
campaign_name = f"{campaign_no}-{funnel_short}-{objective_short}-{audience1}-{audience2}-{budget1_short}-{budget2_short}-{test_short}-{region}-{bid_short}-{location}-{landing_page}-{pricing}"

st.subheader("🪧 Generated Campaign Name")
st.code(campaign_name, language=None)
st.button("📋 Copy Campaign Name", on_click=lambda: pyperclip.copy(campaign_name))

st.divider()

# ===========================================================
# 🧩 AD SET SECTION
# ===========================================================
st.header("🧩 Ad Set Details")
st.caption("Campaign Number automatically included in Ad Set and Ad names.")

col1, col2, col3 = st.columns(3)
with col1:
    adset_suffix = st.text_input("Ad Set Suffix", "A1")
    audience = st.selectbox("Audience Type", ["INT - Interest", "RET - Retargeting", "ECO - Ecom", "NAB - New Audience"], index=0)
with col2:
    placement = st.selectbox("Placement", ["FB", "IG", "REEL", "STORY", "MIX"], index=0)
    attribution = st.selectbox("Attribution Window", ["7DC1V", "1DC1V", "7DC", "1DC"], index=0)
with col3:
    platform_adset = st.selectbox("Platform", ["FB", "IG"], index=0)
    country = st.text_input("Country", "USA")

landing_page_adset = st.text_input("Landing Page (Ad Set)", "LP1")
bid_strategy_adset = st.selectbox(
    "Bid Strategy (Ad Set)",
    ["LC - Lowest Cost", "CO - Cost Cap", "BC - Bid Cap", "MI - Min ROAS"],
    index=0
)
bid_short_adset = bid_strategy_adset.split(" ")[0]
audience_short = audience.split(" ")[0]

# ✅ Automatically prefix Campaign Number
adset_name = f"{campaign_no}-{adset_suffix}-{audience_short}-{placement}-{attribution}-{platform_adset}-{country}-{bid_short_adset}-{landing_page_adset}"

st.subheader("🧾 Generated Ad Set Name")
st.code(adset_name, language=None)
st.button("📋 Copy Ad Set Name", on_click=lambda: pyperclip.copy(adset_name))

st.divider()

# ===========================================================
# 🎬 AD SECTION
# ===========================================================
st.header("🎬 Ad Details")
st.caption("Campaign Number automatically included in Ad names too.")

col1, col2, col3 = st.columns(3)
with col1:
    ad_suffix = st.text_input("Ad Suffix", "A1-V1")
    variation = st.selectbox("Variation", ["V1", "V2", "V3"], index=0)
with col2:
    creative_type = st.selectbox("Creative Type", ["VID - Video", "IMG - Image", "CAR - Carousel"], index=0)
    cta = st.selectbox("CTA (Call to Action)", ["SIN - Sign Up", "LEA - Learn More", "BUY - Buy Now", "DM - Message"], index=0)
with col3:
    caption_id = st.text_input("Caption ID", "CAP1")

creative_short = creative_type.split(" ")[0]
cta_short = cta.split(" ")[0]

# ✅ Automatically prefix Campaign Number
ad_name = f"{campaign_no}-{ad_suffix}-{variation}-{creative_short}-{cta_short}-{caption_id}"

st.subheader("🎥 Generated Ad Name")
st.code(ad_name, language=None)
st.button("📋 Copy Ad Name", on_click=lambda: pyperclip.copy(ad_name))

st.divider()

# ===========================================================
# ✅ SUMMARY
# ===========================================================

