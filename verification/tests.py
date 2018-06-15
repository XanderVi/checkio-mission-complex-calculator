init_code = """
if not "SimpleCalculator" in USER_GLOBAL:
    raise NotImplementedError("Where is 'SimpleCalculator'?")
SimpleCalculator = USER_GLOBAL['SimpleCalculator']

if not "ComplexCalculator" in USER_GLOBAL:
    raise NotImplementedError("Where is 'ComplexCalculator'?")
ComplexCalculator = USER_GLOBAL['ComplexCalculator']
"""

run_test = """
RET['code_result'] = {}
"""


def prepare_test(test="", answer=None, middle_code="", show_code=None):
    if show_code is None:
        show_code = middle_code + "\n" + test
    if not test:
        return_code = "\nRET['code_result'] = ''"
        answer = ''
    else:
        return_code = run_test.format(test)
    return {"test_code": {"python-3": init_code + middle_code + return_code},
            "show": {"python-3": show_code},
            "answer": answer}


TESTS = {
    "1. Add": [
        prepare_test(middle_code="calc = SimpleCalculator()",
                     test="calc.add(1, 5, 0.3)",
                     answer=6.3)
    ],
    "2. Sub": [
        prepare_test(middle_code="calc = SimpleCalculator()",
                     test="calc.sub(99, -1)",
                     answer=100)
    ],
    "3. Add": [
        prepare_test(middle_code='''calc = SimpleCalculator()
calc = ComplexCalculator(calc)
''',
                     test="calc.add(10, 9, -19)",
                     answer=0)
    ],
    "4. Sub": [
        prepare_test(middle_code='''calc = SimpleCalculator()
calc = ComplexCalculator(calc)
''',
                     test="calc.sub(114, 14.1)",
                     answer=99.9)
    ],
    "5. Multi": [
        prepare_test(middle_code='''calc = SimpleCalculator()
calc = ComplexCalculator(calc)
''',
                     test="calc.multi(2, 5, 3.1415926)",
                     answer=31.41593)
    ],
    "6. Div": [
        prepare_test(middle_code='''calc = SimpleCalculator()
calc = ComplexCalculator(calc)
''',
                     test="calc.div(2, 3)",
                     answer=0.66667)
    ],
    "7. Power": [
        prepare_test(middle_code='''calc = SimpleCalculator()
calc = ComplexCalculator(calc)
''',
                     test="calc.power(2, 10)",
                     answer=1024)
    ],
    "8. Root": [
        prepare_test(middle_code='''calc = SimpleCalculator()
calc = ComplexCalculator(calc)
''',
                     test="calc.root(81, 4)",
                     answer=3)
    ],
    "9. Add": [
        prepare_test(middle_code="calc = SimpleCalculator()",
                     test="calc.add(34, 5, 0.23456789)",
                     answer=39.23457)
    ],
    "10. Sub": [
        prepare_test(middle_code="calc = SimpleCalculator()",
                     test="calc.sub(11, 12.5)",
                     answer=-1.5)
    ],
    "11. Add": [
        prepare_test(middle_code='''calc = SimpleCalculator()
calc = ComplexCalculator(calc)
''',
                     test="calc.add(500, -499, -11)",
                     answer=-10)
    ],
    "12. Sub": [
        prepare_test(middle_code='''calc = SimpleCalculator()
calc = ComplexCalculator(calc)
''',
                     test="calc.sub(254, 100)",
                     answer=154)
    ],
    "13. Multi": [
        prepare_test(middle_code='''calc = SimpleCalculator()
calc = ComplexCalculator(calc)
''',
                     test="calc.multi(32, 17, 566, 0.1)",
                     answer=39790.4)
    ],
    "14. Div": [
        prepare_test(middle_code='''calc = SimpleCalculator()
calc = ComplexCalculator(calc)
''',
                     test="calc.div(22, 7)",
                     answer=3.14286)
    ],
    "15. Power": [
        prepare_test(middle_code='''calc = SimpleCalculator()
calc = ComplexCalculator(calc)
''',
                     test="calc.power(100, 0.5)",
                     answer=10)
    ],
    "16. Root": [
        prepare_test(middle_code='''calc = SimpleCalculator()
calc = ComplexCalculator(calc)
''',
                     test="calc.root(33, 3.5)",
                     answer=2.71557)
    ]

}
