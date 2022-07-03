import fuzzywuzzy
## TODO - auto increment id
## TODO - Logic of find_duplicates
class Profile(object):

    def __init__(self):
        pass


    def make_profiles(self) -> list:
        obj = []
        n = int(input("Enter the number of profiles you want\n"))
        for count in range(n):
            name = input("Enter the name of the profile\n")
            obj.append(name)
        return obj


class Fields(Profile):
    def __init__(self):
        super().__init__()



    def make_fields(self, profiles: list, fields:list):
        _id = 0
        all_profiles = []
        total_score = 0
        profiles_list = self.make_profiles()
        for profile in profiles_list:
            m = int(input(f"Enter the number of fields you want for {profile}\n"))
            field_dict = {}
            for count in range(m):
                #fields["id"] = _id + 1
                key, value = input().split()
                # if key == "id":
                #     print("Your id is already taken care of...please continue")
                #     continue
                field_dict[key] = value
            all_profiles.append({profile: field_dict})
        print(all_profiles)
        final = {}
        first_profile, second_profile = {}, {}
        for index in range(len(all_profiles)):
            profiles_dict = {k: all_profiles[index][k] for k in profiles if k in all_profiles[index]}
            if len(profiles_dict) == 1:
                final.update(profiles_dict)
            for profile_value in profiles_dict.values():
                if not (set(fields) - profile_value.keys()):

                    first_profile = final[profiles[0]]
                    second_profile = final[profiles[1]]
                    total_score = self.find_duplicates_utils(first_profile, second_profile, fields)
        return total_score


    def _extract_keys_from_fields(self):
        pass

    def find_duplicates_utils(self, profile1: dict, profile2: dict, fields: list):
        total_score = 0
        pass




if __name__ == '__main__':
    obj = Fields()
    obj.make_fields(profiles=["profile1", "profile2"], fields=["id", "name"])
    #obj.find_duplicates()



#     def __init__(self, fields=None):
#         """
#         constructor
#         """
#         if fields is None:
#             fields = {}
#         self.fields = fields
#
#     def set_fields(self, **kwargs):
#         """
#         set fields
#         :param fields:
#         :return:
#         """
#         m = int(input("Enter the number of fields you want "))
#         allowed_keys = {}
#         for _ in range(m):
#             allowed_keys.update()
#         return self.__dict__.update((k, v) for k, v in self.fields.items() if k in allowed_keys)
#
#
# if __name__ == '__main__':
#     # N = int(input("Enter the number of profile instances you want"))
#     # profiles = []
#     # for _ in range(N):
#     #     print("Enter the name of the Profile: ")
#     #     profile_name = input()
#     #     profiles.append(profile_name)
#     fields={
#         "id": 1,
#         "first_name": "Aditya",
#         "last_name": "Maheshwari"
#     }
#
#     profile1 = Profile(fields=fields)
#     profile2 = Profile(fields=fields)
#
#     print(f"Profile1 - {profile1.set_fields()}")
#     print(f"Profile2 - {profile2.set_fields()}")
