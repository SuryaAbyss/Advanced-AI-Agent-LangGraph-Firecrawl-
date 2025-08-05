#!/usr/bin/env python3
"""
Example script demonstrating how to use the AI Agent for developer tools research.
"""

import os
from src.workflow import Workflow

def main():
    """Main function demonstrating the AI Agent usage."""
    
    print("🤖 AI Agent - Developer Tools Research Assistant")
    print("=" * 50)
    
    # Initialize the workflow
    print("Initializing workflow...")
    workflow = Workflow()
    print("✓ Workflow initialized successfully!")
    
    # Example queries to demonstrate different use cases
    example_queries = [
        "database management tools",
        "cloud deployment platforms", 
        "monitoring and logging tools",
        "authentication providers"
    ]
    
    print(f"\n📋 Available example queries:")
    for i, query in enumerate(example_queries, 1):
        print(f"  {i}. {query}")
    
    # Get user input
    print(f"\n🔍 Enter a query to research (or press Enter for 'database management tools'):")
    user_query = input("Query: ").strip()
    
    if not user_query:
        user_query = "database management tools"
        print(f"Using default query: {user_query}")
    
    print(f"\n🚀 Starting research for: '{user_query}'")
    print("This may take 3-10 minutes depending on the number of tools found...")
    
    try:
        # Run the research workflow
        result = workflow.run(user_query)
        
        # Display results
        print(f"\n✅ Research completed!")
        print("=" * 50)
        
        print(f"📊 Results Summary:")
        print(f"  Query: {result.query}")
        print(f"  Tools Found: {len(result.extracted_tools)}")
        print(f"  Companies Analyzed: {len(result.companies)}")
        
        if result.extracted_tools:
            print(f"\n🛠️  Extracted Tools:")
            for i, tool in enumerate(result.extracted_tools[:5], 1):
                print(f"  {i}. {tool}")
        
        if result.companies:
            print(f"\n🏢 Companies Analyzed:")
            for i, company in enumerate(result.companies[:3], 1):
                print(f"  {i}. {company.name}")
                print(f"     Website: {company.website}")
                print(f"     Pricing: {company.pricing_model or 'Unknown'}")
                print(f"     Open Source: {company.is_open_source or 'Unknown'}")
                if company.tech_stack:
                    print(f"     Tech Stack: {', '.join(company.tech_stack[:3])}")
                print()
        
        if result.analysis:
            print(f"💡 AI Recommendation:")
            print(f"  {result.analysis}")
        
        print(f"\n🎉 Research completed successfully!")
        
    except Exception as e:
        print(f"\n❌ Error during research: {e}")
        print("Please check your API keys and internet connection.")

def test_workflow():
    """Test function to verify the workflow works."""
    print("🧪 Testing workflow initialization...")
    
    try:
        workflow = Workflow()
        print("✓ Workflow test passed!")
        return True
    except Exception as e:
        print(f"✗ Workflow test failed: {e}")
        return False

if __name__ == "__main__":
    # Check if we're in test mode
    if os.getenv("TEST_MODE"):
        test_workflow()
    else:
        main() 