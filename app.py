import streamlit as st
import requests
from datetime import date

st.set_page_config(page_title="Meta Ads Naming Generator", layout="centered")
st.title("Meta Ads Naming Convention Generator")

# ---------------- helper funcs ----------------
def short(v):
    """Return abbreviation (text before '–' or first token)"""
    if not v or v.startswith("Select"):
        return ""
    return v.split("–")[0].strip() if "–" in v else v.split(" ")[0].strip()

def region_code(country, state):
    """Convert country,state to code like IN-TN"""
    if not country or country == "Select Country":
        return ""
    ccode = country[:2].upper()
    if not state or state == "Select State":
        return ccode
    parts = state.split()
    scode = (parts[0][0] + (parts[1][0] if len(parts) > 1 else "")).upper()
    return f"{ccode}-{scode}"

# ===========================================================
# 🎯 CAMPAIGN
# ===========================================================
st.header("🎯 Campaign Details")

col1, col2 = st.columns(2)
with col1:
    campaign_date = st.date_input("Campaign Date", value=None)
    date_code = campaign_date.strftime("%d%m%y") if campaign_date else ""
with col2:
    campaign_digit = st.number_input("Campaign Number (1–9)", min_value=0, max_value=9, step=1, value=None, format="%d")
campaign_id = f"{int(campaign_digit)}00" if campaign_digit else ""

platform_opts = ["Select Platform",
                 "FB – Facebook", "IG – Instagram", "MSN – Messenger", "AN – Audience Network", "ALL – All Platforms"]
funnel_opts = ["Select Funnel",
               "TO – Top of Funnel", "MO – Middle of Funnel", "BO – Bottom of Funnel"]
objective_opts = ["Select Objective",
                  "COV – Conversion", "TRA – Traffic", "ENG – Engagement",
                  "MSG – Messages", "PUR – Purchase", "INS – Installs"]
budget1_opts = ["Select Type",
                "ABO – Ad Set Budget", "CBO – Campaign Budget"]
budget2_opts = ["Select Type",
                "DB – Daily Budget", "MB – Monthly Budget", "LTB – Lifetime Budget"]
stage_opts = ["Select Stage",
              "TST – Test", "SCL – Scale"]
bid_opts = ["Select Bid Strategy",
            "LC – Lowest Cost", "CO – Cost Cap", "BC – Bid Cap", "MI – Min ROAS"]

col1, col2, col3 = st.columns(3)
with col1:
    platform = st.selectbox("Platform", platform_opts, index=0)
    funnel = st.selectbox("Funnel", funnel_opts, index=0)
    objective = st.selectbox("Objective", objective_opts, index=0)
with col2:
    audience1 = st.text_input("Audience 1 (shortform)", placeholder="ECO / RET / INT")
    audience2 = st.text_input("Audience 2 (shortform)", placeholder="Optional")
    budget1 = st.selectbox("Budget Type 1", budget1_opts, index=0)
with col3:
    budget2 = st.selectbox("Budget Type 2", budget2_opts, index=0)
    test_or_scale = st.selectbox("Stage", stage_opts, index=0)
    bid_strategy = st.selectbox("Bid Strategy", bid_opts, index=0)

st.subheader("🌍 Region / Market")
try:
    countries_data = requests.get("https://countriesnow.space/api/v0.1/countries/states", timeout=8).json()
    countries = [c["name"] for c in countries_data["data"]]
except Exception:
    countries, countries_data = [], {"data": []}
    st.warning("Could not fetch country list (offline mode).")

country = st.selectbox("Country", ["Select Country"] + countries, index=0)
states = []
if country != "Select Country":
    for c in countries_data["data"]:
        if c["name"] == country:
            states = [s["name"] for s in c["states"]]
            break
state = st.selectbox("State / Region", ["Select State"] + states if states else ["Select State"], index=0)
region_short = region_code(country, state)
price = st.text_input("Offer / Price", placeholder="RS399")

# campaign name pattern
campaign_name = ""
if all([date_code, campaign_id, short(platform), short(funnel), short(objective),
        audience1, budget1 != "Select Type", budget2 != "Select Type",
        test_or_scale != "Select Stage", region_short, bid_strategy != "Select Bid Strategy", price]):
    campaign_name = (
        f"{date_code}-{campaign_id}-{short(platform)}-"
        f"{short(funnel)}-{short(objective)}-{audience1}-{audience2}"
        f"{short(budget1)}-{short(budget2)}-{short(test_or_scale)}-"
        f"{region_short}-{short(bid_strategy)}-{price}"
    )

st.subheader("🪧 Campaign Name")
if campaign_name:
    st.text_input("📋 Copy to Clipboard ↓", value=campaign_name, disabled=False)
