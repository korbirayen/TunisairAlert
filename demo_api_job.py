"""
Demo version - Daily job to process flight data and generate reports (using sample data instead of API calls)
"""
from datetime import datetime
from data_analysis.pillow_reports import generate_report
from data_pipeline.api_requests import AirLabsData

if __name__ == "__main__":
    today = datetime.now()
    
    print(f"Running demo mode for {today.strftime('%Y-%m-%d')}")
    print("Using sample flight data (no API calls needed)")
    
    # Initialize with force_update=False to skip API calls and use existing JSON files
    airlabs = AirLabsData(today, force_update=False)
    
    print("\nProcessing arrivals...")
    airlabs.get_arrivals()
    
    print("Processing departures...")
    airlabs.get_departures()
    
    print("Cleaning SQL table...")
    airlabs.clean_sql_table(today)
    
    print("\nGenerating report...")
    generate_report(today)
    
    print("\n✅ Demo completed! Check the generated report.")
