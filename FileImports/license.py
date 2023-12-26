import random


license_dict_all = {'Provisional International': '0',
                    'Medical Restricted Provisional 3 Years Or More - Car': '1',
                    'Medical Restricted Provisional 3 Years Or More Motorcycle': '2',
                    'Medical Restricted Provisional  - Less Then 3 Years - Car': '3',
                    'Medical Restricted Provisional  - Less Then 3 Years - Motorcycle': '4',
                    'Medical Restricted (Full) Less Than 3 Years - Car': '5',
                    'Medical Restricted (Full) Less Than 3 Years - Motorcycle': '6',
                    'Full Moped Licence': '7',
                    'A2 Licence (Restricted full test)': '8',
                    'Provisional (UK) HGV Licence': '9',
                    'No Licence Ever Held': 'A',
                    'Licence Revoked Due To Disqualification': 'B',
                    'Licence Revoked (Reason Other Than Disqualification)': 'C',
                    'EEC Licence (EU)': 'E',
                    'Full UK Car Licence': 'F',
                    'European (Non-EU)': 'H',
                    'A1 (up to 125 cc, 11 kw, 14.6 bhp)': 'L',
                    'Category A Full Motorcycle Licence': 'M',
                    'International Licence': 'N',
                    'Provisional EU': 'O',
                    'Provisional (UK) Car Licence': 'P',
                    'Provisional Motorcycle Licence': 'Q',
                    'HGV Class 1': 'T',
                    'Provisional (Non EU)': 'U',
                    'HGV Class 2': 'V',
                    'HGV Class 3': 'W',
                    'Medical Restricted (Full) 3 Years Or More - Car': 'X',
                    'Medical Restricted (Full) 3 Years Or More - Motorcycle': 'Y',
                    'Other': 'Z',
                    'Any other licence type not listed above': '-'}

license_dict_prev_or_full = {
    'Provisional (UK) Car Licence': 'P',
    'Full UK Car Licence': 'F'
}


def get_license_type(license_dict=license_dict_prev_or_full):
    # The weights for the distribution, 99.5% for 'F' and 0.5% for 'P'
    weights = {'F': 99.8, 'P': 0.2}
    # Normalize weights to sum to 1 (percentage conversion)
    total = sum(weights.values())
    normalized_weights = {k: v / total for k, v in weights.items()}

    # Use random.choices() to select a license type based on the specified weights
    license_type = random.choices(
        population=list(license_dict.values()),
        weights=[normalized_weights[license_dict[k]] for k in license_dict],
        k=1
    )[0]

    # Return the license type selected
    return license_type

l = []
for i in range(1000):
    l.append(get_license_type())

print(f'F appears {l.count("F")} times in the list and P appears {l.count("P")} times in the list')