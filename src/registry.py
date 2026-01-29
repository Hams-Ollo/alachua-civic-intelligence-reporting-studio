from typing import List, Dict

# Registry of monitored sources structured by Tier and Priority
SOURCE_REGISTRY = {
    "tier_1_city": [
        {
            "name": "City Meeting Portal (CivicClerk)",
            "url": "https://alachuafl.portal.civicclerk.com/",
            "priority": "CRITICAL",
            "notes": "Definitive source for agendas/minutes"
        },
        {
            "name": "Development Projects Map",
            "url": "https://www.cityofalachua.com/government/planning-community-development/planning-zoning/land-use-map",
            "priority": "CRITICAL",
            "notes": "Project pipeline tracking"
        },
        {
            "name": "Planning Department",
            "url": "https://www.cityofalachua.com/i-want-to/planning-community-development",
            "priority": "HIGH",
            "notes": "Submission requirements and LDRs"
        }
    ],
    "tier_2_county": [
        {
            "name": "County Meeting Portal (eScribe)",
            "url": "https://pub-alachuacounty.escribemeetings.com/",
            "priority": "CRITICAL",
            "notes": "DRC and BOCC meetings"
        },
        {
            "name": "Map Genius",
            "url": "https://mapgenius.alachuacounty.us/development-projects/",
            "priority": "CRITICAL",
            "notes": "County-wide project tracking"
        }
    ],
    "tier_3_state": [
        {
            "name": "SRWMD E-Permitting",
            "url": "https://www.mysuwanneeriver.com/8/Permits-Rules",
            "priority": "CRITICAL",
            "notes": "Search for Tara Forest/Moukhtara"
        },
        {
            "name": "FDEP Oculus",
            "url": "https://floridadep.gov/water/submerged-lands-environmental-resources-coordination/content/finding-erp-permit-dep-internet",
            "priority": "HIGH",
            "notes": "State permit record system"
        }
    ],
    "tier_4_notices": [
        {
            "name": "Mainstreet Daily News Notices",
            "url": "https://www.mainstreetdailynews.com/public-notices",
            "priority": "CRITICAL",
            "notes": "Official legal notices"
        }
    ]
}

def get_critical_urls() -> List[str]:
    """Returns a flat list of all CRITICAL URLs across all tiers."""
    urls = []
    for tier, sources in SOURCE_REGISTRY.items():
        for source in sources:
            if source["priority"] == "CRITICAL":
                urls.append(source["url"])
    return urls
