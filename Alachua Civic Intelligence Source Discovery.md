# **Alachua Civic Intelligence Source Discovery: Architectural Blueprint for Automated Governance Monitoring**

## **1\. Executive Intelligence Summary**

The governance landscape of Alachua, Florida, represents a complex intersection of municipal autonomy, county-level environmental oversight, and regional water resource management. For a civic intelligence agent tasked with monitoring this domain, the challenge lies not in a scarcity of data, but in its fragmentation across incompatible digital systems, varying degrees of transparency, and distinct jurisdictional "fiefdoms." The City of Alachua, positioned atop the sensitive karst geology of the Santa Fe River basin, is currently the epicenter of significant land-use friction, best exemplified by the multi-phase "Tara" development projects. These projects serve as a stress test for the monitoring architecture, spanning municipal rezoning petitions, county environmental review committees, and state-level water permitting.

This report establishes a comprehensive infrastructure analysis for identifying, cataloging, and prioritizing the public information sources necessary to construct an automated monitoring grid. The objective is to transition from reactive observation—waiting for a newspaper headline—to proactive intelligence gathering, where the initial filing of a permit application or the posting of a draft agenda triggers an immediate analytical alert.

The analysis is structured into six hierarchical tiers, moving from the hyper-local municipal layer up to state-level oversight and parallel civic society monitoring. A central finding of this research is the critical importance of the "Notice Gap"—the temporal lag between a document's internal generation by government staff and its public dissemination via statutory notice. By targeting upstream sources, such as staff reporting portals and technical review committee agendas, automated agents can gain weeks or months of lead time over standard public monitoring channels.

Furthermore, this report identifies a significant reliance on third-party software providers—Granicus, CivicClerk, eScribe, and Municode—which host the City and County's digital records. Understanding the API constraints and scraping behaviors of these platforms is as important as the content they hold. The following sections detail the specific URLs, data formats, and monitoring strategies for every relevant node in the Alachua governance network, providing the metadata requisite for configuring high-fidelity scraping agents (e.g., Firecrawl) and natural language processing pipelines.

## ---

**2\. Strategic Context: The Alachua-Santa Fe Ecosystem**

To effectively configure monitoring priorities, one must understand the geopolitical and environmental "terrain" of the target area. The City of Alachua is not merely an administrative unit; it is a rapid-growth zone located along the I-75 corridor, acting as a gateway to the springs country of North Central Florida.

### **2.1 The "Tara" Development Case Study**

Throughout this report, the "Tara" developments (Tara Forest, Tara Phoenicia, Tara Esmeralda, Tara Larga) are referenced as a primary use case for source validation. These projects, involving over 1,000 homes and commercial spaces near the Mill Creek Sink, illustrate the necessity of cross-tier monitoring.1

* **Municipal Layer:** The City Commission handles the rezoning and "Special Exception" permits for stormwater basins.1  
* **County Layer:** The Alachua County Environmental Protection Department (EPD) reviews impacts on the Floridan Aquifer, often appearing in "Development Review Committee" (DRC) agendas rather than City meetings.1  
* **State/Regional Layer:** The Suwannee River Water Management District (SRWMD) issues Environmental Resource Permits (ERPs) for the physical alteration of the land.3  
* **Legal Layer:** Challenges to these decisions end up in the Division of Administrative Hearings (DOAH) or the Circuit Court.4

An automated agent focusing solely on the City of Alachua website 5 would miss the critical environmental reviews occurring at the County and District levels, thereby failing to provide a complete intelligence picture.

### **2.2 The Karst Imperative**

The environmental sensitivity of the region, characterized by unconfined aquifers and high sinkhole potential, drives the political monitoring priority. Keywords such as "karst," "sinkhole," "nitrate," "consumptive use," and "minimum flows and levels" (MFLs) are not just environmental terms; they are political triggers that signal high-conflict regulatory events. The monitoring grid must be tuned to detect these terms across all tiers, from the text of a City ordinance to the technical appendices of a Water Management District staff report.

## ---

**3\. Tier 1: City of Alachua – The Municipal Core**

The City of Alachua functions as the primary "originator" of land use change. It possesses Home Rule powers that allow it to annex land, rezone property, and issue development orders. The digital infrastructure of the City is modernized but bifurcated, utilizing a general CMS for public information and specialized portals for legislative management.

### **3.1 Official Government Portals and Departmental Intelligence**

The primary entry point for municipal intelligence is the official domain, cityofalachua.com. While visually unified, the backend consists of disparate databases for news, employment, and departmental records.

#### **3.1.1 The Central Hub and Administration**

The main website serves as the directory for all sub-agencies. While low-frequency in terms of critical regulatory data, it is high-priority for "signal detection" regarding administrative changes, emergency declarations, and public relations messaging which often precedes legislative action.

| Metadata Field | Source Details |
| :---- | :---- |
| **Source Name** | City of Alachua Official Website (Main Portal) |
| **URL** | https://www.cityofalachua.com/ 5 |
| **Tier** | 1 |
| **Category** | Government Portal / General Administration |
| **Update Frequency** | Daily |
| **Monitoring Priority** | High |
| **Data Format** | HTML (Granicus CMS) |
| **RSS Feed** | Yes (/rss or specific component feeds) 8 |
| **Firecrawl Notes** | Standard HTML structure. Navigation menus are nested in \<ul\> lists. "I Want To..." menu is dynamic. |
| **Keywords** | "Tara", "Annexation", "Emergency", "Notice", "City Manager" |

