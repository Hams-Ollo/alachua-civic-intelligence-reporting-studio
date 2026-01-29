import argparse
import sys
from src.agents.scout import ScoutAgent
from src.database import db

def main():
    parser = argparse.ArgumentParser(description="Alachua Civic Intelligence System")
    parser.add_argument("--agent", type=str, required=True, help="Agent to run (e.g., A1, A2)")
    parser.add_argument("--url", type=str, help="Target URL for the scout to monitor")
    parser.add_argument("--critical", action="store_true", help="Run all CRITICAL sources from registry")
    parser.add_argument("--save", action="store_true", help="Save result to Supabase")
    
    args = parser.parse_args()
    
    # Simple registry of agents (expand this as we add more)
    if args.agent.startswith("A"):
        # Initialize Scout
        agent = ScoutAgent(name=args.agent, prompt_template="Standard Scout Prompt")
        
        targets = []
        if args.critical:
            from src.registry import get_critical_urls
            print("🔍 Loading all CRITICAL sources from registry...")
            targets = get_critical_urls()
        elif args.url:
            targets = [args.url]
        else:
            print("Error: Either --url or --critical is required for Scouts.")
            sys.exit(1)
            
        for url in targets:
            try:
                print(f"🚀 Running Agent {args.agent} on {url}...")
                report = agent.run({"url": url})
                
                print("\n✅ Report Generated:")
                print(f"ID: {report.report_id}")
                print(f"Summary: {report.executive_summary}")
                print(f"Alerts: {len(report.alerts)}")
                
                if args.save:
                    print("💾 Saving to Supabase...")
                    db.save_report(report)
                    print("Done.")
            except Exception as e:
                print(f"❌ Error monitoring {url}: {e}")
                # Continue to next target even if one fails
                continue
    elif args.agent.startswith("B"):
        # Initialize Analyst (Deep Research)
        from src.agents.analyst import AnalystAgent
        agent = AnalystAgent(name=args.agent)
        
        # Analyst needs a topic, not necessarily a URL
        topic = args.url if args.url else "Tara Forest Development" # Default to main topic if not specified
        
        try:
            print(f"🧠 Running Analyst {args.agent} on topic: {topic}...")
            report = agent.run({"topic": topic})
            
            print("\n✅ Intelligence Report Generated:")
            print(f"ID: {report.report_id}")
            print(f"Executive Summary: {report.executive_summary}")
            
            if args.save:
                print("💾 Saving to Supabase...")
                db.save_report(report)
                print("Done.")
                
        except Exception as e:
            print(f"❌ Error running analyst: {e}")
            sys.exit(1)
    else:
        print(f"Unknown agent type: {args.agent}")

if __name__ == "__main__":
    main()
