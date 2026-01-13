#!/usr/bin/env python3
"""
Test script for the specific token that was failing
"""
import asyncio
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

async def test_specific_token():
    """Test the specific token that was failing"""
    from src.services.token_analyzer import TokenAnalyzer
    from src.models.token import ChainType
    
    # The token address that was failing
    test_address = "0x3aAf8a9e6c2A63aF24c97cB29121D19C1cc10993"
    
    print(f"🧪 Testing token analysis for: {test_address}")
    print("=" * 60)
    
    analyzer = TokenAnalyzer()
    
    try:
        # Test chain detection
        print("🔍 Testing chain detection...")
        chain = await analyzer._detect_chain(test_address)
        print(f"✅ Detected chain: {chain.value if chain else 'None'}")
        
        # Test full analysis
        print("\n📊 Testing full analysis...")
        result = await analyzer.analyze_token(test_address)
        
        print(f"✅ Analysis completed!")
        print(f"📋 Token name: {result.basic_info.name or 'Unknown'}")
        print(f"🔗 Chain: {result.basic_info.chain.value if result.basic_info.chain else 'Unknown'}")
        print(f"⚠️ Risk level: {result.risk_assessment.overall_risk.value}")
        print(f"🚨 Is honeypot: {result.is_honeypot()}")
        print(f"📊 Data sources: {', '.join(result.data_sources)}")
        print(f"❌ Errors: {len(result.errors)}")
        
        if result.errors:
            print("\n⚠️ Errors encountered:")
            for error in result.errors:
                print(f"  • {error}")
        
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {str(e)}")
        return False

if __name__ == "__main__":
    success = asyncio.run(test_specific_token())
    if success:
        print("\n🎉 Test completed successfully!")
    else:
        print("\n❌ Test failed!")
    sys.exit(0 if success else 1)