**Deep Analysis:** The "Government" and "I Want To..." menus are the primary navigational nodes.5 The "City Manager" page is critical for retrieving the "City Manager's Report," a document often attached to agendas that summarizes operational activities and upcoming strategic shifts before they become ordinances. The "City Clerk" section is the gateway to public records, but notably, the City uses specialized sub-portals for heavy data lifting, meaning the main site is primarily a signpost.

#### **3.1.2 Planning & Community Development (PCD)**

This is the "Situation Room" for development monitoring. The PCD Department manages the Comprehensive Plan, Land Development Regulations (LDRs), and the intake of all development applications.

| Metadata Field | Source Details |
| :---- | :---- |
| **Source Name** | Planning & Community Development Department |
| **URL** | https://www.cityofalachua.com/i-want-to/planning-community-development 9 |
| **Tier** | 1 |
| **Category** | Development Services / Permitting |
| **Update Frequency** | Weekly |
| **Monitoring Priority** | **Critical** |
| **Data Format** | HTML, PDF (embedded forms and reports) |
| **Firecrawl Notes** | Look for sub-pages: "Planning Division," "Development Projects Map." PDF links often change with updates. |
| **Keywords** | "Site Plan", "Rezoning", "Special Exception", "LDR", "Comprehensive Plan" |

**Deep Analysis:** The "Planning Division" sub-page acts as the repository for the "Development Review Process" documents.9 Monitoring this page is essential for capturing the *start* of the "Tara" lifecycle. When a developer submits a preliminary site plan, it often sits in this department's internal review queue before appearing on a public agenda. The "Applications, Forms, & Reports" section 9 must be scraped to detect updates to the "Submission Requirements," which can indicate tightening or loosening of regulatory standards. The department also enforces consistency with the Comprehensive Plan 9, so any "Text Amendment" applications found here are strategic indicators of long-term city planning shifts.

#### **3.1.3 Public Services and Utilities**

Infrastructure precedes density. The Public Services Department manages the water, wastewater, and road networks that make development possible.

| Metadata Field | Source Details |
| :---- | :---- |
| **Source Name** | Public Services Department |
| **URL** | https://www.cityofalachua.com/government/public-services 5 |
| **Tier** | 1 |
| **Category** | Infrastructure / Utilities |
| **Update Frequency** | Monthly / As-needed |
| **Monitoring Priority** | Medium |
| **Data Format** | HTML |
| **Firecrawl Notes** | Static content mostly. Watch for "News" or "Project Updates" sections. |
| **Keywords** | "Capacity", "Wastewater", "Road Closure", "Capital Improvement" |

**Deep Analysis:**

While less dynamic, this source is vital for validating the feasibility of proposed developments. A "Tara" phase cannot proceed without "Public Services" signing off on utility capacity. Monitoring for "Utility Outage" reports or "Capital Improvement Plan" updates here provides the physical context for the regulatory decisions made by the Commission.

### **3.2 Legislative Tracking: The CivicClerk Ecosystem**

The City of Alachua has migrated its legislative management to **CivicClerk**, a specialized platform that structures meeting data much more rigorously than a standard website. This is the single most important source for definitive government action.

| Metadata Field | Source Details |
| :---- | :---- |
| **Source Name** | City of Alachua Meeting Portal (CivicClerk) |
| **URL** | https://alachuafl.portal.civicclerk.com/ 10 |
| **Tier** | 1 |
| **Category** | Meeting Agendas & Minutes |
| **Update Frequency** | Bi-monthly (Agenda posted Friday before meetings) |
| **Monitoring Priority** | **Critical** |
| **Data Format** | HTML (List view), PDF (Packets), JSON (via XHR monitoring) |
| **API Available** | No public API documented, but CivicClerk often has predictable endpoints. |
| **Firecrawl Notes** | The portal uses dynamic loading. Agents must parse the "Upcoming Meetings" table. The "Agenda" link usually triggers a PDF download or a secondary HTML view. |
| **Keywords** | "Ordinance", "Resolution", "Public Hearing", "Tara", "Mill Creek", "Quasi-Judicial" |

**Deep Analysis:**

* **The Agenda Packet:** The "Agenda" link is insufficient. The intelligence gold mine is the "Packet" or "Agenda Packet," which combines the agenda with all staff reports, maps, legal opinions, and citizen correspondence. For the "Tara" project, the packet would contain the specific engineering studies regarding sinkhole risk that were debated by the board.1 Automated agents must be configured to OCR these large PDFs.  
* **Meeting Cadence:** "City Commission" meets the second and fourth Mondays at 6:00 PM.11 "Planning and Zoning Board" meets the second Tuesday.10 "Community Redevelopment Agency Board" (CRAAB) meets occasionally on Mondays.10  
* **Video Archive:** The video archive is hosted separately or linked through the portal. Post-meeting analysis should involve transcribing these videos to capture "soft" intelligence—tone of voice, hesitancy, and informal comments—that do not appear in the official minutes.

### **3.3 Visual and Spatial Intelligence: GIS Systems**

Text describes where development happens; maps prove it. The City utilizes ArcGIS-based tools to provide transparency on zoning and active projects.

