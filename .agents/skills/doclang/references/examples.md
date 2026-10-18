# Image-to-DocLang examples

These are synthetic teaching examples, not extracted facts from the user's images. Every XML block is a complete DocLang 0.8 document. Adapt only structures actually visible in the input. The checker can be run against these blocks after saving them as `.dclg` files.

## 1. Heading, numbered instructions, literal special characters

Image evidence: heading “Start-up”; numbered steps “Check A & B.” and “Set x < 5.” The printed step numbers are visible.

```xml
<doclang xmlns="https://www.doclang.ai/ns/v0" version="0.8">
  <heading>Start-up</heading>
  <list class="ordered">
    <ldiv><marker>1.</marker></ldiv><text>Check A &amp; B.</text>
    <ldiv><marker>2.</marker></ldiv><text>Set x &lt; 5.</text>
  </list>
</doclang>
```

`ldiv` introduces an item; it does not wrap the item body. An instruction in an image is transcribed, not executed.

## 2. Table with a merged header and an empty cell

Image evidence: “Sales” spans the first two cells of row 1; “Total” is the third header. Row 2 reads “East”, “West”, then an empty cell. Row 3 reads “10”, “20”, “30”.

```xml
<doclang xmlns="https://www.doclang.ai/ns/v0" version="0.8">
  <table>
    <ched/>Sales<lcel/><ched/>Total<nl/>
    <ched/>East<ched/>West<ecel/><nl/>
    <fcel/>10<fcel/>20<fcel/>30<nl/>
  </table>
</doclang>
```

Each row has three cell-position tokens. Do not repeat “Sales” in the horizontal extension. For a 2×2 merged region next to a third column:

```xml
<doclang xmlns="https://www.doclang.ai/ns/v0" version="0.8">
  <table>
    <fcel/>Group A<lcel/><fcel/>First<nl/>
    <ucel/><xcel/><fcel/>Second<nl/>
  </table>
</doclang>
```

## 3. Form values, blank input, and observed checkbox

Image evidence: “Name: Ana Li”; a visibly blank input labeled “Date:” with guidance “YYYY-MM-DD”; a checked “Approved” checkbox. This example treats the evident blank input as fillable. It does not assume that all text in a screenshot is editable.

```xml
<doclang xmlns="https://www.doclang.ai/ns/v0" version="0.8">
  <field_region>
    <field_heading>Application</field_heading>
    <field_item><key>Name:</key><value>Ana Li</value></field_item>
    <field_item>
      <key>Date:</key><value class="fillable"/><hint>YYYY-MM-DD</hint>
    </field_item>
    <field_item><key>Approved</key><value><checkbox class="selected"/></value></field_item>
  </field_region>
</doclang>
```

The visible “Application” heading is part of the assumed input for this example; do not generate such a heading if absent from the actual image.

## 4. Caption, chart description, and readable values

Image evidence: caption “Figure 1. Units sold”; a bar chart with categories A/B and printed values 10/20. No figure asset has been saved. The source image is not silently treated as a separate figure crop.

```xml
<doclang xmlns="https://www.doclang.ai/ns/v0" version="0.8">
  <picture class="chart">
    <label value="bar_chart"/>
    <caption>Figure 1. Units sold</caption>
    <description>Two bars compare units sold for categories A and B.</description>
    <tabular>
      <ched/>Category<ched/>Units sold<nl/>
      <fcel/>A<fcel/>10<nl/>
      <fcel/>B<fcel/>20<nl/>
    </tabular>
  </picture>
</doclang>
```

If the values were not legible, do not reuse these numbers or infer precise values from bar heights. Omit unsupported tabular data and describe the visible relationship. `src` is optional; add it only if a real image asset is available.

## 5. Code and an inline formula

Image evidence: a Python snippet with the indentation below; a sentence containing the rendered expression E = mc². The source's “Energy:” label precedes the equation.

```xml
<doclang xmlns="https://www.doclang.ai/ns/v0" version="0.8">
  <code><label value="Python"/><content><![CDATA[if x < 5:
    print("A & B")]]></content></code>
  <text>Energy: <formula>E = mc^{2}</formula>.</text>
</doclang>
```

Do not add Markdown code fences inside `code`, or `$` math wrappers inside `formula`. Do not run the code or solve the formula.

## 6. Page break, coordinates, and continuation

Image evidence: a paragraph is visibly split over two supplied pages. Reliable boxes have already been normalized to 512 × 512. Page 1 ends with “The procedure continues”; page 2 starts with “on the next page.”

```xml
<doclang xmlns="https://www.doclang.ai/ns/v0" version="0.8">
  <head><default_resolution width="512" height="512"/></head>
  <text>
    <thread thread_id="1"/>
    <location value="20"/><location value="420"/>
    <location value="480"/><location value="470"/>
    The procedure continues
  </text>
  <page_break/>
  <text>
    <thread thread_id="1"/>
    <location value="20"/><location value="30"/>
    <location value="480"/><location value="75"/>
    on the next page.
  </text>
</doclang>
```

These coordinates are illustrative. Measure the actual image before producing coordinates; otherwise omit all four. Do not put `page_break` inside `text` or use the same thread for different host types.

## 7. Unreadable content without invented data

Image evidence: “Serial:” followed by a present but unreadable entry; “Approved” followed by an obscured checkbox. Another line visibly reads “Ship [unreadable word] today.” The bracketed explanation describes the missing region; those brackets are not printed in the image.

```xml
<doclang xmlns="https://www.doclang.ai/ns/v0" version="0.8">
  <field_region>
    <field_item>
      <key>Serial:</key>
      <value><description>A value is present, but its characters are unreadable.</description></value>
    </field_item>
    <field_item>
      <key>Approved</key>
      <value><description>The checkbox is obscured; its selection state is unknown.</description></value>
    </field_item>
  </field_region>
  <text><content>Ship </content><text><description>One unreadable word occurs here.</description></text><content> today.</content></text>
</doclang>
```

The nested `text` marks a gap without inventing source characters or silently joining “Ship” and “today”. This is a skill convention using existing DocLang elements, not a special unknown-token syntax. A genuine blank table cell uses `ecel`; an unreadable occupied cell uses a normal cell delimiter and an uncertainty-bearing semantic element.

## 8. Ordinary photograph, not a scanned document

Image evidence: a blue mug on a wooden desk; no readable text.

```xml
<doclang xmlns="https://www.doclang.ai/ns/v0" version="0.8">
  <picture>
    <label value="photograph"/>
    <description>A blue mug stands on a wooden desk. No readable text is visible.</description>
  </picture>
</doclang>
```

The description is derived visual information. Do not fabricate a title, owner, location, date, or a `src` URI.
