import unittest
import os

from asyncwhois.parser import WhoIsParser


class TestWhoIsParsers(unittest.TestCase):

    @staticmethod
    def get_txt(tld: str):
        with open(os.path.join(os.getcwd(), f"tests/samples/tld_{tld}.txt")) as txt_input:
            query_output = txt_input.read()
        return query_output

    def test_parser_com(self):
        query_output = self.get_txt('com')
        parser = WhoIsParser('com')
        parser.parse(query_output)
        # confirm dates
        created_date = parser.parser_output.get("created")
        updated_date = parser.parser_output.get("updated")
        expires_date = parser.parser_output.get("expires")
        self.assertEqual(created_date.year, 1997)
        self.assertEqual(updated_date.year, 2019)
        self.assertEqual(expires_date.year, 2028)
        self.assertEqual(created_date.month, 9)
        self.assertEqual(updated_date.month, 9)
        self.assertEqual(expires_date.month, 9)
        self.assertEqual(created_date.day, 15)
        self.assertEqual(updated_date.day, 9)
        self.assertEqual(expires_date.day, 13)
        # geo
        self.assertEqual(parser.parser_output.get("registrant_state"), "CA")
        self.assertEqual(parser.parser_output.get("registrant_country"), "US")
        # registrar
        self.assertEqual(parser.parser_output.get("registrar"), "MarkMonitor, Inc.")
        # registrant
        self.assertEqual(parser.parser_output.get("registrant_organization"), "Google LLC")
        # misc
        self.assertEqual(parser.parser_output.get("dnssec"), "unsigned")
        self.assertEqual(len(parser.parser_output.get("name_servers")), 4)
        self.assertEqual(len(parser.parser_output.get("status")), 6)

    def test_parser_in(self):
        query_output = self.get_txt('in')
        parser = WhoIsParser('in')
        parser.parse(query_output)
        # confirm dates
        created_date = parser.parser_output.get("created")
        updated_date = parser.parser_output.get("updated")
        expires_date = parser.parser_output.get("expires")
        self.assertEqual(created_date.year, 2007)
        self.assertEqual(updated_date.year, 2019)
        self.assertEqual(expires_date.year, 2020)
        self.assertEqual(created_date.month, 12)
        self.assertEqual(updated_date.month, 12)
        self.assertEqual(expires_date.month, 12)
        self.assertEqual(created_date.day, 1)
        self.assertEqual(updated_date.day, 1)
        self.assertEqual(expires_date.day, 1)
        # geo
        self.assertEqual(parser.parser_output.get("registrant_state"), "Rajasthan")
        self.assertEqual(parser.parser_output.get("registrant_country"), "IN")
        self.assertEqual(parser.parser_output.get("registrant_address"), None)
        self.assertEqual(parser.parser_output.get("registrant_zipcode"), None)

        self.assertEqual(parser.parser_output.get("dnssec"), "unsigned")
        self.assertEqual(len(parser.parser_output.get("name_servers")), 2)
        self.assertEqual(len(parser.parser_output.get("status")), 1)

    def test_parser_top(self):
        query_output = self.get_txt('top')
        parser = WhoIsParser('top')
        parser.parse(query_output)
        # confirm dates
        created_date = parser.parser_output.get("created")
        updated_date = parser.parser_output.get("updated")
        expires_date = parser.parser_output.get("expires")
        self.assertEqual(created_date.year, 2020)
        self.assertEqual(updated_date.year, 2020)
        self.assertEqual(expires_date.year, 2021)
        self.assertEqual(created_date.month, 2)
        self.assertEqual(updated_date.month, 5)
        self.assertEqual(expires_date.month, 2)
        self.assertEqual(created_date.day, 25)
        self.assertEqual(updated_date.day, 22)
        self.assertEqual(expires_date.day, 25)
        # geo
        self.assertEqual(parser.parser_output.get("registrant_state"), "AZ")
        self.assertEqual(parser.parser_output.get("registrant_country"), "US")
        self.assertEqual(parser.parser_output.get("registrant_zipcode"), "85016")
        self.assertEqual(parser.parser_output.get("registrant_address"), "1928 E. Highland Ave. Ste F104 PMB# 255")
        # registrar
        self.assertEqual(parser.parser_output.get("registrar"), "NameSilo, LLC")
        # registrant
        self.assertEqual(parser.parser_output.get("registrant_organization"), "See PrivacyGuardian.org")
        # misc
        self.assertEqual(parser.parser_output.get("dnssec"), "unsigned")
        self.assertEqual(len(parser.parser_output.get("name_servers")), 3)
        self.assertEqual(len(parser.parser_output.get("status")), 1)

    def test_parser_xyz(self):
        query_output = self.get_txt('xyz')
        parser = WhoIsParser('xyz')
        parser.parse(query_output)
        # confirm dates
        created_date = parser.parser_output.get("created")
        updated_date = parser.parser_output.get("updated")
        expires_date = parser.parser_output.get("expires")
        self.assertEqual(created_date.year, 2019)
        self.assertEqual(updated_date.year, 1)
        self.assertEqual(expires_date.year, 2020)
        self.assertEqual(created_date.month, 10)
        self.assertEqual(updated_date.month, 1)
        self.assertEqual(expires_date.month, 10)
        self.assertEqual(created_date.day, 15)
        self.assertEqual(updated_date.day, 1)
        self.assertEqual(expires_date.day, 15)
        # geo
        self.assertEqual(parser.parser_output.get("registrant_state"), "Panama")
        self.assertEqual(parser.parser_output.get("registrant_country"), "PA")
        self.assertEqual(parser.parser_output.get("registrant_zipcode"), None)
        self.assertEqual(parser.parser_output.get("registrant_address"), "P.O. Box 0823-03411")
        # registrar
        self.assertEqual(parser.parser_output.get("registrar"), "NAMECHEAP INC")
        # registrant
        self.assertEqual(parser.parser_output.get("registrant_organization"), "WhoisGuard, Inc.")
        self.assertEqual(parser.parser_output.get("registrant_name"), "WhoisGuard Protected")
        # misc
        self.assertEqual(parser.parser_output.get("dnssec"), "unsigned")
        self.assertEqual(len(parser.parser_output.get("name_servers")), 3)
        self.assertEqual(len(parser.parser_output.get("status")), 2)

    def test_parser_ir(self):
        query_output = self.get_txt('ir')
        parser = WhoIsParser('ir')
        parser.parse(query_output)
        # confirm dates
        created_date = parser.parser_output.get("created")
        self.assertEqual(created_date, None)
        updated_date = parser.parser_output.get("updated")
        expires_date = parser.parser_output.get("expires")
        self.assertEqual(updated_date.year, 2019)
        self.assertEqual(expires_date.year, 2020)
        self.assertEqual(updated_date.month, 11)
        self.assertEqual(expires_date.month, 12)
        self.assertEqual(updated_date.day, 7)
        self.assertEqual(expires_date.day, 22)
        # geo
        self.assertEqual(parser.parser_output.get("registrant_state"), None)
        self.assertEqual(parser.parser_output.get("registrant_country"), None)
        self.assertEqual(parser.parser_output.get("registrant_zipcode"), None)
        self.assertEqual(parser.parser_output.get("registrant_address"), "1600 Amphitheatre Parkway, Mountain View, CA, US")
        # registrar
        self.assertEqual(parser.parser_output.get("registrar"), None)
        # registrant
        self.assertEqual(parser.parser_output.get("registrant_organization"), "Google Inc.")
        self.assertEqual(parser.parser_output.get("registrant_name"), "(Domain Holder) Google Inc.")

    def test_parser_icu(self):
        query_output = self.get_txt('icu')
        parser = WhoIsParser('icu')
        parser.parse(query_output)
        # confirm dates
        created_date = parser.parser_output.get("created")
        updated_date = parser.parser_output.get("updated")
        expires_date = parser.parser_output.get("expires")
        self.assertEqual(created_date.year, 2019)
        self.assertEqual(updated_date.year, 2019)
        self.assertEqual(expires_date.year, 2020)
        self.assertEqual(created_date.month, 5)
        self.assertEqual(updated_date.month, 10)
        self.assertEqual(expires_date.month, 5)
        self.assertEqual(created_date.day, 11)
        self.assertEqual(updated_date.day, 23)
        self.assertEqual(expires_date.day, 11)
        # geo
        self.assertEqual(parser.parser_output.get("registrant_state"), "Sind(en)")
        self.assertEqual(parser.parser_output.get("registrant_city"), "karachi")
        self.assertEqual(parser.parser_output.get("registrant_country"), "PK")
        self.assertEqual(parser.parser_output.get("registrant_zipcode"), "75640")
        self.assertEqual(parser.parser_output.get("registrant_address"), "Manzoor Colony")
        # registrar
        self.assertEqual(parser.parser_output.get("registrar"), "PDR Ltd. d/b/a PublicDomainRegistry.com")
        # registrant
        self.assertEqual(parser.parser_output.get("registrant_organization"), None)
        self.assertEqual(parser.parser_output.get("registrant_name"), None)
        # misc
        self.assertEqual(parser.parser_output.get("dnssec"), "Unsigned")
        self.assertEqual(len(parser.parser_output.get("name_servers")), 2)
        self.assertEqual(len(parser.parser_output.get("status")), 4)

    def test_parser_ie(self):
        query_output = self.get_txt('ie')
        parser = WhoIsParser('ie')
        parser.parse(query_output)
        # confirm dates
        created_date = parser.parser_output.get("created")
        expires_date = parser.parser_output.get("expires")
        self.assertEqual(created_date.year, 2002)
        self.assertEqual(expires_date.year, 2021)
        self.assertEqual(created_date.month, 3)
        self.assertEqual(expires_date.month, 3)
        self.assertEqual(created_date.day, 21)
        self.assertEqual(expires_date.day, 21)
        # registrar
        self.assertEqual(parser.parser_output.get("registrar"), "Markmonitor Inc")
        # registrant
        self.assertEqual(parser.parser_output.get("registrant_organization"), None)
        self.assertEqual(parser.parser_output.get("registrant_name"), "Google, Inc")
        # misc
        self.assertEqual(len(parser.parser_output.get("name_servers")), 3)
        self.assertEqual(len(parser.parser_output.get("status")), 1)

    def test_parser_uk(self):
        query_output = self.get_txt('uk')
        parser = WhoIsParser('uk')
        parser.parse(query_output)
        # confirm dates
        created_date = parser.parser_output.get("created")
        updated_date = parser.parser_output.get("updated")
        expires_date = parser.parser_output.get("expires")
        self.assertEqual(created_date.year, 2014)
        self.assertEqual(updated_date.year, 2020)
        self.assertEqual(expires_date.year, 2021)
        self.assertEqual(created_date.month, 6)
        self.assertEqual(updated_date.month, 5)
        self.assertEqual(expires_date.month, 6)
        self.assertEqual(created_date.day, 11)
        self.assertEqual(updated_date.day, 10)
        self.assertEqual(expires_date.day, 11)
        # registrar
        self.assertEqual(parser.parser_output.get("registrar"), "Markmonitor Inc. t/a MarkMonitor Inc. [Tag = MARKMONITOR]")
        # registrant
        self.assertEqual(parser.parser_output.get("registrant_organization"), None)
        self.assertEqual(parser.parser_output.get("registrant_name"), None)
        # misc
        self.assertEqual(len(parser.parser_output.get("name_servers")), 1)
        self.assertEqual(len(parser.parser_output.get("status")), 0)

    def test_parser_cl(self):
        query_output = self.get_txt('cl')
        parser = WhoIsParser('cl')
        parser.parse(query_output)
        # confirm dates
        created_date = parser.parser_output.get("created")
        expires_date = parser.parser_output.get("expires")
        self.assertEqual(created_date.year, 2002)
        self.assertEqual(expires_date.year, 2020)
        self.assertEqual(created_date.month, 10)
        self.assertEqual(expires_date.month, 11)
        self.assertEqual(created_date.day, 22)
        self.assertEqual(expires_date.day, 20)
        # registrar
        self.assertEqual(parser.parser_output.get("registrar"), "MarkMonitor Inc.")
        # registrant
        self.assertEqual(parser.parser_output.get("registrant_organization"), "Google LLC")
        self.assertEqual(parser.parser_output.get("registrant_name"), "Google LLC")
        # misc
        self.assertEqual(len(parser.parser_output.get("name_servers")), 4)

    def test_parser_be(self):
        query_output = self.get_txt('be')
        parser = WhoIsParser('be')
        parser.parse(query_output)
        # confirm dates
        created_date = parser.parser_output.get("created")
        self.assertEqual(created_date.year, 2000)
        self.assertEqual(created_date.month, 12)
        self.assertEqual(created_date.day, 12)
        self.assertEqual(parser.parser_output.get("registrar"), " MarkMonitor Inc.")
        # registrant
        self.assertEqual(parser.parser_output.get("registrant_organization"), None)
        self.assertEqual(parser.parser_output.get("registrant_name"), None)

    def test_parser_de(self):
        query_output = self.get_txt('de')
        parser = WhoIsParser('de')
        parser.parse(query_output)

        self.assertEqual(len(parser.parser_output.get('status')), 1)

    def test_parse_us(self):
        query_output = self.get_txt('us')
        parser = WhoIsParser('us')
        parser.parse(query_output)
        # confirm dates
        created_date = parser.parser_output.get("created")
        updated_date = parser.parser_output.get("updated")
        expires_date = parser.parser_output.get("expires")
        self.assertEqual(created_date.year, 2002)
        self.assertEqual(updated_date.year, 2020)
        self.assertEqual(expires_date.year, 2021)
        self.assertEqual(created_date.month, 4)
        self.assertEqual(updated_date.month, 3)
        self.assertEqual(expires_date.month, 4)
        self.assertEqual(created_date.day, 19)
        self.assertEqual(updated_date.day, 22)
        self.assertEqual(expires_date.day, 18)
        # geo
        self.assertEqual(parser.parser_output.get("registrant_state"), "CA")
        self.assertEqual(parser.parser_output.get("registrant_city"), "Mountain View")
        self.assertEqual(parser.parser_output.get("registrant_country"), "US")
        self.assertEqual(parser.parser_output.get("registrant_zipcode"), "94043")
        self.assertEqual(parser.parser_output.get("registrant_address"), "1600 Amphitheatre Parkway")
        # registrar
        self.assertEqual(parser.parser_output.get("registrar"), "MarkMonitor, Inc.")
        # registrant
        self.assertEqual(parser.parser_output.get("registrant_organization"), "Google LLC")
        self.assertEqual(parser.parser_output.get("registrant_name"), "Google Inc")
        # misc
        self.assertEqual(parser.parser_output.get("dnssec"), "unsigned")
        self.assertEqual(len(parser.parser_output.get("name_servers")), 4)
        self.assertEqual(len(parser.parser_output.get("status")), 3)

    def test_parse_ar(self):
        query_output = self.get_txt('ar')
        parser = WhoIsParser('ar')
        parser.parse(query_output)
        # confirm dates
        created_date = parser.parser_output.get("created")
        updated_date = parser.parser_output.get("updated")
        expires_date = parser.parser_output.get("expires")
        self.assertEqual(created_date.year, 2013)
        self.assertEqual(updated_date.year, 2019)
        self.assertEqual(expires_date.year, 2020)
        self.assertEqual(created_date.month, 10)
        self.assertEqual(updated_date.month, 11)
        self.assertEqual(expires_date.month, 11)
        self.assertEqual(created_date.day, 29)
        self.assertEqual(updated_date.day, 1)
        self.assertEqual(expires_date.day, 1)
        # registrar
        self.assertEqual(parser.parser_output.get("registrar"), "nicar")
        # registrant
        self.assertEqual(parser.parser_output.get("registrant_name"), "GOOGLE INC.")
        # misc
        self.assertEqual(len(parser.parser_output.get("name_servers")), 2)
        self.assertEqual(len(parser.parser_output.get("status")), 0)

    def test_parse_no(self):
        query_output = self.get_txt('no')
        parser = WhoIsParser('no')
        parser.parse(query_output)
        # confirm dates
        created_date = parser.parser_output.get("created")
        updated_date = parser.parser_output.get("updated")
        expires_date = parser.parser_output.get("expires")
        self.assertIsNone(expires_date)
        self.assertEqual(created_date.year, 2001)
        self.assertEqual(updated_date.year, 2020)
        self.assertEqual(created_date.month, 2)
        self.assertEqual(updated_date.month, 1)
        self.assertEqual(created_date.day, 26)
        self.assertEqual(updated_date.day, 27)
        # registrar
        self.assertEqual(parser.parser_output.get("registrar"), "REG466-NORID")
        # misc
        self.assertEqual(len(parser.parser_output.get("name_servers")), 4)

    def test_parser_ai(self):
        query_output = self.get_txt('ai')
        parser = WhoIsParser('ai')
        parser.parse(query_output)
        # confirm dates
        created_date = parser.parser_output.get("created")
        updated_date = parser.parser_output.get("updated")
        expires_date = parser.parser_output.get("expires")
        self.assertEqual(created_date.year, 2017)
        self.assertEqual(updated_date.year, 2019)
        self.assertEqual(expires_date.year, 2021)
        self.assertEqual(created_date.month, 12)
        self.assertEqual(updated_date.month, 8)
        self.assertEqual(expires_date.month, 9)
        self.assertEqual(created_date.day, 16)
        self.assertEqual(updated_date.day, 24)
        self.assertEqual(expires_date.day, 25)
        # geo
        self.assertEqual(parser.parser_output.get("registrant_state"), "CA")
        self.assertEqual(parser.parser_output.get("registrant_country"), "US")
        self.assertEqual(parser.parser_output.get("registrant_city"), "Mountain View")
        self.assertEqual(parser.parser_output.get("registrant_zipcode"), "94043")
        self.assertEqual(parser.parser_output.get("registrant_address"), "1600 Amphitheatre Parkway")
        # registrar
        self.assertEqual(parser.parser_output.get("registrar"), "Markmonitor")
        # registrant
        self.assertEqual(parser.parser_output.get("registrant_organization"), "Google LLC")
        self.assertEqual(parser.parser_output.get("registrant_name"), "Domain Administrator")
        # misc
        self.assertEqual(parser.parser_output.get("dnssec"), "unsigned")
        self.assertEqual(len(parser.parser_output.get("name_servers")), 4)
        self.assertEqual(len(parser.parser_output.get("status")), 3)

    def test_parser_me(self):
        query_output = self.get_txt('me')
        parser = WhoIsParser('me')
        parser.parse(query_output)
        # confirm dates
        created_date = parser.parser_output.get("created")
        updated_date = parser.parser_output.get("updated")
        expires_date = parser.parser_output.get("expires")
        self.assertEqual(created_date.year, 2008)
        self.assertEqual(updated_date.year, 2020)
        self.assertEqual(expires_date.year, 2021)
        self.assertEqual(created_date.month, 6)
        self.assertEqual(updated_date.month, 5)
        self.assertEqual(expires_date.month, 6)
        self.assertEqual(created_date.day, 13)
        self.assertEqual(updated_date.day, 12)
        self.assertEqual(expires_date.day, 13)
        # geo
        self.assertEqual(parser.parser_output.get("registrant_state"), "CA")
        self.assertEqual(parser.parser_output.get("registrant_country"), "US")
        # registrar
        self.assertEqual(parser.parser_output.get("registrar"), "MarkMonitor Inc.")
        # registrant
        self.assertEqual(parser.parser_output.get("registrant_organization"), "Google LLC")
        # misc
        self.assertEqual(parser.parser_output.get("dnssec"), "unsigned")
        self.assertEqual(len(parser.parser_output.get("name_servers")), 4)
        self.assertEqual(len(parser.parser_output.get("status")), 6)

    def test_parser_cc(self):
        query_output = self.get_txt('cc')
        parser = WhoIsParser('cc')
        parser.parse(query_output)
        # confirm dates
        created_date = parser.parser_output.get("created")
        updated_date = parser.parser_output.get("updated")
        expires_date = parser.parser_output.get("expires")
        self.assertEqual(created_date.year, 2002)
        self.assertEqual(updated_date.year, 2016)
        self.assertEqual(expires_date.year, 2024)
        self.assertEqual(created_date.month, 8)
        self.assertEqual(updated_date.month, 11)
        self.assertEqual(expires_date.month, 8)
        self.assertEqual(created_date.day, 4)
        self.assertEqual(updated_date.day, 12)
        self.assertEqual(expires_date.day, 4)
        # geo
        self.assertEqual(parser.parser_output.get("registrant_state"), "CA")
        self.assertEqual(parser.parser_output.get("registrant_city"), "Cupertino")
        self.assertEqual(parser.parser_output.get("registrant_country"), "US")
        self.assertEqual(parser.parser_output.get("registrant_zipcode"), "95014")
        self.assertEqual(parser.parser_output.get("registrant_address"), "1 Infinite Loop")
        # registrar
        self.assertEqual(parser.parser_output.get("registrar"), "CSC CORPORATE DOMAINS, INC.")
        # registrant
        self.assertEqual(parser.parser_output.get("registrant_organization"), "Apple Inc.")
        self.assertEqual(parser.parser_output.get("registrant_name"), "Domain Administrator")
        # misc
        self.assertEqual(parser.parser_output.get("dnssec"), "unsigned")
        self.assertEqual(len(parser.parser_output.get("name_servers")), 4)
        self.assertEqual(len(parser.parser_output.get("status")), 1)