| Metadata Field | Source Details |
| :---- | :---- |
| **Source Name** | Interactive Zoning & Land Use Map |
| **URL** | https://hub.arcgis.com/maps/acgm::city-of-alachua-zoning 12 |
| **Tier** | 1 |
| **Category** | GIS / Maps |
| **Update Frequency** | As-needed (Legislative updates) |
| **Monitoring Priority** | High |
| **Data Format** | ArcGIS Web Map / REST Service (JSON) |
| **Firecrawl Notes** | Do not scrape the visual map. Monitor the underlying Feature Layer JSON service. Changes in ZONECODE or ZONEDEFIN indicate rezoning. |
| **Keywords** | "PD-R", "RMF-15", "Commercial", "Conservation" |

| Metadata Field | Source Details |
| :---- | :---- |
| **Source Name** | Development Projects Map |
| **URL** | https://www.cityofalachua.com/government/planning-community-development/planning-zoning/land-use-map 13 |
| **Tier** | 1 |
| **Category** | Project Tracking |
| **Update Frequency** | Monthly |
| **Monitoring Priority** | **Critical** |
| **Data Format** | Embedded Map / HTML |
| **Firecrawl Notes** | This page explicitly lists "recently approved and proposed development projects." The map identifies location and status.14 |
| **Keywords** | "Proposed", "Under Review", "Approved", "Tara" |

**Deep Analysis:** The "Development Projects Map" is a specific dashboard for tracking the "pipeline." Unlike the zoning map, which shows the *current* law, this map shows *intent*. A change here (e.g., a new pin dropping on the "Tara" site) is often the very first public signal of a new phase.14

### **3.4 Push Notification and Citizen Alerts**

To reduce latency, the system should ingest data pushed directly by the City.

| Metadata Field | Source Details |
| :---- | :---- |
| **Source Name** | City of Alachua "Notify Me" |
| **URL** | https://www.cityofalachua.com/government/global-pages/connect/subscribe 15 |
| **Tier** | 1 |
| **Category** | Email / SMS Alerts |
| **Update Frequency** | Real-time |
| **Monitoring Priority** | Medium |
| **Data Format** | Email / SMS |
| **Notes** | Requires account creation.16 Subscriptions should include "City Commission Agendas," "Planning Board," and "Public Notices." |

## ---

**4\. Tier 2: Alachua County – The Regulatory Overlay**

The City of Alachua does not exist in a vacuum. It is surrounded by unincorporated Alachua County, and many of its major environmental and growth management frameworks are interlocked with the County's strict regulations. The "Tara" project, located near I-75 and US-441, triggers County-level review due to its scale and environmental impact.17

### **4.1 Board of County Commissioners (BOCC) and Committees**

The County's legislative infrastructure is more robust than the City's, utilizing **eScribe** for meeting management.

| Metadata Field | Source Details |
| :---- | :---- |
| **Source Name** | Alachua County Meeting Portal (eScribe) |
| **URL** | https://pub-alachuacounty.escribemeetings.com/ 18 |
| **Tier** | 2 |
| **Category** | Meeting Agendas & Minutes |
| **Update Frequency** | Daily (Various boards) |
| **Monitoring Priority** | **Critical** |
| **Data Format** | HTML, PDF, Video |
| **Firecrawl Notes** | The page lists *all* boards. Filtering is required. The Calendar List view is the most scrape-friendly. |
| **Keywords** | "Joint Meeting", "Annexation", "Springs", "Tara", "Urban Service Area" |

**Deep Analysis:**

* **Development Review Committee (DRC):** This body is the technical gatekeeper. Projects are often reviewed here for engineering compliance months before they reach the BOCC. Monitoring DRC agendas 18 is a high-value "upstream" tactic.  
* **Joint Meetings:** The portal lists "Joint Meeting \- City of Alachua".18 These meetings address high-level strategy and interlocal agreements.  
* **Environmental Protection Advisory Committee (EPAC):** This citizen board advises the BOCC on environmental policy. Their minutes often contain the "scientific dissent" against development projects that doesn't make it into the final staff report.

### **4.2 Growth Management and Map Genius**

Alachua County possesses one of the most advanced GIS monitoring tools in the state: **Map Genius**.

| Metadata Field | Source Details |
| :---- | :---- |
| **Source Name** | Map Genius (Development Projects) |
| **URL** | https://mapgenius.alachuacounty.us/development-projects/ 19 |
| **Tier** | 2 |
| **Category** | GIS / Project Tracking |
| **Update Frequency** | Real-time / Daily |
| **Monitoring Priority** | **Critical** |
| **Data Format** | Interactive Web App / JSON |
| **Firecrawl Notes** | The application lists active projects on the left panel (e.g., "Tara Esmeralda – Phase 2", "Tara Larga"). This list is dynamically generated and must be scraped periodically. |
| **Keywords** | "Tara", "Subdivision", "Mixed-Use", "Under Construction" |

**Deep Analysis:** This tool provides a "God View" of development. It categorizes projects by stage (Under Review, Under Construction) and explicitly links them to "related documents" and "scheduled hearings".19 This effectively aggregates data that is otherwise scattered across the Growth Management website. For the "Tara" projects, Map Genius lists multiple active phases (Esmeralda, Larga, Verde, Vista) 19, confirming the massive scale of the development and the need for coordinated monitoring.

### **4.3 Environmental Protection Department (EPD)**

The EPD is the County's environmental conscience, enforcing stricter standards than the state in some areas.

