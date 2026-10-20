"""Check an actual CV-linear extraction; set DOCLANG_CV_OUTPUT to its XML path.

These image-specific expectations do not run a model or establish full OCR accuracy.
"""

import os
import unittest
import xml.etree.ElementTree as ET


NS = {"d": "https://www.doclang.ai/ns/v0"}
OUTPUT = os.environ.get("DOCLANG_CV_OUTPUT")
JOBS = (
    ("Boston, MA", "Perform substantive", "Mastery of desktop"),
    ("Houston, TX", "Support Configuration", "Submit revised"),
    ("Chicago, IL", "Identify and make", "Manage document libraries"),
)


def visible_text(element):
    return " ".join("".join(element.itertext()).split())


@unittest.skipUnless(OUTPUT, "Set DOCLANG_CV_OUTPUT to a generated CV-linear result.")
class CVLinearStructureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = ET.parse(OUTPUT).getroot()
        cls.parents = {child: parent for parent in cls.root.iter() for child in parent}

    def find_one(self, tag, text):
        matches = [e for e in self.root.findall(f".//d:{tag}", NS) if visible_text(e) == text]
        self.assertEqual(len(matches), 1, f"Expected one {tag}: {text}")
        return matches[0]

    def group_for(self, element, with_list=False):
        while element in self.parents:
            element = self.parents[element]
            if element.tag == f'{{{NS["d"]}}}group':
                if not with_list or element.find(".//d:list", NS) is not None:
                    return element
        self.fail("Missing group for the associated content")

    def job_group(self, city):
        return self.group_for(self.find_one("text", city), with_list=True)

    def test_heading_hierarchy(self):
        headings = self.root.findall(".//d:heading", NS)
        self.assertEqual(len(headings), 8)
        for heading in headings:
            self.assertGreater(int(heading.get("level", "0")), 0, "Use explicit heading levels")
        self.assertEqual(self.find_one("heading", "Dashawn Koelpin").get("level"), "1")
        sections = [self.find_one("heading", s) for s in ("EXPERIENCE", "EDUCATION", "SKILLS")]
        self.assertEqual(len({e.get("level") for e in sections}), 1)
        level = int(sections[0].get("level"))
        for city, _, _ in JOBS:
            titles = self.job_group(city).findall(".//d:heading", NS)
            self.assertEqual(len(titles), 1)
            self.assertEqual(int(titles[0].get("level")), level + 1)
        university = self.find_one("heading", "EMORY UNIVERSITY")
        self.assertEqual(int(university.get("level")), level + 1)

    def test_employment_groups_and_list_membership(self):
        groups = [self.job_group(city) for city, _, _ in JOBS]
        self.assertEqual(len(set(groups)), 3)
        for group, (city, first, last) in zip(groups, JOBS):
            with self.subTest(city=city):
                lists = group.findall(".//d:list", NS)
                self.assertEqual(len(lists), 1)
                self.assertEqual(len(lists[0].findall("d:ldiv", NS)), 7)
                items = lists[0].findall("d:text", NS)
                self.assertEqual(len(items), 7)
                self.assertTrue(visible_text(items[0]).startswith(first))
                self.assertTrue(visible_text(items[-1]).startswith(last))
                for other, _, _ in JOBS:
                    if other != city:
                        self.assertNotIn(other, visible_text(group))

    def test_present_belongs_to_third_employment_group(self):
        present = self.find_one("text", "present")
        self.assertIn(present, list(self.job_group("Chicago, IL").iter()))
        for city in ("Boston, MA", "Houston, TX"):
            self.assertNotIn(present, list(self.job_group(city).iter()))

    def test_education_group(self):
        university = self.find_one("heading", "EMORY UNIVERSITY")
        group = self.group_for(university)
        text = visible_text(group).replace("’", "'")
        self.assertIn("Bachelor's Degree in Business", text)

    def test_list_counts_and_reading_order(self):
        lists = self.root.findall(".//d:list", NS)
        self.assertEqual([len(e.findall("d:ldiv", NS)) for e in lists], [7, 7, 7, 10])
        for index, (city, _, _) in enumerate(JOBS):
            self.assertIs(lists[index], self.job_group(city).find(".//d:list", NS))
        skills = lists[-1].findall("d:text", NS)
        self.assertEqual(len(skills), 10)
        self.assertTrue(visible_text(skills[0]).startswith("Strong analytical"))
        self.assertTrue(visible_text(skills[-1]).startswith("Ability to analyze target audience"))


if __name__ == "__main__":
    unittest.main()
