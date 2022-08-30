import unittest

from mfreport.parser import Parser

HTML = """
<div id="portfolio_det_eq">
    <table>
        <tbody>
            <tr>
                <td>1111</td>
                <td>test name</td>
                <td class="number">1</td>
                <td class="number">1,2</td>
                <td class="number">33</td>
                <td class="number">44,444円</td>
                <td class="number"><span class="minus-color">0円</span></td>
                <td class="number"><span class="plus-color">22,222円</span></td>
                <td class="number"><span class="plus-color">11.11%</span></td>
                <td class="nowrap">test description</td>
                <td class="entry-date"></td>
                <td class="button"></td>
                <td class="button"></td>
            </tr>
            <tr>
                <td>2222</td>
                <td>test name</td>
                <td class="number">1</td>
                <td class="number">1,2</td>
                <td class="number">33</td>
                <td class="number">44,444円</td>
                <td class="number"><span class="minus-color">0円</span></td>
                <td class="number"><span class="plus-color">22,222円</span></td>
                <td class="number"><span class="plus-color">11.11%</span></td>
                <td class="nowrap">test description</td>
                <td class="entry-date"></td>
                <td class="button"></td>
                <td class="button"></td>
            </tr>
        </tbody>
    </table>
</div>
"""  # noqa: E501


class TestParse(unittest.TestCase):
    def test_parse(self):
        p = Parser(HTML)
        df = p.get_stock()
        self.assertEqual("test name", df.at[1111, "name"])
        self.assertEqual(12, df.at[1111, "avg_unit_price"])
        self.assertEqual(44444, df.at[1111, "cur_sum_price"])