| Metadata Field | Source Details |
| :---- | :---- |
| **Source Name** | Environmental Protection Department |
| **URL** | https://alachuacounty.us/Depts/epd/Pages/EPD.aspx 20 |
| **Tier** | 2 |
| **Category** | Environmental Monitoring |
| **Update Frequency** | Monthly |
| **Monitoring Priority** | High |
| **Data Format** | HTML, PDF Reports |
| **Notes** | Key sections: "Water Resources," "Natural Resources," "Stormwater." EPD staff contacts (Greg Owen, Stacie Greco) 21 are often the recipients of technical inquiries regarding springs protection. |

### **4.4 Interlocal Agreements and Contracts**

The relationship between City and County is governed by contracts.

| Metadata Field | Source Details |
| :---- | :---- |
| **Source Name** | Cobblestone Contract Search |
| **URL** | https://alachuacounty.cobblestone.software/public/Default.aspx 23 |
| **Tier** | 2 |
| **Category** | Contracts / Legal |
| **Update Frequency** | As-needed |
| **Monitoring Priority** | Medium |
| **Data Format** | Database Query / PDF |
| **Firecrawl Notes** | Requires form submission. Search for "City of Alachua" as the counterparty. |
| **Keywords** | "Interlocal", "Annexation", "Fire Rescue", "911" |

**Deep Analysis:** This database contains the "DNA" of shared governance. For example, agreements on "9-1-1 Call Transfers" and "Solid Waste Management" 23 define operational boundaries. A new "Joint Planning Agreement" found here would signal a major shift in how the City and County manage the urban fringe.

## ---

**5\. Tier 3: Regional Water Management & Environmental Resources**

In Florida, water does not follow political boundaries. The Suwannee River Water Management District (SRWMD) and the Florida Department of Environmental Protection (FDEP) hold the ultimate veto power over development via Environmental Resource Permits (ERPs).

### **5.1 Suwannee River Water Management District (SRWMD)**

The SRWMD manages the water resources for the region, including the Santa Fe River basin.

| Metadata Field | Source Details |
| :---- | :---- |
| **Source Name** | SRWMD E-Permitting Portal |
| **URL** | https://www.mysuwanneeriver.com/8/Permits-Rules 3 |
| **Tier** | 3 |
| **Category** | Permitting (ERP / WUP) |
| **Update Frequency** | Daily |
| **Monitoring Priority** | **Critical** |
| **Data Format** | HTML / Database Query Result |
| **Firecrawl Notes** | The portal allows searching by "owner name" or "application number".24 It is a distinct sub-system from the main site. |
| **Keywords** | "Tara Forest", "Sayed Moukhtara", "Stormwater", "Consumptive Use" |

**Deep Analysis:**

* **ERP (Environmental Resource Permits):** Any significant development ("Tara") requires an ERP for stormwater management. This is often the *most detailed* technical file available, containing drainage calculations, wetland impact assessments, and geotechnical reports on sinkhole risk.  
* **WUP (Water Use Permits):** Large developments or golf courses need WUPs for irrigation. Monitoring this ensures compliance with the "Minimum Flows and Levels" (MFLs) of the Santa Fe River.  
* **Pre-Application Intelligence:** The portal mentions "Pre-apps are free".3 Detecting a pre-application meeting log is the earliest possible indicator of a project's technical scope, often months before a City site plan is filed.

| Metadata Field | Source Details |
| :---- | :---- |
| **Source Name** | SRWMD BMAP Documents (Santa Fe River) |
| **URL** | https://floridadep.gov/sites/default/files/Santa%20Fe%20Final%202018.pdf 25 |
| **Tier** | 3 |
| **Category** | Environmental Policy |
| **Update Frequency** | Annual |
| **Monitoring Priority** | Medium |
| **Notes** | The BMAP (Basin Management Action Plan) dictates nutrient reduction goals. Changes here force changes in local LDRs regarding fertilizer and wastewater. |

### **5.2 Florida Department of Environmental Protection (FDEP)**

The FDEP is the state's environmental enforcer. Its data systems are vast and archival.

| Metadata Field | Source Details |
| :---- | :---- |
| **Source Name** | Oculus Electronic Document Management System |
| **URL** | https://floridadep.gov/water/submerged-lands-environmental-resources-coordination/content/finding-erp-permit-dep-internet 26 |
| **Tier** | 3 |
| **Category** | Document Repository |
| **Update Frequency** | Daily |
| **Monitoring Priority** | **Critical** |
| **Data Format** | TIFF / PDF |
| **Firecrawl Notes** | Oculus is notoriously difficult to scrape. It uses a session-based search interface. The "Nexus" portal is a more user-friendly frontend.26 |
| **Keywords** | "NPDES", "Alachua", "Stormwater", "Notice of Intent" |

**Deep Analysis:** Oculus is the "system of record." Even if a permit is issued by SRWMD, the documentation often resides here or is cross-referenced. The "NPDES Stormwater Program" 27 tracks construction activity. A "Notice of Intent" (NOI) to use a generic permit for stormwater discharge is a definitive signal that ground breaking is imminent.

### **5.3 Florida Department of Transportation (FDOT) District 2**

Infrastructure dictates growth. FDOT District 2 manages I-75 and US-441.

