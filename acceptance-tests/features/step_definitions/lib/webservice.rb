
#######
# Function: get_register_details
# Description: Gets the register json structure
# Inputs:
#     - title_no
# Outputs:
#     - json register structure
######
def get_register_details(title_no)

  response = rest_get_call($LR_SEARCH_API_DOMAIN + '/auth/titles/' + title_no)

  return  JSON.parse(response.body)

end

#######
# Function: link_title_to_email
# Description: Connects a title to a person's email address
# Inputs:
#     - email = email address of the user
#     - title_number = title number to be linked
#     - role = the role id of the person (e.g. citizen, conveyancer)
# Outputs:
#     - json register structure
######
def link_title_to_email(email, title_number, role)

  response = rest_post_call($LR_FIXTURES_URL + '/create-matching-data-and-ownership', {'email' => email, 'title_number' => title_number, 'role_id' => role,'submit' => 'submit'})

  if (response.body != 'OK') then
    raise "Could not match title(#{title_number}), email(#{email}) and role(#{role}): " + response.body
  end

end

#######
# Function: does_title_exist
# Description: Does the title exist in the system of records
# Inputs:
#     - title_no
# Outputs:
#     - boolean if title exists (true = exists, false = doesn't exist)
######
def does_title_exist(title_no)

  response = rest_get_call($SYSTEM_OF_RECORD_API_DOMAIN + '/titles/' + title_no)

  if (response.code == '404') then
    return false
  else
    return true
  end

end

#######
# Function: wait_for_case_to_exist
# Description: Once a case has been submitted, this function will wait for it to exist. If after
#              the 25 seconds it doesn't exist then an exception will be raised.
# Inputs:
#     - title_no
# Outputs:
#     - curl response body
######
def wait_for_case_to_exist(title_no)
  found_count = 0
  count = 0

  while (found_count != 1 && count < 25) do
    puts 'waiting for case to be created'
    sleep(1)
    response = rest_get_call($CASES_URL + '/cases/property/' + title_no)
    if (!response.nil?)
      if (!JSON.parse(response.body)[0]['work_queue'].nil?)
        found_count = 1
        puts 'case assigned to ' + JSON.parse(response.body)[0]['work_queue'] + ' queue'
      end
    end
    count = count + 1
  end
  if (found_count != 1) then
    raise "No case found for title " + title_no
  end

  return response.body

end

#######
# Function: get_token_code
# Description: This inserts a conveyancer + client relationship request returns the token
# Inputs:
#     - relationship hash = Structure of relationship request
# Outputs:
#     - token
######
def get_token_code(relationship_hash)


  response = rest_post_call($INTRODUCTIONS_DOMAIN + '/relationship', nil, relationship_hash.to_json)

  #uri = URI.parse($INTRODUCTIONS_DOMAIN)
  #http = Net::HTTP.new(uri.host, uri.port)
  #request = Net::HTTP::Post.new('/relationship',  initheader = {'Content-Type' =>'application/json'})
  #request.basic_auth $http_auth_name, $http_auth_password
  #request.body = relationship_hash.to_json
  #response = http.request(request)

  #response = rest_post_call($INTRODUCTIONS_DOMAIN + '/relationship', relationship_hash.to_json)

  if (response.code != '200') then
    raise "Failed creating relationship: " + response.body
  end

  return JSON.parse(response.body)['token']

end

#######
# Function: getlrid
# Description: this gets the lrid (unique id) of a user
# Inputs:
#     - email = user's email address
# Outputs:
#     - curl response body
######
def getlrid(email)

  response = rest_get_call($LR_FIXTURES_URL + '/get-lrid-by-email/' + email)

  if (response.code != '200') then
    raise "Error in finding email for: " + email
  end

  return response.body

end

#######
# Function: associate_client_with_token
# Description: This will confirm a conveyancers relationship
# Inputs:
#     - data_hash = the data structure of the confirmation request
# Outputs:
#     - curl response body
######
def associate_client_with_token(data_hash)

  response = rest_post_call($INTRODUCTIONS_DOMAIN + '/confirm', data_hash.to_json)

  if (response.code != '200') then
    raise "Failed to associate client with token: " + response.body
  end

  return response.body

end

#######
# Function: wait_for_register_to_update_full_name
# Description: This will wait for the new full name to appear on the register. If it doesn't find
#              it then an exception will be raised.
# Inputs:
#     - title_number
#     - full_name = the name you expect it to now be
# Outputs:
#     - none
######
def wait_for_register_to_update_full_name(title_number, full_name)

  found_count = 0
  count = 0
  while (found_count != 1 && count < 50) do
    puts 'waiting for new version of title to be created'
    sleep(1)

    response = rest_get_call($LR_SEARCH_API_DOMAIN + '/auth/titles/' + title_number)
    if (response.code.to_s == '200') then

      puts 'name on title: ' + JSON.parse(response.body)['proprietorship']['fields']['proprietors'][0]['name']['full_name']
      puts 'expected name on title: ' + full_name
      if (!response.nil?)
        if (JSON.parse(response.body)['proprietorship']['fields']['proprietors'][0]['name']['full_name']==full_name)
          found_count = 1
          puts 'Title updated'
        end
      end

    end
    count = count + 1
  end
  if (found_count != 1) then
    raise "Title not updated " + title_number
  end

end

#######
# Function: post_to_historical
# Description: This will create a historical register entry
# Inputs:
#     - data_hash = data structure of the register
#     - title_number = the new title number that will be inserted
# Outputs:
#     - curl response body
######
def post_to_historical(data_hash, title_number)

  response = rest_post_call($HISTORIAN_URL + '/' + title_number, data_hash.to_json)

  if (response.code != '200') then
    raise "Failed to create the historical data: " + response.body
  end

  return response.body
end

#######
# Function: get_all_history
# Description: This will get all history of a title
# Inputs:
#     - title_number
# Outputs:
#     - curl response body
######
def get_all_history(title_number)

  response = rest_get_call($HISTORIAN_URL + '/' + title_number +'?versions=list')

  if (response.code != '200') then
    raise "Failed to retrieve list of historical data: " + response.body
  end

  return JSON.parse(response.body)
end

#######
# Function: get_history_version
# Description: This will get a specific version of a register
# Inputs:
#     - title_number
#     - version = the version you want to return
# Outputs:
#     - curl response body
######
def get_history_version(title_number, version)

  response = rest_get_call($HISTORIAN_URL + '/' + title_number +'?version=' + version.to_s)

  if (response.code != '200') then
    raise "Failed to retrieve historical version specified: " + response.body
  end

  return JSON.parse(response.body)
end

#######
# Function: set_user_view_count
# Description: Sets the view count of the amount of registered than a user has viewed
# Inputs:
#     - email
#     - count = the amount of registered the user has viewed
# Outputs:
#     none
######
def set_user_view_count(email, count)

  response = rest_post_call($LR_FIXTURES_URL + '/set-user-view-count', {'user_view_email' => email, 'view_count' => count.to_s, 'submit' => 'Set view count'})

  if (response.code != '302') then
    raise "Could not set view count: " + response.body
  end

end

#######
# Function: get_cases_by_title_number
# Description: gets all the cases associated to that tile
# Inputs:
#     - title_no
# Outputs:
#     - curl response body
######
def get_cases_by_title_number(title_no)

  response = rest_get_call($CASES_URL + '/cases/property/' + title_no)

  return response.body

end
