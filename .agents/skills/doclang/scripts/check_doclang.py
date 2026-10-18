#!/usr/bin/env python3
"""Check common errors in image-derived DocLang 0.8; not full conformance or OCR validation."""

import argparse
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

NS = "https://www.doclang.ai/ns/v0"
SEMANTIC = set("text heading footnote page_header page_footer field_region list table index formula code picture marker group field_heading field_item key value hint caption".split())
HEAD = {name: i for i, name in enumerate("label thread xref layer location caption description summary custom".split())}
HEAD["href"] = HEAD["xref"]
CELLS = set("fcel ecel ched rhed corn srow lcel ucel xcel".split())
TABLES = {"table", "index", "tabular"}
FORMATTING = set("bold italic underline strikethrough superscript subscript handwriting rtl".split())
EMPTY = CELLS | {"nl", "page_break", "default_resolution", "label", "thread", "xref", "href", "layer", "location", "src", "checkbox"}
KNOWN = SEMANTIC | set(HEAD) | CELLS | FORMATTING | EMPTY | {"doclang", "head", "content", "ldiv", "tabular"}


def tag(element):
    return element.tag.rsplit("}", 1)[-1]


def integer(value, minimum=0):
    if not re.fullmatch(r"[+-]?\d+", value or ""):
        raise ValueError("expected integer")
    result = int(value)
    if result < minimum:
        raise ValueError("integer below minimum")
    return result