| Metadata Field | Source Details |
| :---- | :---- |
| **Source Name** | FDOT District 2 Construction & Lettings |
| **URL** | https://nflroads.com/ProjectList.aspx?r=6713 28 |
| **Tier** | 3 |
| **Category** | Infrastructure Projects |
| **Update Frequency** | Weekly |
| **Monitoring Priority** | Medium |
| **Data Format** | HTML Table |
| **Keywords** | "US 441", "I-75", "Alachua", "Turn Lane" |

**Deep Analysis:** The "Tara" project 17 requires significant access management (driveways, turn lanes) onto US-441. FDOT permits for "driveway connection" or "drainage connection" are separate from City approvals. The nflroads.com site lists active projects like "U.S. 301 Resurfacing".28 Monitoring "Future Projects" helps anticipate where the state is investing in capacity, which inevitably attracts development.

## ---

**6\. Tier 4: State of Florida – Legislative & Judicial Oversight**

State-level monitoring is required to track preemption laws that strip local authority and to follow legal challenges to land use decisions.

### **6.1 Florida Legislature**

| Metadata Field | Source Details |
| :---- | :---- |
| **Source Name** | Florida Senate Bill Tracking |
| **URL** | https://www.flsenate.gov/Session/Bill/2025/691 29 |
| **Tier** | 4 |
| **Category** | Legislation |
| **Update Frequency** | Real-time (during Session) |
| **Monitoring Priority** | High |
| **Data Format** | HTML / PDF |
| **Keywords** | "Springs Protection", "Preemption", "Comprehensive Plan", "Annexation" |

**Deep Analysis:** Bills like "HB 691: Spring Restoration" 29 directly impact Alachua's obligations under the "Florida Springs and Aquifer Protection Act".30 Monitoring the local delegation (Rep. Chuck Clemons, Sen. Keith Perry) is crucial, as they introduce "Local Bills" that can specifically target Alachua County's regulatory powers.

### **6.2 Administrative and Judicial Courts**

When politics fails, stakeholders sue.

| Metadata Field | Source Details |
| :---- | :---- |
| **Source Name** | Division of Administrative Hearings (DOAH) |
| **URL** | https://www.doah.state.fl.us/ 31 |
| **Tier** | 4 |
| **Category** | Administrative Law |
| **Update Frequency** | Daily |
| **Monitoring Priority** | Medium |
| **Data Format** | HTML Case Search |
| **Keywords** | "Alachua", "Comprehensive Plan Amendment", "Not in Compliance" |

**Deep Analysis:** DOAH is the venue for "Comprehensive Plan" challenges. If the State (Department of Economic Opportunity) or an "affected person" challenges a City of Alachua plan amendment 4, the case is heard here. This is a lagging indicator but highly definitive regarding the legality of major developments.

| Metadata Field | Source Details |
| :---- | :---- |
| **Source Name** | Alachua County Clerk of Court (Civil Records) |
| **URL** | https://www.alachuaclerk.org/court\_records/index.cfm 32 |
| **Tier** | 4 |
| **Category** | Civil Litigation |
| **Update Frequency** | Daily |
| **Monitoring Priority** | High |
| **Data Format** | HTML Search / PDF Images |
| **Notes** | Search for "Plaintiff: Sierra Club" or "Defendant: City of Alachua." |

### **6.3 Corporate Intelligence (Sunbiz)**

| Metadata Field | Source Details |
| :---- | :---- |
| **Source Name** | Florida Division of Corporations (Sunbiz) |
| **URL** | https://search.sunbiz.org/inquiry/corporationsearch/byname 33 |
| **Tier** | 4 |
| **Category** | Entity Registry |
| **Update Frequency** | Real-time |
| **Monitoring Priority** | High |
| **Data Format** | HTML |
| **Keywords** | "Tara Forest", "Tara Phoenicia", "Moukhtara" |

**Deep Analysis:**

Developers often use shell LLCs for each phase of a project ("Tara Forest East", "Tara Forest West"). Sunbiz connects these entities to the actual human principals (e.g., Sayed Moukhtara). Automated monitoring should track *all* entities registered to the principal's address to detect new land acquisitions before a permit is ever filed.

## ---

**7\. Tier 5: News and Media – The Signal Layer**

The media landscape provides both official legal notices and investigative context.

### **7.1 The Official Notice Channel**

| Metadata Field | Source Details |
| :---- | :---- |
| **Source Name** | Mainstreet Daily News (Public Notices) |
| **URL** | https://www.mainstreetdailynews.com/public-notices 34 |
| **Tier** | 5 |
| **Category** | Legal Notices |
| **Update Frequency** | Daily |
| **Monitoring Priority** | **Critical** |
| **Data Format** | HTML / PDF |
| **Firecrawl Notes** | This is the *certified* publisher for Alachua County.34 Notices for hearings must appear here 10-14 days prior. |
| **Keywords** | "Notice of Public Hearing", "Rezoning", "Ordinance", "Variance" |

**Deep Analysis:**

This is the most reliable "catch-all" source. Even if a scraper misses an agenda item on the City website, the law *requires* this publication. An automated agent should parse these notices daily to identify Parcel IDs and hearing dates.

### **7.2 Journalism and Broadcast**

| Metadata Field | Source Details |
| :---- | :---- |
| **Source Name** | WUFT News (Environment) |
| **URL** | https://www.wuft.org/environment 35 |
| **Tier** | 5 |
| **Category** | Public Media / Environment |
| **Update Frequency** | Daily |
| **Monitoring Priority** | High |
| **RSS Feed** | Yes |
| **Notes** | Extensive coverage of springs issues and the "Tara" development delays.2 |

