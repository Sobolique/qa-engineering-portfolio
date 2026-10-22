import { test, expect } from '@playwright/test';

test('standard user can log in', async ({ page }) => {
  await page.goto('/');
  await page.locator('#user-name').fill('standard_user');
  await page.locator('#password').fill('secret_sauce');
  await page.locator('#login-button').click();
  await expect(page).toHaveURL(/inventory/);
  await expect(page.locator('.inventory_item')).toHaveCount(6);
});

test('invalid password is rejected', async ({ page }) => {
  await page.goto('/');
  await page.locator('#user-name').fill('standard_user');
  await page.locator('#password').fill('wrong');
  await page.locator('#login-button').click();
  await expect(page.locator('[data-test="error"]')).toBeVisible();
});

test('user can add item to cart', async ({ page }) => {
  await page.goto('/');
  await page.locator('#user-name').fill('standard_user');
  await page.locator('#password').fill('secret_sauce');
  await page.locator('#login-button').click();
  await page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click();
  await expect(page.locator('.shopping_cart_badge')).toHaveText('1');
});

test('checkout validates required first name', async ({ page }) => {
  await page.goto('/');
  await page.locator('#user-name').fill('standard_user');
  await page.locator('#password').fill('secret_sauce');
  await page.locator('#login-button').click();
  await page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click();
  await page.locator('.shopping_cart_link').click();
  await page.locator('[data-test="checkout"]').click();
  await page.locator('[data-test="lastName"]').fill('Tester');
  await page.locator('[data-test="postalCode"]').fill('700000');
  await page.locator('[data-test="continue"]').click();
  await expect(page.locator('[data-test="error"]')).toBeVisible();
});
