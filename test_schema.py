import unittest
from lxml import etree
from io import StringIO

class TestSchema(unittest.TestCase):

    def open_xsd(self):
        return open('socialrss.xsd')

    def is_valid(self, test_xml):
        with self.open_xsd() as xmlschema_file:
            xmlschema_doc = etree.parse(xmlschema_file)
            xmlschema = etree.XMLSchema(xmlschema_doc)

            result = xmlschema.validate(etree.parse(StringIO(test_xml)))

            if not result:
                print(xmlschema.error_log.last_error)

            return result

    def test_valid_email(self):
        valid_xml = '<social:email xmlns:social="http://socialrss.org/schemas/socialrss/1.0">some@email.com</social:email>'
        self.assertTrue(self.is_valid(valid_xml))

    def test_invalid_handle_without_type(self):
        invalid_xml = '<social:handle xmlns:social="http://socialrss.org/schemas/socialrss/1.0">handle</social:handle>'
        self.assertFalse(self.is_valid(invalid_xml))

    def test_valid_handle_with_url_and_text(self):
        valid_xml = '<social:handle xmlns:social="http://socialrss.org/schemas/socialrss/1.0" type="type" url="url" text="text">handle</social:handle>'
        self.assertTrue(self.is_valid(valid_xml))

    def test_invalid_crowdfunding_without_type(self):
        invalid_xml = '<social:crowdfunding xmlns:social="http://socialrss.org/schemas/socialrss/1.0">handler</social:crowdfunding>'
        self.assertFalse(self.is_valid(invalid_xml))

    def test_valid_crowdfunding_with_url_and_text(self):
        valid_xml = '<social:crowdfunding xmlns:social="http://socialrss.org/schemas/socialrss/1.0" type="type" url="url" text="text">handle</social:crowdfunding>'
        self.assertTrue(self.is_valid(valid_xml))

    def test_invalid_participant_simple_without_name(self):
        invalid_xml = '<social:participant xmlns:social="http://socialrss.org/schemas/socialrss/1.0"/>'
        self.assertFalse(self.is_valid(invalid_xml))

    def test_valid_participant_simple_with_name(self):
        valid_xml = '<social:participant xmlns:social="http://socialrss.org/schemas/socialrss/1.0" name="Name"/>'
        self.assertTrue(self.is_valid(valid_xml))

    def test_valid_participant_simple_with_name_and_permanent(self):
        valid_xml = '<social:participant xmlns:social="http://socialrss.org/schemas/socialrss/1.0" name="Name" permanent="true"/>'
        self.assertTrue(self.is_valid(valid_xml))

    def test_invalid_participant_simple_with_name_and_invalid_permanent(self):
        invalid_xml = '<social:participant xmlns:social="http://socialrss.org/schemas/socialrss/1.0" name="Name" permanent="unknown"/>'
        self.assertFalse(self.is_valid(invalid_xml))

    def test_valid_participant_simple_with_name_and_id(self):
        valid_xml = '<social:participant xmlns:social="http://socialrss.org/schemas/socialrss/1.0" name="Name" id="id"/>'
        self.assertTrue(self.is_valid(valid_xml))

    def test_valid_participant_complex(self):
        valid_xml = """<social:participant xmlns:social="http://socialrss.org/schemas/socialrss/1.0" name="Name" id="id">
            <social:email>some@email.com</social:email>
            <social:handle type="type">handle</social:handle>
            <social:handle type="type">handle</social:handle>
        </social:participant>"""
        self.assertTrue(self.is_valid(valid_xml))

    def test_invalid_participant_reference_without_id(self):
        invalid_xml = '<social:participantReference xmlns:social="http://socialrss.org/schemas/socialrss/1.0"/>'
        self.assertFalse(self.is_valid(invalid_xml))

    def test_valid_participant_reference_with_id(self):
        valid_xml = '<social:participantReference xmlns:social="http://socialrss.org/schemas/socialrss/1.0" id="id"/>'
        self.assertTrue(self.is_valid(valid_xml))

    def test_invalid_disqus(self):
        invalid_xml = '<social:disqus xmlns:social="http://socialrss.org/schemas/socialrss/1.0"/>'
        self.assertFalse(self.is_valid(invalid_xml))

    def test_valid_disqus(self):
        valid_xml = '<social:disqus xmlns:social="http://socialrss.org/schemas/socialrss/1.0" shortname="shortname" page_url="url" page_identifier="postid"/>'
        self.assertTrue(self.is_valid(valid_xml))

    def test_invalid_disqus(self):
        valid_xml = '<social:disqus xmlns:social="http://socialrss.org/schemas/socialrss/1.0" shortname="shortname" page_url="url" page_identifier="postid"/>'
        self.assertTrue(self.is_valid(valid_xml))

    def test_valid_hashtag(self):
        valid_xml = '<social:hashtag xmlns:social="http://socialrss.org/schemas/socialrss/1.0">hashtag</social:hashtag>'
        self.assertTrue(self.is_valid(valid_xml))

if __name__ == '__main__':
    unittest.main()