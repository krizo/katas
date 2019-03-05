/* 
Numbers ending with zeros are boring.
They might be fun in your world, but not here.
Get rid of them.Only the ending ones.

1450 -> 145
960000 -> 96
1050 -> 105
  - 1050 -> -105
Zero alone is fine, don't worry about it. Poor guy anyway
*/

export const noBoringZeros = n => {
  const input = [...String(n)].reverse();
  for (let i = 0; i <= input.length; i += 1) {
    if (input[i] !== '0') {
      return Number(
        input
          .slice(i)
          .join('')
          .split('')
          .reverse()
          .join('')
      );
    }
  }
};
