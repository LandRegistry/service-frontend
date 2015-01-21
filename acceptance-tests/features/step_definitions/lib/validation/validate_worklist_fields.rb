def checkMarriageDetails()

  # Gets a list of all elements which contain the title number
  marriageDetails = page.all(:xpath, ".//tr[td//text()[contains(.,'" + $regData['title_number'] + "')]]/following-sibling::tr[1]/td")

  # Run some tests
  assert_match($marriage_data['proprietor_full_name'], marriageDetails[0].text, 'Expected proprietor full name of ' + $marriage_data['proprietor_full_name'] + ' in ' + marriageDetails[0].text)
  assert_match($marriage_data['proprietor_new_full_name'], marriageDetails[0].text, 'Expected proprietor new full name of ' + $marriage_data['proprietor_new_full_name'] + ' in ' + marriageDetails[0].text)
  assert_match($marriage_data['partner_name'], marriageDetails[0].text, 'Expected partner name of ' + $marriage_data['partner_name'] + ' in ' + marriageDetails[0].text)
  assert_match(Time.at($marriage_data['marriage_date']).to_datetime.strftime("%d-%m-%Y").to_s, marriageDetails[0].text, 'Expected marriage date of ' + Time.at($marriage_data['marriage_date']).to_datetime.strftime("%d-%m-%Y").to_s + ' in ' + marriageDetails[0].text)
  assert_match($marriage_data['marriage_place'], marriageDetails[0].text, 'Expected marriage place of ' + $marriage_data['marriage_place'] + ' in ' + marriageDetails[0].text)
  assert_match('United Kingdom', marriageDetails[0].text, 'Expected country of ' + $marriage_data['marriage_country'] + ' in ' + marriageDetails[0].text)
  assert_match($marriage_data['marriage_certificate_number'].to_s, marriageDetails[0].text, 'Expected certificate of ' + $marriage_data['marriage_certificate_number'].to_s + ' in ' + marriageDetails[0].text)
end

def checkTitleNumberInWorklist()

  # Gets a list of all elements which contain the title number
  titleList = page.all(:xpath, ".//tr[td//text()[contains(.,'" + $regData['title_number'] + "')]]")

  # Run some tests
  assert_equal(titleList.length, 1, 'There are zero or more than one entries for title' + $regData['title_number'])
  assert_match($regData['title_number'], titleList[0].text, 'Expected the title number' + $regData['title_number'] + ' in ' + titleList[0].text)

end

def checkDateRequestWasSubmitted()

  # Gets a list of all elements which contain the title number
  titleList = page.all(:xpath, ".//tr[td//text()[contains(.,'" + $regData['title_number'] + "')]]")

  # Run some tests
  assert_equal(titleList.length, 1, 'There are zero or more than one entries for title' + $regData['title_number'])
  assert_match(Date.today.strftime("%e %B %Y").strip, titleList[0].text, 'Expected date today\'s date as date submitted' + titleList[0].text)

end

def checkApplicationTypeOfChangeNameMarriage()

  # Gets a list of all elements which contain the title number
  titleList = page.all(:xpath, ".//tr[td//text()[contains(.,'" + $regData['title_number'] + "')]]")

  # Run some tests
  assert_equal(titleList.length, 1, 'There are zero or more than one entries for title' + $regData['title_number'])
  assert_match('change-name-marriage', titleList[0].text, 'Expected change-name-marriage' + titleList[0].text)

end
