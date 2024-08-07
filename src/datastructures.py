class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = [
            {
                "id": self._generate_id(),
                "first_name": "John",
                "last_name": self.last_name,
                "age": 33,
                "lucky_numbers": [7,13,22]
            },
            {
                "id": self._generate_id(),
                "first_name": "Jane",
                "last_name": self.last_name,
                "age": 35,
                "lucky_numbers": [10,14,3]
            },
            {
                "id": self._generate_id(),
                "first_name": "Jimmy",
                "last_name": self.last_name,
                "age": 5,
                "lucky_numbers": [1]
            },
        ]

    # This method generates a unique 'id' when adding members into the list (you shouldn't touch this function)
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        ## You have to implement this method
        ## Append the member to the list of _members
        member['id'] = self._generate_id(),
        member['last_name'] = self.last_name,
        self._members.append(member)
        pass

    def delete_member(self, id):
        ## You have to implement this method
        ## Loop the list and delete the member with the given id
        self._members = [member for member in self._members if member['id'] != id]


    def get_member(self, id):
        ## You have to implement this method
        ## Loop all the members and return the one with the given id
        for member in self._members:
            if member["id"] == id:
                return member
            return None


    def get_all_members(self):
        return self._members