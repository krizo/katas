import { validatePin } from './validate_pin_code';

test('validate pin', () => {
  expect(validatePin('1234')).toBe(true);
  expect(validatePin('12345')).toBe(false);
  expect(validatePin('a234')).toBe(false);
});
