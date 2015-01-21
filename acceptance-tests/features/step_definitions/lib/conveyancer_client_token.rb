def generate_client_details()

  relationshipData = Hash.new()

  relationshipData['clients'] = Hash.new()
  relationshipData['clients']['full_name'] = 'Walter White'
  relationshipData['clients']['date_of_birth'] = '07-09-1959'
  relationshipData['clients']['address'] = '1 High St, London, N1 4QX'
  relationshipData['clients']['telephone'] = '01752 909 878'
  relationshipData['clients']['email'] = 'citizen@example.org'
  relationshipData['clients']['gender'] = 'M'

  return relationshipData
end


def generate_relationship_details(title_no)

  link_relationship = Hash.new()
  link_relationship['conveyancer_lrid'] = getlrid('conveyancer@example.org')
  link_relationship['title_number'] = title_no
  link_relationship['conveyancer_name'] = 'Tuco Salamanca'
  link_relationship['conveyancer_address'] = '123 Bad Place, Rottentown, ABC 123'
  link_relationship['clients'] = Array.new()
  link_relationship['clients'][0] = Hash.new()
  link_relationship['clients'][0]['lrid'] = getlrid('citizen@example.org')
  link_relationship['title_number'] = title_no
  link_relationship['task'] = 'sell'

  link_relationship['token'] = get_token_code(link_relationship)

  return link_relationship

end