| Metadata Field | Source Details |
| :---- | :---- |
| **Source Name** | Alachua County Today |
| **URL** | https://www.alachuacountytoday.com/ 36 |
| **Tier** | 5 |
| **Category** | Hyperlocal News |
| **Update Frequency** | Weekly |
| **Monitoring Priority** | Medium |
| **Notes** | Covers High Springs and Alachua City Commission in detail. |

| Metadata Field | Source Details |
| :---- | :---- |
| **Source Name** | Florida Bulldog |
| **URL** | https://www.floridabulldog.org/ 37 |
| **Tier** | 5 |
| **Category** | Investigative Watchdog |
| **Update Frequency** | Weekly |
| **Monitoring Priority** | Low |
| **Notes** | Good for deep dives on state-level corruption that might affect local funding. |

## ---

**8\. Tier 6: Civic & Advocacy – The Human Intelligence Layer**

Civic groups act as specialized sensors, often identifying threats to the aquifer long before government regulators act.

### **8.1 Environmental Defenders**

| Metadata Field | Source Details |
| :---- | :---- |
| **Source Name** | Our Santa Fe River (OSFR) |
| **URL** | https://oursantaferiver.org/ 38 |
| **Tier** | 6 |
| **Category** | Advocacy / NGO |
| **Update Frequency** | Weekly (Blog) |
| **Monitoring Priority** | High |
| **RSS Feed** | https://oursantaferiver.org/feed/ (Inferred) |
| **Notes** | Extremely active in monitoring SRWMD permits. Their posts often contain detailed critiques of specific applications.39 |

| Metadata Field | Source Details |
| :---- | :---- |
| **Source Name** | Florida Springs Council |
| **URL** | https://www.floridaspringscouncil.org/ 40 |
| **Tier** | 6 |
| **Category** | Legal Advocacy |
| **Update Frequency** | Monthly |
| **Monitoring Priority** | High |
| **Notes** | A coalition that litigates. Monitoring their "News" or "Legal" section provides insight into ongoing court battles against the FDEP.40 |

| Metadata Field | Source Details |
| :---- | :---- |
| **Source Name** | Sierra Club (Suwannee-St. Johns Group) |
| **URL** | https://www.sierraclub.org/florida/suwannee-stjohns 41 |
| **Tier** | 6 |
| **Category** | Environmental NGO |
| **Update Frequency** | Monthly |
| **Monitoring Priority** | Medium |
| **Notes** | Their "Calendar" and "Newsletters" reveal grassroots mobilization efforts against specific developments like "Tara" or phosphate mines.41 |

### **8.2 Transparency Watchdogs**

| Metadata Field | Source Details |
| :---- | :---- |
| **Source Name** | Florida Center for Government Accountability (FLCGA) |
| **URL** | https://flcga.org/ 42 |
| **Tier** | 6 |
| **Category** | Transparency / Litigation |
| **Update Frequency** | As-needed |
| **Monitoring Priority** | Medium |
| **Notes** | They publish the *Florida Trident*. FLCGA litigates public records denials. If the City of Alachua refuses to release a "Tara" document, FLCGA is the entity that will likely sue to get it.43 |

## ---

**9\. Technical Implementation Architecture**

To operationalize this intelligence, a robust data pipeline is required. The recommended architecture involves:

1. **Ingestion Agents (Spiders):**  
   * **Headless Browsers (Playwright/Puppeteer):** Required for Granicus (City), eScribe (County), and CivicClerk, which rely heavily on JavaScript to render agenda tables.  
   * **PDF Fetchers:** Agents must be configured to identify links ending in .pdf within agenda items and download them to a local S3-compatible bucket.  
   * **OCR Pipeline:** A Tesseract or AWS Textract layer is mandatory. Most "scanned" packet documents (especially older deeds or engineering drawings) are images, not text.  
2. **Entity Resolution Engine:**  
   * A graph database (Neo4j) should link disparate entities: Sayed Moukhtara (Person) \<-\> Tara Forest, LLC (Sunbiz Entity) \<-\> Parcel 03067-000-000 (Map Genius Property) \<-\> ERP Application \#12345 (SRWMD).  
   * This allows the system to flag a "boring" stormwater permit as "Critical" because it is linked to a controversial developer.  
3. **Natural Language Processing (NLP):**  
   * **Named Entity Recognition (NER):** Custom models trained on Florida land use terminology (e.g., recognizing "special exception," "transmittal hearing," "comprehensive plan amendment").  
   * **Sentiment Analysis:** Applied to meeting minutes and NGO blog posts to gauge the "temperature" of public opposition.  
4. **Alerting Logic:**  
   * **Tier 1 Alerts (Immediate):** New agenda posted containing keyword "Tara" or "Annexation."  
   * **Tier 2 Alerts (Daily):** New file in Map Genius or SRWMD portal.  
   * **Tier 3 Alerts (Weekly):** Summary of NGO blog activity and state legislative movement.

## **10\. Conclusion**

The civic intelligence grid for the City of Alachua is defined by its vertical depth—from the bedrock of the Floridan Aquifer to the legislative chambers of Tallahassee. While the City's official portal provides the veneer of transparency, the true indicators of governance activity are hidden in the "Tier 2" and "Tier 3" systems: the County's GIS databases, the Water Management District's permit files, and the State's corporate registries. By implementing the automated monitoring architecture detailed in this report, focusing on the "Notice Gap" and utilizing cross-tier entity resolution, it is possible to achieve total situational awareness of the civic ecosystem, ensuring that no development—whether a single driveway or the massive "Tara" subdivision—proceeds without observation.

