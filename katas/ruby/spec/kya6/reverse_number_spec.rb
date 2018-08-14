require './kyu6/reverse_number'

describe "Reverse the number" do
  let(:test_inputs) do
    [
      {
        input: 123,
        expected_output: 321
      },
      {
        input: -456,
        expected_output: -654
      },
      {
        input: 1000,
        expected_output: 1
      }
    ]
  end


  it "reverse numbers" do
    test_inputs.each do |sample, index|
      expect(reverse_number(sample[:input])).to eq sample[:expected_output]
    end
  end
end
