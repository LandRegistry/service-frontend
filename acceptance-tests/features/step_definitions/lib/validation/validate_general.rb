def validate_title_number(titleNumber)
  assert_equal titleNumber[0,4], 'TEST', 'Title does not have a prefix of TEST'
  assert_equal titleNumber[4,titleNumber.size - 1], titleNumber[4,titleNumber.size - 1].to_i.to_s, 'The title number is not numberic'
  assert_operator titleNumber[4,titleNumber.size - 1].to_i, :>=, 1, 'The number is less than 0'
end

def validate_token_format(token_code)
  assert_operator token_code.size, :<=, 4, 'The token is not 4 in length'
end

def validateField(fieldId, errorMessage)
  assert_selector(".//*[@id='" + fieldId + "']", text: errorMessage)
end
