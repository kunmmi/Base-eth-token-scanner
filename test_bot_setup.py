#!/usr/bin/env python3
"""
Test script to verify BearTech Token Analysis Bot setup
"""
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_imports():
    """Test that all modules can be imported"""
    print("🧪 Testing module imports...")
    
    try:
        import src.config
        print("✅ Config module imported successfully")
        
        import src.models.token
        print("✅ Token models imported successfully")
        
        import src.services.token_analyzer
        print("✅ Token analyzer imported successfully")
        
        import src.bot.handlers
        print("✅ Bot handlers imported successfully")
        
        import src.utils.cache
        print("✅ Cache utilities imported successfully")
        
        return True
    except Exception as e:
        print(f"❌ Import error: {e}")
        return False

def test_config():
    """Test configuration loading"""
    print("\n🔧 Testing configuration...")
    
    try:
        from src.config import TELEGRAM_BOT_TOKEN, GOPLUS_API_KEY
        
        if TELEGRAM_BOT_TOKEN and TELEGRAM_BOT_TOKEN != "your_telegram_bot_token_here":
            print("✅ Telegram bot token configured")
        else:
            print("❌ Telegram bot token not configured")
            return False
        
        if GOPLUS_API_KEY and GOPLUS_API_KEY != "your_goplus_api_key_here":
            print("✅ GoPlus API key configured")
        else:
            print("❌ GoPlus API key not configured")
            return False
        
        return True
    except Exception as e:
        print(f"❌ Configuration error: {e}")
        return False

def test_bot_creation():
    """Test bot creation without starting it"""
    print("\n🤖 Testing bot creation...")
    
    try:
        from src.bot.main import BearTechBot
        from src.config import TELEGRAM_BOT_TOKEN
        
        bot = BearTechBot(TELEGRAM_BOT_TOKEN)
        print("✅ Bot instance created successfully")
        
        return True
    except Exception as e:
        print(f"❌ Bot creation error: {e}")
        return False

def test_token_analyzer():
    """Test token analyzer creation"""
    print("\n🔍 Testing token analyzer...")
    
    try:
        from src.services.token_analyzer import TokenAnalyzer
        
        analyzer = TokenAnalyzer()
        print("✅ Token analyzer created successfully")
        
        # Test address validation
        valid_address = "0x1234567890abcdef1234567890abcdef12345678"
        if analyzer._validate_address(valid_address):
            print("✅ Address validation working")
        else:
            print("❌ Address validation not working")
            return False
        
        return True
    except Exception as e:
        print(f"❌ Token analyzer error: {e}")
        return False

def main():
    """Run all tests"""
    print("🚀 BearTech Token Analysis Bot - Setup Test")
    print("=" * 50)
    
    tests = [
        test_imports,
        test_config,
        test_bot_creation,
        test_token_analyzer
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        else:
            print(f"❌ Test failed: {test.__name__}")
    
    print("\n" + "=" * 50)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Bot is ready to run.")
        print("\n📝 To start the bot, run:")
        print("   python run_bot.py")
        print("\n📱 Or use the module directly:")
        print("   python -m src.bot.main")
        return True
    else:
        print("❌ Some tests failed. Please check the errors above.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)



