# almabase assignment

### <li>Steps</li>

<ol>bash main.sh</ol>


## INPUT
Enter the number of profiles you want
<li>2</li>
Enter the name of the profile
<li>profile1</li>
Enter the name of the profile
<li>profile2</li>
Enter the number of fields you want for profile1
<ul>5
<li>first_name adi</li>
<li>last_name mah</li>
<li>email adi.mah@gmail.com</li>
<li>class_year 2012</li>
<li>birth_date 1990-11-10</li>
</ul>

Enter the number of fields you want for profile2
<ul>5
<li>first_name john</li>
<li>last_name mah</li>
<li>email john.mah@gmail.com</li>
<li>class_year 2012</li>
<li>birth_date 1990-11-01</li>
</ul>

## OUTPUT
<li>
{'duplicate_profiles': ['profile1', 'profile2'], 'total_score': 1, 'matching_attributes': ['class_year'], 'non_matching_attributes': [], 'ignored_attributes': ['birth_date']}
</li>
