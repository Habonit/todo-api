import { test, expect } from '@playwright/test'

// Happy-path: add → visible in list → complete toggle → delete
test('add todo, mark complete, delete', async ({ page }) => {
  const title = `E2E Todo ${Date.now()}`

  await page.goto('/')

  // Add a new todo
  await page.getByLabel('New todo title').fill(title)
  await page.getByLabel('Add todo').click()

  // Verify it appears in the list
  const row = page.locator('li').filter({ hasText: title })
  await expect(row).toBeVisible()

  // Mark as complete
  await row.getByLabel('Mark as complete').click()

  // Verify the check button is now in the completed/disabled state
  await expect(row.getByLabel('Completed')).toBeDisabled()

  // Delete the todo
  await row.getByLabel('Delete todo').click()

  // Verify it is gone
  await expect(page.getByText(title)).not.toBeVisible()
})