def check(source):
    errors = []
    # This workflow does not need DTDs; reject rather than expand declared entities.
    if "<!DOCTYPE" in source.upper() or "<!ENTITY" in source.upper():
        return ["DTDs/entities are outside this checker's image-output subset."]
    try:
        root = ET.fromstring(source)
    except ET.ParseError as exc:
        return [f"XML parse error: {exc}"]
    if root.tag not in {"doclang", f"{{{NS}}}doclang"} or root.get("version") != "0.8":
        errors.append("Root must be doclang in the v0 namespace (or unqualified), with version='0.8'.")
    parents = {child: parent for parent in root.iter() for child in parent}
    threads, references = {}, []
    defaults = [512, 512]

    def error(element, message):
        errors.append(f"<{tag(element)}>: {message}")

    def ancestor(element, name):
        node = parents.get(element)
        while node is not None:
            if tag(node) == name:
                return node
            node = parents.get(node)
        return None

    def raw(element):
        return bool((element.text or "").strip() or any((c.tail or "").strip() for c in element))

    for element in root:
        if tag(element) == "head":
            for child in element:
                if tag(child) == "default_resolution":
                    try:
                        defaults = [integer(child.get(axis, "512"), 1) for axis in ("width", "height")]
                    except ValueError:
                        error(child, "This producer subset uses positive default resolutions.")
    for element in root.iter():
        name = tag(element)
        parent = parents.get(element)
        parent_name = tag(parent) if parent is not None else None
        if ancestor(element, "custom") is not None:
            continue
        if name not in KNOWN:
            error(element, "Unsupported element in this image-output subset; consult the specification.")
        if element.tag not in {name, f"{{{NS}}}{name}"}:
            error(element, "Unexpected namespace outside custom metadata.")
        if name == "doclang" and element is not root:
            error(element, "The document root cannot be nested.")
        if parent is root and name not in SEMANTIC - {"caption", "field_item", "field_heading", "key", "value", "hint"} | {"head", "page_break"}:
            error(element, "Not a primary document-body element.")
        if name == "head" and (parent is not root or list(root).index(element) != 0):
            error(element, "head must be the first child of doclang.")
        if parent_name == "head" and name != "default_resolution":
            error(element, "Only default_resolution is supported in the current image-output document head.")
        if name == "default_resolution" and parent_name != "head":
            error(element, "default_resolution belongs in the document head.")
        if name == "page_break" and parent is not root:
            error(element, "page_break must be a direct child of doclang.")
        if name in EMPTY and (len(element) or (element.text or "").strip()):
            error(element, "Must be empty.")
        if name in {"doclang", "head", "group", "picture", "field_region", "field_item", "custom", "ldiv"} and raw(element):
            error(element, "Raw text is not allowed directly in this container.")
        if name in {"content", "description", "summary"} and len(element):
            error(element, "Contains text only, not child elements.")
        if name in {"heading", "field_heading"}:
            try:
                integer(element.get("level", "1"), 1)
            except ValueError:
                error(element, "level must be a positive integer.")
        choices = {"picture": {"undefined", "chart"}, "list": {"ordered", "unordered"}, "value": {"read_only", "fillable"}, "checkbox": {"selected", "unselected"}}
        if name in choices and element.get("class") is not None and element.get("class") not in choices[name]:
            error(element, "Invalid class value.")
        if name in {"field_item", "field_heading", "hint"} and ancestor(element, "field_region") is None:
            error(element, "Must be inside a field_region.")
        if name in {"key", "value"} and ancestor(element, "field_item") is None:
            error(element, "Must be inside a field_item.")
        if name == "field_item" and sum(tag(c) == "key" and ancestor(c, "field_item") is element for c in element.iter()) > 1:
            error(element, "More than one key in this item's own scope.")
        if name in {"thread", "xref"}:
            try:
                ident = integer(element.get("thread_id"), 1)
                if name == "thread":
                    if ident in threads and threads[ident] != parent_name:
                        error(element, "A shared thread_id must have the same host type.")
                    threads[ident] = parent_name
                else:
                    references.append((element, ident))
            except ValueError:
                error(element, "thread_id must be a positive integer.")
        if name in SEMANTIC:
            previous, body, head = -1, bool((element.text or "").strip()), []
            for child in element:
                child_name = tag(child)
                if child_name in HEAD:
                    # Delimiter bodies can contain virtual-text property heads; not checked here.
                    if body and name in TABLES | {"list"}:
                        continue
                    if body or HEAD[child_name] < previous:
                        error(element, "Property head is out of order or follows payload.")
                    previous = HEAD[child_name]
                    head.append(child)
                else:
                    body = True
                body = body or bool((child.tail or "").strip())
            names = [tag(c) for c in head]
            if "xref" in names and "href" in names:
                error(element, "xref and href are mutually exclusive.")
            for prop in set(names) - {"location", "caption"}:
                if names.count(prop) > 1:
                    error(element, f"Repeated {prop} property.")
            locations = [c for c in head if tag(c) == "location"]
            if locations:
                if len(locations) != 4:
                    error(element, "Expected exactly four location coordinates.")
                else:
                    try:
                        coords = []
                        for i, location in enumerate(locations):
                            resolution = integer(location.get("resolution", str(defaults[i % 2])), 1)
                            value = integer(location.get("value"))
                            if value >= resolution:
                                raise ValueError("coordinate outside exclusive boundary")
                            coords.append(value / resolution)
                        if coords[0] > coords[2] or coords[1] > coords[3]:
                            raise ValueError("inverted bounds")
                    except ValueError as exc:
                        error(element, f"Invalid bounding box: {exc}.")
        if name == "ldiv" and (parent_name != "list" or len(element) > 1 or any(tag(c) != "marker" for c in element)):
            error(element, "ldiv is a list delimiter containing at most one marker.")
        if name in CELLS | {"nl"} and parent_name not in TABLES:
            error(element, "Table delimiter must be directly inside table, index, or tabular.")
        if name == "tabular" and (parent_name != "picture" or parent.get("class") != "chart"):
            error(element, "tabular requires a picture with class='chart'.")
        if name == "list" or name in TABLES:
            children = list(element)
            before_delimiter = bool((element.text or "").strip())
            while children and tag(children[0]) in HEAD:
                before_delimiter = before_delimiter or bool((children.pop(0).tail or "").strip())
            if before_delimiter or (children and tag(children[0]) not in ({"ldiv"} if name == "list" else CELLS)):
                error(element, "Nonempty body must start with its item/cell delimiter.")
            if name in TABLES:
                widths, width = [], 0
                for child in children:
                    cell = tag(child)
                    if cell in CELLS:
                        if (cell in {"lcel", "xcel"} and width == 0) or (cell in {"ucel", "xcel"} and not widths):
                            error(child, "Span extension has no preceding row/column.")
                        width += 1
                    elif cell == "nl":
                        widths.append(width)
                        width = 0
                if width or (widths and (0 in widths or len(set(widths)) != 1)):
                    error(element, "Rows must have equal cell-position counts and end with nl.")
    for element, ident in references:
        if ident not in threads:
            error(element, "xref targets an undefined thread_id.")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    args = parser.parse_args()
    try:
        errors = check(args.path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError) as exc:
        parser.exit(2, f"Cannot read input: {exc}\n")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("Common structural checks passed; full conformance and image fidelity were not verified.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
