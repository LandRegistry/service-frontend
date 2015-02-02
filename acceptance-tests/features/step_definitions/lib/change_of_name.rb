def create_marriage_data(country, full_name, title_number)
  marriage_data = {}
  marriage_data['confirm'] = true
  marriage_data['proprietor_full_name'] = full_name
  marriage_data['proprietor_new_full_name'] = fullName()
  marriage_data['partner_name'] = fullName()
  marriage_data['application_type'] = 'change-name-marriage'
  marriage_data['marriage_country'] = country
  marriage_data['marriage_place'] = townName()
  marriage_data['title_number'] = title_number
  marriage_data['proprietor_full_name'] = full_name
  marriage_data['marriage_certificate_number'] = certificateNumber()
  marriage_data['marriage_date'] = dateInThePast().strftime("%d-%m-%Y")

  return marriage_data

end

def create_change_of_name_marriage_request(marriage_data)

  marriage_data['marriage_date']  = Date.strptime(marriage_data['marriage_date'], "%d-%m-%Y").strftime("%s").to_i

  data = marriage_data
  data['confirm'] = true
  #data['title'] = $regData

  change_of_name = {}
  change_of_name["application_type"] = "change-name-marriage"
  change_of_name["title_number"]  = marriage_data['title_number']
  change_of_name["submitted_by"] = marriage_data['proprietor_full_name']
  change_of_name["request_details"] = {}
  change_of_name["request_details"]["action"] = "change-name-marriage"
  change_of_name["request_details"]["data"] = data.to_json
  change_of_name["request_details"]["context"] = {}
  change_of_name["request_details"]["context"]["session-id"] = "123456"
  change_of_name["request_details"]["context"]["transaction-id"] = "ABCDEFG"

  uri = URI.parse($CASES_URL)
  http = Net::HTTP.new(uri.host, uri.port)
  request = Net::HTTP::Post.new('/cases',  initheader = {'Content-Type' =>'application/json'})
  request.basic_auth $http_auth_name, $http_auth_password
  request.body = change_of_name.to_json
  response = http.request(request)

  change_of_name['case_id'] = JSON.parse(response.body)['id']
  #make sure case is in queued status
  assert_equal check_case_is_with_status(change_of_name['case_id'], marriage_data['title_number'], 'queued'), true, "case not in correct status"

  return change_of_name

end

def complete_case(case_id)

  uri = URI.parse($CASES_URL)
  http = Net::HTTP.new(uri.host, uri.port)
  request = Net::HTTP::Put.new('/cases/complete/' + case_id)
  request.basic_auth $http_auth_name, $http_auth_password
  response = http.request(request)

  if (response.body != 'OK') then
    raise 'Error: ' + response.body
  end

end

def check_case_is_with_status(case_id, title_number, status)
  count = 0
  found = false
  while (found != true && count < 25) do
    sleep(1)
    array = JSON.parse(get_cases_by_title_number(title_number))
    array.each { |row|
      if row['id'] = case_id
        if row['status'] == status
          found = true
          puts 'case is queued'
          break
        end
      end
    }
    count = count + 1
  end

  if (found == true) then
    return true
  else
    return false
  end
end

def get_cases_by_title_number_and_status(title_number, status)
  cases = []
  array = JSON.parse(get_cases_by_title_number(title_number))
  array.each { |row|
      if row['status'] == status
        cases.push(row)
      end
  }
  return cases
end
