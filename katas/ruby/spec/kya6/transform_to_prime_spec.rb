require './kyu6/transform_to_prime'

describe 'Transform prime' do
  let(:expected_results) {
    [
      {
        input: [ 3, 1, 2 ],
        output: 1
      },
      {
        input: [ 5, 2 ],
        output: 0
      },
      {
        input: [ 2, 12, 8, 4, 6 ],
        output: 5
      },
      {
        input: [ 50, 39, 49, 6, 17, 28 ],
        output: 2
      }
    ]
  }

  it "minimium number to be added to all list's elements to become a prime number" do
    expected_results.each do |test_sample|
      input, expected_output = test_sample[:input], test_sample[:output]
      expect(minimum_number(input)).to eq expected_output
    end
  end
end
