import re

from fuzzywuzzy import fuzz
from dateutil.parser import parse
class Profile(object):
    """
    Class to define the Profiles
    """
    def __init__(self):
        pass


    def make_profiles(self) -> list:
        """
        used to make the profiles as per user
        :return: (list) profiles
        """
        obj = []
        n = int(input("Enter the number of profiles you want\n"))
        for count in range(n):
            name = input("Enter the name of the profile\n")
            obj.append(name)
        return obj


class Fields(Profile):
    """
    child class of profiles to add fields to the profile
    """
    def __init__(self):
        super().__init__()

    def find_duplicates(self, profiles: list, fields:list) -> dict:
        """
        finds the duplicates
        :param profiles: the list of profiles to be compared
        :param fields: the fields in the profiles
        :return: total_score (dict)
        """
        all_profiles = [] # stores the information of all the profiles
        total_score = {} # stores the dictionary from util method
        profiles_list = self.make_profiles() # parent method to make profiles
        for profile in profiles_list:
            m = int(input(f"Enter the number of fields you want for {profile}\n"))
            field_dict = {}
            for count in range(m):
                key, value = input().split()
                if key == 'first_name' and value != "":
                    value = input(f"please enter the {key}")
                if key == 'last_name' and value != "":
                    value = input(f"please enter the {key}")
                if key == 'email' and value != re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', key):
                    value = input(f"Enter a valid {key}")
                if key == 'class_year' and value <= 0:
                    value = input(f"Enter a valid {key}")
                if key == 'birth_date' and parse(value):
                    value = input(f"Enter the valid {key}")
                field_dict[key] = value
            all_profiles.append({profile: field_dict})

        final = {} # information about all the dictionaries to be compared from the profile list
        for index in range(len(all_profiles)):
            profiles_dict = {k: all_profiles[index][k] for k in profiles if k in all_profiles[index]}
            if len(profiles_dict) == 1:
                final.update(profiles_dict)
        print(final)
            # for profile_value in profiles_dict.values():
            #     if not (set(fields) - profile_value.keys()): # check to see that the fields are present in the profiles
        first_profile = final[profiles[0]]
        second_profile = final[profiles[1]]
        total_score = self.find_duplicates_utils(profiles, first_profile, second_profile)
        return total_score

    def find_duplicates_utils(self, profiles, profile1: dict, profile2: dict) -> dict:
        """
        util function to find the duplicates
        :param profiles: the duplicate profiles
        :param profile1: the information about first profile
        :param profile2: the information about second profile
        :return: (dict) meta data about duplicate profiles
        """
        total_score = 0
        matching_attributes:list = []
        non_matching_attributes:list = []
        ignored_attributes = []
        _str1 = profile1['first_name'] + profile1['last_name'] + profile1['email']
        _str2 = profile2['first_name'] + profile2['last_name'] + profile2['email']
        if fuzz.ratio(_str1, _str2) > 80:
            total_score += 1
            matching_attributes.append('first_name')
            matching_attributes.append('last_name')
            matching_attributes.append('email')
        else:
            non_matching_attributes.append('first_name')
            non_matching_attributes.append('last_name')
            non_matching_attributes.append('email')
        if profile1.get('class_year') == profile2.get('class_year') \
                and profile1['class_year'] == profile2['class_year']:
            total_score += 1
            matching_attributes.append('class_year')
        elif profile1.get('class_year') == profile2.get('class_year') \
                and profile1['class_year'] != profile2['class_year']:
            total_score -= 1
            non_matching_attributes.append('class_year')
        else:
            ignored_attributes.append('class_year')

        if profile1.get('birth_date') == profile2.get('birth_date') \
                and profile1['birth_date'] == profile2['birth_date']:
            total_score += 1
            matching_attributes.append('birth_date')
        elif profile1.get('birth_date') == profile2.get('birth_date') \
                and profile1['birth_date'] != profile2['birth_date']:
            total_score -= 1
            non_matching_attributes.append('birth_date')
        else:
            ignored_attributes.append('birth_date')
        profile_dup = {}

        profile_dup = {
            'duplicate_profiles': profiles,
            'total_score': total_score if total_score >= 1 else 0,
            'matching_attributes': matching_attributes,
            'non_matching_attributes': non_matching_attributes,
            'ignored_attributes': ignored_attributes
        }
        return profile_dup


if __name__ == '__main__':
    obj = Fields()
    final = obj.find_duplicates(profiles=["profile1", "profile2"],
                        fields=["first_name", "last_name", "email", "class_year", "birth_date"])
    print(final)