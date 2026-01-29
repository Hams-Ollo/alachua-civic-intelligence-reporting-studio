# Source Registry

**Status:** Updated from "Source Discovery Blueprint"
**Date:** January 28, 2026

## Tier 1: City of Alachua (Municipal Core)

| Priority | Name | URL | Notes |
| :--- | :--- | :--- | :--- |
| **CRITICAL** | **City Meeting Portal (CivicClerk)** | `https://alachuafl.portal.civicclerk.com/` | The definitive source for agendas/minutes. Better than the main website. |
| **CRITICAL** | **Development Projects Map** | `https://www.cityofalachua.com/government/planning-community-development/planning-zoning/land-use-map` | Lists "Proposed", "Under Review", and "Approved" projects. |
| **High** | **Planning & Community Dev** | `https://www.cityofalachua.com/i-want-to/planning-community-development` | Watch for "Submission Requirements" changes. |
| **High** | **Zoning Map (ArcGIS)** | `https://hub.arcgis.com/maps/acgm::city-of-alachua-zoning` | Monitor via JSON service for zoning code changes. |
| **Medium** | **Public Services** | `https://www.cityofalachua.com/government/public-services` | Infrastructure capacity checks. |
| **Medium** | **Official Website** | `https://www.cityofalachua.com/` | General signal detection (City Manager reports). |

## Tier 2: Alachua County (Regulatory Overlay)

| Priority | Name | URL | Notes |
| :--- | :--- | :--- | :--- |
| **CRITICAL** | **County Meeting Portal (eScribe)** | `https://pub-alachuacounty.escribemeetings.com/` | Watch for "Development Review Committee" and "Joint Meetings". |
| **CRITICAL** | **Map Genius (Dev Projects)** | `https://mapgenius.alachuacounty.us/development-projects/` | The "God View" of all active projects (Tara Esmeralda, Larga, etc). |
| **High** | **Environmental Protection (EPD)** | `https://alachuacounty.us/Depts/epd/Pages/EPD.aspx` | Stricter environmental standards than state. |
| **Medium** | **Contract Search** | `https://alachuacounty.cobblestone.software/public/Default.aspx` | Search for "City of Alachua" interlocal agreements. |

## Tier 3: Regional & State (Water/Environment)

| Priority | Name | URL | Notes |
| :--- | :--- | :--- | :--- |
| **CRITICAL** | **SRWMD E-Permitting** | `https://www.mysuwanneeriver.com/8/Permits-Rules` | Search for "Tara Forest", "Sayed Moukhtara". |
| **Critical** | **FDEP Oculus** | `https://floridadep.gov/water/submerged-lands-environmental-resources-coordination/content/finding-erp-permit-dep-internet` | "System of Record" for state permits. Hard to scrape. |
| **Medium** | **FDOT District 2** | `https://nflroads.com/ProjectList.aspx?r=6713` | Access management permits for US-441. |

## Tier 4: Public & Legal Notices

| Priority | Name | URL | Notes |
| :--- | :--- | :--- | :--- |
| **CRITICAL** | **Mainstreet Daily News (Notices)** | `https://www.mainstreetdailynews.com/public-notices` | Official legal publisher. The "Catch-all" safety net. |
| **High** | **Sunbiz (Corp Search)** | `https://search.sunbiz.org/inquiry/corporationsearch/byname` | Track "Moukhtara" or "Tara Forest LLC". |
| **High** | **Clerk of Court** | `https://www.alachuaclerk.org/court_records/index.cfm` | Litigation tracking. |

## Tier 5: Media & Civic Signals

| Priority | Name | URL | Notes |
| :--- | :--- | :--- | :--- |
| **High** | **WUFT Environment** | `https://www.wuft.org/environment` | In-depth reporting on springs. |
| **High** | **Our Santa Fe River** | `https://oursantaferiver.org/` | Advocacy intel often beats official notice. |
