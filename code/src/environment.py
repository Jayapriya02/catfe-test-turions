import os
import shutil
from playwright.sync_api import sync_playwright

def before_all(context):
        """Set up environment before tests."""
    generated_feature = "features/generated_feature.feature"

    # Generate AI-based feature file if it doesn't exist
    if not os.path.exists(generated_feature):
        print("🚀 Generating AI-based feature file...")
        os.system("python utils/ai_helper.py")

    if os.path.exists(generated_feature):
        shutil.copy(generated_feature, "features/ai_generated.feature")
        print("✅ AI-generated feature file loaded.")

    print("✅ DEBUG: Running before_all()...")
    context.playwright = sync_playwright().start()

def before_scenario(context, scenario):
    print(f"🔹 Inside scenario: {scenario.name}")
    
    # Launch a new browser for each scenario to start fresh
    context.browser = context.playwright.chromium.launch(headless=False)  # Set True for CI
    context.page = context.browser.new_page()

def after_scenario(context, scenario):
    print(f"✅ DEBUG: Ending scenario: {scenario.name}")
    context.page.close()
    context.browser.close()

def after_all(context):
    """Cleanup after tests."""
    generated_feature = "features/ai_generated.feature"
    if os.path.exists(generated_feature):
    os.remove(generated_feature)
    print("🗑 Cleaned up AI-generated feature file.")

    print("✅ DEBUG: Running after_all()...")
    context.playwright.stop()


