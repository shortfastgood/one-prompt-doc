"""Behavioral tests for the limited DocLang structural checker."""

import re
import unittest
from pathlib import Path

from check_doclang import check


def document(body):
    return f'<doclang xmlns="https://www.doclang.ai/ns/v0" version="0.8">{body}</doclang>'


class CheckerTests(unittest.TestCase):
    def test_all_teaching_examples(self):
        reference = Path(__file__).resolve().parents[1] / "references" / "examples.md"
        examples = re.findall(r"```xml\n(.*?)\n```", reference.read_text(), re.S)
        self.assertEqual(len(examples), 9)
        for source in examples:
            with self.subTest(source=source[:120]):
                self.assertEqual(check(source), [])

    def test_xml_and_document_boundaries(self):
        for source in ["<doclang>", "<doclang/>", document("unwrapped text"), document("<text><page_break/></text>")]:
            with self.subTest(source=source):
                self.assertTrue(check(source))

    def test_property_order(self):
        for body in ['<text>Hello<label value="x"/></text>', '<text><description>Note</description><label value="x"/>Hello</text>', '<text><label/><label/>Hello</text>', '<text><xref thread_id="1"/><href uri="a"/></text>']:
            with self.subTest(body=body):
                self.assertTrue(check(document(body)))

    def test_coordinate_boundaries_and_normalization(self):
        box = lambda values: "<text>" + "".join(f'<location value="{v}"/>' for v in values) + "x</text>"
        self.assertEqual(check(document(box([0, 0, 511, 511]))), [])
        for values in [[0, 0, 512, 511], [100, 0, 20, 50], [-1, 0, 20, 50], [0, 0, 20]]:
            self.assertTrue(check(document(box(values))))
        mixed = '<text><location value="50" resolution="100"/><location value="0"/><location value="100" resolution="1000"/><location value="50"/>x</text>'
        self.assertTrue(check(document(mixed)))

    def test_table_shape_and_delimiters(self):
        for body in ['<table><fcel/>A<nl/><fcel/>B<fcel/>C<nl/></table>', '<table><fcel/>A</table>', '<table><lcel/><nl/></table>', '<table><ucel/><nl/></table>', '<table><caption>Caption</caption>stray<fcel/>A<nl/></table>', '<text><fcel/></text>']:
            with self.subTest(body=body):
                self.assertTrue(check(document(body)))
        nested = '<table><fcel/><table><fcel/>inner<nl/></table><fcel/>outer<nl/></table>'
        self.assertEqual(check(document(nested)), [])

    def test_list_delimiters(self):
        self.assertTrue(check(document('<list><text>Missing delimiter</text></list>')))
        self.assertTrue(check(document('<list><ldiv>Not an item wrapper</ldiv></list>')))
        self.assertEqual(check(document('<list><ldiv/>First<ldiv/><text>Second</text></list>')), [])

    def test_field_scopes_include_nested_items(self):
        self.assertTrue(check(document('<key>Unscoped</key>')))
        self.assertTrue(check(document('<field_region><field_item><key>A</key><group><key>B</key></group></field_item></field_region>')))
        nested = '<field_region><field_item><key>Outer</key><field_item><key>Inner</key><value>X</value></field_item></field_item></field_region>'
        self.assertEqual(check(document(nested)), [])

    def test_references_resolve_and_thread_types_agree(self):
        self.assertTrue(check(document('<text><xref thread_id="7"/>Figure 7</text>')))
        self.assertTrue(check(document('<text><thread thread_id="1"/>A</text><picture><thread thread_id="1"/></picture>')))
        self.assertEqual(check(document('<text><xref thread_id="2"/>See figure</text><picture><thread thread_id="2"/></picture>')), [])

    def test_chart_data_requires_chart_class(self):
        self.assertTrue(check(document('<picture><tabular><fcel/>1<nl/></tabular></picture>')))
        self.assertTrue(check(document('<picture class="bar_chart"/>')))
        self.assertEqual(check(document('<picture class="chart"><tabular><fcel/>1<nl/></tabular></picture>')), [])

    def test_future_and_invented_elements_are_not_core(self):
        self.assertTrue(check(document('<head><title>Future metadata</title></head>')))
        self.assertTrue(check(document('<text><unclear/></text>')))
        self.assertTrue(check(document('<text><checkbox class="unknown"/></text>')))
        self.assertEqual(check(document('<text><custom xmlns:demo="urn:example:custom"><demo:note>App metadata</demo:note></custom>Visible text</text>')), [])


if __name__ == "__main__":
    unittest.main()
