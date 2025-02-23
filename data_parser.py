import json
import xml.etree.ElementTree as ET

def json_parser(json_string):
    """
    Parses a JSON string and converts it into a dictionary.
    """
    try:
        return json.loads(json_string)
    except json.JSONDecodeError:
        return None

def xml_parser(xml_string):
    """
    Parses an XML string and converts it into a dictionary.
    """
    try:
        root = ET.fromstring(xml_string)
        return xml_to_dict(root)
    except ET.ParseError:
        return None

def xml_to_dict(element):
    """
    Helper function that recursively converts an XML element into a dictionary.
    """
    result = {element.tag: {} if element.attrib else None}
    children = list(element)

    if children:
        temp_dict = {}
        for child in children:
            child_dict = xml_to_dict(child)
            for key, value in child_dict.items():
                if key in temp_dict:
                    if not isinstance(temp_dict[key], list):
                        temp_dict[key] = [temp_dict[key]]
                    temp_dict[key].append(value)
                else:
                    temp_dict[key] = value
        result[element.tag] = temp_dict
    elif element.text:
        result[element.tag] = element.text.strip()

    return result

# Sample test data
json_data = '''{
    "name": "Alice Johnson",
    "age": 29,
    "email": "alice.johnson@gmail.com",
    "phone": "+13144985607",
    "city": "New York",
    "occupation": "Software Engineer"
}'''

xml_data = '''<person>
    <name>Bob Smith</name>
    <age>34</age>
    <email>bob.smith@gmail.com.com</email>
    <phone>+1987654321</phone>
    <city>Los Angeles</city>
    <occupation>Graphic Designer</occupation>
</person>'''

# Running and testing the functions
print("JSON Output:", json_parser(json_data))
print("XML Output:", xml_parser(xml_data))
