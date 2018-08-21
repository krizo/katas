require './kyu6/spinning_words'

describe "Reverse the number" do
  let(:test_inputs) do
    [
      {
        input: 'Hey fellow warriors',
        expected_output: 'Hey wollef sroirraw'
      },
      {
        input: 'This is a test',
        expected_output: 'This is a test'
      },
      {
        input: 'This is another test',
        expected_output: 'This is rehtona test'
      }
    ]
  end


  it "check spin words" do
    test_inputs.each do |sample|
      expect(spin_words(sample[:input])).to eq sample[:expected_output]
    end
  end
end
