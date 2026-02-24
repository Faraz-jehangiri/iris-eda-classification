import random
BOLD = "\033[1m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
RESET = "\033[0m"
school_list = [
    'Akbar Public School', 'Metropolitan School', 'Candle Light Secondary School',
    'Little Flower Children Secondary School', 'Standard Govt. Boys Secondary School',
    'APWA Govt. Boys Secondary School', 'Govt. Boys Secondary School No.1',
    'Town Committee Govt. Boys Sec. School', 'Sitara-E-Hydri Govt. Boys Sec. School',
    'Govt. Boys Secondary School No.2', 'Super Secondary School', 'Sun Beam Secondary School',
    'Muslim Secondary School', 'Standard Secondary School', 'The New Green Land School',
    'Govt. Boys Secondary School', 'Sattar Secondary School', 'Dawn Boys & Girls Secondary School',
    "Little Folk's Paradise Sec. School", 'Zeeshan Secondary School', 'Huma Secondary School',
    'Asmara Children Academy', 'London Super Gramer School', 'Golden Career Public School',
    'Falah-E-Millat Model Secondary School', 'North Star Public School', 'Public Model G. B. S.S.',
    'Amina Secondary School', 'Islamia High School', 'Peter & Paul High School',
    'P.F. Model Secondary School', 'Shamim Govt. Bosy Secondary School',
    'The Godhra Tameer-E-Millat Sec. School', "Pak Folk's Grammar School", 'Al Khair Secondary School',
    'New Sun Rise Public School', 'The Nation Public School', 'Dollina Public School',
    'North Karachi Model Academy Sec. School', 'The British Grammer School', 'North Bright Way School',
    'Ghazali Public Grammar School', 'New Green Land Secondary School', 'Victory English Secondary School',
    'Zainab Children Academy', 'D North Public School', 'Mount Hera Secondary School',
    'The Great Miracle Grammer Sec. School', 'Knowledge Inn Grammar Sec. School',
    'New White Rose Secondary School', 'The Citizen Foundation Secondary School',
    'Roseland Secondary School', 'Al-Madinia English School',
    'Bright Children Academy Secondary School', 'Dacca Secondary School', 'Kids Heaven Secondary School',
    'Premier Grammar School', 'National Cambridge Sec. School', 'New Era Grammar School',
    'Al-Ahmad Grammar School', 'Shine Public Secondary School', 'New Era Academy',
    'Cadet Public School', 'New Universal Grammar School', 'Double (A.A.) Grammar Secondary School',
    'Winner Grammer School', 'Urooj Children Academy Sec. School', 'Hira Public Secondary School',
    'Place Heed Secondary School', 'M.D Grammar School.', 'New Oxford Grammar School.',
    'Fast Memory Public School.', "Ibrahim Children's Academy", 'New Oxford Grammer School.',
    'Rehnuma Children Academy', 'R.T. Public Secondary Schoo', 'Pak Horizone Grammar School',
    'Ghazi Foundation School', 'S.K. Grammar Secondary School', 'A.R.I Progressive Academy',
    'Al-Hira English School', 'Moon Light Govt Boys Secondary School', 'T.C.F. Secondary School',
    'District Council Govt. Boys Secondary School', 'Super Mind Grammar Secondary School',
    'Public Paradise Academy', 'Forester Academy', 'Wonderland Grammar Sec. School',
    'Pak Eastern School(Secondary)', 'Happy Home Grammar Sec.School', 'Green Sky Land Grammar School.',
    'Royal Cambridge Sec. School', 'A.I.M.Children Paradise School',
    'C.D.G.K.Dr. Mahmood Hussain Boys Sec.School', 'Galaxy Grammarian School,',
    'Kids Paradise Academy Sec.School', 'Iqbal Public School', 'St. Michales School',
    'Muslim Academy', 'Godhra Shaikh Public Sec. School', 'Blooming Rose Public School',
    'Knowledge English School', 'National Grammar School',
    'New Public Paradise Academy Secondary School', 'Anis Public Public School',
    'Pixy Dale G/B.Secondary School', 'Govt Boys Secondary School',
    'Abi Bakar Academy Secondary School', 'Candle For Candle Secondary School',
    'Noor Academy Secondary School', 'Gulshan Sec School of Information Technology',
    'The Grand Secondary School', 'Rose Petal Secondary School', 'The Shaffaf Angels Academy',
    'Muskan Grammar Academy', 'S.S. Future Bright Grammar School', 'New Standard Secondary School',
    'Al Mustafa Educational World Secondary School', "Scholar's Academy (Secondary)",
    'Ali Grammar Secondary School', 'Lycos Grammar School (Secondary)',
    'Children Heaven Academy Secondary', 'Karachi Generation School,',
    'New Age Grammar School (Secondary)', 'Iqra Tul Ilm Academy Secondary School',
    'Fatima Secondary Academy', 'The Royal Scholar High School', 'County Cambridge School (Secondary)',
    'Educational Rays Grammar School', 'S.N. Public School (Secondary)',
    'Premier Schooling System (Secondary)', 'New Talent Secondary School',
    'The Muslim Generation School', 'New R T Public School', 'The Kid Paradise School Sec',
    'Aziz Public School Sec', 'The Education Academy Sec', 'The Educators New Karachi Campus',
    'Noor Grammar Secondary School', 'Govt. Girls Secondary School Mehak',
    'Al-Huda Children Academy Secondary School', 'Gulshan Public Secondary School',
    'DHA Grammar Secondary School', 'Clifton Grammar Secondary School',
    'PECHS Grammar Secondary School', 'Roshan Children Academy Secondary School',
    'Korangi Model Secondary School', 'Al-Noor Model Secondary School',
    'Govt. Girls Secondary School Gulshan', 'Govt. Girls Secondary School Nazimabad',
    'Govt. Boys Secondary School Defence', 'Govt. Boys Secondary School Roshan',
    'Saddar Public Secondary School', 'Govt. Girls Secondary School DHA',
    'Defence Children Academy Secondary School', 'North Public Secondary School',
    'Bilal Children Academy Secondary School', 'Govt. Girls Secondary School Karachi',
    'Karachi Public Secondary School', 'Gulberg Public Secondary School',
    'Govt. Girls Secondary School Malir', 'DHA Children Academy Secondary School',
    'Govt. Boys Secondary School Shah Faisal', 'Shah Faisal Children Academy Secondary School',
    'Govt. Girls Secondary School West', 'Falak Grammar Secondary School',
    'Mehak Children Academy Secondary School', 'Gulshan Model Secondary School',
    'Govt. Boys Secondary School Noor', 'Govt. Girls Secondary School Saddar',
    'Govt. Girls Secondary School Bilal', 'Govt. Boys Secondary School Clifton',
    'Govt. Boys Secondary School North', 'Clifton Children Academy Secondary School',
    'Govt. Boys Secondary School Lyari', 'East Grammar Secondary School',
    'Govt. Girls Secondary School Lyari', 'East Model Secondary School',
    'Defence Public Secondary School', 'Saddar Grammar Secondary School'
]
print()
day=1

while day<=30 and len(school_list)>=6:
    print(f"\t\t\t{BOLD} {UNDERLINE}====DAY {day}===={RESET}")
    rand=random.sample(school_list, 6)
    print("Today You have to Vist the following schools: ")
    print()
    count = 1
    for i in rand:

        print(f"{count}: {i}")
        print()
        school_list.remove(i)
        count+=1
    cont=input("Do you want to continue? [Y/N]: ")
    if cont.upper()=="N":
        break

    print()
    day+=1