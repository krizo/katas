import { getMiddle } from './get_middle_chars';

test('get middle chars)', () => {
  expect(getMiddle('test')).toEqual('es');
  expect(getMiddle('testing')).toEqual('t');
  expect(getMiddle('middle')).toEqual('dd');
  expect(getMiddle('A')).toEqual('A');
});