else:
    st.info("Fill required fields to generate campaign name.")

st.divider()

# ===========================================================
# 🧩 AD SET
# ===========================================================
st.header("🧩 Ad Set Details")

col1, col2 = st.columns(2)
with col1:
    adset_digit = st.number_input("Ad Set Number (1–9)", min_value=0, max_value=9, step=1, value=None, format="%d")
    adset_id = f"{int(campaign_digit)}{int(adset_digit)}0" if campaign_digit and adset_digit else ""
with col2:
    audience_type = st.text_input("Audience Type (shortform)", placeholder="NAB / ECO / RET")

placement_opts = ["Select", "FB – Facebook Feed", "IG – Instagram Feed",
                  "REEL – Reels", "STORY – Stories", "MIX – Mixed", "ALL – All Placements"]
attrib_opts = ["Select", "1DC1V – 1-Day Click 1-Day View",
               "7DC1V – 7-Day Click 1-Day View", "7DC – 7-Day Click", "1DC – 1-Day Click"]

col1, col2, col3 = st.columns(3)
with col1:
    placement = st.selectbox("Placement", placement_opts, index=0)
    attribution = st.selectbox("Attribution", attrib_opts, index=0)
with col2:
    bid_strategy_adset = st.selectbox("Bid Strategy (Ad Set)", bid_opts, index=0)
with col3:
    platform_adset = st.selectbox("Platform (Ad Set)", platform_opts, index=0)

region_adset_manual = st.text_input("Region Override (optional)", placeholder="If blank, campaign region used")
region_adset = region_adset_manual.strip() if region_adset_manual else region_short

adset_name = ""
if all([date_code, adset_id, audience_type, placement != "Select",
        attribution != "Select", bid_strategy_adset != "Select Bid Strategy",
        platform_adset != "Select Platform", region_adset]):
    adset_name = (
        f"{date_code}-{adset_id}-{audience_type}-"
        f"{short(placement)}-{short(attribution)}-"
        f"{short(bid_strategy_adset)}-{short(platform_adset)}-{region_adset}"
    )

st.subheader("🧾 Ad Set Name")
if adset_name:
    st.text_input("📋 Copy to Clipboard ↓", value=adset_name, disabled=False)
else:
    st.info("Fill required fields to generate ad set name.")

st.divider()

# ===========================================================
# 🎬 AD
# ===========================================================
st.header("🎬 Ad Details")

col1, col2 = st.columns(2)
with col1:
    ad_digit = st.number_input("Ad Number (1–9)", min_value=0, max_value=9, step=1, value=None, format="%d")
    ad_id = f"{int(campaign_digit)}{int(adset_digit)}{int(ad_digit)}" if campaign_digit and adset_digit and ad_digit else ""
with col2:
    adname_custom = st.text_input("Ad Name (shortform)", placeholder="AD1")

variation_opts = ["Select", "V1 – Variation 1", "V2 – Variation 2", "V3 – Variation 3", "Other – Custom Variation"]
creative_opts = ["Select", "VID – Video", "IMG – Image", "CAR – Carousel"]
cta_opts = ["Select", "CONV – Conversion", "INS – Install"]

col1, col2, col3 = st.columns(3)
with col1:
    variation_choice = st.selectbox("Variation", variation_opts, index=0)
    variation_custom = st.text_input("Custom Variation (if Other)", placeholder="VC") if "Other" in variation_choice else ""
    variation = variation_custom if "Other" in variation_choice else variation_choice
with col2:
    creative_type = st.selectbox("Creative Type", creative_opts, index=0)
with col3:
    cta = st.selectbox("CTA", cta_opts, index=0)

caption_id = st.text_input("Caption ID (shortform)", placeholder="CAP1")

ad_name = ""
if all([date_code, ad_id, adname_custom, variation != "Select",
        creative_type != "Select", cta != "Select", caption_id]):
    ad_name = f"{date_code}-{ad_id}-{adname_custom}-{short(variation)}-{short(creative_type)}-{short(cta)}-{caption_id}"

st.subheader("🎥 Ad Name")
if ad_name:
    st.text_input("📋 Copy to Clipboard ↓", value=ad_name, disabled=False)
else:
    st.info("Fill required fields to generate ad name.")

st.divider()

# ===========================================================
# 📋 Summary
# ===========================================================
st.subheader("📋 Summary Preview")
if campaign_name or adset_name or ad_name:
    st.text_area("All Generated Names ↓",
                 f"Campaign: {campaign_name}\nAd Set: {adset_name}\nAd: {ad_name}",
                 height=120)
