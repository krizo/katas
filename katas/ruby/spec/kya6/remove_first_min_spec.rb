require './kyu6/remove_first_min'

describe "Remove first minimum" do
  let(:test_inputs) do
    [
      {
        input: [ 1, 2, 3, 4, 5 ],
        expected_output: [ 2, 3, 4, 5 ]
      },
      {
        input: [ 5, 3, 2, 1, 4 ],
        expected_output: [ 5, 3, 2, 4 ]
      },
      {
        input: [ 2, 2, 1, 2, 1 ],
        expected_output: [ 2, 2, 2, 1 ]
      }
    ]
  end


  it "check first minimums" do
    test_inputs.each do |sample|
      expect(remove_smallest(sample[:input])).to eq sample[:expected_output]
    end
  end
end
