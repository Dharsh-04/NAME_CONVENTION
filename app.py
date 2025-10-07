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

# ✅ Updated Meta Platforms and Placements
platform_opts = [
    "Select Platform",
    "FB – Facebook",
    "IG – Instagram",
    "MSN – Messenger",
    "AN – Audience Network",
    "WA – WhatsApp",
    "THR – Threads",
    "FBIG – Facebook + Instagram",
    "FBMSN – Facebook + Messenger",
    "FBAN – Facebook + Audience Network",
    "ALL – All Meta Platforms"
]

funnel_opts = ["Select Funnel",
               "TO – Top of Funnel", "MO – Middle of Funnel", "BO – Bottom of Funnel"]

objective_opts = ["Select Objective",
                  "COV – Conversion", "TRA – Traffic", "ENG – Engagement",
                  "MSG – Messages", "PUR – Purchase", "INS – Installs",
                  "LID – Lead Gen", "VDO – Video Views", "AWA – Awareness", "RCH – Reach"]

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

# 🌍 Region
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

# ✅ Updated Placement Options (Meta-supported)
placement_opts = [
    "Select Placement",
    "FBFEED – Facebook Feed",
    "FBVID – Facebook Video Feed",
    "FBSTORY – Facebook Stories",
    "FBREEL – Facebook Reels",
    "FBMARKET – Facebook Marketplace",
    "FBRIGHT – Facebook Right Column",
    "FBSEARCH – Facebook Search Results",
    "IGFEED – Instagram Feed",
    "IGEXP – Instagram Explore",
    "IGREEL – Instagram Reels",
    "IGSTORY – Instagram Stories",
    "MSNINBOX – Messenger Inbox",
    "MSNSTORY – Messenger Stories",
    "ANINAPP – Audience Network In-App",
    "ANREWARD – Audience Network Rewarded Video",
    "WASTATUS – WhatsApp Status",
    "THREADFEED – Threads Feed",
    "ALL – All Placements (Auto)"
]
