#required fields
def checkTitleNumber()
  assert_match(/#{$regData['title_number']}/i, page.body, 'Expected to see title number')
end

def checkPricePaid()
  assert_match(/#{$regData['price_paid']['fields']['amount']}/i, page.body, 'Expected to see price paid')
end

def checkTenure()
  assert_match(/#{$regData['property_description']['fields']['tenure']}/i, page.body, 'Expected to see tenure value')
end

def checkStructuredPropertyAddress()
  assert_match(/#{$regData['property_description']['fields']['addresses'][0]['house_no']}/i, page.body, 'Expected to see full address')
  assert_match(/#{$regData['property_description']['fields']['addresses'][0]['street_name']}/i, page.body, 'Expected to see full address')
  assert_match(/#{$regData['property_description']['fields']['addresses'][0]['town']}/i, page.body, 'Expected to see full address')
  assert_match(/#{$regData['property_description']['fields']['addresses'][0]['postal_county']}/i, page.body, 'Expected to see full address')
  assert_match(/#{$regData['property_description']['fields']['addresses'][0]['region_name']}/i, page.body, 'Expected to see full address')
  assert_match(/#{$regData['property_description']['fields']['addresses'][0]['country']}/i, page.body, 'Expected to see full address')
  assert_match(/#{$regData['property_description']['fields']['addresses'][0]['postcode']}/i, page.body, 'Expected to see full address')
end

def checkPropertyAddress()

  # The address is unstructured, so is 1 long string. The application is trying to split the address
  # by commas and displaying it in multiple lines. We need to do the same to check it
  unstructured_address_parts = $regData['property_description']['fields']['addresses'][0]['full_address'].split(',')

  unstructured_address_parts.each do |address_parts|
    assert_match(/#{address_parts}/i, page.body, 'Expected to see full address')
  end

end

def checkRestrictiveCovenants()
  assert_match(/#{$regData['restrictive_covenants'][0]['full_text'].gsub('(', '\(').gsub(')', '\)')}/i, page.body, 'Expected to see Restrictive Covenants')
end

def checkBankruptcyNotice()
  assert_match(/#{$regData['bankruptcy'][0]['full_text'].gsub('(', '\(').gsub(')', '\)')}/i, page.body, 'Expected to see Restrictive Covenants')
end

def checkEasement()
  assert_match(/#{$regData['easements'][0]['full_text'].gsub('(', '\(').gsub(')', '\)')}/i, page.body, 'Expected to see Restrictive Covenants')
end

def checkRestriction()
  assert_match(/#{$regData['restrictions'][0]['full_text'].gsub('(', '\(').gsub(')', '\)')}/i, page.body, 'Expected to see Restrictive Covenants')
end




def checkProprietors()
  assert_match(/#{$regData['proprietorship']['fields']['proprietors'][0]['name']['full_name']}/i, page.body, 'Expected to see proprietor name')
end

def checkProvision()
  assert_match(/#{$regData['provisions'][0]['full_text']}/i, page.body, 'Expected to see provision full text')
end

def checkRegisterDetails()
  checkTitleNumber()
  checkPricePaid()
  checkTenure()
  checkClassOfTitle()
  checkPropertyAddress()
  checkProprietors()
end
