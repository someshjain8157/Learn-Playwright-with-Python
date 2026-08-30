import pytest
from playwright.async_api import async_playwright, expect

@pytest.mark.asyncio
async def test_authenticated_session():
    async with async_playwright() as p:
        # Reuse saved auth.json
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(storage_state="auth.json")
        page = await context.new_page()

        await page.goto("https://example.com/dashboard")
        await expect(page).to_have_url("https://example.com/dashboard")

        await browser.close()
