import { noBoringZeros } from './no_zeros_to_heros';

it('No Boring heroes', () => {
  expect(noBoringZeros(1450)).toEqual(145);
  expect(noBoringZeros(960000)).toEqual(96);
  expect(noBoringZeros(1050)).toEqual(105);
  expect(noBoringZeros(-1050)).toEqual(-105);
});