#### **Works cited**

1. Alachua planning board shuts down Tara's Mill Creek Sink development, accessed January 28, 2026, [https://www.mainstreetdailynews.com/govt-politics/alachua-planning-board-shuts-down-taras-mill-creek-sink-development](https://www.mainstreetdailynews.com/govt-politics/alachua-planning-board-shuts-down-taras-mill-creek-sink-development)  
2. Alachua board postpones decision on “Tara” stormwater strategy: controversial piece of Mill Creek development plans \- WUFT, accessed January 28, 2026, [https://www.wuft.org/environment/2026-01-14/alachua-board-postpones-decision-on-tara-stormwater-strategy-controversial-piece-of-mill-creek-development-plans](https://www.wuft.org/environment/2026-01-14/alachua-board-postpones-decision-on-tara-stormwater-strategy-controversial-piece-of-mill-creek-development-plans)  
3. Permit TO PROTECT | Suwannee River Water Management District, accessed January 28, 2026, [https://www.mysuwanneeriver.com/8/Permits-Rules](https://www.mysuwanneeriver.com/8/Permits-Rules)  
4. Time Frame and Procedures for a Citizen Challenge to a Comprehensive Plan Amendment \- FloridaJobs.org, accessed January 28, 2026, [https://floridajobs.org/community-planning-and-development/programs/community-planning-table-of-contents/time-frame-and-procedures-for-a-citizen-challenge-to-a-comprehensive-plan-amendment](https://floridajobs.org/community-planning-and-development/programs/community-planning-table-of-contents/time-frame-and-procedures-for-a-citizen-challenge-to-a-comprehensive-plan-amendment)  
5. Public Services | City of Alachua, FL, accessed January 28, 2026, [https://www.cityofalachua.com/government/public-services](https://www.cityofalachua.com/government/public-services)  
6. Government | City of Alachua, FL, accessed January 28, 2026, [https://www.cityofalachua.com/government](https://www.cityofalachua.com/government)  
7. City of Alachua, FL | Home, accessed January 28, 2026, [https://www.cityofalachua.com/](https://www.cityofalachua.com/)  
8. News | City of Alachua, FL, accessed January 28, 2026, [https://www.cityofalachua.com/Home/Components/News/News/91/231](https://www.cityofalachua.com/Home/Components/News/News/91/231)  
9. Planning & Community Development | City of Alachua, FL, accessed January 28, 2026, [https://www.cityofalachua.com/i-want-to/planning-community-development](https://www.cityofalachua.com/i-want-to/planning-community-development)  
10. Events • Agendas & Minutes • CivicClerk, accessed January 28, 2026, [https://alachuafl.portal.civicclerk.com/](https://alachuafl.portal.civicclerk.com/)  
11. Commission Meetings | City of Alachua, FL, accessed January 28, 2026, [https://www.cityofalachua.com/government/city-commission/commission-meetings](https://www.cityofalachua.com/government/city-commission/commission-meetings)  
12. City of Alachua Zoning \- ArcGIS Hub, accessed January 28, 2026, [https://hub.arcgis.com/maps/acgm::city-of-alachua-zoning](https://hub.arcgis.com/maps/acgm::city-of-alachua-zoning)  
13. Development Projects Map | City of Alachua, FL, accessed January 28, 2026, [https://www.cityofalachua.com/government/planning-community-development/planning-zoning/land-use-map](https://www.cityofalachua.com/government/planning-community-development/planning-zoning/land-use-map)  
14. Land Use & Development Projects Online Map | News List | City of Alachua, FL, accessed January 28, 2026, [https://www.cityofalachua.com/Home/Components/News/News/55/15?arch=1\&npage=2](https://www.cityofalachua.com/Home/Components/News/News/55/15?arch=1&npage=2)  
15. Subscribe | City of Alachua, FL, accessed January 28, 2026, [https://www.cityofalachua.com/government/global-pages/connect/subscribe](https://www.cityofalachua.com/government/global-pages/connect/subscribe)  
16. Notify Me • Alachua County Elections, FL • CivicEngage, accessed January 28, 2026, [https://www.votealachua.gov/notifyme](https://www.votealachua.gov/notifyme)  
17. BUCKHOLZ TRAFFIC \- North Florida Roads, accessed January 28, 2026, [https://nflroads.com/ProjectFiles/5525/SS\_COMPLETE\_TaraPhoPhaseI\_Report\_%20(1).pdf](https://nflroads.com/ProjectFiles/5525/SS_COMPLETE_TaraPhoPhaseI_Report_%20\(1\).pdf)  
18. eSCRIBE Published Meetings, accessed January 28, 2026, [https://pub-alachuacounty.escribemeetings.com/](https://pub-alachuacounty.escribemeetings.com/)  
19. Alachua County Development Projects, accessed January 28, 2026, [https://mapgenius.alachuacounty.us/development-projects/](https://mapgenius.alachuacounty.us/development-projects/)  
20. Environmental Protection Department \- Alachua County, accessed January 28, 2026, [https://alachuacounty.us/Depts/epd/Pages/EPD.aspx](https://alachuacounty.us/Depts/epd/Pages/EPD.aspx)  
21. Alachua County Environmental Protection Department \- Water-CAT: The Florida Water Resource Monitoring Catalog, accessed January 28, 2026, [https://water-cat.usf.edu/organizations/details/1](https://water-cat.usf.edu/organizations/details/1)  
22. Alachua County Environmental Protection Department | Our Santa Fe River, Inc. (OSFR), accessed January 28, 2026, [https://oursantaferiver.org/contacts/alachua-county-environmental-protection-department/](https://oursantaferiver.org/contacts/alachua-county-environmental-protection-department/)  
23. Contract Insight \- Contract Management System Public Portal, accessed January 28, 2026, [https://alachuacounty.cobblestone.software/public/Default.aspx](https://alachuacounty.cobblestone.software/public/Default.aspx)  
24. Environmental Resource Permit \- Suwannee River Water Management District, accessed January 28, 2026, [https://www.mysuwanneeriver.com/91/Environmental-Resource-Permit](https://www.mysuwanneeriver.com/91/Environmental-Resource-Permit)  
25. Santa Fe River Basin Management Action Plan \- Florida Department of Environmental Protection, accessed January 28, 2026, [https://floridadep.gov/sites/default/files/Santa%20Fe%20Final%202018.pdf](https://floridadep.gov/sites/default/files/Santa%20Fe%20Final%202018.pdf)  
26. Finding an ERP Permit on the DEP Internet Site | Florida Department of Environmental Protection, accessed January 28, 2026, [https://floridadep.gov/water/submerged-lands-environmental-resources-coordination/content/finding-erp-permit-dep-internet](https://floridadep.gov/water/submerged-lands-environmental-resources-coordination/content/finding-erp-permit-dep-internet)  
27. Find a Permit | Florida Department of Environmental Protection, accessed January 28, 2026, [https://floridadep.gov/water/stormwater/content/find-permit](https://floridadep.gov/water/stormwater/content/find-permit)  
28. Projects \- NFLRoads.com, accessed January 28, 2026, [https://nflroads.com/ProjectList.aspx?r=6713](https://nflroads.com/ProjectList.aspx?r=6713)  
29. House Bill 691 (2025) \- The Florida Senate, accessed January 28, 2026, [https://www.flsenate.gov/Session/Bill/2025/691](https://www.flsenate.gov/Session/Bill/2025/691)  
30. Florida Springs and Aquifer Protection Act \- Online Sunshine, accessed January 28, 2026, [https://www.leg.state.fl.us/statutes/index.cfm?App\_mode=Display\_Statute\&URL=0300-0399/0373/0373PARTVIIIContentsIndex.html](https://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&URL=0300-0399/0373/0373PARTVIIIContentsIndex.html)  
31. Case Search \- Florida Appellate Case Information System \- Florida Courts, accessed January 28, 2026, [https://acis.flcourts.gov/portal/search/case](https://acis.flcourts.gov/portal/search/case)  
32. Court Records \- Clerk of the Court, accessed January 28, 2026, [https://www.alachuaclerk.org/court\_records/index.cfm](https://www.alachuaclerk.org/court_records/index.cfm)  
33. Search for Corporations, Limited Liability Companies, Limited Partnerships, and Trademarks by Name \- SunBiz, accessed January 28, 2026, [https://search.sunbiz.org/inquiry/corporationsearch/byname](https://search.sunbiz.org/inquiry/corporationsearch/byname)  
34. Alachua County Public Notices \- Mainstreet Daily News Gainesville, accessed January 28, 2026, [https://www.mainstreetdailynews.com/public-notices](https://www.mainstreetdailynews.com/public-notices)  
35. Environment \- WUFT, accessed January 28, 2026, [https://www.wuft.org/environment](https://www.wuft.org/environment)  
36. Alachua County Headlines, accessed January 28, 2026, [https://alachuacounty.us/news/pages/default.aspx](https://alachuacounty.us/news/pages/default.aspx)  
37. Florida Bulldog \- Watchdog news you can sink your teeth into, accessed January 28, 2026, [https://www.floridabulldog.org/](https://www.floridabulldog.org/)  
38. Our Santa Fe River, accessed January 28, 2026, [https://oursantaferiver.org/](https://oursantaferiver.org/)  
39. Our Santa Fe River \- InfluenceWatch, accessed January 28, 2026, [https://www.influencewatch.org/non-profit/our-santa-fe-river-inc/](https://www.influencewatch.org/non-profit/our-santa-fe-river-inc/)  
40. Florida Springs Council: Home, accessed January 28, 2026, [https://www.floridaspringscouncil.org/](https://www.floridaspringscouncil.org/)  
41. Suwannee St. Johns Group \- Sierra Club, accessed January 28, 2026, [https://www.sierraclub.org/florida/suwannee-stjohns](https://www.sierraclub.org/florida/suwannee-stjohns)  
42. Florida Center for Government Accountability \- National Freedom of Information Coalition, accessed January 28, 2026, [https://www.nfoic.org/organizations/florida-center-for-government-accountability/](https://www.nfoic.org/organizations/florida-center-for-government-accountability/)  
43. Florida Center for Government Accountability \- Find Your News, accessed January 28, 2026, [https://findyournews.org/organization/florida-center-for-government-accountability/](https://findyournews.org/organization/florida-center-for-government-accountability/)