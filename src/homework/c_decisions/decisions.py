#
def get_options_ratio(option, total):
    ratio = option / total
    return ratio

def get_faculty_rating(ratio):
    if ratio >= 0.9 and ratio < 1:
        return "Excellent"
    elif ratio > 0.8 and ratio < 1:
        return "Very Good"
    elif ratio > 0.7 and ratio < 1:
        return "Good"
    elif ratio > 0.6 and ratio < 1:
        return "Needs Improvement"
    elif ratio >= 0 and ratio < 1:
        return "Unacceptable"
    else:
        return "Error"
