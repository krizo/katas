require './kyu6/good_vs_evil'

describe "good vs evil katas" do

  let(:good_win) { 'Battle Result: Good triumphs over Evil' }
  let(:tie) { 'Battle Result: No victor on this battle field' }

   it 'Good should triumph' do
     expect(goodVsEvil('0 0 0 0 0 10', '0 1 1 1 1 0 0')).to eq good_win
   end

   it 'Should be a tie' do
     expect(goodVsEvil('1 0 0 0 0 0', '1 0 0 0 0 0 0')).to eq tie
   end
end
